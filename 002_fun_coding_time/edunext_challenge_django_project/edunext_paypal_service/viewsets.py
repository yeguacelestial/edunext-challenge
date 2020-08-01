from rest_framework import viewsets
from . import models
from . import serializers


class PaypalViewset(viewsets.ModelViewSet):
    queryset = models.Paypal.objects.all()
    serializer_class = serializers.PaypalSerializer