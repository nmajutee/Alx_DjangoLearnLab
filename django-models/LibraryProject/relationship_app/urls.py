from django.urls import path
from . import views
from .views import list_books, LibraryDetailView


urlpatterns = [
    path('list_books/', views.list_books, name='list_books'), 
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),
    ] 