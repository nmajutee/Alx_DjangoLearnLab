# Retrieving a Book Instance

## Command:
```python
from bookshelf.models import Book  # Import the Book model

book = Book.objects.get(title="1984")  # Retrieve the book

# Display all attributes
print(f"Title: {book.title}")
print(f"Author: {book.author}")
print(f"Publication Year: {book.publication_date}")

# Expected output
Title: 1984
Author: George Orwell
Publication Year: 1949