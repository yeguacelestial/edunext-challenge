from django.urls import path
from . import views

urlpatterns = [
    path('paypal/', views.ipnNotif_create, name="ipnNotif_create"),
]