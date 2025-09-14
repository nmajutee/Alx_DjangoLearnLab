from django.db import models
from django.conf import settings
from django.utils.translation import gettext_lazy as _


class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    publication_year = models.IntegerField()

    # Reference to the custom user model
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='owned_books',
        null=True,
        blank=True,
        help_text=_('The user who owns this book')
    )

    # Many-to-many relationship for favorite books
    favorited_by = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        related_name='favorite_books',
        blank=True,
        help_text=_('Users who marked this book as favorite')
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.title} by {self.author} ({self.publication_year})"

    class Meta:
        ordering = ['title']
        verbose_name = _('Book')
        verbose_name_plural = _('Books')
        permissions = [
            ('can_view', 'Can view book'),
            ('can_create', 'Can create book'),
            ('can_edit', 'Can edit book'),
            ('can_delete', 'Can delete book'),
        ]
