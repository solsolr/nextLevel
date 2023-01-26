from django.urls import path
from . import views

app_name = 'traffic'


urlpatterns = [
    path('', views.index, name='index'),
    path('fileupload/', views.fileUpload, name="fileupload"),
    path('<int:box_id>', views.detail, name="detail"),
    path('traffic_create/<int:box_id>', views.traffic_create, name="traffic_create"),
]