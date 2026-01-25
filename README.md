# ENSIT Spotted

ENSIT Spotted is a web project inspired by the well-known “Spotted” Facebook pages.  
It allows users to submit messages or images anonymously through a website, which are then automatically posted on a Facebook page.

The main goal of this project is to experiment with anonymity, automation, and web development using Django and n8n.

---

## Project Idea

The platform works like this:

1. A user submits a message or an image anonymously
2. The Django backend receives and validates the content
3. The backend sends the data to an n8n webhook
4. n8n publishes the content on a Facebook page

No login system is required, and no user identity is stored.

---

## Technologies Used

- Backend: Django (Python)
- Frontend: HTML, CSS, JavaScript (Django templates)
- Automation: n8n
- Database: SQLite (development)
- External API: Facebook Graph API

---

## Project Structure

```
EnsitSpotted/
│
├── core/                 # Main Django app
│   ├── views.py
│   ├── forms.py
│   ├── models.py
│   └── templates/
│
├── static/               # Static files (CSS, JS, images)
├── EnsitSpotted/         # Project configuration
│   ├── settings.py
│   ├── urls.py
│
├── manage.py
├── requirements.txt
└── README.md
```

---

## Installation

### Clone the repository

```bash
git clone https://github.com/your-username/EnsitSpotted.git
cd EnsitSpotted
```

### Create a virtual environment

```bash
python -m venv venv
source venv/bin/activate      # Linux / Mac
venv\Scripts\activate         # Windows
```

### Install dependencies

```bash
pip install -r requirements.txt
```

### Environment variables

Create a `.env` file in the project root:

```env
SECRET_KEY=your_secret_key
DEBUG=True
N8N_WEBHOOK_URL=https://your-n8n-webhook-url
```

### Run the server

```bash
python manage.py migrate
python manage.py runserver
```

---

## n8n Integration

The Django backend sends a POST request to an n8n webhook.  
The n8n workflow is responsible for formatting the content and publishing it on a Facebook page.

Required Facebook permissions:
- pages_manage_posts
- pages_read_engagement

---

## Anonymity and Privacy

- No user accounts
- No authentication system
- No personal information collected by the application
- Submissions are anonymous by design

Note: As with any web application, hosting providers may still log technical metadata.

---

## Possible Improvements

- Admin moderation dashboard
- Post scheduling
- Automatic content filtering
- Support for multiple Facebook pages
- Improved UI and accessibility

---

## Purpose

This project was created for learning purposes, mainly to practice:
- Django backend development
- API integration
- Workflow automation with n8n
- Designing systems with privacy in mind

---

## Author

Bechir Chemam  
ENSIT – Software Engineering Student

