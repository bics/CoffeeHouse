from django.shortcuts import render, redirect
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
            # Code snippet generated using ChatGPT
            obj = form.save(commit=False)
            obj.createdBy= request.user
            obj.save()
            form.save_m2m()
            return redirect('tables')    
        else:            
            messages.success(request, ("There were some errors with some fields"))
    else:
        form = CoffeeTableForm
        return render(request, "tables.html", {'tables_list':tables_list, 'images_list': images_list, 'form': form})
    
def conversation(request):
    return render(request, "conversation.html")
