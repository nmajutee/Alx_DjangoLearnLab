# Django Blog Authentication System Documentation

## Table of Contents
1. [Overview](#overview)
2. [Features](#features)
3. [System Architecture](#system-architecture)
4. [Component Details](#component-details)
5. [Setup Instructions](#setup-instructions)
6. [User Guide](#user-guide)
7. [Security Features](#security-features)
8. [Testing Guide](#testing-guide)
9. [Troubleshooting](#troubleshooting)
10. [Future Enhancements](#future-enhancements)

---

## Overview

This Django blog application implements a complete user authentication system that allows users to register, login, logout, and manage their profiles. The system is built using Django 4.2's robust authentication framework with custom extensions for additional user information.

**Key Technologies:**
- Django 4.2.25
- Python 3.8+
- Django's built-in authentication system
- PostgreSQL database
- Django template engine

---

## Features

### User Registration
- Custom registration form with extended fields (email, phone)
- Username and email validation
- Strong password requirements with built-in validators:
  - Minimum length of 8 characters
  - Cannot be too similar to user information
  - Cannot be a commonly used password
  - Cannot be entirely numeric
- Automatic login after successful registration
- CSRF protection on all forms

### User Login
- Secure login using Django's AuthenticationForm
- Session-based authentication
- "Remember me" functionality via session cookies
- Redirect to profile page after successful login
- Custom login template with user-friendly interface

### User Logout
- Secure logout functionality
- Session cleanup
- Confirmation page before redirect
- Automatic redirect to login page

### User Profile
- View user information (username, email, join date)
- Edit email address
- Protected by @login_required decorator
- Only authenticated users can access

---

## System Architecture

### Authentication Flow Diagram

```
┌─────────────┐
│   Browser   │
└──────┬──────┘
       │
       │ 1. Access /register/
       ▼
┌─────────────────────────────┐
│  Registration View          │
│  (views.register)           │
│                             │
│  - Display form (GET)       │
│  - Process form (POST)      │
│  - Validate data            │
│  - Create user              │
│  - Auto-login               │
└──────┬──────────────────────┘
       │
       │ 2. Redirect to /profile/
       ▼
┌─────────────────────────────┐
│  Profile View               │
│  (views.profile)            │
│  @login_required            │
│                             │
│  - Check authentication     │
│  - Display user info        │
│  - Allow email update       │
└─────────────────────────────┘
```

### File Structure

```
django_blog/
│
├── blog/                           # Main blog application
│   ├── forms.py                    # CustomUserCreationForm definition
│   ├── views.py                    # register() and profile() views
│   ├── urls.py                     # URL routing for authentication
│   ├── models.py                   # Post model (for future blog posts)
│   │
│   ├── templates/
│   │   └── blog/
│   │       ├── base.html          # Base template with navigation
│   │       ├── register.html      # Registration form
│   │       ├── login.html         # Login form
│   │       ├── logout.html        # Logout confirmation
│   │       └── profile.html       # User profile page
│   │
│   └── static/
│       └── blog/
│           └── css/
│               └── style.css      # Custom styles
│
├── django_blog/                    # Project configuration
│   ├── settings.py                # Django settings with auth configuration
│   └── urls.py                    # Main URL configuration (includes blog.urls)
│
├── db.sqlite3                      # PostgreSQL database
├── manage.py                       # Django management script
└── requirements.txt                # Python dependencies

```

---

## Component Details

### 1. Forms (blog/forms.py)

#### CustomUserCreationForm
Extends Django's `UserCreationForm` to include additional fields.

**Fields:**
- `username`: Unique username (inherited)
- `email`: User's email address (required, custom)
- `phone`: Phone number (optional, custom)
- `password1`: Password (inherited)
- `password2`: Password confirmation (inherited)

**Validation:**
- Email format validation
- Password strength validation (via Django's built-in validators)
- Username uniqueness check

**Code Snippet:**
```python
class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    phone = forms.CharField(max_length=15, required=False)

    class Meta:
        model = User
        fields = ['username', 'email', 'phone', 'password1', 'password2']
```

### 2. Views (blog/views.py)

#### register(request)
Handles user registration with automatic login.

**Process:**
1. **GET request**: Display empty registration form
2. **POST request**:
   - Validate form data
   - Create new user
   - Log user in automatically
   - Redirect to profile page

**Security Features:**
- CSRF token validation
- Form validation
- Password hashing (automatic via Django)

#### profile(request)
Displays and updates user profile information.

**Decorator:** `@login_required` - Ensures only authenticated users can access

**Process:**
1. **GET request**: Display user information
2. **POST request**: Update email address

**Available Data:**
- Username (read-only)
- Email (editable)
- Date joined (read-only)

### 3. URL Patterns (blog/urls.py)

| URL Pattern | View | Template | Description |
|------------|------|----------|-------------|
| `/register/` | `views.register` | `blog/register.html` | User registration |
| `/login/` | `LoginView` | `blog/login.html` | User login |
| `/logout/` | `LogoutView` | `blog/logout.html` | User logout |
| `/profile/` | `views.profile` | `blog/profile.html` | User profile |

### 4. Templates

#### base.html
Base template with:
- Navigation bar with conditional links (login/logout based on auth status)
- Block structure for child templates
- Responsive design
- User greeting for authenticated users

#### register.html
Registration form with:
- Individual field rendering for custom styling
- Error message display per field
- CSRF protection
- Submit button

#### login.html
Login form with:
- Simple `{{ form.as_p }}` rendering
- Error messages
- Link to registration page
- CSRF protection

#### profile.html
Profile page with:
- User information display
- Email editing form
- Formatted date display
- CSRF protection

#### logout.html
Logout confirmation with:
- Success message
- Link back to login page

### 5. Settings Configuration (django_blog/settings.py)

**Authentication Settings:**
```python
# Redirect after successful login
LOGIN_REDIRECT_URL = 'profile'

# Redirect after logout
LOGOUT_REDIRECT_URL = 'login'

# Redirect when @login_required is triggered
LOGIN_URL = 'login'
```

**Password Validators:**
- `UserAttributeSimilarityValidator`: Prevents passwords similar to user info
- `MinimumLengthValidator`: Enforces minimum 8 characters
- `CommonPasswordValidator`: Blocks common passwords
- `NumericPasswordValidator`: Prevents all-numeric passwords

---

## Setup Instructions

### 1. Prerequisites
```bash
# Ensure you have Python 3.8+ installed
python --version

# Navigate to project directory
cd /home/alx/Alx_DjangoLearnLab/django_blog
```

### 2. Database Setup
```bash
# Apply migrations to create database tables
python manage.py makemigrations
python manage.py migrate
```

### 3. Create Superuser (Optional)
```bash
# Create admin account for Django admin panel
python manage.py createsuperuser
```

### 4. Run Development Server
```bash
# Start the Django development server
python manage.py runserver

# Access the application at:
# http://127.0.0.1:8000/
```

### 5. Test Authentication URLs
- Registration: http://127.0.0.1:8000/register/
- Login: http://127.0.0.1:8000/login/
- Profile: http://127.0.0.1:8000/profile/
- Logout: http://127.0.0.1:8000/logout/

---

## User Guide

### How to Register a New Account

1. Navigate to `/register/` or click "Register" in the navigation bar
2. Fill in the registration form:
   - **Username**: Choose a unique username (required)
   - **Email**: Enter your email address (required)
   - **Phone**: Optionally add your phone number
   - **Password**: Create a strong password (min 8 characters)
   - **Password Confirmation**: Re-enter your password
3. Click "Register" button
4. Upon successful registration:
   - You will be automatically logged in
   - Redirected to your profile page

**Note:** If any errors occur (duplicate username, weak password, etc.), they will be displayed next to the relevant field.

### How to Login

1. Navigate to `/login/` or click "Login" in the navigation bar
2. Enter your credentials:
   - **Username**: Your registered username
   - **Password**: Your password
3. Click "Login" button
4. Upon successful login:
   - Redirected to your profile page
   - See personalized greeting in navigation

### How to View/Edit Profile

1. After logging in, navigate to `/profile/` or click "Profile" in navigation
2. View your information:
   - Username (cannot be changed)
   - Current email
   - Date you joined
3. To update email:
   - Enter new email in the input field
   - Click "Update Email"
   - Page will refresh showing updated information

**Note:** Profile page is protected - must be logged in to access.

### How to Logout

1. Click "Logout" in the navigation bar
2. You'll see a confirmation page
3. You'll be automatically redirected to the login page
4. Your session will be cleared

---

## Security Features

### 1. Password Security
- **Hashing**: All passwords are hashed using Django's PBKDF2 algorithm with SHA256
- **Salting**: Random salt added to each password before hashing
- **Validators**: Multiple validators enforce strong password policies
- **Never Stored Plain**: Passwords are never stored in plain text

### 2. CSRF Protection
- All forms include CSRF tokens via `{% csrf_token %}`
- Protects against Cross-Site Request Forgery attacks
- Django validates token on every POST request

### 3. Session Security
- Session-based authentication using secure cookies
- Sessions expire after inactivity (Django default: 2 weeks)
- Session data stored server-side (only session ID in cookie)

### 4. Access Control
- `@login_required` decorator protects sensitive views
- Unauthenticated users automatically redirected to login
- Users can only access their own profile (via request.user)

### 5. SQL Injection Prevention
- Django ORM automatically escapes all queries
- Parameterized queries prevent SQL injection
- No raw SQL queries used in authentication system

### 6. XSS Prevention
- Django templates auto-escape all variables
- User input sanitized before rendering
- Safe HTML tags require explicit marking with `|safe` filter

---

## Testing Guide

### Manual Testing Checklist

#### 1. Registration Testing
```bash
# Start the server
python manage.py runserver

# In your browser, test:
□ Access http://127.0.0.1:8000/register/
□ Try registering with invalid data (see error messages)
□ Register with valid data (check auto-login and redirect)
□ Try registering duplicate username (should show error)
```

**Test Cases:**
- Empty form submission → Should show "This field is required" errors
- Weak password → Should show password validation errors
- Mismatched passwords → Should show "Passwords don't match" error
- Invalid email format → Should show "Enter a valid email" error
- Valid registration → User created and logged in automatically

#### 2. Login Testing
```bash
# Test login functionality:
□ Access http://127.0.0.1:8000/login/
□ Try invalid credentials (check error message)
□ Login with valid credentials (check redirect to profile)
□ Verify navigation shows "Logout" instead of "Login/Register"
```

**Test Cases:**
- Wrong username → "Please enter a correct username and password"
- Wrong password → Same error message (security feature)
- Correct credentials → Successful login and redirect

#### 3. Profile Testing
```bash
# Test profile access and editing:
□ Access profile while logged in (should work)
□ Try accessing /profile/ while logged out (should redirect to login)
□ Update email address (check if it saves)
□ Verify all user information displays correctly
```

**Test Cases:**
- Logged out access → Redirect to `/login/?next=/profile/`
- Email update → New email saves and displays
- Refresh page → Updated email persists

#### 4. Logout Testing
```bash
# Test logout functionality:
□ Click logout while logged in
□ Verify logout confirmation page
□ Check redirect to login page
□ Try accessing /profile/ (should require login again)
```

**Test Cases:**
- Logout → Session cleared
- Post-logout navigation → Shows login/register links
- Profile access after logout → Redirected to login

### Automated Testing

Create a test file `blog/tests.py`:

```python
from django.test import TestCase, Client
from django.contrib.auth.models import User
from django.urls import reverse

class AuthenticationTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(
            username='testuser',
            email='test@example.com',
            password='TestPass123!'
        )

    def test_registration_view(self):
        """Test user can access registration page"""
        response = self.client.get(reverse('register'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'blog/register.html')

    def test_login_view(self):
        """Test user can access login page"""
        response = self.client.get(reverse('login'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'blog/login.html')

    def test_profile_requires_login(self):
        """Test profile page requires authentication"""
        response = self.client.get(reverse('profile'))
        self.assertEqual(response.status_code, 302)  # Redirect
        self.assertTrue(response.url.startswith('/login/'))

    def test_successful_login(self):
        """Test user can login with valid credentials"""
        response = self.client.post(reverse('login'), {
            'username': 'testuser',
            'password': 'TestPass123!'
        })
        self.assertEqual(response.status_code, 302)  # Redirect after login

    def test_registration_creates_user(self):
        """Test registration creates new user"""
        response = self.client.post(reverse('register'), {
            'username': 'newuser',
            'email': 'new@example.com',
            'password1': 'NewPass123!',
            'password2': 'NewPass123!'
        })
        self.assertTrue(User.objects.filter(username='newuser').exists())
```

**Run Tests:**
```bash
python manage.py test blog
```

### Database Testing

```bash
# Check if users are being created correctly
python manage.py shell

# In the Python shell:
>>> from django.contrib.auth.models import User
>>> User.objects.all()
>>> User.objects.filter(username='your_test_user')
>>> user = User.objects.get(username='your_test_user')
>>> user.email
>>> user.date_joined
```

---

## Troubleshooting

### Common Issues and Solutions

#### 1. "CSRF verification failed"
**Symptom:** Error when submitting forms

**Causes:**
- Missing `{% csrf_token %}` in template
- Cookies disabled in browser
- Form submitted from different domain

**Solution:**
```html
<!-- Ensure this is in every form -->
<form method="POST">
    {% csrf_token %}
    <!-- form fields -->
</form>
```

#### 2. "Redirect loop between login and profile"
**Symptom:** Browser shows "too many redirects" error

**Cause:** `LOGIN_REDIRECT_URL` or `LOGIN_URL` misconfigured

**Solution:** Check `settings.py`:
```python
LOGIN_REDIRECT_URL = 'profile'  # Name, not URL path
LOGIN_URL = 'login'             # Name, not URL path
```

#### 3. "Page not found (404)" on /login/
**Symptom:** Django shows 404 error for authentication URLs

**Cause:** URLs not properly included in main urls.py

**Solution:** Check `django_blog/urls.py`:
```python
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blog.urls')),  # Include blog URLs
]
```

#### 4. Profile page accessible without login
**Symptom:** Can access /profile/ without logging in

**Cause:** Missing `@login_required` decorator

**Solution:** Check `blog/views.py`:
```python
from django.contrib.auth.decorators import login_required

@login_required
def profile(request):
    # view code
```

#### 5. Password too weak error
**Symptom:** Registration fails with password validation errors

**Cause:** Password doesn't meet Django's validators

**Solution:** Create stronger password:
- At least 8 characters
- Mix of letters and numbers
- Not similar to username/email
- Not a common password

#### 6. Static files (CSS) not loading
**Symptom:** Pages have no styling

**Cause:** `STATIC_URL` or `STATICFILES_DIRS` misconfigured

**Solution:** Check `settings.py`:
```python
STATIC_URL = 'static/'
STATICFILES_DIRS = [BASE_DIR / 'blog' / 'static']
```

And in templates:
```html
{% load static %}
<link rel="stylesheet" href="{% static 'blog/css/style.css' %}">
```

#### 7. "Reverse for 'profile' not found"
**Symptom:** Error when redirecting to profile

**Cause:** URL name doesn't match in urls.py

**Solution:** Verify URL pattern has correct name:
```python
path('profile/', views.profile, name='profile'),  # name= must match
```

---

## Future Enhancements

### Planned Features

#### 1. Password Reset Functionality
- Email-based password reset
- Secure token generation
- Password reset form

**Implementation Plan:**
```python
# Add to blog/urls.py
from django.contrib.auth import views as auth_views

urlpatterns += [
    path('password-reset/',
         auth_views.PasswordResetView.as_view(),
         name='password_reset'),
    path('password-reset/done/',
         auth_views.PasswordResetDoneView.as_view(),
         name='password_reset_done'),
    path('reset/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(),
         name='password_reset_confirm'),
]
```

#### 2. Email Verification
- Send confirmation email on registration
- Verify email before account activation
- Resend confirmation email

#### 3. Two-Factor Authentication (2FA)
- SMS or authenticator app based 2FA
- Backup codes for account recovery
- Optional 2FA for enhanced security

#### 4. Social Authentication
- Login with Google, GitHub, Facebook
- Using django-allauth package
- Link multiple accounts to one profile

#### 5. Enhanced Profile Features
- Profile picture upload
- Bio/description field
- Additional contact information
- Privacy settings

#### 6. Password Change Feature
- In-profile password change
- Require old password for verification
- Password strength indicator

**Implementation:**
```python
# Add to blog/urls.py
path('password-change/',
     auth_views.PasswordChangeView.as_view(),
     name='password_change'),
```

#### 7. Account Deletion
- Allow users to delete their accounts
- Confirmation dialog
- Option to download data before deletion

#### 8. Login Activity Tracking
- Show last login date/time
- Display login history
- Alert on suspicious activity

---

## Appendix

### Django Authentication System Components

**Models:**
- `User`: Built-in Django user model
- Fields: username, password, email, first_name, last_name, is_active, is_staff, date_joined

**Forms:**
- `UserCreationForm`: Base registration form
- `AuthenticationForm`: Login form
- `PasswordChangeForm`: Password change form
- `PasswordResetForm`: Password reset request form

**Views:**
- `LoginView`: Handles user login
- `LogoutView`: Handles user logout
- `PasswordChangeView`: Password change
- `PasswordResetView`: Password reset initiation

**Decorators:**
- `@login_required`: Restricts view to authenticated users
- `@user_passes_test`: Custom authentication tests
- `@permission_required`: Checks specific permissions

**Helper Functions:**
- `authenticate()`: Verify credentials
- `login()`: Log user in (create session)
- `logout()`: Log user out (clear session)
- `get_user()`: Get current user from request

### Useful Django Commands

```bash
# Create new migrations
python manage.py makemigrations

# Apply migrations
python manage.py migrate

# Create superuser
python manage.py createsuperuser

# Run development server
python manage.py runserver

# Run tests
python manage.py test

# Open Django shell
python manage.py shell

# Check for problems
python manage.py check

# Show all URLs
python manage.py show_urls  # Requires django-extensions
```

### Relevant Django Documentation

- [Django Authentication System](https://docs.djangoproject.com/en/4.2/topics/auth/)
- [User Authentication in Django](https://docs.djangoproject.com/en/4.2/topics/auth/default/)
- [Customizing Authentication](https://docs.djangoproject.com/en/4.2/topics/auth/customizing/)
- [Using the Django Authentication System](https://docs.djangoproject.com/en/4.2/topics/auth/default/#using-the-django-authentication-system)
- [Password Management](https://docs.djangoproject.com/en/4.2/topics/auth/passwords/)

---

## Contact & Support

For issues, questions, or contributions:
- Project Repository: [Alx_DjangoLearnLab](https://github.com/nmajutee/Alx_DjangoLearnLab)
- Author: nmajutee

---

**Last Updated:** October 5, 2025
**Django Version:** 4.2.25
**Python Version:** 3.8+

---

*This documentation is part of the Django Blog Learning Project.*
