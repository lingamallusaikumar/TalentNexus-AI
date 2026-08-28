import difflib
from ml.matching.embedder import SemanticEmbedder

class FuzzyCandidateMatcher:
    """Calculates multi-dimensional fuzzy similarity across candidate profile fields."""

    @classmethod
    def calculate_name_similarity(cls, name1: str, name2: str) -> float:
        if not name1 or not name2:
            return 0.0
        n1 = " ".join(name1.lower().split())
        n2 = " ".join(name2.lower().split())
        return difflib.SequenceMatcher(None, n1, n2).ratio()

    @classmethod
    def calculate_text_similarity(cls, text1: str, text2: str) -> float:
        if not text1 or not text2:
            return 0.0
        embedder = SemanticEmbedder.get_instance()
        return max(0.0, embedder.calculate_similarity(text1[:1500], text2[:1500]))
