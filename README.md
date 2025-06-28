# 🧠 Django Intern App

This is a sample backend project for a Django internship assignment.
It demonstrates API development with **Django REST Framework**, authentication, **Celery** background tasks, and **Telegram Bot** integration.

---

## 📦 Features

* 🔐 Token-based authentication using DRF
* ✅ Public & Protected API endpoints
* 🧠 Background task using **Celery + Redis**
* 🤖 Telegram bot integration (via BotFather)
* 🖥️ Simple web login and dashboard views
* 📁 Clean, production-ready structure with environment variables

---

## ⚙️ Technologies Used

* Django 5.x
* Django REST Framework
* Celery
* Redis
* python-telegram-bot
* SQLite (for dev)
* Python-Decouple for environment config

---

## 🚀 Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/YOUR_USERNAME/DJANGO_INTERN_APP.git
cd DJANGO_INTERN_APP
```

---

### 2. Create Virtual Environment

```bash
python -m venv env
env\Scripts\activate    # Windows
# source env/bin/activate   # Linux/macOS
```

---

### 3. Install Requirements

```bash
pip install -r requirements.txt
```

---

### 4. Add `.env` file in root directory

Create a `.env` file and add the following:

```env
SECRET_KEY=your-django-secret-key
DEBUG=False
TELEGRAM_BOT_TOKEN=your-telegram-bot-api-key
```

---

### 5. Run Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

---

### 6. Create Superuser (optional)

```bash
python manage.py createsuperuser
```

---

### 7. Run Development Server

```bash
python manage.py runserver
```

---

### 8. Run Redis Server (separate terminal)

Make sure Redis is installed and running:

```bash
redis-server
```

---

### 9. Run Celery Worker (new terminal)

```bash
celery -A DJANGO_INTERN_APP worker --loglevel=info
```

---

### 10. Run Telegram Bot Script (optional)

```bash
python core/telegram_bot.py
```

---

## 🌐 API Endpoints

| Endpoint           | Method   | Auth | Description         |
| ------------------ | -------- | ---- | ------------------- |
| `/api/public/`     | GET      | ❌    | Public endpoint     |
| `/api/protected/`  | GET      | ✅    | Token required      |
| `/api/token-auth/` | POST     | ❌    | Get auth token      |
| `/login/`          | GET/POST | ❌    | Web login           |
| `/dashboard/`      | GET      | ✅    | Protected dashboard |
| `/test-task/`      | GET      | ❌    | Test Celery task    |
| `/admin/`          | -        | ✅    | Django Admin Panel  |

---

## 📦 Environment Variables Used

| Variable             | Purpose                      |
| -------------------- | ---------------------------- |
| `SECRET_KEY`         | Django secret key            |
| `DEBUG`              | Set to `False` in production |
| `TELEGRAM_BOT_TOKEN` | Telegram bot API token       |

---

## 🤖 Telegram Bot Setup

1. Open Telegram and talk to [@BotFather](https://t.me/BotFather)
2. Run `/newbot` and follow instructions
3. Copy the token and paste it in `.env` as `TELEGRAM_BOT_TOKEN`
4. Run the bot with:

   ```bash
   python core/telegram_bot.py
   ```
5. Say `/start` to your bot — it will store your Telegram username in the database.

---

## 📁 Folder Structure

```
DJANGO_INTERN_APP/
├── core/
│   ├── views.py
│   ├── tasks.py
│   ├── telegram_bot.py
│   ├── models.py
│   ├── urls.py
│   └── templates/
│       ├── login.html
│       └── dashboard.html
├── DJANGO_INTERN_APP/
│   ├── __init__.py
│   ├── celery.py
│   ├── settings.py
│   ├── urls.py
├── db.sqlite3
├── .env
├── requirements.txt
└── README.md
```

---

## ✅ Notes

* This project is not deployed, as per assignment instructions.
* Set `DEBUG=True` only for local testing.

---

## 🧑‍💻 Author

**Samruddhi Tiwari**
Built as part of Django Internship Assignment

---
