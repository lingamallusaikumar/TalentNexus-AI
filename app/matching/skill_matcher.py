from typing import List, Dict, Any

class SkillMatchScorer:
    """Calculates weighted similarity score between candidate skills and job requirements."""

    def __init__(self, required_weight: float = 0.7, bonus_weight: float = 0.3):
        self.required_weight = required_weight
        self.bonus_weight = bonus_weight

    def calculate_score(self, candidate_skills: List[str], required_skills: List[str], preferred_skills: List[str] = None) -> float:
        if not required_skills:
            return 100.0

        preferred_skills = preferred_skills or []
        c_skills_lower = {s.lower() for s in candidate_skills}

        matched_required = sum(1 for req in required_skills if req.lower() in c_skills_lower)
        req_score = (matched_required / len(required_skills)) * 100.0

        pref_score = 0.0
        if preferred_skills:
            matched_pref = sum(1 for pref in preferred_skills if pref.lower() in c_skills_lower)
            pref_score = (matched_pref / len(preferred_skills)) * 100.0

        total_score = (req_score * self.required_weight) + (pref_score * self.bonus_weight)
        return round(min(total_score, 100.0), 2)
