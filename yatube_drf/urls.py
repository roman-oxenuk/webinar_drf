"""yatube_drf URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('plain_views/', include('app_plain_views.urls')),
    path('cbv_views/', include('app_cbv.urls')),
    path('serializers/', include('app_serializers.urls')),
    path('api_views/', include('app_api_views.urls')),
    path('api_generics/', include('app_generics_views.urls')),
    path('api_viewsets/', include('app_viewsets.urls')),
]
