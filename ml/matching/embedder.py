import logging

try:
    from sentence_transformers import SentenceTransformer
    import numpy as np
    from sklearn.metrics.pairwise import cosine_similarity
    _ML_AVAILABLE = True
except ImportError:
    _ML_AVAILABLE = False
    SentenceTransformer = None
    np = None
    cosine_similarity = None
    logging.warning("ML libraries (sentence-transformers/torch) not installed. Matching engine will use fallback mode.")

logger = logging.getLogger(__name__)

class SemanticEmbedder:
    _instance = None
    
    @classmethod
    def get_instance(cls):
        if cls._instance is None:
            cls._instance = cls()
        return cls._instance

    def __init__(self, model_name='all-MiniLM-L6-v2'):
        try:
            self.model = SentenceTransformer(model_name)
            logger.info(f"Loaded sentence transformer model: {model_name}")
        except Exception as e:
            logger.error(f"Failed to load sentence transformer model: {e}")
            self.model = None

    def encode(self, texts: list[str]) -> np.ndarray:
        if not self.model or not texts:
            return np.array([])
        return self.model.encode(texts)

    def calculate_similarity(self, text1: str, text2: str) -> float:
        if not text1 or not text2:
            return 0.0
        
        embeddings = self.encode([text1, text2])
        if len(embeddings) < 2:
            return 0.0
            
        sim = cosine_similarity([embeddings[0]], [embeddings[1]])
        return float(sim[0][0])
