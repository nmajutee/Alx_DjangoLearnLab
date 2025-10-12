from rest_framework import serializers
from .models import Post, Comment
from django.contrib.auth import get_user_model

User = get_user_model()

# serializer for posts
class PostSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')
    author_id = serializers.ReadOnlyField(source='author.id')

    class Meta:
        model = Post
        fields = ['id', 'author', 'author_id', 'title', 'content', 'created_at', 'updated_at']
        read_only_fields = ['created_at', 'updated_at']

# serializer for comments
class CommentSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')
    author_id = serializers.ReadOnlyField(source='author.id')
    post_title = serializers.ReadOnlyField(source='post.title')

    class Meta:
        model = Comment
        fields = ['id', 'post', 'post_title', 'author', 'author_id', 'content', 'created_at', 'updated_at']
        read_only_fields = ['created_at', 'updated_at']
