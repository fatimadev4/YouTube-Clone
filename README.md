
# YouTube Clone Project

## Overview
This project is a YouTube Clone built to simulate core features of a video streaming platform. It includes user authentication, video upload, video streaming, and basic account management functionalities. The backend handles video processing and streaming through uploaded files and URL-based streaming using ImageKit.io.

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
- Backend handling for media storage using ImageKit.io

### Upload System
- Upload video files
- Add video metadata
- Support for:
  - File upload
  - URL-based streaming input

---

## Tech Stack
- Frontend: HTML, CSS, JavaScript / React
- Backend: Django
- Database: SQLite / MySQL
- Media Handling: ImageKit.io

---

## Installation & Setup

### Clone the repository
```bash
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name
````

---

### Install pipenv

```bash
pip install pipenv
```

---

### Create virtual environment and activate it

```bash
pipenv shell
```

---

### Install dependencies

```bash
pipenv install django
pipenv install imagekitio
pipenv install python-dotenv
```

---

### Run migrations

```bash
python manage.py migrate
```

---

### Start server

```bash
python manage.py runserver
```

---

## Project Structure

```
project/
│
├── accounts/          # Login, Register, Logout, Profile
├── videos/            # Video upload & streaming logic
├── templates/         # HTML files
├── static/            # CSS, JS, images
├── media/             # Uploaded videos (or ImageKit references)
├── manage.py
```

---

## Core Pages

* /register → Create account
* /login → User login
* /logout → Logout user
* /account → User profile
* /upload → Upload videos
* /videos → Watch videos

---

## Key Functionality

* Secure authentication system
* Video upload and streaming
* URL-based video streaming support
* ImageKit.io integration for media handling
* Clean modular backend structure

---

## ImageKit.io Configuration

Create a `.env` file in your project root:

```
IMAGEKIT_PUBLIC_KEY=your_public_key
IMAGEKIT_PRIVATE_KEY=your_private_key
IMAGEKIT_URL_ENDPOINT=your_url_endpoint
```

ImageKit.io is used for:

* Fast image/video delivery via CDN
* Media optimization
* Scalable storage instead of local media files



