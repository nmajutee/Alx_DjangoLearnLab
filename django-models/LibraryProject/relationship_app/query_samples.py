from relationship_app.models import Author, Book, Library, Librarian

def query_books_by_author(author_name):
    try:
        author_name = Author.objects.get(name=author_name)
        book = Book.objects.filter(author=author_name)
        return book
    except Author.DoesNotExist:
        print(f"Author '{author_name}' does not exist.")
        return None


def list_all_books_in_library(library_name):
    try:
        library = Library.objects.get(name=library_name)
        books = library.books.all()
        return books
    except Library.DoesNotExist:
        print(f"Library '{library_name}' does not exist.")
        return None
    
def retrieve_librarian_for_library(name_value):
    try:
        library = Library.objects.get(name=name_value)
        librarian = library.librarian
        return librarian
    except Library.DoesNotExist:
        print(f"Library '{name_value}' does not exist.")
        return None
    except Librarian.DoesNotExist:
        print(f"No librarian assigned for library '{name_value}'.")
        return None