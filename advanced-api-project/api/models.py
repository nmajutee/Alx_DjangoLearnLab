from django.db import models

# this is for authors who write books
class Author(models.Model):
    name = models.CharField(max_length=100)  # author name

    def __str__(self):
        return self.name

# this is for books
class Book(models.Model):
    title = models.CharField(max_length=200)  # book title
    publication_year = models.IntegerField()  # when it was published
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='books')  # which author wrote it, related_name for reverse lookup

    def __str__(self):
        return self.title
