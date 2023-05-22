from django.urls import path
from GerenteApp import views

urlpatterns = [    
    path('sucursal/', views.sucursal, name="sucursal"),
    path('new/', views.crear_sucursal, name="createsucursal")
    
]