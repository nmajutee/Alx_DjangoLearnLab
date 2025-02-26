from django.db import models

# Create Book model
class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    publication_date = models.IntegerField()
    
    def __str__(self):
        return f"{self.title} by {self.author} on {self.publication_date}"