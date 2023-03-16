from django.urls import path
from . import views
from . import tkinter4

app_name = 'login'

urlpatterns = [
    path('', views.index, name='index'),
    path('auth/', views.auth, name='auth'),
    path('<str:user_id>/<int:box_id>/', views.box_detail, name='box_detail'),
    path('<str:user_id>/<int:box_id>/<int:traffic_id>', views.traffic_detail, name='traffic_detail'),
    path('image_slide/', views.traffic, name='image_slide'),
    path('gin/', views.traffic2, name='gin'),

    # path('kakao/', views.kakao, name='kakao'),
]
