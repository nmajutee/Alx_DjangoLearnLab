from django.shortcuts import render
from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend  # for exact filtering
from rest_framework import filters  # for search and ordering
from .models import Book
from .serializers import BookSerializer

# view to list all books - anyone can see this
# now has filtering, searching and ordering (copied from tutorial)
class BookListView(generics.ListAPIView):
    queryset = Book.objects.all()  # get all books from database
    serializer_class = BookSerializer  # use BookSerializer to convert to json

    # filtering stuff - not sure how all this works but it does
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]

    # these let you filter by exact values
    filterset_fields = ['title', 'author', 'publication_year']

    # these let you search with partial matches
    search_fields = ['title', 'author__name']  # author__name goes to related model

    # these let you sort the results
    ordering_fields = ['title', 'publication_year']
    ordering = ['title']  # books sorted by title by default

    # how to use (just add to url):
    # ?title=Harry Potter - find books with exact title
    # ?author=1 - find books by author id 1
    # ?publication_year=1997 - find books from 1997
    # ?search=harry - search for 'harry' in title or author name
    # ?ordering=publication_year - sort by year (old to new)
    # ?ordering=-title - sort by title (z to a)

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
