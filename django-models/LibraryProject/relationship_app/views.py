from django.shortcuts import render
from django.views.generic.detail import DetailView
from .models import Author
from .models import Book
from .models import Library

def list_all_books(request):
    """Retrieves all books and renders a template displaying the list of books, titles and their authors"""
    books = Book.objects.all()
    authors = Author.objects.all()
    context = {
        'books': books,
        'authors': authors
    }
    return render(request, 'relationship_app/list_books.html', context)

class BookDetailView(DetailView):
    """A class-based view for displaying details of a specific book."""
    model = Book
    template_name = 'relationship_app/book_detail.html'

class LibraryDetailView(DetailView):
    """A class-based view for displaying details of a specific library."""
    model = Library
    template_name = 'relationship_app/library_detail.html'