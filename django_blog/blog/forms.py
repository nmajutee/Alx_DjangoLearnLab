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
from .models import Post, Comment


class CustomUserCreationForm(UserCreationForm):
    """
    Custom user registration form extending Django's built-in UserCreationForm.
    This form adds email and phone fields to the default username and password fields.
    """

    email = forms.EmailField(required=True)
    phone = forms.CharField(max_length=15, required=False)

    class Meta:
        model = User
        fields = ['username', 'email', 'phone', 'password1', 'password2']

class PostForm(forms.ModelForm):
    """
    Form for creating and updating blog posts.
    Automatically handles validation for title and content fields.
    Author and publication date are set automatically in the view.
    """

    class Meta:
        model = Post
        fields = ['title', 'content']

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
        widgets = {
            'content': forms.Textarea(attrs={'rows': 3, 'placeholder': 'Write a comment...'}),
        }