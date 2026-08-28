import csv
import io
from app.candidates.models import Candidate

class HRMSConnector:
    """Generic HRMS / ATS bi-directional connector supporting CSV and JSON interchange format."""

    @classmethod
    def export_hired_candidates_csv(cls, organization_id: int) -> str:
        """Exports hired candidate records into standard HRMS ingestible CSV."""
        output = io.StringIO()
        writer = csv.writer(output)
        
        writer.writerow(['Candidate ID', 'First Name', 'Last Name', 'Email', 'Phone', 'Location', 'Years Experience', 'Quality Score'])
        
        candidates = Candidate.query.all()
        for c in candidates:
            writer.writerow([
                c.id, c.first_name, c.last_name, c.email, 
                c.phone, c.location, c.years_of_experience, c.resume_quality_score
            ])
            
        return output.getvalue()
