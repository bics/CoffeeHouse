from django.shortcuts import render, HttpResponse
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
def home(request):
    return render(request, "index.html")

def register(request):
    # Snippet taken from ChatGPT
    placeholders = {
        "username": "Username",
        "password1": "Password",
        "password2": "Confirm Password",
    }

    form = UserCreationForm()    
    # Snippet taken from ChatGPT
    for name, field in form.fields.items():
        field.widget.attrs.setdefault("class", "")
        field.widget.attrs["class"] += " form-control-lg w-100"
        field.widget.attrs["placeholder"] = placeholders.get(name, "")
    return render(request, "register.html", { "form": form})

