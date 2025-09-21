from django.shortcuts import render
from rest_framework import generics
from .models import Book
from .serializers import BookSerializer

# This is my first API view! It will show all the books
class BookList(generics.ListAPIView):
    queryset = Book.objects.all()  # get all books from database
    serializer_class = BookSerializer  # use the BookSerializer I made
