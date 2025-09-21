from rest_framework import serializers
from .models import Book

# this is for making books into json or something like that
class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'