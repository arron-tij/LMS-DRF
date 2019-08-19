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


class OrderBookSerializer(serializers.Serializer):
    book = serializers.PrimaryKeyRelatedField(queryset=Book.objects.all())


    def save(self):
        book = self.validated_data['book']
        user=self.context['request'].user
        order, created = BookOrder.objects.get_or_create(customer=user)
        if order.books.filter(id=book.id):
            raise serializers.ValidationError("Book already loaned")
        order.books.add(book)
        return order 

class ReturnBookSerializer(serializers.Serializer):
    book = serializers.PrimaryKeyRelatedField(queryset=Book.objects.all())


    def remove(self):
        book = self.validated_data['book']
        user=self.context['request'].user
        order, created = BookOrder.objects.get_or_create(customer=user)
        if not order.books.filter(id=book.id):
            raise serializers.ValidationError("Book not loaned")
        order.books.remove(book)
        return order 