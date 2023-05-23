from django.urls import path
from ConcesionariaApp import views

urlpatterns = [    
    path('', views.home, name="home"),
    path('login/', views.login, name="login"),

    # User
    path('user_create/', views.user_create, name='user_create'),
    path('user_get_all/', views.user_get_all , name='user_get_all'),
    path('user_get/<int:user_id>/', views.user_get, name='user_get'),
    path('user_verify_login/email=<str:email>&password=<str:password>/', 
         views.user_verify_login, name='user_verify_login'),
    path('user_delete/<int:user_id>/', views.user_delete, name='user_delete'),
    path('user_modify/<int:user_id>/', views.user_modify, name='user_modify'),

]