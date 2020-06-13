from django.urls import path
from . import views

urlpatterns = [
    path('', views.store, name='store'),
    path('login/', views.login_page, name='login'),
    path('register/', views.register_page, name='register'),
    path('clothes/', views.clothes, name='clothes'),
    path('clothes_detail/<str:pk>/', views.clothes_detail, name='clothes_detail'),
    path('shoes/', views.shoes, name='shoes'),
    path('shoes_detail/<str:pk>/', views.shoes_detail, name='shoes_detail'),
    path('accessories/', views.accessories, name='accessories'),
    path('accessories_detail/<str:pk>/', views.accessories_detail, name='accessories_detail'),
    path('checkout/', views.checkout, name='checkout'),
]