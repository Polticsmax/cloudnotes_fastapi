☁️ CloudNotes Backend API

A production‑style FastAPI backend deployed on AWS with authentication, database storage, file uploads, HTTPS, and monitoring.


---

🚀 What This Project Demonstrates

Area	Implementation

Authentication	JWT tokens + password hashing
Database	PostgreSQL with SQLAlchemy ORM
File Storage	AWS S3 uploads & delete
Deployment	EC2 Linux server
Production Server	Gunicorn + Uvicorn workers
Reverse Proxy	NGINX
Security	HTTPS SSL certificate
Monitoring	CloudWatch metrics & logs
Reliability	systemd auto‑restart service
DevOps	GitHub version control



---

🧩 Features

User registration & login

Token protected routes

Notes CRUD operations

Upload image/file to S3

Replace & delete file

Persistent DB storage

HTTPS live deployment

Environment based configuration



---

🔐 Authentication Flow

Login → Token Generated → Stored by Client
      → Sent in Header → Verified → Access Granted

Header format:

Authorization: Bearer <JWT_TOKEN>


---

📡 API Routes

Auth

Method	Endpoint	Description

POST	/register	Create user
POST	/login	Get token


Notes (Protected)

Method	Endpoint	Description

POST	/notes	Create note
GET	/notes	Get all notes
PUT	/notes/{id}/title	Update title
PUT	/notes/{id}/file	Update file
DELETE	/notes/{id}	Delete note



---

📁 Project Structure

app/
 ├─ main.py        → API routes
 ├─ auth.py        → JWT logic
 ├─ models.py      → DB models
 ├─ schemas.py     → Pydantic schemas
 ├─ database.py    → DB connection
 ├─ s3.py          → S3 upload/delete
 └─ config.py      → Environment loader

system/
 ├─ cloudnotes.service → Linux service
 └─ nginx.conf         → Reverse proxy

.env  (not committed)


---

🏗 Architecture

Client
  ↓
HTTPS Domain
  ↓
NGINX Reverse Proxy
  ↓
Gunicorn
  ↓
FastAPI (Uvicorn Workers)
  ↓           ↓
PostgreSQL   AWS S3
  ↓
CloudWatch Monitoring


---

🔄 Request Lifecycle

1. User logs in


2. Server returns JWT token


3. Client sends token in header


4. FastAPI validates user


5. Data saved in PostgreSQL


6. Files stored in S3


7. URL saved in DB


8. Response returned via Gunicorn + NGINX


9. systemd keeps service alive


10. CloudWatch tracks health




---

⚙️ Environment Variables

DATABASE_URL=db_url

SECRET_KEY=yoursecretkey

ALGORITHM=HS256

ACCESS_TOKEN_EXPIRE_MINUTES=30

AWS_REGION=region

BUCKET_NAME=bucket_name


---

🖥 Run Locally

pip install -r requirements.txt
uvicorn app.main:app --reload


---

☁️ Deployment Summary

EC2 → Gunicorn → NGINX → HTTPS → Domain → CloudWatch


---

📌 Why This Project Matters

This backend shows real production concepts expected from backend engineers:

Secure auth implementation

Cloud storage integration

API design

Linux deployment

Reverse proxy usage

Monitoring awareness

Environment separation

Git workflow
