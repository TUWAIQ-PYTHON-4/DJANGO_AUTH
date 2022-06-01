from django.urls import path
from . import views

#add namespace for the app
app_name = "appblog"

urlpatterns = [
    path("", views.index, name="index"),
    path('register', views.register, name='register'),

    ]