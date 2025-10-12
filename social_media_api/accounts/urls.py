from django.urls import path
from .views import RegisterView, LoginView, FollowUserView, UnfollowUserView

# urls for auth and follow
urlpatterns = [
    path('register/', RegisterView.as_view()),  # register url
    path('login/', LoginView.as_view()),  # login url
    path('follow/<int:user_id>/', FollowUserView.as_view()),  # follow user
    path('unfollow/<int:user_id>/', UnfollowUserView.as_view()),  # unfollow user
]
