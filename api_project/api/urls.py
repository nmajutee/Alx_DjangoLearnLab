from django.urls import path
from . import views

# these are the urls for my api app
urlpatterns = [
    path('books/', views.BookList.as_view(), name='book-list'),  # this will show all books
]