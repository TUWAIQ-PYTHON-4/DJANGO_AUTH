from django.urls import  path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',views.list_post,name='home'),
    path('add/',views.add_post,name='add'),
    path('post/<pk>', views.comment_detile, name='post')

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)