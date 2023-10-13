from django.db import models
from django.contrib.auth.models import User

class Photo(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    image = models.CharField(max_length=500)
    upload_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=[('moderation', 'На модерации'), ('approved', 'Одобрена'), ('deleted', 'На удалении')])
    author = models.ForeignKey(User, on_delete=models.CASCADE)