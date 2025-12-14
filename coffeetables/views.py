from django.shortcuts import render, redirect
from .models import CoffeeTable
from .forms import CoffeeTableForm, ReplyForm
from django.contrib import messages
# Snippet taken from ChatGPT
from django.contrib.auth.decorators import login_required

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
        form = CoffeeTableForm()
        return render(request, "tables.html", {'tables_list':tables_list, 'images_list': images_list, 'form': form})
    
@login_required
def conversation(request, pk):
    # Code snippet generated using ChatGPT
    table = CoffeeTable.objects.get(pk=pk)
    replies = table.replies.all()

    if request.method == "POST":
        form = ReplyForm(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.createdBy= request.user
            obj.save()
            table.replies.add(obj)
            return redirect('conversation', table.id) 
        else:            
            messages.success(request, ("There were some errors with some fields"))
    else:
        form = ReplyForm()
        return render(request, "conversation.html", {"table": table, "replies": replies, "form": form} )
    
def close_table(request, pk):    
    table = CoffeeTable.objects.get(pk=pk)
    table.active = False
    table.save()
    return redirect('tables')

