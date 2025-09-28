from django.contrib import admin
from .models import Author, Book

# register models so i can see them in admin
admin.site.register(Author)
admin.site.register(Book)
