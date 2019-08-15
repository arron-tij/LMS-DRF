from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from store import views

urlpatterns = [
    path('store/', views.BookList.as_view()),
    path('store/<int:pk>/', views.BookDetail.as_view()),
    path('orders/', views.BookOrderList.as_view()),
    path('order/<int:pk>/', views.OrderBook.as_view()),
    path('return/<int:pk>/', views.ReturnBook.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)