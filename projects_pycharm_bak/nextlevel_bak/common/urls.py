from django.urls import path
from . import views

app_name = 'common'


urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login, name='login'),
    path('signup/', views.signup, name='sign_up'),
]