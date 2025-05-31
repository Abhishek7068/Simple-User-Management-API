###FastAPI User Authentication System with JWT
A secure user authentication API built with FastAPI, PostgreSQL, and JWT (JSON Web Tokens) for token-based authentication.

##Features
✅ User registration with email/password

✅ JWT token-based authentication

✅ Password hashing with bcrypt

✅ Protected endpoints with user-specific access

✅ PostgreSQL database integration

✅ Pydantic data validation

Tech Stack
Framework: FastAPI

Database: PostgreSQL

Authentication: JWT

Password Hashing: Bcrypt

ORM: SQLAlchemy

Validation: Pydantic

Installation
Clone the repository:

bash
git clone https://github.com/yourusername/fastapi-jwt-auth.git
cd fastapi-jwt-auth
Create and activate a virtual environment:

bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate    # Windows
Install dependencies:

bash
pip install -r requirements.txt
Set up PostgreSQL:

Create a database named user_auth

Update the connection string in app/config.py

Run the application:

bash
uvicorn app.main:app --reload
API Endpoints
Authentication
POST /register - Register a new user

POST /token - Login and get access token

User Profile
GET /profile/{user_id} - Get user profile (authenticated)

PUT /profile/{user_id} - Update user profile (authenticated)

Environment Variables
Create a .env file with the following variables:

DATABASE_URL=postgresql://username:password@localhost:5432/user_auth
SECRET_KEY=your-secret-key-here
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
Generate a secure secret key with:

bash
openssl rand -hex 32
Testing with Postman
Import the Postman collection

Test the flow:

Register → Login → Access Protected Routes

Project Structure
fastapi-jwt-auth/
├── app/
│   ├── __init__.py
│   ├── main.py         # FastAPI app and routes
│   ├── database.py     # Database connection
│   ├── models.py       # SQLAlchemy models
│   ├── schemas.py      # Pydantic models
│   ├── crud.py         # Database operations
│   ├── auth.py         # Authentication utilities
│   └── config.py       # Configuration settings
├── tests/              # Test cases
├── requirements.txt    # Dependencies
└── README.md           # This file
Development
Run tests:

bash
pytest
Check API documentation:

Swagger UI: http://localhost:8000/docs

ReDoc: http://localhost:8000/redoc
