from django.db import models

# Create your models here.

# Overall function: The service will RECEIVE an IPN notification from PayPal, will process it and 
#                   then UPDATE the customer information on the customer API.

# PayPal table
class Paypal(models.Model):
    protection_eligibility = models.CharField(max_length=50)
    address_status = models.CharField(max_length=50)
    payer_id = models.CharField(max_length=250)
    payment_date = models.CharField(max_length=30)
    payment_status = models.CharField(max_length=30)
    notify_version = models.DecimalField(max_digits=5, decimal_places=3)
    verify_sign = models.CharField(max_length=250)
    receiver_id = models.CharField(max_length=100)
    txn_type = models.CharField(max_length=50)
    item_name = models.CharField(max_length=25)
    mc_currency = models.CharField(max_length=10)
    payment_gross = models.DecimalField(max_digits=8, decimal_places=2)
    shipping = models.CharField(max_length=20)

    def __str__(self):
        return self.payer_id