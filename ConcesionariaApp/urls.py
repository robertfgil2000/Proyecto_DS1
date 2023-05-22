from django.urls import path
from ConcesionariaApp import views

urlpatterns = [    
    path('', views.home, name="home"),
    path('login/', views.login, name="login"),

]