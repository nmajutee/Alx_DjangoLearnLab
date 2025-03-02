from relationship_app.models import Author, Book, Library, Librarian

def query_books_by_author(author_name):
    try:
        # Retrieve the author instance using the given name.
        author = Author.objects.get(name=author_name)
        # Use the retrieved author to filter books.
        book = Book.objects.filter(author=author)
        return book
    except Author.DoesNotExist:
        print(f"Author '{author_name}' does not exist.")
        return None


def list_all_books_in_library(library_name):
    try:
        # Retrieve the library instance using its name.
        library = Library.objects.get(name=library_name)
         # Access the related books (assuming the related_name is 'books').
        books = library.books.all()
    
        return books
    except Library.DoesNotExist:
        print(f"Library '{library_name}' does not exist.")
        return None
    
def retrieve_librarian_for_library(library_name):
    try:
        librarian = librarian.objects.get(library=library_name)
        return librarian
    except Library.DoesNotExist:
        print(f"Library '{library_name}' does not exist.")
        return None
    except Librarian.DoesNotExist:
        print(f"No librarian assigned for library '{library_name}'.")
        return None