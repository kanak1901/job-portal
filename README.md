# Job Portal — Django

A complete web-based job portal built with **Django**, **HTML**, **CSS**, **Bootstrap 5**, **JavaScript**, and **SQLite**. Connects job seekers with employers for browsing listings, applying to jobs, and managing applications.

## Features

| Feature | Description |
| -------- | ------------- |
| Home Page | Hero section, featured jobs, and quick links |
| Header & Footer | Responsive navigation with Bootstrap 5 |
| User Registration | Job seeker sign-up with profile |
| Login | Job seeker authentication |
| Employer Login | Separate login for employers |
| Job Listing | Search and filter jobs by keyword, location, type |
| Job Details | Full job description and requirements |
| Apply Job | Submit cover letter and resume |
| Admin Panel | Django admin for users, jobs, and applications |
| Employer Dashboard | Post jobs and view applications |

## Tech Stack

| Layer | Technology |
| ----- | ---------- |
| Backend | Django 6 |
| Frontend | HTML, CSS, Bootstrap 5, JavaScript |
| Database | SQLite |
| Auth | Django Sessions |

## Project Structure

```
Job Portal Project Intership/
├── manage.py
├── requirements.txt
├── job_portal/              # Project settings & URLs
│   ├── settings.py
│   └── urls.py
├── accounts/                # Registration & login
│   ├── models.py            # UserProfile
│   ├── views.py
│   ├── forms.py
│   └── urls.py
├── jobs/                    # Jobs & applications
│   ├── models.py            # Job, Application
│   ├── views.py
│   ├── forms.py
│   └── urls.py
├── templates/               # HTML templates
│   ├── base.html
│   ├── includes/
│   ├── accounts/
│   └── jobs/
├── static/                  # CSS & JS
│   ├── css/style.css
│   └── js/main.js
└── media/                   # Uploaded resumes
```

## Getting Started

### Prerequisites

- Python 3.10+
- pip

### Installation

1. Open a terminal in the project folder:

```bash
cd "Job Portal Project Intership"
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Run database migrations:

```bash
python manage.py migrate
```

4. Create an admin account:

```bash
python manage.py createsuperuser
```

5. Load sample jobs and demo accounts (optional):

```bash
python manage.py load_sample_data
```

Demo credentials after loading sample data:
- **Employer:** `employer_demo` / `demo1234`
- **Job Seeker:** `seeker_demo` / `demo1234`

6. Start the development server:

```bash
python manage.py runserver
```

7. Open in your browser:
   - **Website:** http://127.0.0.1:8000/
   - **Admin Panel:** http://127.0.0.1:8000/admin/

## URL Routes

| URL | Page |
| --- | ---- |
| `/` | Home |
| `/jobs/` | Job Listing |
| `/jobs/<id>/` | Job Details |
| `/jobs/<id>/apply/` | Apply for Job |
| `/accounts/register/` | Job Seeker Registration |
| `/accounts/login/` | Job Seeker Login |
| `/accounts/employer/login/` | Employer Login |
| `/accounts/employer/register/` | Employer Registration |
| `/employer/dashboard/` | Employer Dashboard |
| `/employer/post-job/` | Post a Job |
| `/admin/` | Admin Panel |

## Admin Panel

Use the Django admin at `/admin/` to:

- Manage users and profiles
- Create, edit, and deactivate job postings
- Review and update application statuses
- View uploaded resumes

## License

This project is for educational / internship purposes.

## Author

**Your Name** — Internship Project
