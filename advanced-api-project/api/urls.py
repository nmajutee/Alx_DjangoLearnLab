from django.urls import path
from . import views

# url patterns for book api
urlpatterns = [
    path('books/', views.BookListView.as_view(), name='book-list'),  # get all books
    path('books/<int:pk>/', views.BookDetailView.as_view(), name='book-detail'),  # get one book
    path('books/create/', views.BookCreateView.as_view(), name='book-create'),  # create new book
    path('books/<int:pk>/update/', views.BookUpdateView.as_view(), name='book-update'),  # update book
    path('books/<int:pk>/delete/', views.BookDeleteView.as_view(), name='book-delete'),  # delete book
]