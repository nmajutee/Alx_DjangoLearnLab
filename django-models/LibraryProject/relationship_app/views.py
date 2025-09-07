from django.shortcuts import render, redirect
from django.views.generic.detail import DetailView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView, LogoutView
from .models import Author
from .models import Book
from .models import Library

def list_books(request):
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

# Authentication Views
class CustomLoginView(LoginView):
    """Custom login view using Django's built-in LoginView"""
    template_name = 'relationship_app/login.html'

class CustomLogoutView(LogoutView):
    """Custom logout view using Django's built-in LogoutView"""
    template_name = 'relationship_app/logout.html'

def register(request):
    """Registration view for new users"""
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('list_books')
    else:
        form = UserCreationForm()
    return render(request, 'relationship_app/register.html', {'form': form})