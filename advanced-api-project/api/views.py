from django.shortcuts import render
from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from .models import Book
from .serializers import BookSerializer

# view to list all books - anyone can see this
class BookListView(generics.ListAPIView):
    queryset = Book.objects.all()  # get all books from database
    serializer_class = BookSerializer  # use BookSerializer to convert to json

# view to get one book by id - anyone can see this too
class BookDetailView(generics.RetrieveAPIView):
    queryset = Book.objects.all()  # get all books
    serializer_class = BookSerializer  # serialize the book

# view to create new book - need to be logged in
class BookCreateView(generics.CreateAPIView):
    queryset = Book.objects.all()  # not sure why i need this for create but tutorial said so
    serializer_class = BookSerializer  # use serializer for validation
    permission_classes = [IsAuthenticated]  # only logged in users

# view to update existing book - need login
class BookUpdateView(generics.UpdateAPIView):
    queryset = Book.objects.all()  # all books
    serializer_class = BookSerializer  # serialize the data
    permission_classes = [IsAuthenticated]  # must be logged in

# view to delete book - need login too
class BookDeleteView(generics.DestroyAPIView):
    queryset = Book.objects.all()  # all books
    serializer_class = BookSerializer  # need serializer i think?
    permission_classes = [IsAuthenticated]  # must be authenticated
