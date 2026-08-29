from datetime import datetime, timedelta
from typing import List, Dict, Any

def generate_available_slots(
    start_date: datetime,
    end_date: datetime,
    slot_duration_minutes: int = 45,
    business_hours_start: int = 9,
    business_hours_end: int = 17,
    existing_bookings: List[Dict[str, datetime]] = None
) -> List[Dict[str, datetime]]:
    """Generates available interview time slots excluding existing bookings."""
    slots = []
    existing_bookings = existing_bookings or []
    current_date = start_date.replace(hour=business_hours_start, minute=0, second=0, microsecond=0)

    while current_date < end_date:
        if current_date.weekday() < 5:  # Monday to Friday
            day_end = current_date.replace(hour=business_hours_end, minute=0, second=0, microsecond=0)
            slot_start = current_date
            while slot_start + timedelta(minutes=slot_duration_minutes) <= day_end:
                slot_end = slot_start + timedelta(minutes=slot_duration_minutes)

                # Check conflict
                is_conflicting = any(
                    b['start'] < slot_end and b['end'] > slot_start
                    for b in existing_bookings
                )

                if not is_conflicting:
                    slots.append({"start": slot_start, "end": slot_end})

                slot_start += timedelta(minutes=slot_duration_minutes)

        current_date += timedelta(days=1)
        current_date = current_date.replace(hour=business_hours_start, minute=0, second=0, microsecond=0)

    return slots
