from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import AccountUpdateForm

# Create your views here.

def account_management(request):
    if request.method == "POST":
        form =  AccountUpdateForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('account_management')
    else:
        form = AccountUpdateForm(instance=request.user)
    return render(request, 'account_management.html', { "form": form})

def logout_user(request):
    logout(request)
    return redirect('home')