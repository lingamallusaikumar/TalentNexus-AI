import re

SECTION_HEADERS = {
    'summary': [
        'summary', 'professional summary', 'executive summary', 'about me', 'profile', 
        'career objective', 'objective', 'overview', 'personal profile'
    ],
    'skills': [
        'skills', 'technical skills', 'core competencies', 'expertise', 'technologies',
        'key skills', 'competencies', 'tech stack', 'tools & technologies', 'programming languages'
    ],
    'experience': [
        'experience', 'work experience', 'professional experience', 'employment history',
        'work history', 'career history', 'relevant experience', 'internships'
    ],
    'education': [
        'education', 'educational background', 'academic history', 'qualifications',
        'academic qualifications', 'degrees', 'education & training'
    ],
    'projects': [
        'projects', 'personal projects', 'key projects', 'academic projects',
        'portfolio', 'technical projects', 'open source contributions'
    ],
    'certifications': [
        'certifications', 'licenses', 'credentials', 'courses', 'professional certifications',
        'accreditations', 'certificates'
    ]
}

class ResumeSectionDetector:
    """Detects and isolates standard resume sections from unstructured raw text."""
    
    @classmethod
    def detect_sections(cls, text: str) -> dict[str, str]:
        if not text:
            return {}
            
        lines = [line.strip() for line in text.split('\n') if line.strip()]
        sections = {
            'header': '',
            'summary': '',
            'skills': '',
            'experience': '',
            'education': '',
            'projects': '',
            'certifications': '',
            'other': ''
        }
        
        current_section = 'header'
        section_content = {sec: [] for sec in sections}
        
        for line in lines:
            line_lower = line.lower()
            cleaned_line = re.sub(r'[^a-z0-9\s]', '', line_lower).strip()
            
            # Check if this line is a known section header
            matched_section = None
            if len(cleaned_line) < 40: # Section headers are short
                for sec_name, keywords in SECTION_HEADERS.items():
                    if cleaned_line in keywords or any(cleaned_line == kw for kw in keywords):
                        matched_section = sec_name
                        break
                    # Also check starts with/ends with for things like "1. Education" or "TECHNICAL SKILLS:"
                    if any(re.match(rf'^(?:[0-9]\.\s*)?{re.escape(kw)}[:\s]*$', cleaned_line) for kw in keywords):
                        matched_section = sec_name
                        break
                        
            if matched_section:
                current_section = matched_section
            else:
                section_content[current_section].append(line)
                
        # Join lines for each section
        return {sec: "\n".join(lines).strip() for sec, lines in section_content.items()}
