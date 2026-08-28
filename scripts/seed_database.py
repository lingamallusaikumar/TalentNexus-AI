import os
import sys
from datetime import datetime, date, timedelta

# Ensure root path is in sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app import create_app
from app.extensions import db
from app.organizations.models import Organization, Department
from app.users.models import User, Role, Permission, RolePermission
from app.skills.models import Skill, SkillCategory, SkillAlias, SkillRelationship
from app.candidates.models import Candidate, Experience, Education, CandidateSkill
from app.jobs.models import Job, JobRequirement
from app.applications.models import Application, ApplicationHistory
from app.matching.services import evaluate_and_save_match

def seed_enterprise_data():
    app = create_app('dev')
    with app.app_context():
        print("🌱 Seeding TalentNexus AI Enterprise Database...")
        db.create_all()

        # 1. Seed Roles & Permissions
        roles_data = [
            ("Super Admin", "SUPER_ADMIN", "Full platform administrative access"),
            ("Organization Admin", "ORG_ADMIN", "Full access to organization tenant"),
            ("HR Manager", "HR_MANAGER", "Manages requisitions, hiring pipelines, and interviews"),
            ("Recruiter", "RECRUITER", "Screens resumes, moves stages, and evaluates matches"),
            ("Hiring Manager", "HIRING_MANAGER", "Reviews shortlisted candidates and conducts interviews"),
            ("Interviewer", "INTERVIEWER", "Submits scorecard ratings and interview feedback"),
            ("Candidate", "CANDIDATE", "Candidate applicant portal access")
        ]
        
        role_map = {}
        for name, code, desc in roles_data:
            role = Role.query.filter_by(code=code).first()
            if not role:
                role = Role(name=name, code=code, description=desc)
                db.session.add(role)
                db.session.commit()
            role_map[code] = role

        # 2. Seed Default Organization
        org = Organization.query.filter_by(name="Acme Technology Corp").first()
        if not org:
            org = Organization(
                name="Acme Technology Corp",
                slug="acme-tech",
                domain="acme.com",
                branding={"primary_color": "#3B82F6", "logo_url": "/static/images/logo.png"}
            )
            db.session.add(org)
            db.session.commit()

        # 3. Seed Users
        admin_user = User.query.filter_by(email="admin@acme.com").first()
        if not admin_user:
            admin_user = User(
                email="admin@acme.com",
                first_name="Eleanor",
                last_name="Vance",
                password="Password123!",
                role_id=role_map['ORG_ADMIN'].id,
                current_organization_id=org.id,
                is_active=True,
                is_verified=True
            )
            db.session.add(admin_user)
            db.session.commit()

        recruiter_user = User.query.filter_by(email="recruiter@acme.com").first()
        if not recruiter_user:
            recruiter_user = User(
                email="recruiter@acme.com",
                first_name="Marcus",
                last_name="Brody",
                password="Password123!",
                role_id=role_map['RECRUITER'].id,
                current_organization_id=org.id,
                is_active=True,
                is_verified=True
            )
            db.session.add(recruiter_user)
            db.session.commit()

        # 4. Seed Skill Categories & Canonical Taxonomy
        cat_backend = SkillCategory.query.filter_by(name="Backend Development").first() or SkillCategory(name="Backend Development")
        cat_ai = SkillCategory.query.filter_by(name="AI & Machine Learning").first() or SkillCategory(name="AI & Machine Learning")
        cat_devops = SkillCategory.query.filter_by(name="DevOps & Cloud").first() or SkillCategory(name="DevOps & Cloud")
        db.session.add_all([cat_backend, cat_ai, cat_devops])
        db.session.commit()

        skills_to_seed = [
            ("Python", "python", cat_backend.id, ["py", "python3"]),
            ("Flask", "flask", cat_backend.id, ["flask-restful"]),
            ("Django", "django", cat_backend.id, ["django-rest-framework"]),
            ("PostgreSQL", "postgresql", cat_backend.id, ["postgres", "pgsql"]),
            ("Redis", "redis", cat_backend.id, ["redis-cache"]),
            ("Celery", "celery", cat_backend.id, ["celery-worker"]),
            ("Docker", "docker", cat_devops.id, ["docker-compose"]),
            ("Kubernetes", "kubernetes", cat_devops.id, ["k8s"]),
            ("Machine Learning", "machine-learning", cat_ai.id, ["ml"]),
            ("PyTorch", "pytorch", cat_ai.id, ["torch"]),
            ("spaCy", "spacy", cat_ai.id, ["spacy-nlp"])
        ]

        for s_name, s_slug, c_id, aliases in skills_to_seed:
            sk = Skill.query.filter_by(slug=s_slug).first()
            if not sk:
                sk = Skill(name=s_name, slug=s_slug, category_id=c_id)
                db.session.add(sk)
                db.session.commit()
                for al in aliases:
                    db.session.add(SkillAlias(alias=al, canonical_skill_id=sk.id))
                db.session.commit()

        # 5. Seed Realistic Job Requisitions
        job1 = Job.query.filter_by(title="Senior Backend & ML Engineer").first()
        if not job1:
            job1 = Job(
                organization_id=org.id,
                created_by_user_id=admin_user.id,
                title="Senior Backend & ML Engineer",
                description="We are seeking an experienced Senior Backend & Machine Learning Engineer to design scalable Python microservices, implement distributed Celery task pipelines, and deploy Sentence-Transformer models for our real-time matching engine.",
                location="San Francisco, CA",
                is_remote=True,
                remote_type="FULLY_REMOTE",
                employment_type="FULL_TIME",
                salary_min=150000,
                salary_max=195000,
                status="PUBLISHED",
                description_quality_score=92.0,
                inclusive_language_score=98.0
            )
            db.session.add(job1)
            db.session.commit()

            reqs = [
                JobRequirement(job_id=job1.id, skill_name="Python", is_required=True, min_years_experience=4.0, weight=2.0),
                JobRequirement(job_id=job1.id, skill_name="Flask", is_required=True, min_years_experience=3.0, weight=1.5),
                JobRequirement(job_id=job1.id, skill_name="PostgreSQL", is_required=True, min_years_experience=3.0, weight=1.0),
                JobRequirement(job_id=job1.id, skill_name="Docker", is_required=True, min_years_experience=2.0, weight=1.0),
                JobRequirement(job_id=job1.id, skill_name="Machine Learning", is_required=False, min_years_experience=2.0, weight=1.5),
            ]
            db.session.add_all(reqs)
            db.session.commit()

        # 6. Seed Sample Candidates
        candidates_seed = [
            {
                "email": "alex.rivera@example.com",
                "first_name": "Alex",
                "last_name": "Rivera",
                "headline": "Staff Python & Machine Learning Architect",
                "summary": "Senior software engineer with 7+ years of experience architecting high-scale backend microservices using Python, Flask, Celery, and PostgreSQL. Extensive hands-on experience deploying PyTorch models.",
                "years": 7.0,
                "skills": ["Python", "Flask", "PostgreSQL", "Docker", "Machine Learning", "PyTorch", "Redis"]
            },
            {
                "email": "sarah.chen@example.com",
                "first_name": "Sarah",
                "last_name": "Chen",
                "headline": "Senior Full Stack Engineer",
                "summary": "Experienced engineer with 4 years building scalable web services in Python and TypeScript. Strong background with Flask and PostgreSQL databases.",
                "years": 4.0,
                "skills": ["Python", "Flask", "PostgreSQL", "JavaScript", "Docker"]
            }
        ]

        for c_data in candidates_seed:
            cand_user = User.query.filter_by(email=c_data['email']).first()
            if not cand_user:
                cand_user = User(
                    email=c_data['email'],
                    first_name=c_data['first_name'],
                    last_name=c_data['last_name'],
                    password="Password123!",
                    role_id=role_map['CANDIDATE'].id,
                    current_organization_id=org.id,
                    is_active=True,
                    is_verified=True
                )
                db.session.add(cand_user)
                db.session.commit()

                cand = Candidate(
                    user_id=cand_user.id,
                    first_name=c_data['first_name'],
                    last_name=c_data['last_name'],
                    email=c_data['email'],
                    headline=c_data['headline'],
                    summary=c_data['summary'],
                    years_of_experience=c_data['years'],
                    resume_quality_score=94.5,
                    location="San Francisco, CA"
                )
                db.session.add(cand)
                db.session.commit()

                for sk_name in c_data['skills']:
                    db.session.add(CandidateSkill(candidate_id=cand.id, skill_name=sk_name, years_of_experience=3.0))

                db.session.commit()

                # Evaluate match against Job 1
                evaluate_and_save_match(cand, job1)

                # Create ATS Application
                app_record = Application(candidate_id=cand.id, job_id=job1.id, current_stage="Shortlisted")
                db.session.add(app_record)
                db.session.commit()

        print("✅ Enterprise database seeded successfully with Multi-Tenancy, Taxonomies, Requisitions, and XAI Matches!")

if __name__ == '__main__':
    seed_enterprise_data()
