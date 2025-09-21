# Django Security Setup

I added security settings to protect my Django app.

## Security Settings

In settings.py I added:
```python
SECURE_BROWSER_XSS_FILTER = True
X_FRAME_OPTIONS = 'DENY'  
SECURE_CONTENT_TYPE_NOSNIFF = True
CSRF_COOKIE_HTTPONLY = True
SESSION_COOKIE_HTTPONLY = True
```

## CSRF Protection

I added {% csrf_token %} to all my forms:
- book_create.html
- book_edit.html  
- book_delete.html
- form_example.html

## Safe Database Queries

I use Django forms and get_object_or_404() to make safe database queries.

## Content Security Policy

I made a simple middleware in bookshelf/middleware.py that adds security headers.

## Testing

To test:
1. Try forms without CSRF tokens
2. Check that permissions work
3. Make sure only authorized users can access views