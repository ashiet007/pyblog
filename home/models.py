from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=1000)
    content = models.TextField(max_length=1000)
    slug = models.SlugField(max_length=2000)
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, blank=False, null=False)
    image = models.ImageField(upload_to='blog')
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
