from django.contrib import admin
from .models import CoffeeTable, Reply

# Register your models here.
# register inspired by tutorial made by Codemy.com
admin.site.register(CoffeeTable)
admin.site.register(Reply)
