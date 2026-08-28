import json
from ml.matching.embedder import SemanticEmbedder

def calculate_candidate_match(candidate, job) -> dict:
    """
    Calculates a hybrid match score between a candidate and a job.
    Returns a dictionary with the score and explainable reasons.
    """
    embedder = SemanticEmbedder.get_instance()
    
    # 1. Semantic Job Description vs Resume Text similarity (Weight: 20%)
    semantic_score = 0.0
    if candidate.summary and job.description:
        # In a real app, we'd use candidate.resumes[0].raw_text if available
        semantic_score = embedder.calculate_similarity(candidate.summary, job.description)
        semantic_score = max(0.0, semantic_score) # Ensure no negative
        
    # 2. Hard Skills Match (Weight: 80%)
    reqs = job.requirements
    cand_skills = {s.skill_name.lower(): s for s in candidate.skills}
    
    skill_score = 0.0
    matched_skills = []
    missing_skills = []
    
    total_weight = sum([r.weight for r in reqs]) if reqs else 0
    
    if total_weight > 0:
        earned_weight = 0.0
        for req in reqs:
            # We do a basic exact/lower match here, but we could use embeddings for alias mapping
            if req.skill_name.lower() in cand_skills:
                earned_weight += req.weight
                matched_skills.append(req.skill_name)
            else:
                if req.is_required:
                    missing_skills.append(req.skill_name)
        
        skill_score = earned_weight / total_weight

    # Final Hybrid Score
    # For this phase: 80% explicit skills, 20% semantic similarity
    final_score = (skill_score * 0.8) + (semantic_score * 0.2)
    final_percentage = min(100.0, final_score * 100)
    
    # Generate Explanation
    explanation = {
        "overall_score": round(final_percentage, 2),
        "strengths": [f"Matches required skill: {s}" for s in matched_skills],
        "weaknesses": [f"Missing required skill: {s}" for s in missing_skills],
        "semantic_similarity_percentage": round(semantic_score * 100, 2),
        "recommendation": "SHORTLIST" if final_percentage >= 75 else "REVIEW"
    }
    
    return {
        "score": final_percentage,
        "explanation": explanation
    }
