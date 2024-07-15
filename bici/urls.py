from django.urls import path
from . import views

urlpatterns = [
    path('index/', views.index, name='index'),
    path('nosotros/', views.nosotros, name='nosotros'),
    path('inicio/', views.inicio, name='inicio'),
    path('tienda/', views.tienda, name='tienda'),
    path('accesorios/', views.accesorios, name='accesorios'),
    path('registro/', views.registro, name='registro'),
    path('API/', views.API, name='API'),

    path('list/', views.list, name='list'),
   

    path('modificar/<int:pk>/', views.modificar_cliente, name='modificar_cliente'),
    path('eliminar/<int:pk>/', views.eliminar_cliente, name='eliminar_cliente'),
     path('modificar/<int:pk>/', views.modificar_cliente, name='modificar_cliente'),

]
