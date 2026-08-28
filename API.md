# TalentNexus AI — API Reference (`v1`)

All endpoints are prefixed with `/api/v1` and require `Authorization: Bearer <JWT_TOKEN>` unless stated otherwise.

## 1. Authentication & Users
- `POST /api/v1/auth/register` — Register new user and organization.
- `POST /api/v1/auth/login` — Authenticate and receive JWT token.
- `GET /api/v1/auth/me` — Retrieve currently authenticated user context.

## 2. Candidate Domain
- `GET /api/v1/candidates` — Paginated list of candidate profiles with optional search query (`?page=1&per_page=20&search=python`).
- `GET /api/v1/candidates/{id}` — Detailed candidate profile, experiences, educations, skills, and quality breakdown.

## 3. Job Domain
- `GET /api/v1/jobs` — List jobs filtered by organization and status (`?status=PUBLISHED`).
- `POST /api/v1/jobs` — Create new job with automated AI description analysis and skill extraction.

## 4. Resume Processing
- `POST /api/v1/resumes/upload` — Upload PDF/DOCX/TXT resume file and enqueue asynchronous Celery parsing job.

## 5. Candidate Matching & Ranking
- `POST /api/v1/matches/evaluate` — Trigger multi-factor scoring for candidate against job.
- `GET /api/v1/matches/job/{id}/rankings` — Retrieve live candidate leaderboard with XAI factor breakdown.
- `POST /api/v1/matches/override` — Human recruiter decision override for AI audit compliance.

## 6. ATS Pipeline & Applications
- `POST /api/v1/applications/apply` — Submit candidate application to job.
- `POST /api/v1/applications/{id}/move-stage` — Move candidate across recruitment stages (`Applied` -> `Shortlisted` -> `Interview`).

## 7. Natural Language Semantic Search & Recommendations
- `GET /api/v1/search/candidates?q=...` — Natural language candidate search query.
- `GET /api/v1/search/recommendations/jobs/{candidate_id}` — Candidate-to-Job recommendations.
- `GET /api/v1/search/recommendations/similar-candidates/{candidate_id}` — Similar candidate discovery.

## 8. Analytics & Funnel Metrics
- `GET /api/v1/analytics/funnel` — Funnel stage counts, active job metrics, and shortlisting rate.
