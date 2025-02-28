from django.db import models

# Create Author model
class Author(models.Model):
    name = models.CharField(max_length = 100)
    
    def __str__(self):
        return self.name

# Create Book model
class Book(models.Model):
    title = models.CharField(max_length = 250)
    author = models.ForeignKey(Author, on_delete= models.CASCADE)
    
    def __str__(self):
        return self.title

# Create Library model
class Library(models.Model):
    name = models.CharField(max_length = 100)
    books = models.ManyToManyField(Book, related_name= 'books')
    
    def __str__(self):
        return self.name
    
# Create Librarian model
class Librarian(models.Model):    
    name = models.CharField(max_length = 100)
    library = models.OneToOneField(Library, on_delete= models.CASCADE)
    
    def __str__(self):
        return self.name
