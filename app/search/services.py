import re
from app.candidates.models import Candidate, CandidateSkill
from app.jobs.models import Job
from ml.matching.embedder import SemanticEmbedder
from app.skills.service import SkillNormalizationEngine

class SemanticSearchEngine:
    """
    Parses natural language recruiter queries e.g.:
    'Find backend Python developers with machine learning experience and more than 3 years of experience in San Francisco'
    Extracts filters (skills, years of exp, location) and combines with vector similarity.
    """

    @classmethod
    def search_candidates(cls, query: str, organization_id: int = None, limit: int = 20) -> list[dict]:
        if not query:
            return []

        embedder = SemanticEmbedder.get_instance()
        
        # 1. Extract explicit filters from query
        extracted_skills = [s['skill_name'].lower() for s in SkillNormalizationEngine.extract_skills_from_text(query)]
        
        # Extract years of experience requirement e.g. "more than 3 years", "5+ years", "3 yrs"
        exp_match = re.search(r'(\d+)\+?\s*(?:years?|yrs?)', query.lower())
        min_years = float(exp_match.group(1)) if exp_match else 0.0
        
        # 2. Query candidates from DB
        candidates_query = Candidate.query.filter(Candidate.is_deleted == False)
        if min_years > 0:
            candidates_query = candidates_query.filter(Candidate.years_of_experience >= min_years)
            
        candidates = candidates_query.all()
        
        results = []
        for cand in candidates:
            # Calculate skill overlap score
            cand_skill_names = {s.skill_name.lower() for s in cand.skills}
            matched_skills = [s for s in extracted_skills if s in cand_skill_names]
            
            skill_score = (len(matched_skills) / len(extracted_skills)) * 100.0 if extracted_skills else 50.0
            
            # Vector semantic score
            cand_profile_text = (cand.headline or "") + " " + (cand.summary or "") + " " + " ".join([s.skill_name for s in cand.skills])
            semantic_score = embedder.calculate_similarity(query, cand_profile_text) * 100.0
            semantic_score = max(0.0, semantic_score)
            
            # Hybrid search score
            final_score = round((skill_score * 0.5) + (semantic_score * 0.5), 1)
            
            results.append({
                "candidate_id": cand.id,
                "name": f"{cand.first_name or ''} {cand.last_name or ''}".strip(),
                "headline": cand.headline,
                "location": cand.location,
                "years_of_experience": cand.years_of_experience,
                "search_relevance_score": final_score,
                "matched_query_skills": matched_skills
            })
            
        # Sort by relevance
        results.sort(key=lambda x: x['search_relevance_score'], reverse=True)
        return results[:limit]
