# 📝 Todo Management API

## 🏗️ Core Architecture

- ✅ Follows RESTful principles with JWT authentication  
- 🏗️ Uses Flask framework with a modular structure  
- 📐 Implements MVC pattern with a clear separation of concerns  
- 📜 Features Swagger documentation for API endpoints  

## 🔑 Key Components

### 🔐 A. Authentication System (`auth.py`)

- 🔑 JWT-based security using `flask-jwt-extended`
- 📌 Endpoints:
  - 🆕 `/register`: Creates new users with password hashing
  - 🔓 `/login`: Issues JWT access tokens
  - 🚪 `/logout`: Ends authenticated sessions
- 🔒 Password security using bcrypt hashing

### 📌 B. Task Management (`task.py`)

- ✅ Full CRUD operations for todo items
- 🔹 Features:
  - 📅 Due dates with ISO format validation
  - 🚦 Priority levels (low/medium/high)
  - 📌 Status tracking (pending/completed)
  - 👤 User-specific task isolation
- 📌 Endpoints:
  - `GET/POST /tasks`
  - `GET/PUT/DELETE /tasks/<id>`

### 🗄️ C. Database Layer (`models.py`)

- 🏛️ SQLAlchemy ORM models:
  - 👤 `User`: Stores credentials and relationships
  - ✅ `Task`: Manages todo items with timestamps
- 🔗 Relationships:
  - 1️⃣ One-to-Many: `User → Tasks`
- 🕒 Automatic timestamp handling

### 🔒 D. Security Infrastructure (`security.py`)

- 🔐 BCrypt password hashing
- 🛡️ Methods:
  - 🛠️ `hash_password()`: Secure password storage
  - ✅ `check_password()`: Credential verification

## ⚙️ Configuration Management

- 🌍 Environment-based settings (`config.py`):
  - 🗄️ Database URI configuration
  - 🔑 JWT secret key management
  - ⏳ Token expiration policies
- 📂 Dotenv support for secrets (`.env`)

## 📜 API Documentation

- 📘 Integrated Swagger UI (`/apidocs`)
- 📝 Automatic endpoint documentation
- 🎮 Interactive testing interface
- 🔐 Security scheme definitions

## 🔄 Workflow Process

### 🚀 User Journey:
1. 🆕 Registration
2. 🔑 Authentication
3. 📝 Task Management

### 🔄 Data Flow:
1. 📩 Client Request
2. 🔑 JWT Validation
3. 🏗️ Business Logic
4. 🗄️ Database Operation
5. 📤 Response

### 🔒 Security Measures:
- 🔑 JWT token authentication
- 🔒 Password hashing with BCrypt
- 🛡️ Secure headers configuration
- ⏳ Token expiration (1 hour)
- 🔄 SQL injection prevention through ORM

### ⚠️ Error Handling:

#### ❌ HTTP Status Codes:
- `400` ❌ Bad requests
- `401` 🚫 Unauthorized access
- `404` 🔍 Missing resources
- `500` ⚙️ Server errors (implicit)

#### ✅ Validation Checks:
- 🔁 Duplicate usernames
- 📅 ISO date formatting
- ❗ Required fields

## 🗄️ Database Operations

- 🛠️ SQLAlchemy ORM for CRUD operations
- 🏗️ Automatic table creation
- 🔄 Migration support via Flask-Migrate
- 🔄 Session management with atomic transactions

## 📥 API Response Structure

Consistent JSON formatting:

```json
{
  "id": 1,
  "title": "Buy groceries",
  "description": "Milk and eggs",
  "due_date": "2023-12-31T23:59:59",
  "priority": "medium",
  "status": "pending",
  "created_at": "2023-01-01T00:00:00"
}
```
### 🛠️ Clone this Repository 
```bash
git clone https://github.com/MasteriNeuron/ToDo-List-Project.git
```

## 🛠️ Development Setup

### 1️⃣ Setup Virtual Environment
```bash
conda create -n venv python=3.11 -y
conda activate venv/
```

### 2️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```

### 3️⃣ Initialize the Database
Run these commands one by one in the terminal:
```bash
flask db init
flask db migrate
flask db upgrade
```

### 4️⃣ Start the Flask Server
```bash
python run.py
```

### 5️⃣ Test the API using Postman or Swagger UI
Swagger documentation available at:
```
http://localhost:5000/apidocs
```

## 🚀 API Usage Examples

### 1️⃣ Register User
**Example Request:**
```json
{
  "email": "shubham@pw.live",
  "password": "shubham@123",
  "username": "shubham"
}
```

### 2️⃣ Login User
```json
{
  "email": "shubham@pw.live",
  "password": "shubham@123",
  "username": "shubham"
}
```
Copy `access_token` and use it in Authorization header:
```
Bearer <your-access-token>
```

### 3️⃣ Create Task
**Request Body:**
```json
{
    "title": "Finish project report",
    "description": "Complete the final report for the client presentation.",
    "due_date": "2025-02-15",
    "due_time": "17:00:00",
    "priority": "High"
  }
```

### 4️⃣ Access Tasks
Use the Authorization token:
```
Bearer <your-access-token>
```

### 5️⃣ Update Task
**Request Body:**
```json
{
    "title": "Finish project report",
    "description": "Complete the final report for the client presentation.",
    "due_date": "2025-02-15",
    "due_time": "12:00:00",
    "priority": "High"
  }
```

### 6️⃣ Delete Task
Provide the task ID and send DELETE request.

## 🚀 Future Enhancements

This architecture provides a secure, scalable foundation for todo management with:
- 📌 Clear separation of concerns
- 🏗️ Maintainable code structure
- 🔒 Production-ready security features
- 📜 Comprehensive documentation
- 🔄 Easy extensibility for new features

Possible future enhancements:
- 🏷️ Task categories
- ⏰ Due date reminders
- 👥 User roles/permissions
- 📎 File attachments
- 🔎 Advanced filtering/sorting

