from rest_framework import serializers
from .models import Book, BookOrder


class BookSerializer(serializers.ModelSerializer):

    class Meta:
        model = Book
        fields = ('id', 'name', )

class BookDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = Book
        fields = ('id', 'name', 'author', 'mrp', )

class BookOrderSerializer(serializers.ModelSerializer):

    class Meta:
        model = BookOrder
        fields = ('id', 'books', 'customer', )
