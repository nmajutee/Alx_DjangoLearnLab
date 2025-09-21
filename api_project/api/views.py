from django.shortcuts import render
from rest_framework import generics
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Book
from .serializers import BookSerializer

# basic list view
class BookList(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

# this one needs login
class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]  # need to login first
