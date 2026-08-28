import re
from app.extensions import db
from app.skills.models import Skill, SkillAlias, SkillCategory

# Curated initial alias mapping for fast in-memory normalization fallback
DEFAULT_ALIASES = {
    'js': 'JavaScript',
    'ts': 'TypeScript',
    'py': 'Python',
    'postgres': 'PostgreSQL',
    'postgresql': 'PostgreSQL',
    'react': 'React',
    'reactjs': 'React',
    'node': 'Node.js',
    'nodejs': 'Node.js',
    'vue': 'Vue.js',
    'vuejs': 'Vue.js',
    'golang': 'Go',
    'k8s': 'Kubernetes',
    'aws': 'Amazon Web Services',
    'gcp': 'Google Cloud Platform',
    'azure': 'Microsoft Azure',
    'docker': 'Docker',
    'ml': 'Machine Learning',
    'ai': 'Artificial Intelligence',
    'nlp': 'Natural Language Processing',
    'cv': 'Computer Vision',
    'dl': 'Deep Learning',
    'flask': 'Flask',
    'django': 'Django',
    'fastapi': 'FastAPI',
    'spring': 'Spring Boot',
    'springboot': 'Spring Boot',
    'sql': 'SQL',
    'nosql': 'NoSQL',
    'mongo': 'MongoDB',
    'mongodb': 'MongoDB'
}

class SkillNormalizationEngine:
    """Enterprise skill normalizer and taxonomy resolver."""
    _alias_cache = {}

    @classmethod
    def load_cache(cls):
        try:
            aliases = SkillAlias.query.join(Skill).all()
            for a in aliases:
                cls._alias_cache[a.alias.lower()] = a.canonical_skill.name
        except Exception:
            cls._alias_cache = {k.lower(): v for k, v in DEFAULT_ALIASES.items()}

    @classmethod
    def normalize_skill(cls, raw_skill_name: str) -> str:
        if not raw_skill_name:
            return ""
        
        cleaned = raw_skill_name.strip()
        lower = cleaned.lower()
        
        if not cls._alias_cache:
            cls.load_cache()
            
        if lower in cls._alias_cache:
            return cls._alias_cache[lower]
        if lower in DEFAULT_ALIASES:
            return DEFAULT_ALIASES[lower]
            
        # Capitalize nicely if standard
        return cleaned.title() if len(cleaned) > 3 else cleaned.upper()

    @classmethod
    def extract_skills_from_text(cls, text: str) -> list[dict]:
        """Extracts and normalizes known skills from arbitrary resume or job text."""
        if not text:
            return []
            
        found_skills = {}
        # Ensure cache
        if not cls._alias_cache:
            cls.load_cache()

        all_target_skills = list(set(list(cls._alias_cache.keys()) + [s.lower() for s in DEFAULT_ALIASES.values()]))
        
        lower_text = " " + re.sub(r'[^a-zA-Z0-9\+\#\.]', ' ', text.lower()) + " "
        
        for skill_query in all_target_skills:
            # Word boundary check
            pattern = r'(?<![a-zA-Z0-9])' + re.escape(skill_query) + r'(?![a-zA-Z0-9])'
            if re.search(pattern, lower_text):
                canonical = cls.normalize_skill(skill_query)
                if canonical not in found_skills:
                    found_skills[canonical] = {
                        "skill_name": canonical,
                        "confidence": 0.95 if skill_query == canonical.lower() else 0.85
                    }
                    
        return list(found_skills.values())
