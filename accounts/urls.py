from django.urls import path
from . import views

urlpatterns = [
    path('', views.accountProfile, name="account-profile"),
    path('login/', views.accountLogin, name="account-login"),
    path('register/', views.accountRegister, name="account-register"),
    path('logout/', views.accountLogout, name="account-logout"),
]