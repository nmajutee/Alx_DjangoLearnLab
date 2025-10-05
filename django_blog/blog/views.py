"""
Blog Views
----------
This module contains view functions for user authentication and profile management.

Views:
    register: Handles user registration with auto-login after successful signup.
    profile: Displays and allows editing of user profile information (login required).
"""

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .forms import CustomUserCreationForm, PostForm, CommentForm
from .models import Post, Comment
from django.db.models import Q


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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comments'] = self.object.comments.all()
        context['comment_form'] = CommentForm()
        return context

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

class CommentCreateView(LoginRequiredMixin, CreateView):
    model = Comment
    form_class = CommentForm
    template_name = 'blog/comment_form.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.post = get_object_or_404(Post, pk=self.kwargs['pk'])
        return super().form_valid(form)

class CommentUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Comment
    form_class = CommentForm
    template_name = 'blog/comment_form.html'

    def test_func(self):
        comment = self.get_object()
        return self.request.user == comment.author

class CommentDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Comment
    template_name = 'blog/comment_confirm_delete.html'

    def get_success_url(self):
        return reverse_lazy('post-detail', kwargs={'pk': self.object.post.pk})

    def test_func(self):
        comment = self.get_object()
        return self.request.user == comment.author

def search_posts(request):
    query = request.GET.get('q', '')
    results = Post.objects.filter(
        Q(title__icontains=query) |
        Q(content__icontains=query) |
        Q(tags__name__icontains=query)
    ).distinct()
    return render(request, 'blog/search_results.html', {'results': results, 'query': query})

class TaggedPostListView(ListView):
    model = Post
    template_name = 'blog/tagged_posts.html'
    context_object_name = 'posts'

    def get_queryset(self):
        return Post.objects.filter(tags__slug=self.kwargs['tag_slug'])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tag'] = self.kwargs['tag_slug']
        return context