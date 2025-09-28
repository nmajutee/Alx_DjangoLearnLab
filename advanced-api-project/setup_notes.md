# my advanced api project

so i made this django project with custom serializers. its pretty basic but it works i guess.

## what i have

### models
- Author: has name field
- Book: has title, publication_year, and author (foreignkey to Author)

### serializers
- BookSerializer: serializes books, has validation so publication year cant be in future
- AuthorSerializer: serializes author with nested books using related_name

## how i set it up

1. made new django project: `django-admin startproject advanced_api_project .`
2. created api app: `python manage.py startapp api`
3. added rest_framework and api to INSTALLED_APPS
4. made Author and Book models with relationship
5. created custom serializers with validation
6. ran migrations
7. tested everything

## testing

you can test in django shell:
```python
from api.models import Author, Book
from api.serializers import AuthorSerializer, BookSerializer

# create author
author = Author.objects.create(name='Test Author')

# create book
book = Book.objects.create(title='Test Book', publication_year=2020, author=author)

# serialize author (includes nested books)
serializer = AuthorSerializer(author)
print(serializer.data)
```

## validation
BookSerializer validates that publication_year is not in future. if you try to create book with year like 2030, it gives error.

## relationship explanation
- Author has many Books (one-to-many)
- Book belongs to one Author (foreign key)
- used related_name='books' so AuthorSerializer can access author.books
- AuthorSerializer uses nested BookSerializer to show all books by that author

the nested serializer thing was confusing but i think i got it right. basically AuthorSerializer shows the author name plus all their books automatically.