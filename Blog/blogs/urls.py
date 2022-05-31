from django.urls import path
from . import views

app_name= 'blogs'

urlpatterns = [
    path("", views.index, name="index"),
    path("add_post/", views.add_post, name="add_post"),
    path("post_detail/<post_id>", views.post_detail, name="post_detail"),

]