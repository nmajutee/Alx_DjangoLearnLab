## Update Book Title - "1984" to "Nineteen Eighty-Four"

### Python Command:

```python
# Retrieve the book with title "1984"
book = Book.objects.get(title="1984")

# Update the title to "Nineteen Eighty-Four"
book.title = "Nineteen Eighty-Four"

# Save the changes to the database
book.save()

# Print the updated title to confirm the change
print(book.title)

# Expected output
Nineteen Eighty-Four
