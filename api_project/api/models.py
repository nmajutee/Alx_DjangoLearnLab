from django.db import models

# just a simple book model
class Book(models.Model):
    title = models.CharField(max_length=200)  # book name
    author = models.CharField(max_length=100)  # who wrote it
