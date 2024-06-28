"""
URL configuration for base project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import LoginView, PasswordResetView,PasswordResetDoneView,PasswordResetConfirmView,PasswordResetCompleteView

from base.views import index_admin, index_user, logout_user

urlpatterns = [
    path('admin-django/', admin.site.urls),
    path("admin/", index_admin, name="index-admin"),
    path("", index_user, name="index-user"),
    
    path("login/", LoginView.as_view(), name="login"),
    path("logout/", logout_user, name="logout"),
    path('', include('django.contrib.auth.urls')),
    path('reiniciar/',PasswordResetView.as_view(),name='pass_reset'),
    path('reiniciar/enviar',PasswordResetDoneView.as_view(),name='pass_reset_done'),
    path('reiniciar/<uid64>/<token>',PasswordResetConfirmView.as_view(),name='pass_reset_confirm'),
    path('reiniciar/completo',PasswordResetCompleteView.as_view(),name='pass_reset_reset_complete'),
    
    
    path("comunidad/", include("comunidad.urls")),
    path("comunidad/api/", include("comunidad.api_urls")),
    path("servicios/", include("servicios.urls")),
    path("servicios/api/", include("servicios.api_urls")),
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
