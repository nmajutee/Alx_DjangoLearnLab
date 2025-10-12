from rest_framework import viewsets, permissions, filters, generics
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from .models import Post, Comment
from .serializers import PostSerializer, CommentSerializer

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
        serializer.save(author=self.request.user)

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
