from django.shortcuts import render, HttpResponse
from django.shortcuts import redirect

# Create your views here.
def home(request):
    return render(request, "index.html")
