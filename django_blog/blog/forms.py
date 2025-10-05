"""
Blog Forms
----------
This module contains custom forms for user authentication and registration.

Forms:
    CustomUserCreationForm: Extended user registration form with additional fields.
"""

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class CustomUserCreationForm(UserCreationForm):
    """
    Custom user registration form extending Django's built-in UserCreationForm.

    This form adds email and phone fields to the default username and password fields.

    Attributes:
        email (EmailField): User's email address (required).
                           Validated to ensure proper email format.
        phone (CharField): User's phone number (optional, max 15 characters).

    Meta:
        model (User): Django's built-in User model.
        fields (list): Fields to include in the form:
                      - username: Unique username for login
                      - email: User's email address
                      - phone: User's phone number (optional)
                      - password1: Initial password
                      - password2: Password confirmation

    Inherits:
        UserCreationForm: Provides username, password1, and password2 fields
                         with built-in password validation.

    Example:
        >>> form = CustomUserCreationForm(data={
        ...     'username': 'john_doe',
        ...     'email': 'john@example.com',
        ...     'phone': '1234567890',
        ...     'password1': 'SecurePass123',
        ...     'password2': 'SecurePass123'
        ... })
        >>> if form.is_valid():
        ...     user = form.save()
    """

    email = forms.EmailField(required=True)
    phone = forms.CharField(max_length=15, required=False)

    class Meta:
        model = User
        fields = ['username', 'email', 'phone', 'password1', 'password2']