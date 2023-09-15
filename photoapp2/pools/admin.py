from django.contrib import admin
from .models import Comment, Like, Photo

# Зарегистрируйте модели в административной панели

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('user', 'photo', 'text', 'timestamp', 'parent_comment')
    list_filter = ('timestamp', 'user', 'photo')
    search_fields = ('text', 'user__username', 'photo__title')
    list_per_page = 25

@admin.register(Like)
class LikeAdmin(admin.ModelAdmin):
    list_display = ('user', 'photo', 'created_at')
    list_filter = ('created_at', 'user', 'photo')
    search_fields = ('user__username', 'photo__title')
    list_per_page = 25

@admin.register(Photo)
class PhotoAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'image', 'upload_date', 'status', 'author')
    list_filter = ('upload_date', 'status', 'author')
    search_fields = ('title', 'description', 'author__username')
    list_per_page = 25