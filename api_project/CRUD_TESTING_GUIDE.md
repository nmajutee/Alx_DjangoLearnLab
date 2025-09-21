# my first crud api thing

idk what CRUD stands for but it does stuff with books lol

## what i made

so i made these things:
1. BookList - shows books (the easy one)
2. BookViewSet - does everything??? (copied from internet)

## urls that work

### the old one:
- GET /api/books/ - shows books

### new ones (router made these somehow):
- GET /api/books_all/ - list books
- POST /api/books_all/ - make new book
- GET /api/books_all/1/ - get book number 1
- PUT /api/books_all/1/ - change book number 1
- DELETE /api/books_all/1/ - delete book number 1

## testing (copy paste these)

### see all books:
```
curl http://127.0.0.1:8000/api/books_all/
```

### get one book:
```
curl http://127.0.0.1:8000/api/books_all/1/
```

### make new book:
```
curl -X POST http://127.0.0.1:8000/api/books_all/ -H "Content-Type: application/json" -d '{"title": "my book", "author": "me"}'
```

### change book:
```
curl -X PUT http://127.0.0.1:8000/api/books_all/1/ -H "Content-Type: application/json" -d '{"title": "new title", "author": "new guy"}'
```

### delete book:
```
curl -X DELETE http://127.0.0.1:8000/api/books_all/1/
```

## my code

views.py:
```python
# idk what viewset does but it works lol
class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    # TODO: figure out what this does later
```

urls.py:
```python
# not sure how this router works but found it on stackoverflow
router = DefaultRouter()
router.register(r'books_all', views.BookViewSet, basename='book_all')
```

models.py:
```python
# just a simple book model
class Book(models.Model):
    title = models.CharField(max_length=200)  # book name
    author = models.CharField(max_length=100)  # who wrote it
```

i dont really understand how this works but it does stuff!