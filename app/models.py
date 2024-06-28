from django.db import models
class Todo(models.Model):
    title = models.CharField(max_length=100)
    descriptions = models.TextField()
    completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
