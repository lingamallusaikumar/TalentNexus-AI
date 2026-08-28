import math
import re
from collections import Counter
from typing import List, Dict

class TFIDFRelevanceEngine:
    """
    In-memory Term Frequency - Inverse Document Frequency (TF-IDF) Vectorizer
    and Cosine Matrix similarity calculator implemented from scratch.
    """

    def __init__(self):
        self.vocabulary = {}
        self.idf = {}
        self.doc_count = 0

    def fit(self, corpus: List[str]):
        self.doc_count = len(corpus)
        doc_term_freqs = []
        all_terms = set()

        for doc in corpus:
            tokens = self._tokenize(doc)
            unique_tokens = set(tokens)
            all_terms.update(unique_tokens)
            doc_term_freqs.append(unique_tokens)

        self.vocabulary = {term: idx for idx, term in enumerate(sorted(all_terms))}
        
        # Calculate IDF
        for term in self.vocabulary:
            doc_freq = sum(1 for doc_tokens in doc_term_freqs if term in doc_tokens)
            self.idf[term] = math.log((self.doc_count + 1) / (doc_freq + 1)) + 1.0

    def transform(self, doc: str) -> Dict[str, float]:
        tokens = self._tokenize(doc)
        token_counts = Counter(tokens)
        total_tokens = len(tokens) or 1
        
        vector = {}
        for token, count in token_counts.items():
            if token in self.idf:
                tf = count / total_tokens
                vector[token] = tf * self.idf[token]
                
        # L2 Normalize
        norm = math.sqrt(sum(v ** 2 for v in vector.values())) or 1.0
        return {k: v / norm for k, v in vector.items()}

    def calculate_cosine_similarity(self, doc1: str, doc2: str) -> float:
        v1 = self.transform(doc1)
        v2 = self.transform(doc2)
        
        common_terms = set(v1.keys()).intersection(set(v2.keys()))
        dot_product = sum(v1[term] * v2[term] for term in common_terms)
        return float(round(max(0.0, min(1.0, dot_product)), 4))

    def _tokenize(self, text: str) -> List[str]:
        if not text: return []
        cleaned = re.sub(r'[^a-zA-Z0-9\s]', ' ', text.lower())
        return [w for w in cleaned.split() if len(w) > 2]
