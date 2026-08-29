import os
import re

ALLOWED_EXTENSIONS = {'.pdf', '.docx', '.txt'}
MAX_FILE_SIZE_BYTES = 10 * 1024 * 1024  # 10 MB

def is_allowed_file(filename: str) -> bool:
    ext = os.path.splitext(filename)[1].lower()
    return ext in ALLOWED_EXTENSIONS

def validate_file_size(file_size: int) -> bool:
    return 0 < file_size <= MAX_FILE_SIZE_BYTES

def sanitize_resume_text(text: str) -> str:
    """Removes potential script tags, executive metadata leaks, and excessive whitespace."""
    if not text:
        return ""
    # Strip HTML/script tags
    text = re.sub(r'<script.*?>.*?</script>', '', text, flags=re.DOTALL | re.IGNORECASE)
    text = re.sub(r'<[^>]+>', ' ', text)
    # Normalize multiple whitespace characters
    return re.sub(r'\s+', ' ', text).strip()
