from rest_framework import serializers
from .models import Notification

# serializer for notifications
class NotificationSerializer(serializers.ModelSerializer):
    actor = serializers.ReadOnlyField(source='actor.username')
    actor_id = serializers.ReadOnlyField(source='actor.id')
    
    class Meta:
        model = Notification
        fields = ['id', 'actor', 'actor_id', 'verb', 'target_content_type', 'target_object_id', 'timestamp', 'read']
        read_only_fields = ['timestamp']
