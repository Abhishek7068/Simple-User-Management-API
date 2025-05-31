### FastAPI User Authentication System with JWT
A secure user authentication API built with FastAPI, PostgreSQL, and JWT (JSON Web Tokens) for token-based authentication.

## Features
1. User registration with email/password

2. JWT token-based authentication

3. Password hashing with bcrypt

4. Protected endpoints with user-specific access

5. PostgreSQL database integration
   
6. Pydantic data validation

## Tech Stack
**Framework:** FastAPI

**Database:** PostgreSQL

**Authentication**: JWT

**Password Hashing**: Bcrypt

**ORM:** SQLAlchemy

**Validation: **Pydantic

## Installation
**Clone the repository:**
git clone https://github.com/yourusername/fastapi-jwt-auth.git
cd fastapi-jwt-auth

**Create and activate a virtual environment:**
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate    # Windows

**Install dependencies:**
pip install -r requirements.txt

**Set up PostgreSQL:**
Create a database named user_auth
Update the connection string in app/config.py

**Run the application:**
uvicorn app.main:app --reload

## API Endpoints
**Authentication**
POST /register - Register a new user
POST /token - Login and get access token

**User Profile**
GET /profile/{user_id} - Get user profile (authenticated)
PUT /profile/{user_id} - Update user profile (authenticated)

### Breaking down the components to show thier working

## cCRUD operations  # (crud.py)
**What it does:**

1. Takes a database session and email string as input
2. Queries the User table for a record matching the email
3. Returns the first matching user or None if not found

**Output:**
Returns: User model object if found, None if not found

**Example:**
Input: email="test@example.com"
Output: User(id=1, email="test@example.com", hashed_password="...")

## Authentication (auth.py)
**What it does:**

1. Gets user by email (calls get_user_by_email)
2. If no user found → returns False
3. If user exists → verifies password against stored hash
4. Returns user if credentials valid, False otherwise

**Output:**
Returns: User object if valid, False if invalid

**Password Verification:**
Uses passlib to compare password input with hashed_password
Example: verify_password("secret123", "$2b$12$...") → True/False

## Token creation # (auth.py)
**What it does:**
1. Takes payload data (typically {"sub": email})
2. Adds expiration time (default 15 mins)
3. Signs token with secret key using HS256 algorithm

**Output:**
Returns: JWT string like "eyJhbGciOiJIUzI1NiIs..."

## Visual Flow
Client → POST /token (credentials) → Server → 
   ↓ (if valid) 
JWT Token → Client → GET /profile (with token) → 
   ↓ (if valid token)
User Data

## Key Security Features
Key Security Features:
Password Hashing: Never stores plaintext passwords
JWT Expiration: Tokens automatically expire
Signature Verification: Tokens can't be tampered with
User Context: Each token is tied to a specific user
