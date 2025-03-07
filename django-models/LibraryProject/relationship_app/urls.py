from django.urls import path
from . import views
from .views import LibraryListView

urlpatterns = [
    path('relationship_app/list_books.html', views.list_book_view, name='list books'),
    path('relationship_app/library_detail.html', LibraryListView.as_view(), name='list_books'),
]