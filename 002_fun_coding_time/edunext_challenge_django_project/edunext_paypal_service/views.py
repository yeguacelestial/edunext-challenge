from django.shortcuts import render
from django.http import JsonResponse

# DRF
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import PaypalSerializer

from .models import Paypal

# Create your views here.

# Manipulate GET request
@api_view(['GET'])
def ipnNotif_list(request):
    ipnNotifications = Paypal.objects.all()

    # 'many' means we want a list of all notifications
    serializer = PaypalSerializer(ipnNotifications, many=True)
    return Response(serializer.data)


# Manipulate POST request
@api_view(['POST'])
def ipnNotif_create(request):
    # request.data object is a JSON object
    serializer = PaypalSerializer(data=request.data)

    # Validate that we have every field on the request
    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)