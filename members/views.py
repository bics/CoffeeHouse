from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

# Create your views here.

def account_management(request):
    return render(request, 'account_management.html')

def logout_user(request):
    logout(request)
    return redirect('home')