from django.urls import path
from . import views

name = 'BlogApp'
urlpatterns = [
    path('', views.posts_list, name='home'),
    path('posts_list', views.posts_list, name='posts_list'),
    path('post_detail/<id>/', views.post_detail, name='post_detail'),
]
