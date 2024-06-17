from django.contrib import admin
from django.urls import include, path
from app import views
from app.views import HomeView
urlpatterns = [
    path("", HomeView.as_view(), name="index"),
    path("",views.index),
    path("team/<int:s>/",views.cls)
]

