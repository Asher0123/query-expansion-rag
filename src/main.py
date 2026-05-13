from sentence_transformers import SentenceTransformer
import numpy as np
from embedder import MockTextEmbeddingModel
from loaders import PDFLoader, Document
from splitter import SentenceSplitter
import faiss
import json
from dataclasses import asdict
import os
from exceptions import RetrievalError

class Retriever:

    def __init__(self, loader=None, splitter=None, embedder=None):
        self.loader = loader or PDFLoader()
        self.splitter = splitter or SentenceSplitter()
        self.embedder = embedder or MockTextEmbeddingModel()
        os.makedirs('vectorstore',exist_ok=True)
        self.vectorstore_dir = "vectorstore"
        self.index_path = os.path.join(self.vectorstore_dir, "index.faiss")
        self.chunks_path = os.path.join(self.vectorstore_dir, "chunks.json")
        

    def ingest(self, path):
       
        print("Started")
        try:
            document=self.loader.load_document(path)
            print("Document Loaded")

            chunks=self.splitter.split(document)
            print("Document split")

            chunk_content=[doc.content for doc in chunks]

            with open(self.chunks_path,'w') as f:
                json.dump([asdict(chunk) for chunk in chunks], f, indent=3)

            embeddings=self.embedder.get_embeddings(chunk_content)
            print("Embeddings created")

            faiss.normalize_L2(embeddings)
            print("Embeddings normalised")

            index=faiss.IndexFlatIP(len(embeddings[0]))

            index.add(embeddings)
            print("Docs added to faiss")

            index_path=os.path.join('vectorstore','index.faiss')

            faiss.write_index(index, index_path)

            return index
        
        except RetrievalError:
            raise
        except Exception as e:
            raise RetrievalError(f"Error in ingesting document: {e}") from e


    def query(self, query, k=4):
        try:
            if not query.strip():
                raise RetrievalError("Query cannot be empty.")

            query_embeddings=self.embedder.get_embeddings([query])

            faiss.normalize_L2(query_embeddings)

            if not os.path.exists(self.index_path):
                raise RetrievalError("No FAISS index found. Run ingestion first.")

            if not os.path.exists(self.chunks_path):
                raise RetrievalError("No chunk metadata found. Run ingestion first.")

            index=faiss.read_index(self.index_path)
            
            with open(self.chunks_path, 'r') as f:
                chunks=json.load(f)

            D, I= index.search(query_embeddings, k=k)
            print("D and I")

            retrieved_chunks=[]

            for dist, idx in zip(D[0],I[0]):
                if idx==-1:
                    continue
                doc = chunks[idx]

                retrieved_chunks.append({
                    "page_content": doc['content'],
                    "metadata": doc['metadata'],
                    "cosine similarity": float(dist)
                })
            print("Chunks retrieved")
            return retrieved_chunks
        
        except RetrievalError:
            raise
        except Exception as e:
            raise RetrievalError(f"Error in querying document: {e}") from e

def precision_at_k(relevance_labels, k):
    relevant = 0

    for label in relevance_labels[:k]:
        if label.lower() in ["high", "medium"]:
            relevant += 1

    return relevant / k

if __name__=='__main__':

    from mock_generator import GenerativeModel

    retrieve=Retriever(embedder= MockTextEmbeddingModel(model=SentenceTransformer("all-MiniLM-L6-v2"), method_name='encode'))

    path = input("Enter document path: ")
    
    retrieve.ingest(path)

    query= "What is AWS?"

    model=GenerativeModel()
    print("Before query enhanced")
    query_enhanced = model.generate_content(query)

    print("after query enhanced")
    retrieved_chunks=retrieve.query(query)
    retrieved_chunks_enhanced=retrieve.query(query_enhanced.text)
    

    data = {
        "original_query": {
            "query": query,
            "retrieved_chunks": retrieved_chunks
        },
        "enhanced_query": {
            "query": query_enhanced.text,
            "retrieved_chunks": retrieved_chunks_enhanced
        }
    }


    with open("query.json", "w", encoding='utf-8') as f:
        json.dump([data], f, indent=3, ensure_ascii=False)

    strategy_a_labels = ["High", "Medium", "Medium", "Low"]
    strategy_b_labels = ["High", "High", "High", "Medium"]

    precision_a = precision_at_k(strategy_a_labels, 4)
    precision_b = precision_at_k(strategy_b_labels, 4)

    print(f"\nStrategy A Precision@4: {precision_a:.2f}")
    print(f"Strategy B Precision@4: {precision_b:.2f}")