import contractions
import re
import random

PHRASE_EXPANSIONS = {
    "peak load": [
        "high traffic",
        "heavy workloads",
        "traffic spikes"
    ],

    "cloud computing": [
        "distributed systems",
        "virtual infrastructure"
    ]
}


WORD_EXPANSIONS = {
    "aws": [
        "Amazon Web Services"
    ],

    "ec2": [
        "Elastic Compute Cloud(EC2)"
    ],

    "s3": [
        "Simple Storage Service(S3)"
    ],

    "sdk": [
        "Software Development Kits"
    ],

    "ebs": [
        "Elastic Block Store(EBS)"
    ],

    "vpc": [
        "Virtual Private Cloud(VPC)"
    ],

    "dns": [
        "Domain Name System"
    ],

    "iam": [
        "Identity and Access Management(IAM)"
    ],

    "saas": [
        "Software as a Service"
    ],

    "iaas": [
        "Infrastructure as a Service"
    ],

    "paas": [
        "Platform as a Service"
    ],

    "cli": [
        "Command Line Interface(CLI)"
    ],

    "infra": [
        "Infrastructure"
    ],

    "auth": [
        "Authorization"
    ],

    "scale": [
        "scalability"
    ],

    "performance": [
        "throughput"
    ],

    "security": [
        "authentication"
    ],

    "deploy": [
        "deployment"
    ],

    "cloud": [
        "cloud computing"
    ],

    "infrastructure": [
        "compute resources"
    ],

    "handle": [
        "manage"
    ]
}

class MockResponse:
    """Mocks the response object returned by Vertex AI's generate_content."""
    def __init__(self, text: str):
        self.text = text

class GenerativeModel:
    """
    Mocked version of vertexai.language_models.GenerativeModel.
    """
    def __init__(self, model_name: str = "gemini-pro"):
        self.model_name = model_name
        self.phrase_expansions = PHRASE_EXPANSIONS
        self.word_expansions = WORD_EXPANSIONS

    def generate_content(self, prompt: str) -> MockResponse:
        """
        Simulates the model rewriting the query.
        """
        expanded_text = self._expand_logic(prompt)
        return MockResponse(expanded_text)

    def _expand_logic(self, query: str) -> str:
        """The internal semantic rewriting logic."""
        query = contractions.fix(query.lower())
        enhanced_query = query

        for phrase, replacements in self.phrase_expansions.items():
            if phrase in enhanced_query:
                replacement = replacements[0]
                enhanced_query = enhanced_query.replace(phrase, replacement)

        words = re.findall(r"\b\w+\b", enhanced_query)
        rewritten_words = []

        for word in words:
            if word in self.word_expansions:
                replacement = self.word_expansions[word][0]
                rewritten_words.append(replacement)
            else:
                rewritten_words.append(word)

        return " ".join(rewritten_words)


if __name__ == "__main__":

    model = GenerativeModel()

    query = "How does aws store data?"

    response = model.generate_content(query)

    print("Original Query:")
    print(query)

    print("\nExpanded Query:")
    print(response.text)