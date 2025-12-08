from django.urls import path
from . import views

urlpatterns = [
    path("tables", views.tables, name="tables"),
    path("tables/conversation/<str:name>/", views.conversation, name="conversation")
]