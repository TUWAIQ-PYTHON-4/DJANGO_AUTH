from django.urls import path
from . import views
from .views import login_user

urlpatterns = [
    path("", views.index, name="index"),
    path('login/',login_user,name='login'),
    path("add_post/", views.add_post,name='add_post')

]