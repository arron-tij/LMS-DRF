from rest_framework import generics,authentication,permissions,status
from rest_framework.response import Response
from .models import *
from .serializers import BookSerializer, BookDetailSerializer, BookOrderSerializer, OrderBookSerializer
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






