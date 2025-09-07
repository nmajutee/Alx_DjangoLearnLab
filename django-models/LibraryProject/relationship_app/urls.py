from django.urls import path
from . import views

urlpatterns = [
    path('list_books/', views.list_all_books, name='list_books'),
    path('book/<int:pk>/', views.BookDetailView.as_view(), name='book_detail'),
]
