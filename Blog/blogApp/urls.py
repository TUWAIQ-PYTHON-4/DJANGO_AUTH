from django.urls import path
from . import views

# add namespace for the app

urlpatterns = [
    path("", views.Blog, name="index"),
    path("showDetails/<int:id>", views.ShowDetials, name='showDetails'),
    path("comment/<int:id>",views.Comment,name='comment')
]
