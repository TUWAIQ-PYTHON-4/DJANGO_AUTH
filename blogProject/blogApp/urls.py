from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from . import views
from django.urls import path

urlpatterns = [
     path('admin/', admin.site.urls),
     path('', views.index, name="index"),
     path('add_post/', views.add_post, name="add_post"),
     path('post_detail/<p_id>', views.post_detail, name="post_detail")
 ]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)