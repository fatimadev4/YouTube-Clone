# YouTube Clone Project

## Overview
This project is a **YouTube Clone** built to simulate core features of a video streaming platform. It includes user authentication, video upload, video streaming, and basic account management functionalities. The backend handles video processing and streaming through uploaded files and URL-based streaming.

---

## Features

### User System
- User Registration
- User Login / Logout
- Account Page (Profile management)

### Video System
- Upload videos from local device
- Stream videos via URL
- Video listing and playback
- Backend handling for media storage

### Upload System
- Upload video files
- Add video metadata
- Support for:
  - File upload
  - URL-based streaming input

---

## Tech Stack
- Frontend: HTML, CSS, JavaScript / React
- Backend: Django / Node.js
- Database: SQLite / MySQL
- Media Handling: Django Media / Cloud Storage

---

## Installation & Setup

```bash
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name
````

### Create Virtual Environment (Django)

```bash
python -m venv env
env\Scripts\activate   # Windows
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run Migrations

```bash
python manage.py migrate
```

### Start Server

```bash
python manage.py runserver
```

---

## 📂 Project Structure

```
project/
│
├── accounts/          # Login, Register, Logout, Profile
├── videos/            # Video upload & streaming logic
├── templates/         # HTML files
├── static/            # CSS, JS, images
├── media/             # Uploaded videos
├── manage.py
```

---

## Core Pages

* `/register` → Create account
* `/login` → User login
* `/logout` → Logout user
* `/account` → User profile
* `/upload` → Upload videos
* `/videos` → Watch videos

---

## 🎯 Key Functionality

* Secure authentication system
* Video upload and streaming
* URL-based video streaming support
* Clean modular backend structure

