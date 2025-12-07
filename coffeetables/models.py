from django.db import models

# Snipper taken from ChatGPT
from django.contrib.auth import get_user_model
User = get_user_model()

# Create your models here.
    
class Reply(models.Model):
    message = models.TextField(max_length=255)
    createdBy = models.ForeignKey()
    time = models.DateTimeField(editable=False, auto_now=True, auto_now_add=True)
    
    def __str__(self):
        return self.message + ' ' + self.createdBy
    

# model inspired by tutorial made by Codemy.com
class CoffeeTable(models.Model):
    name = models.CharField(max_length=255)
    image = models.CharField() # TODO add enum for available images or from html select
    description = models.CharField(max_length=255)
    participants = models.ManyToManyField(User, blank=True)
    replies = models.ManyToManyField(Reply, blank=True)
    # TODO implement other fields
    # createdBy
    # time

    def __str__(self):
        return self.name




