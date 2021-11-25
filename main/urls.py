from django.urls import path
from . import views


urlpatterns = [
    path("", views.index,name="index"),
    path("download/", views.view,name="indexi"),
    path("downloads/", views.download,name="indexq")
]
