from django.urls import path 

from . import views 

urlpatterns = [
    path("", views.dashboard, name="dashboard"),
    path("add_thought", views.add_thought, name="add_thought"),
]