from django.urls import path
from . import views

urlpatterns = [
    path("tables", views.tables, name="tables"),
    path("tables/conversation/<int:pk>/", views.conversation, name="conversation"),
    path("tables/conversation/<int:pk>/close_table/", views.close_table, name="close_table")
]