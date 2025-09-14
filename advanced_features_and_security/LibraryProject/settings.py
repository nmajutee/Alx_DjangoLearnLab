from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-gu@75dddrya1y6%g1v1z$kk49*q*y6l+2j-84p!ug@39y$@b*8"

# SECURITY WARNING: don't run with debug turned on in production!
# Set to False in production for security
DEBUG = False

ALLOWED_HOSTS = ['localhost', '127.0.0.1', '*']  # Configure for your domain in production


# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "bookshelf",
    "accounts",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "LibraryProject.middleware.SecurityHeadersMiddleware",  # Custom security headers
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "LibraryProject.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "LibraryProject.wsgi.application"


# Database
# https://docs.djangoproject.com/en/5.2/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}


# Password validation
# https://docs.djangoproject.com/en/5.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# Internationalization
# https://docs.djangoproject.com/en/5.2/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.2/howto/static-files/

STATIC_URL = "static/"

# Media files (User uploaded content)
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

# Custom User Model
AUTH_USER_MODEL = 'accounts.CustomUser'

# Default primary key field type
# https://docs.djangoproject.com/en/5.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# Security Settings
# https://docs.djangoproject.com/en/5.2/topics/security/

# Browser XSS filtering
SECURE_BROWSER_XSS_FILTER = True

# Prevent clickjacking attacks
X_FRAME_OPTIONS = 'DENY'

# Prevent MIME type sniffing
SECURE_CONTENT_TYPE_NOSNIFF = True

# CSRF protection settings
CSRF_COOKIE_SECURE = True  # Send CSRF cookie over HTTPS only
CSRF_COOKIE_HTTPONLY = True  # Prevent JavaScript access to CSRF cookie

# Session security settings
SESSION_COOKIE_SECURE = True  # Send session cookie over HTTPS only
SESSION_COOKIE_HTTPONLY = True  # Prevent JavaScript access to session cookie
SESSION_COOKIE_AGE = 3600  # Session timeout (1 hour)

# HTTPS Security Settings
# Force HTTPS redirect - redirects all HTTP requests to HTTPS
SECURE_SSL_REDIRECT = True

# HTTP Strict Transport Security (HSTS) settings
# Instructs browsers to only access site via HTTPS for specified time (1 year)
SECURE_HSTS_SECONDS = 31536000  # 1 year in seconds

# Include all subdomains in HSTS policy
SECURE_HSTS_INCLUDE_SUBDOMAINS = True

# Allow site to be included in HSTS preload list for faster security
SECURE_HSTS_PRELOAD = True

# Ensure proxy headers are properly handled for HTTPS detection
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
