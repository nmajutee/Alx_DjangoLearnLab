from django.urls import path
from . import views
from .views import list_books, LibraryDetailView


urlpatterns = [
    path('relationship_app/list_books.html', views.list_book_view, name='list_books'),
    
    path('relationship_app/library_detail.html', LibraryDetailView.as_view(template_name='library_detail.html'))
    ]