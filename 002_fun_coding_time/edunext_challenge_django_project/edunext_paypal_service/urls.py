from django.urls import path
from . import views

urlpatterns = [
    path('ipn_notifications_list/', views.ipnNotif_list, name="ipnNotif_list"),
    path('ipn_notifications/', views.ipnNotif_create, name="ipnNotif_create")
]
