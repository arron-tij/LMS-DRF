from rest_framework import generics,authentication,permissions,status
from rest_framework.response import Response
from .models import *
from .serializers import BookSerializer, BookDetailSerializer, OrderBookSerializer, ReturnBookSerializer
from django.http import HttpResponse
class BookList(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class OrderBook(generics.GenericAPIView):
    permission_classes=[permissions.IsAuthenticated]
    queryset = Book.objects.all()
    serializer_class = OrderBookSerializer

    def post(self, request, *args, **kwargs):
        self.request = request
        self.serializer = self.get_serializer(data = request.data)
        self.serializer.is_valid(raise_exception=True)
        order = self.serializer.save()
        return Response(status = status.HTTP_200_OK)

class ReturnBook(generics.GenericAPIView):
    queryset = Book.objects.all()
    serializer_class = ReturnBookSerializer

    def post(self, request, *args, **kwargs):
        self.request = request
        self.serializer = self.get_serializer(data = request.data)
        self.serializer.is_valid(raise_exception=True)
        order = self.serializer.remove()
        return Response(status = status.HTTP_200_OK)

class BookDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookDetailSerializer

class BookOrderList(generics.GenericAPIView):
    
    def get(self,request):
        return Response(BookOrder.objects.get(customer=request.user.id).books.values())






