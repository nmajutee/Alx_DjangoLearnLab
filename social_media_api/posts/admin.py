from django.contrib import admin
from .models import Post, Comment

# register models so we can see them in admin panel
admin.site.register(Post)
admin.site.register(Comment)
