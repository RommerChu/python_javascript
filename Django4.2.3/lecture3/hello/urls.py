from . import views
from django.urls import path

urlpatterns = [
     path("", views.index, name="index"),
     path("corazon", views.corazon, name="corazon"),
     path("<str:name>", views.greet, name="greet")
]