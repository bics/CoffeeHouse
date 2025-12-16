from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import AccountUpdateForm
from django.db import IntegrityError

# Create your views here.

def account_management(request):
    if request.method == "POST":
        form =  AccountUpdateForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, "Your details have been updated.")
            return redirect('account_management')
    else:
        form = AccountUpdateForm(instance=request.user)
    return render(request, 'account_management.html', { "form": form})

def user_deletion(request):
    if request.method == "POST":
        # Try-catch logic generated using ChatGPT
        try:
            user = request.user
            logout(request)      # end session first
            user.delete()        # then delete user
            messages.success(request, "Your account has been deleted.")
            return redirect("account_login")  # or a "goodbye" page
        except IntegrityError:
            messages.error(
                request,
                "Your account cannot be deleted because it still owns content."
            )
            return redirect("account_management")

    return render(request, 'user_deletion.html')