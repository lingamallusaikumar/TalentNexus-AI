# TalentNexus AI

Real-Time Intelligent Talent Screening, Candidate Matching & Recruitment Intelligence Platform.

## Architecture
Modular monolith using Flask, SQLAlchemy, Celery, Redis, and PostgreSQL. 

## Phase 1
- Initial project structure
- Flask application factory
- Docker/docker-compose setup
- SQLAlchemy/PostgreSQL setup
- Celery/Redis setup
- Pytest configuration
- Health check endpoints

## Setup
1. Clone the repository.
2. Run `docker-compose up -d --build`.
3. The API is available at `http://localhost:8000`.

## Testing
Run tests using:
```
pytest
```
