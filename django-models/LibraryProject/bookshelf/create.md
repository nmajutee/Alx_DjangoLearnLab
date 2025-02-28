# Creating a Book Instance in Django

## Command to Create a Book Instance:
```python
from bookshelf.models import Book  # Import the Book model

# Create and save a new Book instance
book = Book.objects.create(title="1984", author="George Orwell", publication_date=1949)
book.save()  # Saves the instance to the database

# Expected output
1984 by George Orwell on 1949
