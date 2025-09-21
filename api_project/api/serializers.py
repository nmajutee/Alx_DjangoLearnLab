from rest_framework import serializers
from .models import Book

# converts book to json i think
class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'  # just give me everything