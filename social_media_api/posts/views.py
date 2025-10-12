from rest_framework import viewsets, permissions, filters
from rest_framework.pagination import PageNumberPagination
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
