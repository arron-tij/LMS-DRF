from rest_framework import generics
from rest_framework.response import Response
from .models import *
from .serializers import BookSerializer, BookDetailSerializer, BookOrderSerializer
from django.http import HttpResponse
class BookList(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class OrderBook(generics.GenericAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    def get(self,request,pk):
        serializer = self.queryset.get(pk=pk)
        try:
            instnc=BookOrder.objects.get(customer=request.user.id)
            BookOrder.objects.get(id=instnc.id).books.add(serializer)
        except:
            BookOrder.objects.create(customer=request.user)
            instnc=BookOrder.objects.get(customer=request.user.id)
            BookOrder.objects.get(id=instnc.id).books.add(serializer)
        return Response()

class ReturnBook(generics.GenericAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    def get(self,request,pk):
        serializer = self.queryset.get(pk=pk)
        try:
            instnc=BookOrder.objects.get(customer=request.user.id)
            BookOrder.objects.get(id=instnc.id).books.remove(serializer)
        except:
            pass
        return Response()

class BookDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookDetailSerializer

class BookOrderList(generics.GenericAPIView):
    
    def get(self,request):
        return Response(BookOrder.objects.get(customer=request.user.id).books.values())






