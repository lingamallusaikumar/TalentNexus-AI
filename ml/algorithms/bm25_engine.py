import math
import re
from typing import List, Dict

class BM25OkapiRanker:
    """
    BM25 (Best Matching 25) Okapi Probabilistic Text Retrieval and Relevance Scorer.
    Widely used in production search engines for keyword saturation and length normalization.
    """

    def __init__(self, k1: float = 1.5, b: float = 0.75):
        self.k1 = k1
        self.b = b
        self.corpus_size = 0
        self.avg_doc_len = 0
        self.doc_lengths = []
        self.doc_term_freqs = []
        self.idf = {}

    def fit(self, corpus: List[str]):
        self.corpus_size = len(corpus)
        self.doc_lengths = []
        self.doc_term_freqs = []
        
        total_len = 0
        term_doc_occurrences = {}

        for doc in corpus:
            tokens = self._tokenize(doc)
            length = len(tokens)
            self.doc_lengths.append(length)
            total_len += length
            
            freqs = {}
            for t in tokens:
                freqs[t] = freqs.get(t, 0) + 1
            self.doc_term_freqs.append(freqs)
            
            for t in set(tokens):
                term_doc_occurrences[t] = term_doc_occurrences.get(t, 0) + 1

        self.avg_doc_len = total_len / max(self.corpus_size, 1)

        # Calculate BM25 IDF
        for term, n_q in term_doc_occurrences.items():
            self.idf[term] = math.log((self.corpus_size - n_q + 0.5) / (n_q + 0.5) + 1.0)

    def score(self, query: str, doc_idx: int) -> float:
        query_tokens = self._tokenize(query)
        doc_len = self.doc_lengths[doc_idx]
        freqs = self.doc_term_freqs[doc_idx]
        score = 0.0

        for token in query_tokens:
            if token not in freqs or token not in self.idf:
                continue
            f_q = freqs[token]
            idf = self.idf[token]
            
            numerator = f_q * (self.k1 + 1.0)
            denominator = f_q + self.k1 * (1.0 - self.b + self.b * (doc_len / self.avg_doc_len))
            score += idf * (numerator / denominator)

        return float(round(score, 4))

    def _tokenize(self, text: str) -> List[str]:
        if not text: return []
        return [w.lower() for w in re.findall(r'\b[a-zA-Z0-9]{2,}\b', text)]
