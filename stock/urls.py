from django.contrib import admin
from django.urls import path, include
from user import views as user_view
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('dashboard.urls')),
    path('', include('user.urls')),
    # path('register/', user_view.register, name='user-register'),
    # path('login/', auth_views.LoginView.as_view(template_name='user/login.html'), name='user-login'),
    # path('logout/', auth_views.LogoutView.as_view(template_name='user/logout.html'), name='user-logout'),
]
urlpatterns += static(settings.MEDIA_URL , document_root=settings.MEDIA_ROOT)