from django.urls import path
from . import views

urlpatterns = [
    path("tables", views.tables, name="tables"),
    path("tables/conversation/<int:pk>/", views.conversation, name="conversation")
]