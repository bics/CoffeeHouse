from django.shortcuts import render, HttpResponse
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
def home(request):
    return render(request, "index.html")

def register(request):
    form = UserCreationForm()
    return render(request, "register.html", { "form": form})

