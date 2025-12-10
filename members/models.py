from django.db import models
from django.contrib.auth.models import AbstractUser
import random

def getRandomAvatar():
    default_images = [
        'avatar_images/avatar_default_female_red.png',
        'avatar_images/avatar_default_female_yellow.png',
        'avatar_images/avatar_default_male_red.png',
        'avatar_images/avatar_default_male_blue.png',
        'avatar_images/avatar_default_male_yellow.png',
    ]
    return default_images[random.randint(0,4)]

# Create your models here.
class CoffeeDrinker(AbstractUser):
    avatar = models.ImageField(null=True, blank=True, default=getRandomAvatar, upload_to="avatar_images/")




