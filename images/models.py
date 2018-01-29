from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Image(models.Model):
    file = models.FileField(max_length=1000)
    location = models.CharField(max_length=50)
    caption = models.TextField()
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f'{self.location} - {self.caption}'

class Comment(models.Model):
    message = models.TextField()
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    created_for = models.ForeignKey(Image, on_delete=models.CASCADE, null=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f'{self.created_by.username}'

class Like(models.Model):
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    created_for = models.ForeignKey(Image, on_delete=models.CASCADE, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    