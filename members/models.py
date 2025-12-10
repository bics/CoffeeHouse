from django.db import models
from django.contrib.auth.models import AbstractUser
import random

def getRandomAvatar():
    default_images = [
        'static/assets/images/avatar_images/avatar_default_female_red.png',
        'static/assets/images/avatar_images/avatar_default_female_yellow.png',
        'static/assets/images/avatar_images/avatar_default_male_red.png',
        'static/assets/images/avatar_images/avatar_default_male_blue.png',
        'static/assets/images/avatar_images/avatar_default_male_yellow.png',
    ]

    return default_images[random.randint(0,4)]

# Create your models here.
class CoffeeDrinker(AbstractUser):
    avatar = models.ImageField(null=True, blank=True, default=getRandomAvatar)




