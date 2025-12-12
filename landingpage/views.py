from django.shortcuts import redirect
from django.contrib import messages

# Create your views here.
# view created following tutorial made by Codemy.com
def home(request):
    return redirect("account_login")
