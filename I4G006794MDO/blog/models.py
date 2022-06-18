from django.db import models
from django.conf import settings

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
    author = models.ForeignKey(settings.AUTH_USER_MODEL, default=None, on_delete=models.SET_DEFAULT)
    created_date = models.DateTimeField(auto_now_add=True)
    Published_date = models.DateTimeField()