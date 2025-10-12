from django.urls import path
from .views import NotificationListView, MarkNotificationReadView

# urls for notifications
urlpatterns = [
    path('', NotificationListView.as_view(), name='notifications'),  # list notifications
    path('<int:pk>/read/', MarkNotificationReadView.as_view(), name='mark-read'),  # mark as read
]
