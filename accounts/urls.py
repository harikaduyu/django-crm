from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('login/', views.user_login, name="login"),
    path('register/', views.user_register, name="register"),
    path('products/', views.product, name="products"),
    path('customer/<str:pk>/', views.customer, name="customer"),
    path('create_order/<str:pk>/', views.create_order_view, name='create_order'),
    path('update_order/<str:pk>/', views.update_order_view, name='update_order'),
    path('delete_order/<str:pk>/', views.delete_order_view, name='delete_order'),
]
