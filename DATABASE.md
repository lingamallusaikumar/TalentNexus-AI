# TalentNexus AI — Database Schema & Architecture

The database is built on PostgreSQL with SQLAlchemy ORM, incorporating strict referential integrity, cascading rules, soft deletes, and high-performance indexing.

## Entity Relationship Overview

### 1. Multi-Tenant & Identity
- `organizations` — Top-level tenant container.
- `workspaces` — Division/workspace isolation.
- `departments` — Internal corporate departments.
- `teams` — Functional teams within departments.
- `organization_memberships` — User-to-organization RBAC junction.
- `invitations` — Pending and accepted organization invitations.
- `users` — Primary user identity.
- `roles` & `permissions` & `role_permissions` — Fine-grained RBAC matrix.
- `user_sessions` & `login_histories` & `password_reset_tokens` — Security and device tracking.

### 2. Candidate Domain
- `candidates` — Candidate profile with summary, headline, contact, and quality scores.
- `experiences` — Work history with achievements and date ranges.
- `educations` — Academic qualifications and degrees.
- `candidate_skills` — Extracted skills with confidence and proficiency ratings.
- `candidate_certifications`, `candidate_languages`, `candidate_projects` — Portfolio records.
- `candidate_tags`, `candidate_notes`, `candidate_activities` — Recruiter collaboration tools.

### 3. Skill Intelligence
- `skills` — Canonical taxonomy.
- `skill_categories` — Skill classifications (Frontend, Backend, DevOps, Data Science).
- `skill_aliases` — Synonyms (e.g. `py` -> `Python`).
- `skill_relationships` — Graph relationships (e.g. `Flask` -> `Python`).

### 4. Job Requisitions
- `jobs` — Job listings with salary, location, remote settings, and quality scores.
- `job_requirements` — Weighted mandatory and preferred skills.
- `job_templates` & `job_approvals` & `job_activities` — Requisition lifecycle.

### 5. AI Matching & Ranking
- `candidate_matches` — Calculated hybrid scores, XAI explanations, and human overrides.
- `scoring_profiles` — Configurable organization weighting profiles.
- `ranking_histories` — Position shift logs for candidate leaderboards.

### 6. ATS Pipeline & Interviews
- `recruitment_pipelines` & `pipeline_stages` — Custom hiring pipelines with SLA limits.
- `applications` & `application_history` — Candidate application tracking.
- `interviews` & `interviewers` & `interview_scorecard_templates` & `interview_feedback` — Multi-round scorecards.
- `assessments` & `assessment_questions` & `assessment_attempts` — Technical test evaluations.

### 7. Governance, Integrations & ML
- `event_logs`, `audit_logs`, `security_logs` — Complete compliance audit stream.
- `workflow_rules`, `workflow_executions` — Automation rules.
- `notifications`, `notification_preferences` — Multi-channel messaging.
- `api_keys`, `webhook_endpoints`, `webhook_deliveries` — Integration hub.
- `ml_model_registries`, `ml_model_versions`, `model_inference_logs` — ML lifecycle.
- `feature_flags`, `system_configs` — Dynamic platform administration.
