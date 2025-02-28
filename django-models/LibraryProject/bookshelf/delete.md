## Delete Book - "1984"

### Python Command:

```python
from bookshelf.models import Book
# Retrieve the book with title "1984"
book = Book.objects.get(title="1984")

# Delete the book from the database
book.delete()

# Try to retrieve all books to confirm deletion
books = Book.objects.all()

# Print the list of books, it should be empty if the deletion was successful
print(books)
