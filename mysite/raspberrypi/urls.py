from django.urls import path
from django.contrib import admin
from . import views

app_name = 'rasp'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('mqtt/', views.mqttTest, name='mqtt'),
    path('socket/', views.socketTest, name='socket'),
]