from django.urls import path
from . import views

urlpatterns = [
    path('relationship_app/list_books.html', views.list_book_view, name='list books'),
]