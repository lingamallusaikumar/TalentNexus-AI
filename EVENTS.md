# TalentNexus AI — Event System & Sourcing

## Published Domain Events

| Event Name | Trigger | Payload |
|---|---|---|
| `resume.uploaded` | Resume file uploaded to API | `{resume_id, candidate_id, file_type}` |
| `resume.parsing.started` | Celery worker dequeues parsing job | `{resume_id, job_id}` |
| `resume.parsed` | Text and entities extracted | `{candidate_id, quality_score, skills_count}` |
| `candidate.profile.updated` | Candidate edits profile | `{candidate_id, fields_updated}` |
| `job.created` | New requisition published | `{job_id, title, organization_id}` |
| `candidate.match.completed` | Hybrid score computed | `{candidate_id, job_id, score, recommendation}` |
| `candidate.score.updated` | Match score mutated | `{candidate_id, job_id, score}` |
| `candidate.rank.changed` | Leaderboard order shifted | `{job_id, candidate_id, new_rank}` |
| `interview.scheduled` | Interview round booked | `{interview_id, application_id, scheduled_at}` |
| `assessment.completed` | Candidate finishes assessment | `{attempt_id, percentage_score, is_passed}` |
| `notification.created` | System notice dispatched | `{user_id, title, notification_type}` |
