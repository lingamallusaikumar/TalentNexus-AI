import re
from app.skills.service import SkillNormalizationEngine

# Standard gender-coded and aggressive jargon words for inclusive language check
MASCULINE_CODED_WORDS = {
    'rockstar', 'ninja', 'guru', 'dominant', 'aggressive', 'driven', 'fearless',
    'dominate', 'command', 'crush', 'assertive', 'superior', 'ruthless', 'hacker'
}

FEMININE_CODED_WORDS = {
    'supportive', 'compassionate', 'collaborative', 'nurturing', 'empathetic',
    'interpersonal', 'understanding', 'pleasant', 'warmth'
}

class JobDescriptionIntelligence:
    """AI engine for Job Description Quality, Skill Extraction, and Inclusive Language Analysis."""

    @classmethod
    def analyze_job_description(cls, title: str, description: str) -> dict:
        if not description or len(description.strip()) < 40:
            return {
                "quality_score": 20.0,
                "inclusive_score": 100.0,
                "extracted_skills": [],
                "warnings": ["Job description is too brief. Provide detailed responsibilities and requirements."],
                "inclusive_suggestions": []
            }

        extracted_skills = SkillNormalizationEngine.extract_skills_from_text(description)
        
        # 1. Inclusive Language Bias Check
        words = re.findall(r'\b[a-zA-Z]{3,}\b', description.lower())
        masculine_found = set(words).intersection(MASCULINE_CODED_WORDS)
        feminine_found = set(words).intersection(FEMININE_CODED_WORDS)
        
        bias_deductions = (len(masculine_found) * 15.0)
        inclusive_score = max(30.0, min(100.0, 100.0 - bias_deductions))
        
        inclusive_suggestions = []
        for word in masculine_found:
            inclusive_suggestions.append(f"Consider replacing overly aggressive or gender-coded term '{word}' with neutral phrasing.")

        # 2. Description Quality & Completeness
        quality_score = 0.0
        warnings = []
        
        # Has title
        if title and len(title.strip()) > 3:
            quality_score += 20.0
        else:
            warnings.append("Job title is missing or too vague.")
            
        # Length check
        desc_length = len(description.split())
        if desc_length >= 150:
            quality_score += 30.0
        elif desc_length >= 75:
            quality_score += 20.0
        else:
            warnings.append("Description is short. Ideal descriptions have at least 150-300 words.")

        # Skills found check
        if len(extracted_skills) >= 5:
            quality_score += 30.0
        elif len(extracted_skills) >= 2:
            quality_score += 15.0
        else:
            warnings.append("Few technical skills identified. Clearly list required tools and frameworks.")

        # Structure check (bullet points or sections)
        if any(marker in description for marker in ['•', '-', '*', 'Responsibilities', 'Requirements', 'Qualifications']):
            quality_score += 20.0
        else:
            warnings.append("Add bullet points to separate 'Responsibilities' from 'Requirements'.")

        quality_score = min(100.0, quality_score)

        return {
            "quality_score": round(quality_score, 1),
            "inclusive_score": round(inclusive_score, 1),
            "extracted_skills": extracted_skills,
            "detected_biases": {
                "masculine_coded": list(masculine_found),
                "feminine_coded": list(feminine_found)
            },
            "warnings": warnings,
            "inclusive_suggestions": inclusive_suggestions
        }
