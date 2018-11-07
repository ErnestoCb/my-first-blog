from django.urls import path
from . import views
from django.conf.urls import url, include

urlpatterns = [
    path('', views.home, name = 'home'),
    path('perro/', views.perro_list, name = 'perro_list'),
    path('perro/<int:pk>/', views.perro_detail, name='perro_detail'),
]