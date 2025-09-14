from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext_lazy as _
from .models import CustomUser


class CustomUserAdmin(UserAdmin):
    """
    Custom admin interface for CustomUser model.
    Extends the default UserAdmin to include the additional fields.
    """

    # Fields to display in the admin list view
    list_display = ('username', 'email', 'first_name', 'last_name', 'date_of_birth', 'is_staff')

    # Fields to filter by in the admin interface
    list_filter = UserAdmin.list_filter + ('date_of_birth',)

    # Fields to search by in the admin interface
    search_fields = ('username', 'first_name', 'last_name', 'email')

    # Organize fields into sections for the detail view
    fieldsets = UserAdmin.fieldsets + (
        (_('Additional Information'), {
            'fields': ('date_of_birth', 'profile_photo'),
        }),
    )

    # Fields to show when adding a new user
    add_fieldsets = UserAdmin.add_fieldsets + (
        (_('Additional Information'), {
            'fields': ('date_of_birth', 'profile_photo'),
        }),
    )

    # Make the form more readable
    readonly_fields = ('last_login', 'date_joined')


# Register the CustomUser with the CustomUserAdmin
admin.site.register(CustomUser, CustomUserAdmin)
