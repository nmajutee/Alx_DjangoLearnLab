"""
Blog Models
-----------
This module defines the database models for the blog application.

Models:
    Post: Represents a blog post with title, content, author, and publish date.
"""

from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    """
    Model representing a blog post.

    Attributes:
        title (CharField): The title of the blog post (max 200 characters).
        content (TextField): The main content/body of the blog post.
        published_date (DateTimeField): Timestamp when the post was created (auto-generated).
        author (ForeignKey): Reference to the User who created the post.
                            Uses CASCADE deletion - if user is deleted, their posts are also deleted.

    Methods:
        __str__: Returns the title of the post as its string representation.

    Example:
        >>> post = Post.objects.create(
        ...     title="My First Post",
        ...     content="This is the content of my first blog post.",
        ...     author=user
        ... )
        >>> print(post)
        'My First Post'
    """

    title = models.CharField(max_length=200)
    content = models.TextField()
    published_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)

    def __str__(self):
        """Return string representation of the post (its title)."""
        return self.title

