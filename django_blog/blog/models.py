"""
Blog Models
-----------
This module defines the database models for the blog application.

Models:
    Post: Represents a blog post with title, content, author, and publish date.
"""

from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

class Post(models.Model):
    """
    Model representing a blog post.
    """

    title = models.CharField(max_length=200)
    content = models.TextField()
    published_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)

    def __str__(self):
        """Return string representation of the post (its title)."""
        return self.title

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})

