from django.urls import path
from . import views

urlpatterns = [
    path('paypal/ipnNotif_list/', views.ipnNotif_list, name="ipnNotif_list"),
    path('paypal/', views.ipnNotif_create, name="ipnNotif_create"),
]