# TalentNexus AI — Development Guide

## 1. Local Setup
```bash
# 1. Clone the repository
git clone https://github.com/lingamallusaikumar/TalentNexus-AI.git
cd TalentNexus-AI

# 2. Start all services using Docker
docker-compose up -d --build
```

## 2. Running Tests
```bash
pytest -v --cov=app --cov=ml
```

## 3. Architecture Guidelines
- Keep business logic in `services.py` layers.
- Blueprints in `app/api/` should remain thin controllers.
- Celery background tasks belong in `tasks.py`.
- ML model inference is encapsulated in `ml/`.
