from django.contrib import admin

# Register your models here.
from posts.models import Post

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    """Profile admin."""

    list_display = ('id', 'user', 'title', 'photo')
    search_fields = ('title', 'user_username', 'user_email')
    list_filter = ('created', 'modified')
