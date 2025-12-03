from django.shortcuts import render, HttpResponse
from django.contrib.auth.forms import UserCreationForm
from .forms import RegisterForm
from django.shortcuts import redirect

# Create your views here.
def home(request):
    return render(request, "index.html")

# view created following tutorial made by Codemy.com https://www.youtube.com/watch?v=HdrOcreAXKk
def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            #login(request, user)
            #message
            return redirect('home')
    else:
        form = RegisterForm()
    return render(request, "register.html", { "form": form})
