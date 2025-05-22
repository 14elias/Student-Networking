# ETalpha

ETalpha is a Django-based Q&A and news platform for Ethiopian students, providing department-based question answering, news updates, and user management.

## Features

- User registration, login, and profile management
- Department and course-based Q&A system
- Save questions for future reference
- News section with comments
- Admin dashboard for managing users and content
- Payment and premium user management

## Project Structure

```
ETalpha/
├── alpha/                # Main app: models, views, forms, admin, etc.
│   ├── migrations/
│   ├── templates/
│   ├── static/
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── models.py
│   ├── serializers.py
│   ├── tests.py
│   └── views.py
├── ETalpha/              # Project settings and URLs
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── media/                # Uploaded files (profile pics, receipts, etc.)
├── static/               # Static files (CSS, JS, images)
├── templates/            # HTML templates
├── db.sqlite3            # SQLite database
└── manage.py             # Django management script
```

## Setup

1. **Clone the repository**
2. **Install dependencies**
   ```sh
   pip install -r requirements.txt
   ```
3. **Apply migrations**
   ```sh
   python manage.py migrate
   ```
4. **Create a superuser**
   ```sh
   python manage.py createsuperuser
   ```
5. **Run the development server**
   ```sh
   python manage.py runserver
   ```

## Configuration

- Update email settings in [`ETalpha/settings.py`](ETalpha/settings.py) for password reset and notifications.
- Media and static files are configured in the settings.

## Usage

- Visit `/register/` to create a new account.
- Log in at `/login/`.
- Access Q&A at `/questions/` and news at `/news/`.
- Admin interface is available at `/admin/`.

## License

This project is for educational purposes.

---

For more details, see the code in [alpha/views.py](alpha/views.py), [alpha/models.py](alpha/models.py), and [ETalpha/settings.py](ETalpha/settings.py).
