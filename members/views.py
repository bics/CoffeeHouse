from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import AccountUpdateForm

# Create your views here.

def account_management(request):
    form = AccountUpdateForm(request.POST)
    return render(request, 'account_management.html', { "form": form})

def logout_user(request):
    logout(request)
    return redirect('home')