import pytest
from app.matching.skill_matcher import SkillMatchScorer

def test_skill_match_scorer_full_match():
    scorer = SkillMatchScorer()
    candidate_skills = ["Python", "FastAPI", "Docker", "PostgreSQL"]
    required_skills = ["Python", "FastAPI"]
    preferred_skills = ["Docker"]
    score = scorer.calculate_score(candidate_skills, required_skills, preferred_skills)
    assert score == 100.0

def test_skill_match_scorer_partial_match():
    scorer = SkillMatchScorer(required_weight=0.7, bonus_weight=0.3)
    candidate_skills = ["Python", "Git"]
    required_skills = ["Python", "React"]
    preferred_skills = ["Docker"]
    score = scorer.calculate_score(candidate_skills, required_skills, preferred_skills)
    # req_score = (1/2)*100 = 50 -> 50 * 0.7 = 35.0
    assert score == 35.0
