from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
                  path('', views.index, name='home'),
                  path('post<int:id>', views.post_infor, name="post"),
                  path('push_post', views.push_post, name="push_post"),

              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
