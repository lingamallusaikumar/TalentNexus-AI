import re
from app.skills.service import SkillNormalizationEngine

EMAIL_REGEX = r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+'
PHONE_REGEX = r'(?:(?:\+?1\s*(?:[.-]\s*)?)?(?:\(\s*([2-9]1[02-9]|[2-9][02-8]1|[2-9][02-8][02-9])\s*\)|([2-9]1[02-9]|[2-9][02-8]1|[2-9][02-8][02-9]))\s*(?:[.-]\s*)?)?([2-9]1[02-9]|[2-9][02-9]1|[2-9][02-9]{2})\s*(?:[.-]\s*)?([0-9]{4})(?:\s*(?:#|x\.?|ext\.?|extension)\s*(\d+))?'
LINKEDIN_REGEX = r'https?:\/\/(?:www\.)?linkedin\.com\/in\/[a-zA-Z0-9_-]+'
GITHUB_REGEX = r'https?:\/\/(?:www\.)?github\.com\/[a-zA-Z0-9_-]+'

class StructuredResumeExtractor:
    """Extracts structured entities, contacts, skills, and experience items from resume text."""
    
    @classmethod
    def extract_contact_info(cls, text: str) -> dict:
        email_match = re.search(EMAIL_REGEX, text)
        phone_match = re.search(PHONE_REGEX, text)
        linkedin_match = re.search(LINKEDIN_REGEX, text)
        github_match = re.search(GITHUB_REGEX, text)
        
        return {
            "email": email_match.group(0) if email_match else None,
            "phone": phone_match.group(0) if phone_match else None,
            "linkedin_url": linkedin_match.group(0) if linkedin_match else None,
            "github_url": github_match.group(0) if github_match else None
        }

    @classmethod
    def estimate_years_of_experience(cls, experience_text: str) -> float:
        """Estimates total years of experience from date patterns e.g. 2018 - 2022 or Jan 2020 - Present."""
        if not experience_text:
            return 0.0
            
        years_found = re.findall(r'\b(19\d\d|20\d\d)\b', experience_text)
        if len(years_found) >= 2:
            try:
                int_years = sorted([int(y) for y in years_found])
                total = min(int_years[-1] - int_years[0], 35)
                return max(float(total), 1.0)
            except Exception:
                pass
        return 1.5 # default baseline fallback
