from rest_framework import serializers
from .models import Book

# I'm creating a serializer for the Book model
class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'  # this will include all fields from the Book model