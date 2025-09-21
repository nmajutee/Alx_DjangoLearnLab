import django
import os

# Setup Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'LibraryProject.settings')
django.setup()

from relationship_app.models import Author, Book, Library, Librarian

def query_books_by_author(author_name):
    """
    Query all books by a specific author.
    """
    try:
        # Get the author object
        author = Author.objects.get(name=author_name)
        # Query all books by this author
        books = Book.objects.filter(author=author)

        print(f"Books by {author_name}:")
        for book in books:
            print(f"- {book.title}")

        return books
    except Author.DoesNotExist:
        print(f"Author '{author_name}' not found.")
        return None

def list_books_in_library(library_name):
    """
    List all books in a library.
    """
    try:
        # Get the library object
        library = Library.objects.get(name=library_name)
        # Get all books in this library
        books = library.books.all()

        print(f"Books in {library_name}:")
        for book in books:
            print(f"- {book.title} by {book.author.name}")

        return books
    except Library.DoesNotExist:
        print(f"Library '{library_name}' not found.")
        return None

def retrieve_librarian_for_library(library_name):
    """
    Retrieve the librarian for a library.
    """
    try:
        # Get the library object
        library = Library.objects.get(name=library_name)
        # Get the librarian for this library (OneToOne relationship)
        librarian = Librarian.objects.get(library=library)

        print(f"Librarian for {library_name}: {librarian.name}")

        return librarian
    except Library.DoesNotExist:
        print(f"Library '{library_name}' not found.")
        return None
    except Librarian.DoesNotExist:
        print(f"No librarian assigned to '{library_name}'.")
        return None

# Alternative query methods using Django ORM relationships

def query_books_by_author_alternative(author_name):
    """
    Alternative method: Query all books by a specific author using direct relationship.
    """
    try:
        author = Author.objects.get(name=author_name)
        # Using reverse foreign key relationship
        books = author.book_set.all()

        print(f"Books by {author_name} (alternative method):")
        for book in books:
            print(f"- {book.title}")

        return books
    except Author.DoesNotExist:
        print(f"Author '{author_name}' not found.")
        return None

def retrieve_librarian_for_library_alternative(library_name):
    """
    Alternative method: Retrieve librarian using reverse OneToOne relationship.
    """
    try:
        library = Library.objects.get(name=library_name)
        # Using reverse OneToOne relationship
        librarian = library.librarian

        print(f"Librarian for {library_name} (alternative method): {librarian.name}")

        return librarian
    except Library.DoesNotExist:
        print(f"Library '{library_name}' not found.")
        return None
    except Librarian.DoesNotExist:
        print(f"No librarian assigned to '{library_name}'.")
        return None

if __name__ == "__main__":
    # Example usage - you can uncomment these lines to test the functions

    # Test the queries (make sure you have some data in your database first)
    print("=== Query Samples Demo ===\n")

    # Query 1: All books by a specific author
    print("1. Query all books by a specific author:")
    # query_books_by_author("J.K. Rowling")
    # query_books_by_author_alternative("J.K. Rowling")
    print("Uncomment the lines above and replace with actual author names from your database.\n")

    # Query 2: List all books in a library
    print("2. List all books in a library:")
    # list_books_in_library("Central Library")
    print("Uncomment the line above and replace with actual library name from your database.\n")

    # Query 3: Retrieve the librarian for a library
    print("3. Retrieve the librarian for a library:")
    # retrieve_librarian_for_library("Central Library")
    # retrieve_librarian_for_library_alternative("Central Library")
    print("Uncomment the lines above and replace with actual library name from your database.\n")

    print("Note: To use these functions, first create some sample data in your Django admin or shell.")
