import re
from app.skills.service import SkillNormalizationEngine

TECH_PATTERNS = [
    # Programming languages & Frameworks with versions e.g. Python 3.12, Java 21, Angular 17
    r'\b(?:python|java|c\+\+|c\#|javascript|typescript|golang|rust|kotlin|swift|ruby|php)\s*(?:[0-9]+(?:\.[0-9]+)*)?\b',
    # Frameworks & Libraries
    r'\b(?:flask|django|fastapi|spring\s*boot|react(?:\.js)?|vue(?:\.js)?|angular|express(?:\.js)?|next(?:\.js)?|nestjs)\b',
    # Databases & Queues
    r'\b(?:postgresql|postgres|mysql|mongodb|redis|rabbitmq|kafka|elasticsearch|cassandra|sqlite|dynamodb)\b',
    # Cloud & DevOps
    r'\b(?:docker|kubernetes|k8s|terraform|ansible|jenkins|github\s*actions|aws|gcp|azure)\b',
    # AI / ML
    r'\b(?:machine\s*learning|deep\s*learning|nlp|computer\s*vision|pytorch|tensorflow|scikit-learn|spacy|huggingface|llms?|transformers?)\b'
]

class CustomTechnicalNER:
    """Domain-specific Named Entity Recognizer for technical terms, frameworks, and tools."""

    @classmethod
    def extract_entities(cls, text: str) -> list[dict]:
        if not text:
            return []

        found_entities = {}
        for pattern in TECH_PATTERNS:
            matches = re.finditer(pattern, text, re.IGNORECASE)
            for m in matches:
                raw_match = m.group(0).strip()
                canonical = SkillNormalizationEngine.normalize_skill(raw_match)
                if canonical not in found_entities:
                    found_entities[canonical] = {
                        "text": canonical,
                        "label": "TECHNICAL_SKILL",
                        "start_char": m.start(),
                        "end_char": m.end(),
                        "confidence": 0.96
                    }
                    
        return list(found_entities.values())
