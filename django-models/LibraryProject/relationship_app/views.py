from relationship_app.models import Author, Book, Library, Librarian
from django.shortcuts import render
from django.http import HttpResponse

def bookview(request):
    books = Book.objects.all()
    context = {'title':'author'}
    return (render, context)