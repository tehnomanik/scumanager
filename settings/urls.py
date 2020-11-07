from django.urls import path
from . import views

urlpatterns = [
    path('', views.settingsHome, name="settings-home"),
    path('refresh-players/', views.settingsRefreshPlayers, name="settings-refresh-players"),
]