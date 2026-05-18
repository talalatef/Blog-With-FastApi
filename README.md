# Blog With FastAPI

A RESTful blog API built with FastAPI, SQLAlchemy, and JWT authentication.

## Features

- User registration and login
- JWT Bearer authentication
- Full blog post CRUD
- User–Blog relationship (each post belongs to a user)
- Repository pattern for clean separation of concerns

## Tech Stack

- **FastAPI** — web framework
- **SQLAlchemy** — ORM with SQLite
- **Pydantic** — request/response validation
- **python-jose** — JWT token creation and verification
- **bcrypt** — password hashing

## Project Structure

```
src/blog/
├── main.py           # App entry point, router registration
├── database.py       # DB engine, session, get_db dependency
├── models.py         # SQLAlchemy models (User, Blog)
├── schemas.py        # Pydantic schemas
├── token.py          # JWT create/verify utilities
├── oauth2.py         # get_current_user dependency
├── hassing.py        # Password hash and verify
├── routers/
│   ├── auth.py       # POST /auth/login
│   ├── blogs.py      # Blog CRUD endpoints
│   └── users.py      # User endpoints
└── repo/
    ├── auth.py       # Login logic
    ├── blogs.py      # Blog DB operations
    └── users.py      # User DB operations
```

## Setup

**1. Create and activate a virtual environment**

```bash
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
```

**2. Install dependencies**

```bash
pip install -r requirements.txt
```

**3. Run the server**

```bash
uvicorn src.blog.main:app --reload
```

The API will be available at `http://localhost:8000`.  
Interactive docs: `http://localhost:8000/docs`

## Authentication

All endpoints except `POST /user/` (register) and `POST /auth/login` require a JWT Bearer token.

**1. Register**

```http
POST /user/
Content-Type: application/json

{
  "name": "John Doe",
  "email": "john@example.com",
  "password": "secret"
}
```

**2. Login**

```http
POST /auth/login
Content-Type: application/json

{
  "username": "john@example.com",
  "password": "secret"
}
```

Response:
```json
{
  "access_token": "<token>",
  "token_type": "bearer"
}
```

**3. Use the token**

Add this header to all protected requests:

```
Authorization: Bearer <access_token>
```

In Swagger UI (`/docs`), click the **Authorize** lock icon and paste the token.

## API Endpoints

### Auth

| Method | Endpoint | Auth | Description |
|--------|----------|------|-------------|
| POST | `/auth/login` | No | Login and get JWT token |

### Users

| Method | Endpoint | Auth | Description |
|--------|----------|------|-------------|
| POST | `/user/` | No | Register a new user |
| GET | `/user/` | Yes | Get all users |
| GET | `/user/{id}` | Yes | Get user by ID |

### Blogs

| Method | Endpoint | Auth | Description |
|--------|----------|------|-------------|
| POST | `/blog/` | Yes | Create a new post |
| GET | `/blog/` | Yes | Get all posts |
| GET | `/blog/{id}` | Yes | Get post by ID |
| PUT | `/blog/{id}` | Yes | Update a post |
| DELETE | `/blog/{id}` | Yes | Delete a post |

### Create Post Request Body

```json
{
  "title": "My First Post",
  "content": "Hello world!",
  "user_id": 1
}
```

## Environment

> Before going to production, replace the `SECRET_KEY` in `token.py` with a strong random value:
>
> ```python
> SECRET_KEY = "your-secret-key-change-in-production"
> ```
>
> Generate one with: `openssl rand -hex 32`
