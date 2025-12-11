from django.db import models

# Snippet taken from ChatGPT
from django.contrib.auth import get_user_model
User = get_user_model()

# Create your models here.
    
class Reply(models.Model):
    message = models.TextField(max_length=255)
    createdBy = models.ForeignKey(User, blank=True, on_delete=models.RESTRICT)
    time = models.DateTimeField(editable=False, auto_now_add=True)
    
    def __str__(self):
        return self.message + ' ' + self.createdBy.__str__() + ' ' + self.time.isoformat()
    

# model inspired by tutorial made by Codemy.com
class CoffeeTable(models.Model):
    name = models.CharField(max_length=255)
    image = models.CharField(blank=True) # TODO add enum for available images or from html select
    description = models.CharField(max_length=255)
    replies = models.ManyToManyField(Reply, blank=True)
    createdBy = models.ForeignKey(User, on_delete=models.RESTRICT, related_name="table_creator")
    participants = models.ManyToManyField(User, blank=True, related_name="table_participant")
    time = models.DateTimeField(editable=False, auto_now_add=True)
    active = models.BooleanField(default=True)
    def __str__(self):
        return self.name + ' by ' + self.createdBy.username  + ' at ' + self.time.isoformat()




