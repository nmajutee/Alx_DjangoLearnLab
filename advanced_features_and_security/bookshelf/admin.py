from django.contrib import admin
from .models import Book


class BookAdmin(admin.ModelAdmin):
    list_display = ("title", "author", "publication_year", "owner", "created_at")
    list_filter = ("author", "publication_year", "owner", "created_at")
    search_fields = ("title", "author")
    filter_horizontal = ("favorited_by",)  # Makes the many-to-many field easier to manage
    readonly_fields = ("created_at", "updated_at")

    fieldsets = (
        ('Book Information', {
            'fields': ('title', 'author', 'publication_year')
        }),
        ('Ownership & Favorites', {
            'fields': ('owner', 'favorited_by')
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )


admin.site.register(Book, BookAdmin)