from relationship_app.models import Author, Book, Library, Librarian

def query_books_by_author(author_name):
    try:
        author = Author.objects.get(name = author_name)
        books = Book.objects.filter(author = author)
        return books
    except Author.DoesNotExist:
        return f" Author {author_name} not found."

def list_all_books_in_library(library_name):
    try:
        library = Library.objects.get(name = library_name)
        books = Book.objects.all()
        return books
    except Library.DoesNotExist:
        return f"Library {library} not found."

def retrieve_librarian_for_library(library_name):
    try:
        library = Library.objects.get(name = library_name)
        librarian = library.librarian
        return librarian
    except Library.DoesNotExist:
        return f"Library {library_name} not found."
    except Librarian.DoesNotExist:
        return f"Library {library_name} not found."