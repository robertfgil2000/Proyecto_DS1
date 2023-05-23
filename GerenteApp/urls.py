from django.urls import path, include
from rest_framework import routers
from GerenteApp import views

router = routers.DefaultRouter()
router.register(r'vendedor', views.SellerView, 'vendedor')

urlpatterns = [    
    path('sucursal/', views.sucursal, name="sucursal"),
    path('new/', views.crear_sucursal, name="createsucursal"),
    path('api/', include(router.urls))
]