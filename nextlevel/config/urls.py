"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.conf.urls.static import static
from django.conf import settings
from common import views

# from pybo import views # 더 이상 필요하지 않으므로 삭제

urlpatterns = [
    path('', views.index),
    path('admin/', admin.site.urls),
    path('pybo/', include('pybo.urls')),
    path('traffic/', include('traffic.urls')),
    path('common/', include('common.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
