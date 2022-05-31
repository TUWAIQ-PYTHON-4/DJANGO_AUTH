from django.urls import path
from . import views


app_name = "blog"

urlpatterns = [
    path("", views.index, name="index"),
    path("add/", views.add_blog, name="add_blog"),
    path("detail/<blog_id>", views.blog_detail, name="blog_detail"),
]