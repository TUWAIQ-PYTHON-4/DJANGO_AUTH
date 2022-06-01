from django.urls import  path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',views.postlist,name='home'),
    path('post/<pk>',views.comment_detile,name='post'),
    path('add/',views.add,name='add'),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)