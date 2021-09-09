"""course URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('secret-admin/', admin.site.urls),
    path('api/', include('bookAPI.urls')),
    path('auth/', include('loginAPI.urls')),
    path('', include('tempapp.urls')),
              # 127.0.0.1:8000/api/
    path('api-auth/', include('rest_framework.urls')),
    path('drf_api/', include('drf_book_api.urls'))

              ]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)\
              + static(settings.TEMPLATE_URL,document_root=settings.TEMPLATE_ROOT) + \
              static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
