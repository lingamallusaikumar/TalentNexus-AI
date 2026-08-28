import re
from ml.resume_parser.section_detector import ResumeSectionDetector
from ml.resume_parser.structured_extractor import StructuredResumeExtractor
from app.skills.service import SkillNormalizationEngine

# Action verbs that indicate strong accomplishment-oriented bullet points
ACTION_VERBS = {
    'developed', 'engineered', 'architected', 'spearheaded', 'managed', 'led',
    'created', 'implemented', 'designed', 'optimized', 'reduced', 'increased',
    'automated', 'built', 'delivered', 'launched', 'scaled', 'refactored',
    'collaborated', 'analyzed', 'orchestrated', 'deployed', 'maintained'
}

class ResumeQualityAnalyzer:
    """
    Evaluates a resume and generates a 0-100 Quality Score with deep explainable metrics:
    - Completeness (contact info, sections present)
    - Action Verb & Impact Language Strength
    - Metric/Quantifiable Achievement density
    - Skill clarity & modern tech stack coverage
    - Length & Readability
    """

    @classmethod
    def analyze(cls, raw_text: str) -> dict:
        if not raw_text or len(raw_text.strip()) < 50:
            return {
                "overall_score": 10.0,
                "breakdown": {
                    "completeness_score": 10.0,
                    "impact_score": 0.0,
                    "metrics_score": 0.0,
                    "skill_clarity_score": 10.0,
                    "structure_score": 10.0
                },
                "strengths": [],
                "improvements": ["Resume is too short or unreadable. Upload a complete resume."]
            }

        sections = ResumeSectionDetector.detect_sections(raw_text)
        contacts = StructuredResumeExtractor.extract_contact_info(raw_text)
        skills = SkillNormalizationEngine.extract_skills_from_text(raw_text)
        
        strengths = []
        improvements = []
        
        # 1. Completeness Score (Weight: 25%)
        completeness = 0
        if contacts.get('email'): completeness += 25
        else: improvements.append("Add a professional email address.")
        
        if contacts.get('phone'): completeness += 25
        else: improvements.append("Add a valid contact phone number.")
        
        if contacts.get('linkedin_url') or contacts.get('github_url'): 
            completeness += 25
            strengths.append("Includes relevant professional links (LinkedIn / GitHub).")
        else:
            improvements.append("Include links to your LinkedIn or GitHub profile.")
            
        if len(sections.get('summary', '')) > 30: 
            completeness += 25
            strengths.append("Has a concise professional summary.")
        else:
            improvements.append("Add a 2-3 sentence executive summary highlighting core expertise.")

        # 2. Structure & Sections Score (Weight: 20%)
        structure_points = 0
        essential_sections = ['skills', 'experience', 'education']
        for sec in essential_sections:
            if len(sections.get(sec, '')) > 20:
                structure_points += 33.33
            else:
                improvements.append(f"Missing distinct '{sec.title()}' section.")
        structure_score = min(100.0, structure_points)

        # 3. Action Verbs & Impact Score (Weight: 20%)
        exp_text = sections.get('experience', '') + " " + sections.get('projects', '')
        words = [w.lower() for w in re.findall(r'\b[a-zA-Z]{3,}\b', exp_text)]
        found_action_verbs = set(words).intersection(ACTION_VERBS)
        
        action_verb_count = len(found_action_verbs)
        impact_score = min(100.0, (action_verb_count / 8.0) * 100.0)
        if action_verb_count >= 5:
            strengths.append(f"Uses strong action verbs ({', '.join(list(found_action_verbs)[:4])}).")
        else:
            improvements.append("Begin bullet points with strong action verbs (e.g., Engineered, Scaled, Architected).")

        # 4. Metrics & Quantifiable Achievements (Weight: 15%)
        # Check for numbers, percentages, dollar signs, multipliers e.g. "reduced latency by 40%", "managed 5 engineers"
        metric_matches = re.findall(r'(\d+%\s*|\$\s*\d+|\b\d+x\b|\b\d+\+\b|\b\d+\s*(?:users|clients|requests|ms|seconds|teams|engineers|services)\b)', exp_text.lower())
        metrics_score = min(100.0, len(metric_matches) * 20.0)
        if len(metric_matches) >= 3:
            strengths.append("Highlights quantifiable achievements with concrete metrics and statistics.")
        else:
            improvements.append("Quantify your achievements (e.g., 'Improved query performance by 35%').")

        # 5. Skill Clarity Score (Weight: 20%)
        skill_count = len(skills)
        skill_score = min(100.0, (skill_count / 10.0) * 100.0)
        if skill_count >= 6:
            strengths.append(f"Clear presentation of technical skills ({skill_count} detected).")
        else:
            improvements.append("List relevant technical tools, frameworks, and programming languages clearly.")

        # Calculate Final Weighted Score
        overall = (
            (completeness * 0.25) +
            (structure_score * 0.20) +
            (impact_score * 0.20) +
            (metrics_score * 0.15) +
            (skill_score * 0.20)
        )
        overall_score = round(max(10.0, min(100.0, overall)), 1)

        return {
            "overall_score": overall_score,
            "breakdown": {
                "completeness_score": round(completeness, 1),
                "structure_score": round(structure_score, 1),
                "impact_score": round(impact_score, 1),
                "metrics_score": round(metrics_score, 1),
                "skill_clarity_score": round(skill_score, 1)
            },
            "strengths": strengths,
            "improvements": improvements
        }
