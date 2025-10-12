from django.db import models
from django.contrib.auth.models import AbstractUser

# my custom user
class CustomUser(AbstractUser):
    bio = models.TextField(blank=True)  # user bio
    profile_picture = models.ImageField(upload_to='profile_pics/', blank=True, null=True)  # profle pic
    followers = models.ManyToManyField('self', symmetrical=False, related_name='following', blank=True)  # followers list
