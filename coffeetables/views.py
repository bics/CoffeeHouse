from django.shortcuts import render, HttpResponse
from .models import CoffeeTable

# Create your views here.

# view created following tutorial made by Codemy.com
def tables(request):
    tables_list = CoffeeTable.objects.all()
    images_list = [
        'static/assets/images/table_images/coffee_drank.jpg',
        'static/assets/images/table_images/coffee_mug_cartoony.jpg',
        'static/assets/images/table_images/coffee_mug_tilted.jpg',
    ]
    return render(request, "tables.html", {'tables_list':tables_list, 'images_list': images_list})
