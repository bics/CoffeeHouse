from django.shortcuts import render, HttpResponse
from .models import CoffeeTable

# Create your views here.

# view created following tutorial made by Codemy.com
def tables(request):
    tables_list = CoffeeTable.objects.all()
    images_list = None
    return render(request, "tables.html", {'tables_list':tables_list, 'images_list': images_list})
