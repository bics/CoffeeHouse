from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class CoffeeDrinker(AbstractUser):
    avatar = models.TextField()
