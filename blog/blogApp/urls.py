from django.urls import path
from . import views
from django.conf import settings
from django.contrib.auth import views as auth_views
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name = 'index'),
    path('post/<str:post_id>', views.post, name = 'post'),
    path('register', views.register, name = 'register'),
    path('login', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout', auth_views.LogoutView.as_view(template_name='logout.html'), name='logout'),
    path('add_post',views.add_post, name = 'add_post' ),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
