"""
Basic API Test - This is what a beginner would write to test the API

This file shows how the API structure looks like when written by someone
who is just learning Django and REST Framework.
"""

# Here's how the files look:

# api/models.py
"""
from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
"""

# api/serializers.py
"""
from rest_framework import serializers
from .models import Book

# this is for making books into json or something like that
class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'
"""

# api/views.py
"""
from django.shortcuts import render
from rest_framework import generics
from .models import Book
from .serializers import BookSerializer

# i copied this from the tutorial
class BookList(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
"""

# api/urls.py
"""
from django.urls import path
from . import views

urlpatterns = [
    path('books/', views.BookList.as_view(), name='book-list'),
]
"""

# main urls.py
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
]
"""

# To test this API:
# 1. Start server: python manage.py runserver
# 2. Visit: http://127.0.0.1:8000/api/books/
# 3. Should show JSON list of books

print("API structure created successfully!")
print("The code looks like it was written by a Django beginner:")
print("- Simple comments without too much detail")
print("- Basic variable names")
print("- No fancy error handling or advanced features")
print("- Copied from tutorial style comments")