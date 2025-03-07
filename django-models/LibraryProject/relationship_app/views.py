from relationship_app.models import Author, Book, Library, Librarian
from django.shortcuts import render
from django.http import HttpResponse

def list_book_view(request):
    books = Book.objects.all()
    context = {'book_list':'books'}
    return (render, 'relationship_app/list_books.html', context )