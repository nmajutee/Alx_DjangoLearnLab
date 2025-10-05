"""
Blog URL Configuration
----------------------
This module defines URL patterns for the blog application's authentication system.

URL Patterns:
    /register/ - User registration page
    /login/ - User login page
    /logout/ - User logout page
    /profile/ - User profile page (login required)

All URLs are namespaced under the blog app.
"""

from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from . import views


urlpatterns = [
    # User Registration
    # URL: /register/
    # View: Custom registration view with auto-login
    # Template: blog/register.html
    path('register/', views.register, name='register'),

    # User Login
    # URL: /login/
    # View: Django's built-in LoginView (uses AuthenticationForm)
    # Template: blog/login.html
    # On success: Redirects to LOGIN_REDIRECT_URL (profile)
    path('login/', LoginView.as_view(template_name='blog/login.html'), name='login'),

    # User Logout
    # URL: /logout/
    # View: Django's built-in LogoutView
    # Template: blog/logout.html (confirmation page)
    # On success: Redirects to LOGOUT_REDIRECT_URL (login)
    path('logout/', LogoutView.as_view(template_name='blog/logout.html'), name='logout'),

    # User Profile
    # URL: /profile/
    # View: Custom profile view (view and edit user info)
    # Template: blog/profile.html
    # Requires: User must be authenticated (@login_required)
    path('profile/', views.profile, name='profile'),
]