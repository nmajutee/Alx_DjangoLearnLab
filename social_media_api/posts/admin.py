from django.contrib import admin
from .models import Post, Comment, Like

# register models so we can see them in admin panel
admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Like)
