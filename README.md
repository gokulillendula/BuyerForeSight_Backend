# 🚀 Django CRUD API – User Management

This is a simple REST API built using **Django** and **Django REST Framework (DRF)** that supports full CRUD operations with search and sorting functionality.

---

## 📌 Features

* ✅ Create User
* ✅ Read Users (List & Detail)
* ✅ Update User (PUT / PATCH)
* ✅ Delete User
* ✅ Search by name/email
* ✅ Sort by fields (name, age, etc.)

---

## 🛠️ Tech Stack

* Python
* Django
* Django REST Framework
* SQLite (for development)
* Gunicorn (for deployment)

---

## 📂 Project Structure

```
crud/
│── crud/              # Main project folder
│── user/              # App containing models, views, serializers
│── manage.py
│── requirements.txt
```

---

## ⚙️ Installation & Setup

### 1. Clone the repository

```
git clone <your-repo-url>
cd crud
```

### 2. Create virtual environment

```
python -m venv env
env\Scripts\activate   # Windows
```

### 3. Install dependencies

```
pip install -r requirements.txt
```

### 4. Run migrations

```
python manage.py migrate
```

### 5. Start server

```
python manage.py runserver
```

---

## 🌐 API Base URL

```
http://127.0.0.1:8000/api/users/
```

---

## 📡 API Endpoints

### 🔹 Get all users

```
GET /api/users/
```

---

### 🔹 Get single user

```
GET /api/users/{id}/
```

---

### 🔹 Create user

```
POST /api/users/
```

**Body:**

```json
{
  "name": "Gokul",
  "email": "gokul@gmail.com",
  "age": 22
}
```

---

### 🔹 Update user (PUT)

```
PUT /api/users/{id}/
```

---

### 🔹 Partial update (PATCH)

```
PATCH /api/users/{id}/
```

---

### 🔹 Delete user

```
DELETE /api/users/{id}/
```

---

## 🔍 Query Parameters

### 🔹 Search

```
/api/users/?search=gokul
```

---

### 🔹 Sorting

```
/api/users/?sort=name&order=asc
/api/users/?sort=age&order=desc
```

---

## 🚀 Deployment

This project is deployed on Render:

```
https://buyerforesight-backend-qw3p.onrender.com/api/users/
```

---

## ⚠️ Notes

* SQLite is used for development (data resets on redeploy)
* For production, PostgreSQL is recommended
* Ensure `DEBUG = False` in production

---

## 👨‍💻 Author

Gokul

---

## ⭐ Future Improvements

* Add authentication (JWT)
* Add pagination
* Use PostgreSQL for production
* Add API documentation (Swagger)

---
