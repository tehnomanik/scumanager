from django.urls import path
from . import views

urlpatterns = [
    path('', views.playersHome, name="players-home"),
    path('create_player/', views.createPlayer, name="players-create"),
    path('update_player/<str:pk>', views.updatePlayer, name="players-update"),
    path('delete_player/<str:pk>', views.deletePlayer, name="players-delete"),

    path('squad/', views.squadHome, name="squad-home"),
    path('create_squad/', views.createSquad, name="squad-create"),
    path('update_squad/<str:pk>', views.updateSquad, name="squad-update"),
    path('delete_squad/<str:pk>', views.deleteSquad, name="squad-delete"),

    path('donation/', views.donationHome, name="donation-home"),
    path('create_donation/', views.createDonation, name="donation-create"),
    path('update_donation/<str:pk>', views.updateDonation, name="donation-update"),
    path('delete_donation/<str:pk>', views.deleteDonation, name="donation-delete"),

    path('vehicle/', views.vehicleHome, name="vehicle-home"),
    path('create_vehicle/', views.createVehicle, name="vehicle-create"),
    path('update_vehicle/<str:pk>', views.updateVehicle, name="vehicle-update"),
    path('delete_vehicle/<str:pk>', views.deleteVehicle, name="vehicle-delete"),

    path('case/', views.caseHome, name="case-home"),
    path('create_case/', views.createCase, name="case-create"),
    path('update_case/<str:pk>', views.updateCase, name="case-update"),
    path('delete_case/<str:pk>', views.deleteCase, name="case-delete"),

    path('flag/', views.flagHome, name="flag-home"),
    path('create_flag/', views.createFlag, name="flag-create"),
    path('update_flag/<str:pk>', views.updateFlag, name="flag-update"),
    path('delete_flag/<str:pk>', views.deleteFlag, name="flag-delete"),
]