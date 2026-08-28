from app.candidates.models import Candidate
from app.extensions import db
from ml.matching.embedder import SemanticEmbedder
import difflib

class DuplicateDetectionEngine:
    """
    Multi-attribute duplicate candidate detection using:
    - Exact email match
    - Phone number match
    - Fuzzy name similarity
    - Resume text cosine similarity
    """

    @classmethod
    def find_potential_duplicates(cls, candidate_id: int) -> list[dict]:
        target = Candidate.query.get(candidate_id)
        if not target:
            return []

        duplicates = []
        all_cands = Candidate.query.filter(Candidate.id != candidate_id, Candidate.is_deleted == False).all()
        embedder = SemanticEmbedder.get_instance()

        for cand in all_cands:
            match_reasons = []
            confidence = 0.0
            
            # 1. Email check
            if target.email and cand.email and target.email.lower() == cand.email.lower():
                match_reasons.append("Exact Email Match")
                confidence += 0.60
                
            # 2. Phone check
            if target.phone and cand.phone and target.phone == cand.phone:
                match_reasons.append("Exact Phone Number Match")
                confidence += 0.50

            # 3. Fuzzy Name match
            target_name = f"{target.first_name} {target.last_name}".strip().lower()
            cand_name = f"{cand.first_name} {cand.last_name}".strip().lower()
            if target_name and cand_name:
                name_sim = difflib.SequenceMatcher(None, target_name, cand_name).ratio()
                if name_sim > 0.85:
                    match_reasons.append(f"Name Match ({round(name_sim * 100)}% similarity)")
                    confidence += 0.30

            # 4. Resume text similarity
            if target.resumes and cand.resumes and target.resumes[0].raw_text and cand.resumes[0].raw_text:
                sim = embedder.calculate_similarity(target.resumes[0].raw_text[:1500], cand.resumes[0].raw_text[:1500])
                if sim > 0.88:
                    match_reasons.append(f"High Resume Semantic Overlap ({round(sim * 100)}%)")
                    confidence += 0.40

            if confidence >= 0.50:
                duplicates.append({
                    "candidate_id": cand.id,
                    "name": f"{cand.first_name or ''} {cand.last_name or ''}".strip(),
                    "email": cand.email,
                    "confidence_score": min(1.0, round(confidence, 2)),
                    "match_reasons": match_reasons
                })

        duplicates.sort(key=lambda x: x['confidence_score'], reverse=True)
        return duplicates
