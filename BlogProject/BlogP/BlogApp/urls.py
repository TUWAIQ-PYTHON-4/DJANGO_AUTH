from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin


urlpatterns = [
    path('admin/', admin.site.urls),
    path("", views.index, name="index"),
    path("add/", views.add, name="add"),
    path("comment/<post_id>", views.comment, name="comment"),


]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)