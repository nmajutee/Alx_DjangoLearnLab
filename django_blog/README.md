# Django Blog Application

A complete Django blog application with user authentication, blog post management, commenting system, and advanced features like tagging and search.

## Project Overview

This is a learning project built to understand Django fundamentals and best practices. The application is being developed in phases, each adding new functionality.

## Development Phases

### ✅ Task 0: Initial Setup (Completed)
- Created Django project `django_blog`
- Created app `blog`
- Set up Post model
- Created directory structure for templates and static files
- Applied initial migrations

### ✅ Task 1: User Authentication System (Completed)
- Custom user registration with email and phone fields
- Secure login/logout functionality
- User profile viewing and editing
- Protected routes using `@login_required`
- Comprehensive authentication documentation

**See [AUTHENTICATION_README.md](./AUTHENTICATION_README.md) for detailed authentication documentation.**

### 🚧 Task 2: Blog Post Management (In Progress)
- CRUD operations for blog posts
- Class-based views (ListView, DetailView, CreateView, UpdateView, DeleteView)
- Post ownership and permissions
- Rich text editor for content

### 📋 Task 3: Comment System (Planned)
- Add comments to blog posts
- Comment moderation
- Nested comments/replies
- User-specific comment management

### 📋 Task 4: Advanced Features (Planned)
- Tagging system for posts
- Search functionality
- Post filtering and sorting
- RSS feed generation

## Technology Stack

- **Framework:** Django 4.2.25
- **Language:** Python 3.8+
- **Database:** PostgreSQL
- **Frontend:** Django Templates, CSS
- **Authentication:** Django built-in auth system

## Project Structure

```
django_blog/
├── blog/                          # Main blog application
│   ├── forms.py                   # Custom forms (registration, etc.)
│   ├── views.py                   # View functions and class-based views
│   ├── models.py                  # Database models (Post, Comment, etc.)
│   ├── urls.py                    # URL routing
│   ├── admin.py                   # Django admin configuration
│   ├── templates/blog/            # HTML templates
│   │   ├── base.html             # Base template
│   │   ├── register.html         # Registration page
│   │   ├── login.html            # Login page
│   │   ├── profile.html          # User profile
│   │   └── logout.html           # Logout confirmation
│   └── static/blog/css/           # CSS stylesheets
├── django_blog/                   # Project configuration
│   ├── settings.py               # Django settings
│   └── urls.py                   # Main URL configuration
├── manage.py                      # Django management script
├── requirements.txt               # Python dependencies
├── README.md                      # This file
└── AUTHENTICATION_README.md       # Authentication system documentation
```

## Installation & Setup

### 1. Clone the Repository
```bash
cd /home/alx/Alx_DjangoLearnLab/django_blog
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Configure Database
Update `django_blog/settings.py` with your PostgreSQL credentials:
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'blog_db',
        'USER': 'your_username',
        'PASSWORD': 'your_password',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```

### 4. Run Migrations
```bash
python manage.py makemigrations
python manage.py migrate
```

### 5. Create Superuser (Optional)
```bash
python manage.py createsuperuser
```

### 6. Run Development Server
```bash
python manage.py runserver
```

Access the application at: http://127.0.0.1:8000/

## Available URLs

### Authentication URLs
- `/register/` - User registration
- `/login/` - User login
- `/logout/` - User logout
- `/profile/` - User profile (login required)

### Admin Interface
- `/admin/` - Django admin panel (superuser required)

## Features

### Current Features (Task 1)
✅ User registration with custom fields (email, phone)
✅ Secure login/logout
✅ User profile viewing and editing
✅ Password validation and security
✅ CSRF protection
✅ Session management
✅ Protected routes

### Upcoming Features (Task 2-4)
🚧 Blog post creation, editing, deletion
🚧 Post listing and detail views
🚧 Comment system
🚧 Post tagging
🚧 Search functionality

## Documentation

- **[AUTHENTICATION_README.md](./AUTHENTICATION_README.md)** - Complete authentication system documentation with:
  - System architecture and flow diagrams
  - Component details (forms, views, templates)
  - Setup and configuration instructions
  - User guide and testing procedures
  - Security features explanation
  - Troubleshooting guide

## Testing

### Run Automated Tests
```bash
python manage.py test blog
```

### Manual Testing
Follow the testing guide in [AUTHENTICATION_README.md](./AUTHENTICATION_README.md#testing-guide)

## Development Guidelines

### Code Style
- Follow PEP 8 style guidelines
- Use meaningful variable and function names
- Add docstrings to all functions and classes
- Include comments for complex logic

### Git Workflow
```bash
# Check current status
git status

# Add changes
git add .

# Commit with descriptive message
git commit -m "Add: Description of changes"

# Push to repository
git push origin main
```

### Documentation
- Update README.md when adding new features
- Create detailed documentation for major components
- Include code examples and usage instructions
- Keep troubleshooting section updated

## Common Commands

```bash
# Run development server
python manage.py runserver

# Make migrations
python manage.py makemigrations

# Apply migrations
python manage.py migrate

# Create superuser
python manage.py createsuperuser

# Run tests
python manage.py test

# Open Django shell
python manage.py shell

# Check for problems
python manage.py check
```

## Troubleshooting

See [AUTHENTICATION_README.md - Troubleshooting](./AUTHENTICATION_README.md#troubleshooting) for common issues and solutions.

## Learning Resources

- [Django Documentation](https://docs.djangoproject.com/en/4.2/)
- [Django Authentication System](https://docs.djangoproject.com/en/4.2/topics/auth/)
- [Django Class-Based Views](https://docs.djangoproject.com/en/4.2/topics/class-based-views/)
- [Django Template Language](https://docs.djangoproject.com/en/4.2/topics/templates/)

## Project Status

**Current Phase:** Task 1 Complete - User Authentication System
**Next Phase:** Task 2 - Blog Post Management with CRUD Operations
**Last Updated:** October 5, 2025

## Repository

**GitHub:** [Alx_DjangoLearnLab](https://github.com/nmajutee/Alx_DjangoLearnLab)
**Author:** nmajutee

## License

This is a learning project created as part of the ALX Django course.

---

*For detailed authentication system documentation, see [AUTHENTICATION_README.md](./AUTHENTICATION_README.md)*
