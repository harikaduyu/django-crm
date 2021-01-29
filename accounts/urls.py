from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('login/', views.user_login, name="login"),
    path('logout/', views.user_logout, name="logout"),
    path('user/', views.user_profile, name="user"),
    path('register/', views.user_register, name="register"),
    path('account/', views.account_settings, name="account"),
    path('products/', views.products, name="products"),
    path('customer/<str:pk>/', views.customer, name="customer"),
    path('create_order/<str:pk>/', views.create_order_view, name='create_order'),
    path('update_order/<str:pk>/', views.update_order_view, name='update_order'),
    path('delete_order/<str:pk>/', views.delete_order_view, name='delete_order'),
    path('reset_password/', auth_views.PasswordResetView.as_view(),
         name="reset_password"),
    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(),
         name="password_reset_done"),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(),
         name="password_reset_confirm"),
    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(),
         name="password_reset_complete")
]
