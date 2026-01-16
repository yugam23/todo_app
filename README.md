# ✅ Todo App

[![Python](https://img.shields.io/badge/python-3.10%2B-blue)](https://www.python.org/) [![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE) [![Build Status](https://img.shields.io/badge/build-passing-brightgreen.svg)](#)

A simple, clean Flask-based Todo application using SQLite and SQLAlchemy.

---

## 🔧 Features

- Add, edit, delete tasks
- Mark tasks as completed and view completed tasks
- Simple SQLite database (auto-created on first run)

---

## 🚀 Quick Start (Windows)

### Prerequisites

- Python 3.10+ installed
- Git (optional)

### Using the existing virtual environment

1. Open PowerShell in the project root:

```powershell
cd "...\Python Projects\Todo App"
```

2. Activate the bundled virtual environment:

- PowerShell:

```powershell
.\env\Scripts\Activate.ps1
```

- Command Prompt:

```cmd
.\env\Scripts\activate.bat
```

3. Install (or verify) dependencies:

```powershell
pip install -r requirements.txt
```

### Create a new virtual environment (if you prefer)

```powershell
python -m venv env
.\env\Scripts\Activate.ps1
pip install -r requirements.txt
```

### Run the app

```powershell
python run.py
```

Open your browser at: http://127.0.0.1:5000

> The SQLite database `todoDataBase.db` is created automatically on first run.

---

## 🧭 How it works

- The app uses `Flask` for the web server and `Flask-SQLAlchemy` for the ORM.
- Data model: `ToDo` (id, status, content, date).
- Routes:
  - `/` — view and add active tasks
  - `/edit/<id>` — edit a task
  - `/delete/<id>` — delete a task
  - `/complete/<id>` — mark a task completed
  - `/completed` — view completed tasks

---

## 🛠 Development Tips

- To update `requirements.txt` after adding packages:

```powershell
pip freeze > requirements.txt
```

- Toggle debug mode by changing `app.run(debug=True)` in `run.py` to `False` for production.

---

## ✅ Testing Checklist

- [ ] Start the server and visit the root page
- [ ] Create a new task
- [ ] Edit a task
- [ ] Mark a task as completed and confirm it appears on `/completed`
- [ ] Delete a task

---

## 📦 Deployment Notes

For production, consider using a WSGI server (e.g., Gunicorn on Linux) and a more robust DB (Postgres, etc.). Adjust config and disable debug mode.

---

## 📫 Contributing

Contributions are welcome — please open an issue or a PR.

---

## 📝 License

This project is licensed under the **MIT License** — see the [LICENSE](LICENSE) file for details.

---
