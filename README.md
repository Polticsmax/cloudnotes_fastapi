🚀 CloudNotes API

A production-style Notes Backend built using FastAPI + AWS + Docker

This project demonstrates how real backend systems store data and files in the cloud instead of local storage.

---

🌍 Live Architecture

Client Request → FastAPI (EC2 Docker) → JWT Auth → PostgreSQL (RDS) → Images (S3)

---

✨ Features

Authentication

- User Registration
- Secure Login (JWT Token)
- Protected Routes

Notes

- Create note with image upload
- Update only title
- Update only description
- Update only image
- Fetch all notes
- Delete notes

Cloud Integration

- Images stored in AWS S3
- Data stored in AWS RDS PostgreSQL
- Fully Dockerized deployment

---

📡 API Endpoints

Auth

Method|    Endpoint|   Description
POST|      /register|  Create account
POST|      /login|     Get access token

Notes

Method|    Endpoint|                         Description
POST|      /notes|                           Create note with image
GET|       /notes|                           Get all notes
PATCH|     /notes/{id}/title|                Update title
PATCH|     /notes/{id}/description|          Update description
PATCH|     /notes/{id}/image|                Update image
DELETE|    /notes/{id}|                      Delete note

---

🐳 Run Using Docker

Build Image

docker build -t cloudnotes .

Run Container

docker run -p 8000:8000 cloudnotes

Open Swagger Docs
http://localhost:8000/docs

---

🧪 Example Flow

1. Register user
2. Login and copy token
3. Click Authorize in Swagger
4. Create note with image
5. Image uploads to S3 automatically
6. Fetch notes returns S3 image URL

---

🛠 Tech Stack

- FastAPI
- PostgreSQL (AWS RDS)
- AWS S3
- JWT Authentication
- SQLAlchemy
- Docker
- AWS EC2

---

📚 Learning Outcomes

- Building production backend architecture
- Authentication using JWT
- Cloud storage handling (S3)
- Container deployment using Docker
- Connecting API to managed database (RDS)

---

👨‍💻 Author

Abhilash
Backend Developer | Cloud & API Enthusiast
