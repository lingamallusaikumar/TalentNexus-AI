# TalentNexus AI — Security Architecture

## 1. Authentication & Session Security
- **JWT (JSON Web Tokens)**: Issued via PyJWT with HMAC SHA-256 signatures, expirations, and user/tenant claims (`sub`, `org_id`, `role`).
- **Password Hashing**: Salted PBKDF2/SHA256 via Werkzeug Security.
- **Two-Factor Authentication (2FA)**: Time-based One-Time Passwords (TOTP).
- **Session Revocation**: Centralized session token JTIs with fast blacklisting.

## 2. Authorization & RBAC
- **Multi-Tenant Isolation**: Query-level filtering on `organization_id` using `TenantAwareMixin`.
- **Role Permissions**: Matrix defining access for *Super Admin, Org Admin, HR Manager, Recruiter, Hiring Manager, Interviewer, Candidate*.
- **Endpoint Decorators**: `@token_required` and `@require_role([...])`.

## 3. Secure File Ingestion
- Strict file type whitelist (`.pdf`, `.docx`, `.txt`).
- `werkzeug.utils.secure_filename` sanitization against directory traversal attacks.
- Isolated Celery worker sandbox for text extraction.

## 4. Audit & Compliance
- Full immutable logging in `audit_logs` and `security_logs` for all state mutations, logins, data exports, and AI decision overrides.
