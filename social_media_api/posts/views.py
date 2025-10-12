from rest_framework import viewsets, permissions, filters, generics, status
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework.decorators import action
from django.shortcuts import get_object_or_404
from .models import Post, Comment, Like
from .serializers import PostSerializer, CommentSerializer, LikeSerializer
from notifications.models import Notification
from django.contrib.contenttypes.models import ContentType

# simple permission to check if user owns the object
class IsAuthorOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        # read permissions for everyone
        if request.method in permissions.SAFE_METHODS:
            return True
        # write permissions only for author
        return obj.author == request.user

# pagination class for posts
class PostPagination(PageNumberPagination):
    page_size = 10  # 10 posts per page

# viewset for posts with CRUD operations
class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsAuthorOrReadOnly]
    pagination_class = PostPagination
    filter_backends = [filters.SearchFilter]
    search_fields = ['title', 'content']  # can search by title or content

    def perform_create(self, serializer):
        # set the author to current user when creating post
        serializer.save(author=self.request.user)

# viewset for comments with CRUD operations
class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsAuthorOrReadOnly]

    def perform_create(self, serializer):
        # set the author to current user when creating comment
        comment = serializer.save(author=self.request.user)
        
        # create notification if commenting on someone else's post
        if comment.post.author != self.request.user:
            Notification.objects.create(
                recipient=comment.post.author,
                actor=self.request.user,
                verb='commented on your post',
                target=comment
            )

# view for user feed - shows posts from users they follow
class FeedView(generics.ListAPIView):
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated]
    pagination_class = PostPagination

    def get_queryset(self):
        # get users that current user is following
        following_users = self.request.user.following.all()
        # get posts from those users, ordered by newest first
        return Post.objects.filter(author__in=following_users).order_by('-created_at')

# view to like a post
class LikePostView(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]
    
    def post(self, request, pk):
        # get the post
        post = generics.get_object_or_404(Post, pk=pk)
        
        # check if already liked
        like, created = Like.objects.get_or_create(user=request.user, post=post)
        
        if not created:
            return Response({'message': 'you already liked this post'}, status=400)
        
        # create notification for post author
        if post.author != request.user:  # dont notify yourself
            Notification.objects.create(
                recipient=post.author,
                actor=request.user,
                verb='liked your post',
                target=post
            )
        
        return Response({'message': 'post liked!'})

# view to unlike a post
class UnlikePostView(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]
    
    def post(self, request, pk):
        # get the post
        post = generics.get_object_or_404(Post, pk=pk)
        
        # try to find and delete the like
        try:
            like = Like.objects.get(user=request.user, post=post)
            like.delete()
            return Response({'message': 'post unliked!'})
        except Like.DoesNotExist:
            return Response({'error': 'you havent liked this post'}, status=400)
