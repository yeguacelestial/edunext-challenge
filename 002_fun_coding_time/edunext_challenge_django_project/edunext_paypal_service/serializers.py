from rest_framework import serializers
from .models import Paypal

class PaypalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Paypal
        fields = '__all__'