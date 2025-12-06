from django.shortcuts import render, HttpResponse
from django.shortcuts import redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

# Create your views here.
# view created following tutorial made by Codemy.com
def home(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.success(request, ("Error while logging in"))
            return redirect('home')
    else:
        return render(request, "index.html")
