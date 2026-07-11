# expense_traker-api


# Expense Tracker API

A production-ready RESTful Expense Tracker API built with **FastAPI**, following a clean **Repository → Service → Router** architecture. The application provides secure JWT-based authentication with refresh token support, user-specific expense category management, and transaction management while following scalable backend development practices.

The project is designed to demonstrate production-level backend concepts such as authentication, authorization, database relationships, layered architecture, request validation, error handling, database migrations, and secure API development.

---

# Project Objectives

* Build a secure REST API using FastAPI.
* Implement JWT Authentication with Access and Refresh Tokens.
* Support user-specific data using authentication and authorization.
* Follow a clean Repository → Service → Router architecture.
* Implement complete CRUD operations.
* Use PostgreSQL as the primary database.
* Manage schema changes using Alembic migrations.
* Validate requests and responses using Pydantic.
* Maintain scalable and reusable backend code.

---

# Features

## Authentication

* User Registration
* User Login
* JWT Access Token
* Refresh Token Authentication
* Logout using Refresh Token Revocation
* Protected Routes
* Password Hashing using bcrypt
* OAuth2 Bearer Authentication
* Access Token and Refresh Token Type Validation

---

## Category Management

* Create Category
* Get All Categories
* Get Category by ID
* Update Category
* Delete Category
* User Ownership Validation
* Duplicate Category Validation (User + Name + Type)

---

## Transaction Management

* Create Transaction
* User-specific Transactions
* Category Ownership Validation
* Amount Validation
* CRUD Operations (In Progress)

---

# Technology Stack

## Backend

* Python 3.12
* FastAPI
* SQLAlchemy 2.0
* Pydantic v2
* Alembic

## Database

* PostgreSQL

## Authentication

* OAuth2 Password Flow
* JWT (python-jose)
* bcrypt
* Passlib

## API Testing

* Swagger UI
* Postman

## Development Tools

* VS Code
* Git
* GitHub

---

# Design Principles

* Clean Architecture
* Layered Architecture
* Repository Pattern
* Dependency Injection
* Separation of Concerns
* REST API Best Practices
* Production-ready Code Structure

---

# Architecture

The application follows the following architecture:

Client

↓

Router

↓

Service

↓

Repository

↓

PostgreSQL Database

Each layer has a single responsibility.

* Router handles HTTP requests and responses.
* Service contains business logic and validations.
* Repository communicates with the database.
* Database stores application data.

This separation keeps the application maintainable, testable, and scalable.


# Project Structure

```text
expense_tracker_api/
│
├── alembic/
│   ├── versions/
│   ├── env.py
│   └── script.py.mako
│
├── app/
│   │
│   ├── api/
│   │   └── v1/
│   │       ├── auth.py
│   │       ├── category.py
│   │       └── transaction.py
│   │
│   ├── core/
│   │   ├── config.py
│   │   ├── dependencies.py
│   │   └── security.py
│   │
│   ├── db/
│   │   ├── base.py
│   │   └── session.py
│   │
│   ├── exceptions/
│   │   ├── auth.py
│   │   ├── handlers.py
│   │   └── response.py
│   │
│   ├── models/
│   │   ├── __init__.py
│   │   ├── user.py
│   │   ├── category.py
│   │   ├── transaction.py
│   │   └── refresh_token.py
│   │
│   ├── repositories/
│   │   ├── auth_repository.py
│   │   ├── category_repository.py
│   │   └── transaction_repository.py
│   │
│   ├── schemas/
│   │   ├── auth.py
│   │   ├── category.py
│   │   └── transaction.py
│   │
│   ├── services/
│   │   ├── auth_service.py
│   │   ├── category_service.py
│   │   └── transaction_service.py
│   │
│   └── main.py
│
├── .env
├── alembic.ini
├── requirements.txt
└── README.md
```

---

# Folder Explanation

## app/api/

Contains all API endpoints (routers). Each module exposes REST endpoints and delegates business logic to the service layer.

Examples:

* Authentication APIs
* Category APIs
* Transaction APIs

---

## app/core/

Contains reusable application components.

### config.py

* Loads environment variables
* Database URL
* JWT Secret Key
* Token expiration settings

### security.py

Handles authentication and security operations.

Responsibilities:

* Password hashing
* Password verification
* JWT Access Token generation
* JWT Refresh Token generation
* JWT decoding

### dependencies.py

Contains reusable FastAPI dependencies.

Examples:

* Database session
* Authentication service
* Category service
* Transaction service
* Current authenticated user

---

## app/db/

Database configuration.

### base.py

Creates the SQLAlchemy Base class.

### session.py

Creates the database engine and session factory.

---

## app/models/

Contains SQLAlchemy ORM models representing database tables.

Current models:

* User
* Category
* Transaction
* RefreshToken

---

## app/repositories/

Responsible only for database operations.

Examples:

* INSERT
* SELECT
* UPDATE
* DELETE

Repositories never contain business logic.

---

## app/services/

Contains business logic.

Responsibilities include:

* Authentication
* Validations
* Ownership checks
* Duplicate checks
* Token generation
* CRUD processing

Services communicate with repositories.

---

## app/schemas/

Contains Pydantic models.

Used for:

* Request validation
* Response serialization
* API documentation

---

## app/exceptions/

Contains reusable exception handling.

Files:

* auth.py
* handlers.py
* response.py

This module centralizes API error responses.

---

## alembic/

Responsible for database migrations.

Used to:

* Create new tables
* Modify existing tables
* Version database schema

---

# Request Flow

Every request follows the same layered architecture.

```text
Client
   │
   ▼
Router
   │
   ▼
Service
   │
   ▼
Repository
   │
   ▼
PostgreSQL
```

### Router

* Receives HTTP requests.
* Validates request body using Pydantic.
* Calls the appropriate service.

### Service

* Implements business logic.
* Performs validations.
* Checks authentication and ownership.
* Calls the repository.

### Repository

* Executes SQLAlchemy database operations.
* Returns ORM objects.

### Database

Stores and retrieves application data.

The response flows back through the same layers until it is returned to the client as JSON.

# Database Design

The Expense Tracker API uses **PostgreSQL** as its primary relational database. The schema is normalized and designed to support secure, user-specific expense tracking.

---

# Database Tables

The project currently contains the following tables:

1. users
2. categories
3. transactions
4. refresh_tokens

---

# 1. users

Stores user account information.

| Column        | Type        | Description                  |
| ------------- | ----------- | ---------------------------- |
| id            | Integer     | Primary Key                  |
| username      | String(50)  | Unique username              |
| email         | String(255) | Unique email address         |
| password_hash | String(255) | Hashed password using bcrypt |
| created_at    | Timestamp   | Account creation time        |
| updated_at    | Timestamp   | Last update time             |

### Constraints

* Primary Key: `id`
* Unique: `username`
* Unique: `email`

---

# 2. categories

Stores user-defined income and expense categories.

Examples:

* Salary
* Food
* Rent
* Shopping
* Fuel

| Column     | Type        | Description           |
| ---------- | ----------- | --------------------- |
| id         | Integer     | Primary Key           |
| name       | String(100) | Category name         |
| type       | Enum        | income / expense      |
| user_id    | Integer     | Owner of the category |
| created_at | Timestamp   | Created time          |
| updated_at | Timestamp   | Updated time          |

### Constraints

Primary Key

* id

Foreign Key

* user_id → users.id

Unique Constraint

```text
(user_id, name, type)
```

This allows different users to have categories with the same name while preventing duplicate categories of the same type for a single user.

Example:

Allowed:

User A

Food (expense)

User B

Food (expense)

Not Allowed:

User A

Food (expense)

Food (expense)

---

# 3. transactions

Stores all income and expense records.

| Column           | Type          | Description          |
| ---------------- | ------------- | -------------------- |
| id               | Integer       | Primary Key          |
| amount           | Numeric(12,2) | Transaction amount   |
| description      | String(255)   | Optional description |
| transaction_date | Date          | Transaction date     |
| category_id      | Integer       | Category reference   |
| user_id          | Integer       | Transaction owner    |
| created_at       | Timestamp     | Created time         |
| updated_at       | Timestamp     | Updated time         |

### Constraints

Primary Key

* id

Foreign Keys

* category_id → categories.id
* user_id → users.id

Business Rules

* Amount must be greater than zero.
* Category must belong to the authenticated user.
* Every transaction belongs to exactly one category.
* Every transaction belongs to exactly one user.

---

# 4. refresh_tokens

Stores active refresh tokens used for JWT authentication.

| Column     | Type        | Description       |
| ---------- | ----------- | ----------------- |
| id         | Integer     | Primary Key       |
| token      | Text/String | JWT Refresh Token |
| user_id    | Integer     | Token owner       |
| expires_at | Timestamp   | Expiration time   |
| is_revoked | Boolean     | Revoked status    |
| created_at | Timestamp   | Created time      |

### Purpose

Used to:

* Issue new access tokens.
* Support logout.
* Revoke refresh tokens.
* Prevent reuse of revoked tokens.

---

# Entity Relationships

```text
                    +--------------------+
                    |       users        |
                    +--------------------+
                    | id (PK)            |
                    | username           |
                    | email              |
                    | password_hash      |
                    +---------+----------+
                              |
             +----------------+----------------+
             |                                 |
           1 |                               1 |
             |                                 |
             ▼                                 ▼
+------------------------+        +------------------------+
|      categories        |        |     refresh_tokens     |
+------------------------+        +------------------------+
| id (PK)                |        | id (PK)                |
| name                   |        | token                  |
| type                   |        | expires_at             |
| user_id (FK)           |        | is_revoked             |
+------------+-----------+        | user_id (FK)           |
             |                    +------------------------+
           1 |
             |
             ▼
+------------------------+
|      transactions      |
+------------------------+
| id (PK)                |
| amount                 |
| description            |
| transaction_date       |
| category_id (FK)       |
| user_id (FK)           |
+------------------------+
```

---

# Relationship Summary

## User → Categories

Relationship:

One-to-Many

One user can create many categories.

Each category belongs to only one user.

---

## User → Transactions

Relationship:

One-to-Many

One user can create many transactions.

Each transaction belongs to only one user.

---

## Category → Transactions

Relationship:

One-to-Many

One category can contain many transactions.

Each transaction belongs to exactly one category.

---

## User → Refresh Tokens

Relationship:

One-to-Many

A user can have multiple refresh tokens.

Each refresh token belongs to one user.

---

# Data Ownership

Every category and transaction is linked to a specific authenticated user.

This ensures:

* Users cannot access another user's categories.
* Users cannot access another user's transactions.
* Users cannot create transactions using another user's categories.
* API responses only return data owned by the authenticated user.

This ownership validation is enforced in the service and repository layers using the authenticated user's ID extracted from the JWT access token.



# Authentication Flow

The Expense Tracker API uses **JWT (JSON Web Token)** authentication with the **OAuth2 Password Bearer** flow. Users authenticate using their email and password, receive an **Access Token** and a **Refresh Token**, and use the Access Token to access protected endpoints.

---

# Authentication Components

| Component            | Purpose                                                             |
| -------------------- | ------------------------------------------------------------------- |
| Access Token         | Used to access protected API endpoints                              |
| Refresh Token        | Used to generate a new Access Token without logging in again        |
| JWT                  | Securely stores user identity and token metadata                    |
| bcrypt               | Hashes user passwords before storing them in the database           |
| OAuth2PasswordBearer | Extracts the Bearer token from incoming requests                    |
| Refresh Token Table  | Stores active refresh tokens and supports logout by revoking tokens |

---

# JWT Payload

## Access Token

The Access Token contains the authenticated user's ID and token type.

```json
{
  "sub": "1",
  "type": "access",
  "exp": "2026-07-10T12:30:00Z"
}
```

## Refresh Token

The Refresh Token contains the authenticated user's ID and is used only to obtain a new Access Token.

```json
{
  "sub": "1",
  "type": "refresh",
  "exp": "2026-07-17T12:30:00Z"
}
```

---

# User Registration Flow

**Endpoint**

```http
POST /auth/register
```

## Flow

1. Client sends username, email, and password.
2. FastAPI validates the request using Pydantic.
3. The service checks whether the email already exists.
4. The service checks whether the username already exists.
5. The password is hashed using bcrypt.
6. The repository stores the user in PostgreSQL.
7. The created user is returned.

## Flow Diagram

```text
Client
   │
   ▼
POST /auth/register
   │
   ▼
Router
   │
   ▼
Pydantic Validation
   │
   ▼
Auth Service
   │
   ├── Check Email
   ├── Check Username
   ├── Hash Password
   │
   ▼
Repository
   │
   ▼
PostgreSQL
   │
   ▼
User Created
```

---

# User Login Flow

**Endpoint**

```http
POST /auth/login
```

## Flow

1. Client submits email and password using the OAuth2 Password flow.
2. The repository finds the user by email.
3. The password is verified using bcrypt.
4. An Access Token is generated.
5. A Refresh Token is generated.
6. The Refresh Token is stored in the database.
7. Both tokens are returned to the client.

## Flow Diagram

```text
Client
   │
   ▼
POST /auth/login
   │
   ▼
Router
   │
   ▼
OAuth2 Form Validation
   │
   ▼
Auth Service
   │
   ├── Find User
   ├── Verify Password
   ├── Generate Access Token
   ├── Generate Refresh Token
   │
   ▼
Repository
   │
   ├── Save Refresh Token
   ▼
PostgreSQL
   │
   ▼
Return Tokens
```

---

# Accessing Protected Endpoints

Protected endpoints require a valid Access Token.

**Example**

```http
GET /auth/me
Authorization: Bearer <access_token>
```

## Flow

1. The client sends the Access Token in the Authorization header.
2. `OAuth2PasswordBearer` extracts the token.
3. `decode_token()` verifies the JWT signature.
4. The token expiration is validated.
5. The service verifies that the token type is `"access"`.
6. The user ID (`sub`) is extracted.
7. The repository loads the user from the database.
8. The authenticated user is returned.

## Flow Diagram

```text
Client
   │
Authorization Header
Bearer <access_token>
   │
   ▼
OAuth2PasswordBearer
   │
Extract Token
   │
   ▼
decode_token()
   │
Verify Signature
   │
Verify Expiration
   │
Verify Type == access
   │
Extract User ID
   │
   ▼
Repository
   │
Load User
   │
   ▼
Authenticated User
```

---

# Refresh Token Flow

**Endpoint**

```http
POST /auth/refresh
```

## Flow

1. Client sends the Refresh Token.
2. The repository checks whether the token exists.
3. The repository verifies that it has not been revoked.
4. The JWT is decoded.
5. The service verifies that the token type is `"refresh"`.
6. A new Access Token is generated.
7. The new Access Token is returned.

## Flow Diagram

```text
Client
   │
Refresh Token
   │
   ▼
Router
   │
   ▼
Repository
   │
Check Token
   │
Not Revoked?
   │
   ▼
decode_token()
   │
Verify Signature
   │
Verify Type == refresh
   │
   ▼
Generate New Access Token
   │
   ▼
Return Access Token
```

---

# Logout Flow

**Endpoint**

```http
POST /auth/logout
```

## Flow

1. Client sends the Refresh Token.
2. The repository locates the stored Refresh Token.
3. The token is marked as revoked (`is_revoked = True`).
4. Changes are committed to the database.
5. A success response is returned.

## Flow Diagram

```text
Client
   │
Refresh Token
   │
   ▼
Router
   │
   ▼
Repository
   │
Find Refresh Token
   │
Mark is_revoked = True
   │
Commit Changes
   │
   ▼
Logout Successful
```

---

# Authentication Sequence

```text
Client
   │
   ├──────────────► Register
   │
   ├──────────────► Login
   │                 │
   │                 ├── Verify Password
   │                 ├── Generate Access Token
   │                 └── Generate Refresh Token
   │
   ◄───────────────── Tokens
   │
   ├──────────────► Protected API
   │                 │
   │                 └── Validate Access Token
   │
   ◄───────────────── Response
   │
   ├──────────────► Refresh Token
   │                 │
   │                 └── Generate New Access Token
   │
   ◄───────────────── New Access Token
   │
   ├──────────────► Logout
   │                 │
   │                 └── Revoke Refresh Token
   │
   ◄───────────────── Logout Successful
```

---

# Security Features

* JWT-based authentication
* OAuth2 Password Bearer authentication
* Secure password hashing with bcrypt
* Access Token expiration
* Refresh Token expiration
* Refresh Token revocation
* Token type validation (`access` and `refresh`)
* User ownership validation
* Protected route authentication
* Invalid and expired token handling

---

# Protected Endpoints

| Endpoint                         | Authentication Required |
| -------------------------------- | ----------------------- |
| GET /auth/me                     | Yes                     |
| POST /categories                 | Yes                     |
| GET /categories                  | Yes                     |
| GET /categories/{category_id}    | Yes                     |
| PUT /categories/{category_id}    | Yes                     |
| DELETE /categories/{category_id} | Yes                     |
| POST /transactions               | Yes                     |




# API Documentation


---

# Authentication Endpoints

## 1. Register User

### Endpoint

```http
POST /auth/register
```

### Description

Creates a new user account after validating the request and hashing the password.

### Request Body

```json
{
  "username": "amal",
  "email": "amal@example.com",
  "password": "Password@123"
}
```

### Success Response

**Status Code:** `201 Created`

```json
{
  "id": 1,
  "username": "amal",
  "email": "amal@example.com",
  "created_at": "2026-07-10T10:30:00Z"
}
```

### Error Responses

| Status Code | Reason                  |
| ----------- | ----------------------- |
| 409         | Email already exists    |
| 409         | Username already exists |
| 422         | Invalid request body    |

### Flow

```text
Client
   │
POST /auth/register
   │
   ▼
Router
   │
Validate Request
   │
   ▼
Service
   │
Check Email
Check Username
Hash Password
   │
   ▼
Repository
   │
Insert User
   │
   ▼
PostgreSQL
```

---

# 2. Login

### Endpoint

```http
POST /auth/login
```

### Description

Authenticates the user and returns an Access Token and Refresh Token.

### Authentication Method

OAuth2 Password Flow

### Request (Form Data)

| Field    | Value                                       |
| -------- | ------------------------------------------- |
| username | [amal@example.com](mailto:amal@example.com) |
| password | Password@123                                |

### Success Response

**Status Code:** `200 OK`

```json
{
  "access_token": "<JWT Access Token>",
  "refresh_token": "<JWT Refresh Token>",
  "token_type": "bearer"
}
```

### Error Responses

| Status Code | Reason                    |
| ----------- | ------------------------- |
| 401         | Invalid email or password |
| 422         | Invalid form data         |

### Flow

```text
Client
   │
Login Form
   │
   ▼
Router
   │
OAuth2PasswordRequestForm
   │
   ▼
Service
   │
Verify User
Verify Password
Generate Access Token
Generate Refresh Token
   │
   ▼
Repository
   │
Save Refresh Token
   │
   ▼
PostgreSQL
```

---

# 3. Get Current User

### Endpoint

```http
GET /auth/me
```

### Authentication

Bearer Access Token Required

### Header

```http
Authorization: Bearer <access_token>
```

### Success Response

**Status Code:** `200 OK`

```json
{
  "id": 1,
  "username": "amal",
  "email": "amal@example.com",
  "created_at": "2026-07-10T10:30:00Z"
}
```

### Error Responses

| Status Code | Reason         |
| ----------- | -------------- |
| 401         | Invalid token  |
| 401         | Expired token  |
| 401         | User not found |

### Flow

```text
Client
   │
Bearer Token
   │
   ▼
OAuth2PasswordBearer
   │
Decode JWT
Verify Signature
Verify Expiration
Verify Token Type
Extract User ID
   │
   ▼
Repository
   │
Load User
```

---

# 4. Refresh Access Token

### Endpoint

```http
POST /auth/refresh
```

### Description

Generates a new Access Token using a valid Refresh Token.

### Request Body

```json
{
  "refresh_token": "<refresh_token>"
}
```

### Success Response

**Status Code:** `200 OK`

```json
{
  "access_token": "<new_access_token>",
  "refresh_token": "<refresh_token>",
  "token_type": "bearer"
}
```

### Error Responses

| Status Code | Reason                |
| ----------- | --------------------- |
| 401         | Invalid refresh token |
| 401         | Revoked refresh token |
| 401         | Expired refresh token |

### Flow

```text
Client
   │
Refresh Token
   │
   ▼
Repository
Check Database
   │
Not Revoked
   │
Decode JWT
Verify Type
   │
Generate Access Token
```

---

# 5. Logout

### Endpoint

```http
POST /auth/logout
```

### Description

Revokes the Refresh Token so it cannot be used again.

### Request Body

```json
{
  "refresh_token": "<refresh_token>"
}
```

### Success Response

**Status Code:** `200 OK`

```json
{
  "message": "Logged out successfully"
}
```

### Error Responses

| Status Code | Reason                |
| ----------- | --------------------- |
| 401         | Invalid refresh token |
| 401         | Token already revoked |

### Flow

```text
Client
   │
Refresh Token
   │
   ▼
Repository
Find Token
   │
Set is_revoked = True
   │
Commit
   │
Return Success

```




# Category Endpoints

All category endpoints require a valid **Access Token**.

### Authorization Header

```http
Authorization: Bearer <access_token>
```

---

# 1. Create Category

### Endpoint

```http
POST /categories
```

### Description

Creates a new category for the authenticated user.

Each category belongs to one user.

A user cannot create duplicate categories with the same **name** and **type**.

---

### Request Body

```json
{
    "name": "Food",
    "type": "expense"
}
```

---

### Success Response

**Status Code:** `201 Created`

```json
{
    "id": 1,
    "name": "Food",
    "type": "expense",
    "user_id": 1,
    "created_at": "2026-07-10T10:30:00Z"
}
```

---

### Error Responses

| Status Code | Description             |
| ----------- | ----------------------- |
| 401         | Unauthorized            |
| 409         | Category already exists |
| 422         | Validation Error        |

---

### Flow

```text
Client
   │
POST /categories
   │
   ▼
Router
   │
Validate Request
Authenticate User
   │
   ▼
Category Service
   │
Check Duplicate Category
   │
Create Category Object
   │
   ▼
Repository
   │
INSERT Category
   │
   ▼
PostgreSQL
```

---

# 2. Get All Categories

### Endpoint

```http
GET /categories
```

### Description

Returns all categories belonging to the authenticated user.

---

### Success Response

**Status Code:** `200 OK`

```json
[
    {
        "id": 1,
        "name": "Food",
        "type": "expense"
    },
    {
        "id": 2,
        "name": "Salary",
        "type": "income"
    }
]
```

---

### Error Responses

| Status Code | Description  |
| ----------- | ------------ |
| 401         | Unauthorized |

---

### Flow

```text
Client
   │
GET /categories
   │
   ▼
Router
   │
Authenticate User
   │
   ▼
Service
   │
Repository
   │
SELECT Categories
WHERE user_id = current_user.id
   │
   ▼
Return Categories
```

---

# 3. Get Category by ID

### Endpoint

```http
GET /categories/{category_id}
```

---

### Example

```http
GET /categories/1
```

---

### Description

Returns a single category belonging to the authenticated user.

---

### Success Response

```json
{
    "id": 1,
    "name": "Food",
    "type": "expense"
}
```

---

### Error Responses

| Status Code | Description        |
| ----------- | ------------------ |
| 401         | Unauthorized       |
| 404         | Category not found |

---

### Flow

```text
Client
   │
GET /categories/{id}
   │
   ▼
Router
   │
Authenticate User
   │
   ▼
Service
   │
Repository
   │
SELECT Category
WHERE
id = category_id
AND
user_id = current_user.id
   │
   ▼
Return Category
```

---

# 4. Update Category

### Endpoint

```http
PUT /categories/{category_id}
```

---

### Request Body

```json
{
    "name": "Groceries",
    "type": "expense"
}
```

---

### Success Response

```json
{
    "id": 1,
    "name": "Groceries",
    "type": "expense"
}
```

---

### Error Responses

| Status Code | Description             |
| ----------- | ----------------------- |
| 401         | Unauthorized            |
| 404         | Category not found      |
| 409         | Category already exists |
| 422         | Validation Error        |

---

### Flow

```text
Client
   │
PUT /categories/{id}
   │
   ▼
Router
   │
Authenticate User
Validate Request
   │
   ▼
Service
   │
Find Category
Check Ownership
Check Duplicate
Update Values
   │
   ▼
Repository
UPDATE Category
   │
   ▼
Database
```

---

# 5. Delete Category

### Endpoint

```http
DELETE /categories/{category_id}
```

---

### Example

```http
DELETE /categories/1
```

---

### Description

Deletes a category owned by the authenticated user.

If the category contains transactions, deletion depends on your database constraints (`CASCADE`).

---

### Success Response

**Status Code:** `204 No Content`

No response body.

---

### Error Responses

| Status Code | Description        |
| ----------- | ------------------ |
| 401         | Unauthorized       |
| 404         | Category not found |

---

### Flow

```text
Client
   │
DELETE /categories/{id}
   │
   ▼
Router
   │
Authenticate User
   │
   ▼
Service
   │
Verify Category Exists
Verify Ownership
   │
   ▼
Repository
DELETE Category
   │
   ▼
PostgreSQL
```

---

# Category Business Rules

The following validations are enforced before creating or updating a category:

* The user must be authenticated.
* Category names must be between 2 and 100 characters.
* Category type must be either `income` or `expense`.
* Category names must be unique per user and type.
* Users can only access their own categories.
* Users cannot update or delete another user's categories.
* Duplicate categories are not allowed for the same user and type.

---

# Category Request Lifecycle

```text
Client
   │
HTTP Request
   │
   ▼
Authentication
   │
JWT Validation
   │
   ▼
Router
   │
Pydantic Validation
   │
   ▼
Category Service
   │
Business Rules
Ownership Validation
Duplicate Validation
   │
   ▼
Repository
   │
SQLAlchemy
   │
   ▼
PostgreSQL
   │
   ▼
JSON Response
```






# Transaction Endpoints

All transaction endpoints require a valid **Access Token**.

### Authorization Header

```http
Authorization: Bearer <access_token>
```

---

# 1. Create Transaction

### Endpoint

```http
POST /transactions
```

### Description

Creates a new income or expense transaction for the authenticated user.

The transaction must belong to an existing category owned by the same user.

---

### Request Body

```json
{
    "amount": 250.00,
    "description": "Lunch",
    "transaction_date": "2026-07-10",
    "category_id": 1
}
```

---

### Success Response

**Status Code:** `201 Created`

```json
{
    "id": 1,
    "amount": 250.00,
    "description": "Lunch",
    "transaction_date": "2026-07-10",
    "category_id": 1,
    "user_id": 1,
    "created_at": "2026-07-10T10:30:00Z"
}
```

---

### Error Responses

| Status Code | Description        |
| ----------- | ------------------ |
| 401         | Unauthorized       |
| 404         | Category not found |
| 422         | Validation Error   |

---

### Flow

```text
Client
   │
POST /transactions
   │
   ▼
Router
   │
Validate Request
Authenticate User
   │
   ▼
Transaction Service
   │
Verify Category Exists
Verify Category Ownership
Create Transaction
   │
   ▼
Repository
   │
INSERT Transaction
   │
   ▼
PostgreSQL
```

---

# 2. Get All Transactions

### Endpoint

```http
GET /transactions
```

### Description

Returns all transactions belonging to the authenticated user.

---

### Success Response

**Status Code:** `200 OK`

```json
[
    {
        "id": 1,
        "amount": 250.00,
        "description": "Lunch",
        "transaction_date": "2026-07-10",
        "category_id": 1
    },
    {
        "id": 2,
        "amount": 50000.00,
        "description": "Monthly Salary",
        "transaction_date": "2026-07-01",
        "category_id": 2
    }
]
```

---

### Flow

```text
Client
   │
GET /transactions
   │
   ▼
Router
   │
Authenticate User
   │
   ▼
Service
   │
Repository
SELECT *
FROM transactions
WHERE user_id = current_user.id
```

---

# 3. Get Transaction by ID

### Endpoint

```http
GET /transactions/{transaction_id}
```

### Example

```http
GET /transactions/1
```

---

### Description

Returns a single transaction owned by the authenticated user.

---

### Success Response

```json
{
    "id": 1,
    "amount": 250.00,
    "description": "Lunch",
    "transaction_date": "2026-07-10",
    "category_id": 1
}
```

---

### Error Responses

| Status Code | Description           |
| ----------- | --------------------- |
| 401         | Unauthorized          |
| 404         | Transaction not found |

---

### Flow

```text
Client
   │
GET /transactions/{id}
   │
   ▼
Router
   │
Authenticate User
   │
   ▼
Service
   │
Repository
SELECT Transaction
WHERE
id = transaction_id
AND
user_id = current_user.id
```

---

# 4. Update Transaction

### Endpoint

```http
PUT /transactions/{transaction_id}
```

### Request Body

```json
{
    "amount": 300.00,
    "description": "Dinner",
    "transaction_date": "2026-07-10",
    "category_id": 1
}
```

---

### Success Response

```json
{
    "id": 1,
    "amount": 300.00,
    "description": "Dinner",
    "transaction_date": "2026-07-10",
    "category_id": 1
}
```

---

### Error Responses

| Status Code | Description           |
| ----------- | --------------------- |
| 401         | Unauthorized          |
| 404         | Transaction not found |
| 404         | Category not found    |
| 422         | Validation Error      |

---

### Flow

```text
Client
   │
PUT /transactions/{id}
   │
   ▼
Router
   │
Authenticate User
Validate Request
   │
   ▼
Transaction Service
   │
Find Transaction
Verify Ownership
Verify Category
Update Values
   │
   ▼
Repository
UPDATE Transaction
```

---

# 5. Delete Transaction

### Endpoint

```http
DELETE /transactions/{transaction_id}
```

### Example

```http
DELETE /transactions/1
```

---

### Description

Deletes a transaction belonging to the authenticated user.

---

### Success Response

**Status Code:** `204 No Content`

No response body.

---

### Error Responses

| Status Code | Description           |
| ----------- | --------------------- |
| 401         | Unauthorized          |
| 404         | Transaction not found |

---

### Flow

```text
Client
   │
DELETE /transactions/{id}
   │
   ▼
Router
   │
Authenticate User
   │
   ▼
Service
   │
Verify Transaction Exists
Verify Ownership
   │
   ▼
Repository
DELETE Transaction
```

---

# Transaction Business Rules

The following rules are enforced:

* The user must be authenticated.
* The amount must be greater than zero.
* The transaction date is required.
* The category must exist.
* The category must belong to the authenticated user.
* Users can only access their own transactions.
* Users cannot modify or delete another user's transactions.

---

# Transaction Request Lifecycle

```text
Client
   │
HTTP Request
   │
   ▼
JWT Authentication
   │
Access Token Validation
   │
   ▼
Router
   │
Pydantic Validation
   │
   ▼
Transaction Service
   │
Category Validation
Ownership Validation
Business Rules
   │
   ▼
Repository
   │
SQLAlchemy ORM
   │
   ▼
PostgreSQL
   │
   ▼
JSON Response
```

---

# Module Summary

## Authentication Module

* User Registration
* User Login
* JWT Authentication
* Refresh Token
* Logout
* Protected Routes

---

## Category Module

* Create Category
* Get All Categories
* Get Category by ID
* Update Category
* Delete Category

---

## Transaction Module

* Create Transaction
* Get All Transactions
* Get Transaction by ID
* Update Transaction
* Delete Transaction

All modules follow the same architecture:

```text
Client
   │
   ▼
Router
   │
   ▼
Service
   │
   ▼
Repository
   │
   ▼
PostgreSQL
```

