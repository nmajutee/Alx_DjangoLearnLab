from rest_framework import generics, permissions
from rest_framework.response import Response
from .models import Notification
from .serializers import NotificationSerializer

# view to list user notifications
class NotificationListView(generics.ListAPIView):
    serializer_class = NotificationSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        # get notifications for current user
        return Notification.objects.filter(recipient=self.request.user)

# view to mark notification as read
class MarkNotificationReadView(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, pk):
        try:
            notification = Notification.objects.get(pk=pk, recipient=request.user)
            notification.read = True
            notification.save()
            return Response({'message': 'notification marked as read'})
        except Notification.DoesNotExist:
            return Response({'error': 'notification not found'}, status=404)
