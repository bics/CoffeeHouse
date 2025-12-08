from django.urls import path
from . import views

urlpatterns = [
    path("tables", views.tables, name="tables"),
    path("tables/conversation", views.conversation, name="conversation")
]