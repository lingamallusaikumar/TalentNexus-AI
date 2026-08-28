from app.jobs.models import Job
from ml.matching.embedder import SemanticEmbedder

class DuplicateJobDetector:
    """Identifies duplicate or redundant job requisitions within an organization."""

    @classmethod
    def check_duplicate_job(cls, organization_id: int, new_title: str, new_description: str, exclude_job_id: int = None) -> list[dict]:
        existing_jobs = Job.query.filter_by(organization_id=organization_id, is_deleted=False)
        if exclude_job_id:
            existing_jobs = existing_jobs.filter(Job.id != exclude_job_id)
            
        jobs = existing_jobs.all()
        embedder = SemanticEmbedder.get_instance()
        duplicates = []
        
        for job in jobs:
            title_sim = 1.0 if job.title.lower() == new_title.lower() else 0.0
            desc_sim = embedder.calculate_similarity(new_description[:1500], job.description[:1500])
            
            combined_sim = (title_sim * 0.4) + (desc_sim * 0.6)
            if combined_sim >= 0.75:
                duplicates.append({
                    "job_id": job.id,
                    "job_title": job.title,
                    "status": job.status,
                    "similarity_score": round(combined_sim * 100.0, 1),
                    "created_at": str(job.created_at)
                })
                
        duplicates.sort(key=lambda x: x['similarity_score'], reverse=True)
        return duplicates
