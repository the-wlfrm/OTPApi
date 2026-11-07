from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    # objects: models.Manager = models.Manager()

    username = models.CharField(max_length=30, unique=True)
    email = models.EmailField(unique=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.username}:{self.email}"