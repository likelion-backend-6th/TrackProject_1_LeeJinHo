from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser

# Create your models here.


class User(AbstractBaseUser):
    name = models.CharField(max_length=30, blank=True, null=True)
    user_id = models.TextField(max_length=24)
    email = models.EmailField(unique=True, default="example@abc.com")

    USERNAME_FIELD = "email"

    def __str__(self):
        return self.user_id

    class Meta:
        db_table = "User"


class Follow(models.Model):
    follower = models.EmailField(verbose_name="email", max_length=100)
    following = models.EmailField(verbose_name="email", max_length=100)
    is_live = models.BooleanField(default=False)

    class Meta:
        db_table = "follow"
        constraints = [
            models.UniqueConstraint(
                fields=["follower", "following"], name="follower-following"
            )
        ]
        indexes = [
            models.Index(fields=["follower"]),
            models.Index(fields=["following"]),
        ]
