from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views


urlpatterns = [
    path("", views.index, name="index"),
    path('addPost',views.add_post,name='addPost'),
    path('detail/<post_id>',views.post_detail,name='detail'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


