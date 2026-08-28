# Import all models across all domains for SQLAlchemy and Alembic migrations
from app.organizations.models import Organization, Workspace, Department, Team, OrganizationMembership, Invitation
from app.users.models import User, Role, Permission, RolePermission, UserSession, LoginHistory, PasswordResetToken
from app.candidates.models import (
    Candidate, Experience, Education, CandidateSkill, 
    CandidateCertification, CandidateLanguage, CandidateProject, 
    CandidateTag, CandidateNote, CandidateActivity
)
from app.skills.models import Skill, SkillCategory, SkillAlias, SkillRelationship
from app.jobs.models import Job, JobRequirement, JobTemplate, JobApproval, JobActivity
from app.resumes.models import Resume, ResumeProcessingJob
from app.matching.models import CandidateMatch, ScoringProfile, RankingHistory
from app.applications.models import Application, ApplicationHistory, RecruitmentPipeline, PipelineStage
from app.interviews.models import Interview, Interviewer, InterviewScorecardTemplate, InterviewFeedback
from app.assessments.models import Assessment, AssessmentQuestion, AssessmentAttempt
from app.workflows.models import WorkflowRule, WorkflowExecution
from app.events.models import EventLog
from app.audit.models import AuditLog, SecurityLog
from app.notifications.models import Notification, NotificationPreference
from app.integrations.models import ApiKey, WebhookEndpoint, WebhookDelivery
from app.ml_registry.models import MLModelRegistry, MLModelVersion, ModelInferenceLog
from app.admin.models import FeatureFlag, SystemConfig
