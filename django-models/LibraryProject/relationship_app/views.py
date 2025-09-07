from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic.detail import DetailView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import user_passes_test, permission_required
from django.contrib import messages
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

# Role checking functions
def is_admin(user):
    return user.is_authenticated and hasattr(user, 'userprofile') and user.userprofile.role == 'Admin'

def is_librarian(user):
    return user.is_authenticated and hasattr(user, 'userprofile') and user.userprofile.role == 'Librarian'

def is_member(user):
    return user.is_authenticated and hasattr(user, 'userprofile') and user.userprofile.role == 'Member'

# Role-based views
@user_passes_test(is_admin)
def admin_view(request):
    """Admin view accessible only to users with Admin role"""
    return render(request, 'relationship_app/admin_view.html')

@user_passes_test(is_librarian)
def librarian_view(request):
    """Librarian view accessible only to users with Librarian role"""
    return render(request, 'relationship_app/librarian_view.html')

@user_passes_test(is_member)
def member_view(request):
    """Member view accessible only to users with Member role"""
    return render(request, 'relationship_app/member_view.html')

# Permission-protected views for book operations
@permission_required('relationship_app.can_add_book', raise_exception=True)
def add_book(request):
    """View to add a new book - requires can_add_book permission"""
    if request.method == 'POST':
        title = request.POST.get('title')
        author_id = request.POST.get('author')

        if title and author_id:
            try:
                author = Author.objects.get(id=author_id)
                book = Book.objects.create(title=title, author=author)
                messages.success(request, f'Book "{book.title}" added successfully!')
                return redirect('list_books')
            except Author.DoesNotExist:
                messages.error(request, 'Selected author does not exist.')
        else:
            messages.error(request, 'Please fill in all required fields.')

    authors = Author.objects.all()
    return render(request, 'relationship_app/add_book.html', {'authors': authors})

@permission_required('relationship_app.can_change_book', raise_exception=True)
def edit_book(request, book_id):
    """View to edit an existing book - requires can_change_book permission"""
    book = get_object_or_404(Book, id=book_id)

    if request.method == 'POST':
        title = request.POST.get('title')
        author_id = request.POST.get('author')

        if title and author_id:
            try:
                author = Author.objects.get(id=author_id)
                book.title = title
                book.author = author
                book.save()
                messages.success(request, f'Book "{book.title}" updated successfully!')
                return redirect('list_books')
            except Author.DoesNotExist:
                messages.error(request, 'Selected author does not exist.')
        else:
            messages.error(request, 'Please fill in all required fields.')

    authors = Author.objects.all()
    return render(request, 'relationship_app/edit_book.html', {'book': book, 'authors': authors})

@permission_required('relationship_app.can_delete_book', raise_exception=True)
def delete_book(request, book_id):
    """View to delete a book - requires can_delete_book permission"""
    book = get_object_or_404(Book, id=book_id)

    if request.method == 'POST':
        book_title = book.title
        book.delete()
        messages.success(request, f'Book "{book_title}" deleted successfully!')
        return redirect('list_books')

    return render(request, 'relationship_app/delete_book.html', {'book': book})