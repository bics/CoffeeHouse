from django.contrib import admin

# Imports and CoffeeDrinkerAdmin register generated using ChatGPT
from django.contrib.auth.admin import UserAdmin
from .models import CoffeeDrinker

# Register your models here.
@admin.register(CoffeeDrinker)
class CoffeeDrinkerAdmin(UserAdmin):
    pass
