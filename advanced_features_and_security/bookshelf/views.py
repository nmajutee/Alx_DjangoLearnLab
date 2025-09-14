from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib import messages
from django.http import HttpResponseForbidden
from django.core.paginator import Paginator
from django.db.models import Q
from django.utils.html import escape
from django.views.decorators.csrf import csrf_protect
from .models import Book
from .forms import BookForm


@login_required
@permission_required('bookshelf.can_view', raise_exception=True)
def book_list(request):
    """
    View to display a list of all books.
    Requires 'can_view' permission.
    SECURITY: Uses Django ORM to prevent SQL injection, escapes search input.
    """
    search_query = request.GET.get('search', '')
    books = Book.objects.all()

    if search_query:
        # SECURITY: Using Django ORM Q objects prevents SQL injection
        # Input is automatically escaped by Django ORM
        search_query = search_query.strip()[:100]  # Limit search query length
        books = books.filter(
            Q(title__icontains=search_query) |
            Q(author__icontains=search_query)
        )

    # Pagination
    paginator = Paginator(books, 10)  # Show 10 books per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'page_obj': page_obj,
        'search_query': search_query,
        'user_can_create': request.user.has_perm('bookshelf.can_create'),
        'user_can_edit': request.user.has_perm('bookshelf.can_edit'),
        'user_can_delete': request.user.has_perm('bookshelf.can_delete'),
    }
    return render(request, 'bookshelf/book_list.html', context)


@login_required
@permission_required('bookshelf.can_view', raise_exception=True)
def book_detail(request, pk):
    """
    View to display details of a specific book.
    Requires 'can_view' permission.
    """
    book = get_object_or_404(Book, pk=pk)

    context = {
        'book': book,
        'user_can_edit': request.user.has_perm('bookshelf.can_edit'),
        'user_can_delete': request.user.has_perm('bookshelf.can_delete'),
        'is_favorite': book.favorited_by.filter(id=request.user.id).exists(),
    }
    return render(request, 'bookshelf/book_detail.html', context)


@login_required
@permission_required('bookshelf.can_create', raise_exception=True)
@csrf_protect
def book_create(request):
    """
    View to create a new book.
    Requires 'can_create' permission.
    SECURITY: Uses Django forms for input validation and CSRF protection.
    """
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            # SECURITY: Form validation prevents malicious input
            book = form.save(commit=False)
            book.owner = request.user  # Assign current user as owner
            book.save()
            messages.success(request, 'Book created successfully!')
            return redirect('book_detail', pk=book.pk)
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = BookForm()

    context = {'form': form, 'action': 'Create'}
    return render(request, 'bookshelf/book_form.html', context)


@login_required
@permission_required('bookshelf.can_edit', raise_exception=True)
def book_edit(request, pk):
    """
    View to edit an existing book.
    Requires 'can_edit' permission.
    """
    book = get_object_or_404(Book, pk=pk)

    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            messages.success(request, 'Book updated successfully!')
            return redirect('book_detail', pk=book.pk)
    else:
        form = BookForm(instance=book)

    context = {'form': form, 'book': book, 'action': 'Edit'}
    return render(request, 'bookshelf/book_form.html', context)


@login_required
@permission_required('bookshelf.can_delete', raise_exception=True)
def book_delete(request, pk):
    """
    View to delete a book.
    Requires 'can_delete' permission.
    """
    book = get_object_or_404(Book, pk=pk)

    if request.method == 'POST':
        title = book.title
        book.delete()
        messages.success(request, f'Book "{title}" deleted successfully!')
        return redirect('book_list')

    context = {'book': book}
    return render(request, 'bookshelf/book_confirm_delete.html', context)


@login_required
@permission_required('bookshelf.can_view', raise_exception=True)
def toggle_favorite(request, pk):
    """
    View to toggle a book as favorite/unfavorite.
    Requires 'can_view' permission.
    """
    book = get_object_or_404(Book, pk=pk)

    if request.method == 'POST':
        if book.favorited_by.filter(id=request.user.id).exists():
            book.favorited_by.remove(request.user)
            messages.success(request, f'"{book.title}" removed from favorites.')
        else:
            book.favorited_by.add(request.user)
            messages.success(request, f'"{book.title}" added to favorites.')

    return redirect('book_detail', pk=pk)


def permission_denied(request, exception=None):
    """
    Custom view for handling permission denied errors.
    """
    return render(request, 'bookshelf/permission_denied.html', status=403)
