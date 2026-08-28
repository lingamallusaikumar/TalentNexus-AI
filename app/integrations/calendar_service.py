from datetime import datetime, timedelta

class CalendarIntegrationService:
    """Generates standard iCalendar (.ics) format payloads for Google Calendar and Outlook."""

    @classmethod
    def generate_ics_invite(cls, title: str, start_time: datetime, duration_minutes: int, location: str, description: str) -> str:
        end_time = start_time + timedelta(minutes=duration_minutes)
        
        fmt = "%Y%m%dT%H%M%SZ"
        ics_content = f"""BEGIN:VCALENDAR
VERSION:2.0
PRODID:-//TalentNexus AI//Recruitment Intelligence//EN
CALSCALE:GREGORIAN
METHOD:REQUEST
BEGIN:VEVENT
UID:tn-interview-{int(start_time.timestamp())}@talentnexus.ai
DTSTAMP:{datetime.utcnow().strftime(fmt)}
DTSTART:{start_time.strftime(fmt)}
DTEND:{end_time.strftime(fmt)}
SUMMARY:{title}
DESCRIPTION:{description}
LOCATION:{location or 'Remote / Online'}
STATUS:CONFIRMED
END:VEVENT
END:VCALENDAR"""
        return ics_content.strip()
