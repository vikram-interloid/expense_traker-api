# Expense Tracker API

A production-ready Expense Tracker REST API built with **FastAPI**, featuring JWT Authentication, PostgreSQL, SQLAlchemy, Alembic, Docker, and role-based architecture using Repository-Service pattern.

---

# Features

- JWT Authentication
- Access & Refresh Token Authentication
- Password Hashing (bcrypt)
- User Management
- Category Management (Income & Expense)
- Transaction Management
- Filtering, Sorting & Pagination
- Monthly & Yearly Reports
- Dashboard Summary APIs
- PostgreSQL Database
- SQLAlchemy ORM
- Alembic Migrations
- Pydantic Validation
- Docker Support
- Production-ready Project Structure

---

# Tech Stack

- Python 3.12+
- FastAPI
- PostgreSQL / Neon Database
- SQLAlchemy
- Alembic
- Pydantic
- JWT (python-jose)
- Passlib (bcrypt)
- Docker
- Uvicorn

---




---

# Prerequisites

- Python 3.12+
- PostgreSQL (or Neon Database)
- Docker (Optional)
- Git

---

# Clone Repository

```bash
git clone git@github.com:vikram-interloid/expense_traker-api.git

cd expense-tracker-api
```

---

# Create Virtual Environment

### Linux / macOS

```bash
python3 -m venv .venv

source .venv/bin/activate
```

### Windows

```cmd
python -m venv .venv

.venv\Scripts\activate
```

---

# Install Dependencies

```bash
pip install -r requirements.txt
```

---

# Configure Environment Variables

Create a `.env` file in the project root.

```env

SECRET_KEY=your-secret-key

ALGORITHM=HS256

ACCESS_TOKEN_EXPIRE_MINUTES=30

REFRESH_TOKEN_EXPIRE_DAYS=7
```

---

# Run Database Migrations

```bash
alembic upgrade head
```

---

# Seed Database

```bash
python3 -m app.seeds.run_seeds
```


---

# Run the Application

```bash
uvicorn app.main:app --reload
```

---

# API Documentation

### Swagger UI

```
http://127.0.0.1:8000/docs
```

### ReDoc

```
http://127.0.0.1:8000/redoc
```

---



---

# API Modules

## Authentication

- Register
- Login
- Refresh Token
- Logout
- Get Current User

## Categories

- Create Category
- Get Categories
- Get Category By ID
- Update Category
- Delete Category

## Transactions

- Create Transaction
- Get Transactions
- Get Transaction By ID
- Update Transaction
- Delete Transaction

Supports:

- Pagination
- Sorting
- Date Filters
- Amount Filters
- Category Filters

## Reports

- Total Income
- Total Expense
- Current Balance
- Monthly Report
- Yearly Report

---




