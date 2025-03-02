from relationship_app.models import Author, Book, Library, Librarian

def query_books_by_author(name_value):
    try:
        author = Author.objects.get(name = name_value)
        book = Book.objects.filter(author = author)
        return book
    except Author.DoesNotExist:
        print(f"Author '{name_value}' does not exist.")
        return None


def list_all_books_in_library(library_name):
    try:
        library = Library.objects.get(name = library_name)
        books = library.objects.all()
        return books
    except Library.DoesNotExist:
        print(f"Library '{library_name}' does not exist.")
        return None
    
def retrieve_librarian_for_library(name_value):
    try:
        library = Library.objects.get(name = name_value)
        librarian = library.librarian
        return librarian
    except Library.DoesNotExist:
        print(f"Library '{name_value}' does not exist.")
        return None
    except Librarian.DoesNotExist:
        print(f"No librarian assigned for library '{name_value}'.")
        return None