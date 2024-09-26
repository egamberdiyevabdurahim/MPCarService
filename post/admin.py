from django.contrib import admin

from post.models import CommentsModel


@admin.register(CommentsModel)
class CommentsAdmin(admin.ModelAdmin):
    list_display = ('description', 'created_at', 'is_pinned')
    list_display_links = list_display
    list_filter = ('is_pinned', 'created_at')
    search_fields = ('author__first_name', 'author__last_name', 'description')
    ordering = ('-created_at',)
