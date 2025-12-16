from django.urls import path
from django.views.generic import RedirectView
from . import views

urlpatterns = [    
    path("register/", RedirectView.as_view(pattern_name="account_signup"), name="register"),
    path("logout_user/", RedirectView.as_view(pattern_name="account_logout"), name="logout_user"),
    path("account_management/", views.account_management, name="account_management")
]