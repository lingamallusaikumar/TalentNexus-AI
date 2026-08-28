# TalentNexus AI — Deployment Guide

## Production Architecture
- **Web App**: Gunicorn WSGI workers (4+ processes) behind Nginx reverse proxy.
- **Background Processing**: Celery worker nodes scaling dynamically.
- **Database**: Managed PostgreSQL 15+ with read-replicas.
- **Cache & Queue**: Managed Redis 7+ cluster.
- **Object Storage**: S3-compatible bucket for resume documents.

## Environment Variables
- `FLASK_ENV=production`
- `SECRET_KEY=<secure-random-key>`
- `DATABASE_URL=postgresql://user:pass@host:5432/talentnexus`
- `REDIS_URL=redis://redis-host:6379/0`
- `CELERY_BROKER_URL=redis://redis-host:6379/1`
