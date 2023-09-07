from django.db import models


# Create your models here.
class Post(models.Model):
    content = models.TextField(max_length=300)
    user_id = models.TextField(max_length=24)
    like_count = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
