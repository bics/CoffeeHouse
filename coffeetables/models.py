from django.db import models

# Snipper taken from ChatGPT
from django.contrib.auth import get_user_model
User = get_user_model()

# Create your models here.
# model inspired by tutorial made by Codemy.com
class CoffeeTable(models.Model):
    name = models.CharField(max_length=255)
    image = models.CharField() # TODO add enum for available images or from html select
    description = models.CharField(max_length=255)
    participants = models.ManyToManyField(User, blank=True)
    # TODO implement other fields
    # createdBy
    # threads
    # time

    def __str__(self):
        return self.name



