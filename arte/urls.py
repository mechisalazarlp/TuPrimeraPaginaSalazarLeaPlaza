from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('crear_artista/', views.crear_artista, name='crear_artista'),
    path('crear_obra/', views.crear_obra, name='crear_obra'),
    path('crear_movimiento/', views.crear_movimiento, name='crear_movimiento'),
    path('buscar/', views.buscar_artista, name='buscar_artista'),
]