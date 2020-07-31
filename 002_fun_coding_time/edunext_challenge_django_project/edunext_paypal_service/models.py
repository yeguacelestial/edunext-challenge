from django.db import models

# Create your models here.

# Overall function: The service will RECEIVE an IPN notification from PayPal, will process it and 
#                   then UPDATE the customer information on the customer API.

# PayPal table
class Paypal(models.Model):
    protection_eligibility = models.CharField(max_length=50, default=None)
    address_status = models.CharField(max_length=50, default=None)
    payer_id = models.CharField(max_length=250, default=None)
    payment_date = models.DateField(default=None)
    payment_status = models.CharField(max_length=30, default=None)
    notify_version = models.FloatField(default=None)
    verify_sign = models.CharField(max_length=250, default=None)
    receiver_id = models.CharField(max_length=100, default=None)
    txn_checkout = models.CharField(max_length=50, default=None)
    item_name = models.CharField(max_length=25, default=None)
    mc_currency = models.CharField(max_length=10, default=None)
    payment_gross = models.DecimalField(max_digits=6, decimal_places=2, default=None)
    shipping = models.DecimalField(max_digits=6, decimal_places=2, default=None)
    ipn_notification = models.CharField(max_length=250, default=None)

    def __str__(self):
        return self.ipn_notification