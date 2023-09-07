from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser

# Create your models here.


class User(AbstractBaseUser):
    user_id = models.TextField(max_length=24)
    email = models.EmailField(unique=True, default="example@abc.com")
    USERNAME_FIELD = "email"

    class Meta:
        db_table = "User"
