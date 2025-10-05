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
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .forms import CustomUserCreationForm, PostForm
from .models import Post

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


class PostListView(ListView):
    """
    Display a list of all blog posts.
    This view shows all published blog posts ordered by newest first.
    Accessible to all users (no login required).
    """

    model = Post
    template_name = 'blog/post_list.html'
    context_object_name = 'posts'
    ordering = ['-published_date']

class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/post_detail.html'
    context_object_name = 'post'

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    form_class = PostForm
    template_name = 'blog/post_form.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'blog/post_form.html'

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    template_name = 'blog/post_confirm_delete.html'
    success_url = reverse_lazy('post-list')

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author