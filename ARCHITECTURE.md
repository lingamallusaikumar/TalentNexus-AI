# TalentNexus AI — System Architecture

## 1. Architectural Overview
TalentNexus AI is an enterprise-grade, real-time recruitment intelligence platform architected as a **modular monolith** with clear domain boundaries, event-driven decoupling, and dedicated machine learning micro-pipelines.

```
+-------------------------------------------------------------------------+
|                           Client Applications                           |
|      (Recruiter Dashboard, Candidate Portal, REST APIs, WebSockets)     |
+------------------------------------+------------------------------------+
                                     |
                                     v
+-------------------------------------------------------------------------+
|                            Flask API Gateway                            |
|             (JWT / RBAC Middleware, Rate Limiting, Versioning)          |
+------------------------------------+------------------------------------+
                                     |
                 +-------------------+-------------------+
                 |                                       |
                 v                                       v
+----------------------------------+   +----------------------------------+
|        Business Services         |   |      Real-Time WebSocket Layer   |
|   (Auth, Jobs, Candidates, ATS)  |   |    (Flask-SocketIO + Redis Pub)  |
+----------------+-----------------+   +-----------------+----------------+
                 |                                       |
                 v                                       v
+----------------------------------+   +----------------------------------+
|           Event Bus              |   |       Workflow Automations       |
|    (In-Process + Audit Event Log)|   |    (Trigger -> Condition -> Act) |
+----------------+-----------------+   +-----------------+----------------+
                 |                                       |
                 +-------------------+-------------------+
                                     |
                                     v
+------------------------------------+------------------------------------+
|                Celery Asynchronous Task Workers                         |
|   (PyMuPDF/OCR Parsing, Sentence Transformers, XAI Scoring, Embeddings) |
+------------------------------------+------------------------------------+
                                     |
        +----------------------------+----------------------------+
        |                            |                            |
        v                            v                            v
+---------------+            +---------------+            +---------------+
|  PostgreSQL   |            |     Redis     |            |  File Storage |
|  (30+ Tables) |            | (Queue/Cache) |            |  (Local / S3) |
+---------------+            +---------------+            +---------------+
```

## 2. Core Subsystems

### 2.1 Multi-Tenant Data Isolation
- Organizations act as the top-level isolation boundary.
- Workspaces, Departments, and Teams enable hierarchical corporate structures.
- All primary data entities inherit `TenantAwareMixin` with foreign key enforcement and soft deletion.

### 2.2 NLP & Machine Learning Engine
1. **Document Ingestion & OCR**: PyMuPDF + Tesseract OCR fallback.
2. **Section Segmentation**: Regex and NLP header boundary detection.
3. **Skill Normalization Engine**: Canonical alias resolving (e.g. `JS` -> `JavaScript`).
4. **Sentence Embeddings**: `SentenceTransformer('all-MiniLM-L6-v2')` generating 384-dimensional dense vectors.
5. **Multi-Factor Hybrid Scorer**: Configurable weighting across skills (30%), semantic similarity (20%), experience (15%), projects (10%), education (10%), certs (5%), location (5%), and preferences (5%).
6. **Explainable AI (XAI)**: Generates human-readable strengths, weaknesses, and recommendations.

### 2.3 Event-Driven Real-Time Sync
- Events like `candidate.match.completed` are published to the `EventBus`.
- Background Celery workers broadcast updates through Redis into Flask-SocketIO rooms.
- Recruiters see instantaneous ranking recalculations without refreshing.
