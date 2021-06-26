from django.urls import path, include

from . import views

app_name = "Converter"
urlpatterns = [
    path("", views.index, name="index"),
]
