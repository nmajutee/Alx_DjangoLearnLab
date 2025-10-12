from rest_framework import status, permissions, generics
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.views import APIView
from django.contrib.auth import authenticate
from .serializers import RegisterSerializer, UserSerializer
from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404
from .models import CustomUser
from notifications.models import Notification

User = get_user_model()

# view for registering
class RegisterView(APIView):
    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            token = Token.objects.get(user=user)  # get token
            return Response({
                'token': token.key,
                'user_id': user.id,
                'username': user.username
            })
        return Response(serializer.errors, status=400)

# view for login
class LoginView(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')

        user = authenticate(username=username, password=password)

        if user:
            token, created = Token.objects.get_or_create(user=user)
            return Response({
                'token': token.key,
                'user_id': user.id,
                'username': user.username
            })
        else:
            return Response({'error': 'wrong credentials'}, status=400)

# view to follow a user
class FollowUserView(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, user_id):
        # get the user to follow
        user_to_follow = get_object_or_404(User, id=user_id)

        # cant follow yourself
        if user_to_follow == request.user:
            return Response({'error': 'you cant follow yourself'}, status=400)

        # add to following list
        request.user.following.add(user_to_follow)

        # create notification
        Notification.objects.create(
            recipient=user_to_follow,
            actor=request.user,
            verb='started following you',
            target=user_to_follow
        )

        return Response({'message': f'you are now following {user_to_follow.username}'})

# view to unfollow a user
class UnfollowUserView(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, user_id):
        # get the user to unfollow
        user_to_unfollow = get_object_or_404(User, id=user_id)

        # remove from following list
        request.user.following.remove(user_to_unfollow)
        return Response({'message': f'you unfollowed {user_to_unfollow.username}'})

# view to list all users
class UserListView(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        # get all users using CustomUser.objects.all()
        all_users = CustomUser.objects.all()
        serializer = UserSerializer(all_users, many=True)
        return Response(serializer.data)
