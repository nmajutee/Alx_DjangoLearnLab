from relationship_app.models import Author, Book, Library, Librarian
from django.views.generic.detail import DetailView
from django.shortcuts import render
from .models import Library

def list_books(request):
    books = Book.objects.all()
    context = {'book_list':'books'}
    return (request, render, 'relationship_app/list_books.html', context )

class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['books'] = self.objects.books.all()