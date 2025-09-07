from django.urls import path
from . import views
from .views import list_books

urlpatterns = [
    path('list_books/', views.list_books, name='list_books'),
    path('book/<int:pk>/', views.BookDetailView.as_view(), name='book_detail'),
    path('library/<int:pk>/', views.LibraryDetailView.as_view(), name='library_detail'),
    
    # Authentication URLs
    path('login/', views.CustomLoginView.as_view(), name='login'),
    path('logout/', views.CustomLogoutView.as_view(), name='logout'),
    path('register/', views.register, name='register'),
]
