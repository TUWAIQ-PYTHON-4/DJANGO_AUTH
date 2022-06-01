from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("", views.index, name="index"),
    path('add_post',views.add_post,name='add_post'),
    path('detail/<post_id>',views.post_detail,name='detail'),
]  + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
