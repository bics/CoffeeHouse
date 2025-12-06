from django.db import models

# Create your models here.
class CoffeeTable(models.Model):
    name = models.CharField(max_length=255)
    image = models.CharField() # TODO add enum for available images or from html select
    description = models.CharField(max_length=255)
    # TODO implement other fields
    # createdBy
    # participants
    # threads
    # time

    def __str__(self):
        return self.name



