from django.urls import path
from .views import RegisterView, LoginView

# urls for auth
urlpatterns = [
    path('register/', RegisterView.as_view()),  # register url
    path('login/', LoginView.as_view()),  # login url
]
