from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

# not sure how this router works but found it on stackoverflow
router = DefaultRouter()
router.register(r'books_all', views.BookViewSet, basename='book_all')

urlpatterns = [
    path('books/', views.BookList.as_view(), name='book-list'),  # old way
    path('', include(router.urls)),  # new way???
]