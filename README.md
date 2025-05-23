# 🐍 Flask + PostgreSQL + pgAdmin (Dockerized)

This project is a minimal Flask API that connects to a PostgreSQL database and provides a `/users` endpoint. It includes **pgAdmin** for visual database management.

---

## 🚀 Features

- Flask web API with `/` and `/users` routes
- PostgreSQL as the backend database
- pgAdmin 4 for database UI (access in browser)
- Dockerized deployment with Docker Compose

---

## 📁 Project Structure

🌐 Accessing the Services
▶️ Flask API
URL: http://localhost:5000

Endpoint: http://localhost:5000/users

📊 pgAdmin (PostgreSQL UI)
URL: http://localhost:8080

Login:

Email: admin@admin.com

Password: admin

Add a new server:

Name: Postgres (any name)

Host: db

Port: 5432

Username: user

Password: password

🧪 Create Sample Table
Once logged into pgAdmin, open a query window and run:

sql
Copy
Edit
CREATE TABLE users (
  id SERIAL PRIMARY KEY,
  name VARCHAR(100)
);

INSERT INTO users (name) VALUES ('Alice'), ('Bob');
📦 Python Requirements (apps/requirements.txt)
php
Copy
Edit
flask
and save it

hope this project will help you to find your best practice in devops-journey 







