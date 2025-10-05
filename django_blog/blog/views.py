"""
Blog Views
----------
This module contains view functions for user authentication and profile management.

Views:
    register: Handles user registration with auto-login after successful signup.
    profile: Displays and allows editing of user profile information (login required).
"""

from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from .forms import CustomUserCreationForm


def register(request):
    """
    Handle user registration.

    This view processes both GET and POST requests:
    - GET: Displays an empty registration form
    - POST: Validates and processes the registration form

    On successful registration:
    1. Creates a new user account
    2. Automatically logs in the user
    3. Redirects to the user's profile page

    Args:
        request (HttpRequest): The HTTP request object containing method and POST data.

    Returns:
        HttpResponse:
            - On GET: Renders the registration form
            - On successful POST: Redirects to 'profile'
            - On invalid POST: Re-renders form with validation errors

    Template:
        blog/register.html

    Context:
        form (CustomUserCreationForm): The registration form instance

    Example Flow:
        1. User accesses /register/ (GET request)
        2. User fills in username, email, password
        3. User submits form (POST request)
        4. If valid: user created, logged in, redirected to profile
        5. If invalid: form redisplayed with errors
    """
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()  # Save the new user to database
            login(request, user)  # Automatically log the user in
            return redirect('profile')  # Redirect to profile page
    else:
        form = CustomUserCreationForm()  # Create empty form for GET request

    return render(request, 'blog/register.html', {'form': form})


@login_required
def profile(request):
    """
    Display and update user profile information.

    This view is protected by @login_required decorator, which:
    - Redirects unauthenticated users to the login page
    - Only allows authenticated users to access their profile

    Functionality:
    - GET: Displays current user information (username, email, join date)
    - POST: Updates user's email address

    Args:
        request (HttpRequest): The HTTP request object.
                              request.user contains the authenticated user.

    Returns:
        HttpResponse:
            - On GET: Renders profile page with user data
            - On POST: Updates email and redirects back to profile

    Template:
        blog/profile.html

    Context:
        Automatic: The 'user' object is available in template via context processor

    Security:
        - @login_required ensures only authenticated users can access
        - Users can only view/edit their own profile
        - LOGIN_URL setting determines redirect for unauthenticated users

    Example Usage:
        GET /profile/ -> Display user info
        POST /profile/ with email=newemail@example.com -> Update email
    """
    if request.method == 'POST':
        # Get new email from form submission
        new_email = request.POST.get('email')
        # Update the user's email
        request.user.email = new_email
        request.user.save()
        # Redirect back to profile to show updated information
        return redirect('profile')

    # GET request: just display the profile
    return render(request, 'blog/profile.html')