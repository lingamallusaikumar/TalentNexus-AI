import pytest
from app.skills.service import SkillNormalizationEngine
from ml.job_intelligence.analyzer import JobDescriptionIntelligence
from ml.quality_analysis.analyzer import ResumeQualityAnalyzer
from app.search.services import SemanticSearchEngine
from app.deduplication.services import DuplicateDetectionEngine
from ml.skill_gap.analyzer import SkillGapAnalyzer
from app.events.bus import EventBus, EVENT_CANDIDATE_MATCH_COMPLETED
from app.audit.service import log_audit, log_security
from app.audit.models import AuditLog, SecurityLog
from app.events.models import EventLog
from app.extensions import db

def test_skill_normalization_engine():
    # Test canonical resolving
    assert SkillNormalizationEngine.normalize_skill("js") == "JavaScript"
    assert SkillNormalizationEngine.normalize_skill("py") == "Python"
    assert SkillNormalizationEngine.normalize_skill("postgres") == "PostgreSQL"
    assert SkillNormalizationEngine.normalize_skill("k8s") == "Kubernetes"
    
    # Test extraction
    text = "Experienced Senior Python developer specializing in Flask, PostgreSQL, and Docker."
    skills = SkillNormalizationEngine.extract_skills_from_text(text)
    skill_names = [s['skill_name'] for s in skills]
    assert "Python" in skill_names
    assert "Flask" in skill_names
    assert "PostgreSQL" in skill_names
    assert "Docker" in skill_names

def test_job_description_intelligence():
    jd_text = """
    We are seeking a rockstar ninja developer who is dominant in backend architecture.
    Responsibilities:
    - Build scalable APIs using Python and Flask.
    - Maintain PostgreSQL databases.
    Requirements:
    - 4+ years of Python development.
    - Strong Docker experience.
    """
    analysis = JobDescriptionIntelligence.analyze_job_description("Senior Backend Engineer", jd_text)
    assert analysis['quality_score'] > 50
    # Check masculine coded detection
    assert 'rockstar' in analysis['detected_biases']['masculine_coded']
    assert 'ninja' in analysis['detected_biases']['masculine_coded']
    assert analysis['inclusive_score'] < 100

def test_resume_quality_analyzer():
    resume_text = """
    Jane Doe
    jane.doe@example.com | (555) 123-4567 | linkedin.com/in/janedoe
    
    Professional Summary
    Results-driven Software Engineer with 5+ years of experience building high-scale distributed systems.
    
    Technical Skills
    Python, Flask, PostgreSQL, Docker, Redis, Kubernetes
    
    Work Experience
    Senior Developer at TechCorp (2020 - Present)
    - Architected and deployed microservices reducing API latency by 45%.
    - Managed a team of 4 engineers and automated CI/CD pipelines.
    
    Education
    Bachelor of Science in Computer Science - University of California (2016 - 2020)
    """
    report = ResumeQualityAnalyzer.analyze(resume_text)
    assert report['overall_score'] >= 75.0
    assert len(report['strengths']) >= 3
    assert report['breakdown']['completeness_score'] == 100.0

def test_event_bus_and_audit_logging(app):
    with app.app_context():
        # Test Audit log
        log_audit(action='CREATE', resource_type='Job', resource_id=1, changes={'title': 'Dev'})
        audit = AuditLog.query.filter_by(action='CREATE').first()
        assert audit is not None
        assert audit.resource_type == 'Job'
        
        # Test Security log
        log_security(event_type='LOGIN_FAILED', severity='WARNING', details={'email': 'bad@test.com'})
        sec = SecurityLog.query.filter_by(event_type='LOGIN_FAILED').first()
        assert sec is not None
        assert sec.severity == 'WARNING'
        
        # Test EventBus logging
        EventBus.publish(event_name=EVENT_CANDIDATE_MATCH_COMPLETED, entity_type='Job', entity_id=1, payload={'score': 92})
        ev = EventLog.query.filter_by(event_name=EVENT_CANDIDATE_MATCH_COMPLETED).first()
        assert ev is not None
        assert ev.payload['score'] == 92
