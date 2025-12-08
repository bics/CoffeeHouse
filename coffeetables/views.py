from django.shortcuts import render, HttpResponse
from .models import CoffeeTable
from .forms import CoffeeTableForm
from django.contrib import messages

# Create your views here.

# view created following tutorial made by Codemy.com
def tables(request):
    tables_list = CoffeeTable.objects.all()
    images_list = [
        'static/assets/images/table_images/coffee_drank.jpg',
        'static/assets/images/table_images/coffee_mug_cartoony.jpg',
        'static/assets/images/table_images/coffee_mug_tilted.jpg',
    ]
    if request.method == "POST":
        form = CoffeeTableForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, "tables.html", {'tables_list':tables_list, 'images_list': images_list, 'form': form})    
        else:            
            messages.success(request, ("There were some errors with some fields"))
    else:
        form = CoffeeTableForm
        return render(request, "tables.html", {'tables_list':tables_list, 'images_list': images_list, 'form': form})
