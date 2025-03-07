from relationship_app.models import Author, Book, Library, Librarian
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.shortcuts import render
from .models import Library

def list_books(request):
    books = Book.objects.all()
    context = {'book_list':'books'}
    return (request, render, 'relationship_app/list_books.html', context )

class LibraryListView(ListView):
    model = Library
    template_name = 'relationship_app/library_detail.html'

class LibraryDetailView(DetailView):
    pass
