# query-expansion-rag


A modular Retrieval-Augmented Generation (RAG) pipeline implementing semantic vector search, query expansion, and retrieval benchmarking using local embeddings and FAISS.

---

## Overview

This project was developed as part of a GenAI assessment focused on:

- semantic retrieval
- vector databases
- embeddings
- query expansion
- benchmarking retrieval quality

The system compares two retrieval strategies:

### Strategy A — Raw Vector Search

Direct embedding-based semantic retrieval.

### Strategy B — AI-Enhanced Retrieval

Query rewriting/expansion before semantic retrieval.

---

## Features

- Semantic vector retrieval using FAISS
- Query expansion using a mocked generative model
- PDF and DOCX document loading
- Sentence-based and fixed-size chunking
- Embedding generation using local embedding models
- Precision@K benchmarking
- Modular pipeline architecture
- Pytest-based testing
- Custom exception handling

---

## Architecture

```text
Document
   ↓
Loader
   ↓
Splitter
   ↓
Embedding Model
   ↓
FAISS Vector Store
   ↓
Semantic Retrieval
   ↓
Benchmark Evaluation
```

---

## Retrieval Strategies

### Strategy A — Raw Retrieval

```text
Query → Embedding → Vector Search
```

### Strategy B — AI-Enhanced Retrieval

```text
Query → Query Expansion → Embedding → Vector Search
```

Example:

```text
Original Query:
What is aws iam?

Enhanced Query:
What is Amazon Web Services Identity and access management(IAM)?
```

---

## Similarity Metric Choice

This project uses **Cosine Similarity** for semantic retrieval.

Embeddings are normalized using:

```python
faiss.normalize_L2(embeddings)
```

FAISS `IndexFlatIP` is used for vector search:

```python
index = faiss.IndexFlatIP(dimension)
```

After normalization, Inner Product becomes equivalent to Cosine Similarity.

Cosine similarity is preferred for semantic search because transformer-based embeddings primarily capture semantic direction rather than vector magnitude.

---

## Cosine Similarity vs Euclidean Distance

| Metric | Best Use Case |
|---|---|
| Cosine Similarity | Semantic text retrieval |
| Euclidean Distance | Spatial/numeric distance problems |

Cosine similarity performs better for:
- semantic search
- NLP tasks
- RAG pipelines
- embedding retrieval systems

---

## Benchmarking

The project benchmarks:
- Raw semantic retrieval
- AI-enhanced retrieval

Evaluation includes:
- qualitative retrieval comparison
- Precision@K analysis

Results are documented in:

```text
retrieval_benchmark.md
```

---

## Precision@K

Precision@K measures the relevance quality of retrieved chunks:

```text
Precision@K = Relevant Retrieved Chunks / K
```

The benchmark demonstrates that AI-enhanced query expansion improves:
- semantic relevance
- terminology alignment
- retrieval specificity
- noise reduction

---

## Project Structure

```text
query-expansion-rag/
│
├── src/
│   ├── loaders.py
│   ├── splitter.py
│   ├── embedder.py
│   ├── mock_generator.py
│   ├── exceptions.py
│   └── main.py
│
├── tests/
├── vectorstore/
├── retrieval_benchmark.md
├── requirements.txt
└── README.md
```
---

## Installation

### Clone Repository

```bash
git clone https://github.com/<your-username>/query-expansion-rag.git
```

---

### Create Virtual Environment

```bash
python -m venv venv
```

---

### Activate Environment

#### Windows

```bash
venv\Scripts\activate
```

#### Linux / MacOS

```bash
source venv/bin/activate
```

---

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

### Run Project

```bash
python src/main.py
```

---

### Run Tests

```bash
pytest
```

---

### Tech Stack

- Python
- FAISS
- FastEmbed
- SentenceTransformers
- NumPy
- PyPDF
- python-docx
- Pytest
