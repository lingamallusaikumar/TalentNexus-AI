from app.candidates.models import Candidate
from app.jobs.models import Job
from app.matching.services import evaluate_and_save_match
from ml.matching.embedder import SemanticEmbedder

class RecommendationEngine:
    """Enterprise AI Recommendation Engine for Candidate-to-Job, Job-to-Candidate, and Similar Candidate discovery."""

    @classmethod
    def recommend_jobs_for_candidate(cls, candidate_id: int, limit: int = 10) -> list[dict]:
        candidate = Candidate.query.get(candidate_id)
        if not candidate:
            return []
            
        published_jobs = Job.query.filter_by(status='PUBLISHED').all()
        recommendations = []
        
        for job in published_jobs:
            match = evaluate_and_save_match(candidate, job)
            if match.overall_score >= 50.0:
                recommendations.append({
                    "job_id": job.id,
                    "job_title": job.title,
                    "location": job.location,
                    "is_remote": job.is_remote,
                    "match_score": match.overall_score,
                    "recommendation": match.recommendation,
                    "strengths": match.explanation.get('strengths', []) if match.explanation else []
                })
                
        recommendations.sort(key=lambda x: x['match_score'], reverse=True)
        return recommendations[:limit]

    @classmethod
    def recommend_similar_candidates(cls, candidate_id: int, limit: int = 5) -> list[dict]:
        target = Candidate.query.get(candidate_id)
        if not target:
            return []
            
        embedder = SemanticEmbedder.get_instance()
        target_text = (target.headline or "") + " " + (target.summary or "") + " " + " ".join([s.skill_name for s in target.skills])
        
        all_candidates = Candidate.query.filter(Candidate.id != candidate_id, Candidate.is_deleted == False).all()
        similar = []
        
        for other in all_candidates:
            other_text = (other.headline or "") + " " + (other.summary or "") + " " + " ".join([s.skill_name for s in other.skills])
            sim = max(0.0, embedder.calculate_similarity(target_text, other_text)) * 100.0
            
            if sim >= 40.0:
                similar.append({
                    "candidate_id": other.id,
                    "name": f"{other.first_name or ''} {other.last_name or ''}".strip(),
                    "headline": other.headline,
                    "similarity_score": round(sim, 1)
                })
                
        similar.sort(key=lambda x: x['similarity_score'], reverse=True)
        return similar[:limit]
