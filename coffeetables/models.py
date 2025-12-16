from django.db import models

# Snippet taken from ChatGPT
from django.contrib.auth import get_user_model
User = get_user_model()

# Create your models here.
    
class Reply(models.Model):
    message = models.TextField(max_length=255)
    createdBy = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    time = models.DateTimeField(editable=False, auto_now_add=True)
    edited = models.BooleanField(default=False)
    history = models.TextField(blank=True)
    timeEdited = models.DateTimeField(editable=False, blank=True, null=True)
    
    def __str__(self):
        # Snippet taken from ChatGPT
        name = self.createdBy.username if self.createdBy else "Deleted User"
        return self.message + ' ' + name + ' ' + self.time.isoformat()
    
    @property
    def creator_name(self):
        name = self.createdBy.username if self.createdBy else "Deleted User"
        return name.__str__()
    

# model inspired by tutorial made by Codemy.com
class CoffeeTable(models.Model):
    name = models.CharField(max_length=255)
    image = models.CharField(blank=True) # TODO add enum for available images or from html select
    description = models.CharField(max_length=255)
    replies = models.ManyToManyField(Reply, blank=True)
    createdBy = models.ForeignKey(User, null=True, on_delete=models.SET_NULL, related_name="table_creator")
    participants = models.ManyToManyField(User, blank=True, related_name="table_participant")
    time = models.DateTimeField(editable=False, auto_now_add=True)
    active = models.BooleanField(default=True)

    def __str__(self):        
        name = self.createdBy.username if self.createdBy else "Deleted User"
        return self.name + ' by ' + name  + ' at ' + self.time.isoformat()
    
    @property
    def creator_name(self):
        name = self.createdBy.username if self.createdBy else "Deleted User"
        return name.__str__()




