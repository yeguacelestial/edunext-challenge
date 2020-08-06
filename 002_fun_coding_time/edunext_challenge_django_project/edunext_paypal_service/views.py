from django.shortcuts import render
from django.http import JsonResponse

# DRF
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import PaypalSerializer

# Models
from .models import Paypal

# For sending requests to Customer API
import requests

# # SETTINGS # #
CUSTOMER_API_ENDPOINT = 'http://localhost:8010/api/v1/customerdata/'

# # VIEWS # #

# Manipulate GET request
@api_view(['GET'])
def ipnNotif_list(request):
    ipnNotifications = Paypal.objects.all()

    # 'many' means we want a list of all notifications
    serializer = PaypalSerializer(ipnNotifications, many=True)
    return Response(serializer.data)


# Manipulate POST request on this API
@api_view(['POST'])
def ipnNotif_create(request):
    # request.data object is a JSON object
    serializer = PaypalSerializer(data=request.data)

    # IF all fields are available on the POST request:
    if serializer.is_valid():

        # IF payment_status IS Completed:
        if request.data['payment_status'] == 'Completed':
            # Current available items
            available_items = [
                'free',
                'basic',
                'premium'
            ]

            # IF item_name IN available_items:
            if request.data['item_name'] in available_items:
                # Send the info to the Customer API
                print('[+] VALIDATED ITEM NAME')
                customerAPI_update(request, payment_is_completed=True)

                # Save the IPN Notif Object in the DB
                serializer.save()
                return Response(serializer.data)

            # ELSE if item_name IS NOT IN available_items:
            else:
                json_detail = {
                    'error': 'Item name is not valid.'
                }
                print("[-] ERROR => ITEM NAME IS NOT VALID")
                return Response(status=status.HTTP_406_NOT_ACCEPTABLE, data=json_detail)

        # ELSE IF payment_status IS NOT "Completed":
        else:
            customerAPI_update(request, payment_is_completed=False)
            return Response(status=status.HTTP_406_NOT_ACCEPTABLE, data=request.data)

    # If the request is not valid, return a HTTP error
    else:
        json_error = {
            'error': 'Invalid request.'
        }
        return Response(data=json_error, status=status.HTTP_406_NOT_ACCEPTABLE)

# TODO
# Update data on Customer API
def customerAPI_update(request, payment_is_completed:bool):
    item_name = request.data['item_name']
    payer_id = request.data['payer_id']
    payer_endpoint_url = CUSTOMER_API_ENDPOINT + payer_id + '/'

    # Get json object from Customer request
    customer_json_object = requests.get(payer_endpoint_url).json()

    # IF payment_status IS Completed:
    if payment_is_completed:
        # Update info on the Customer API
        print(f"[+] REQUEST FROM PAYER {payer_id} RECEIVED, UPDATING DATA ON CUSTOMER API...")

        # Update data of Customer
        customer_json_object['data']['SUBSCRIPTION'] = item_name

        # Send the modified JSON object to the Customer API
        put_customer_data = requests.put(payer_endpoint_url, json=customer_json_object)
        print(put_customer_data)

        return Response(data=customer_json_object, status=status.HTTP_200_OK)
        
    # ELSE IF payment_status IS DIFFERENT THAN completed
    else:
        # On CustomerAPI[payer_id]:
            # Update SUBSCRIPTION field to free
        customer_json_object['data']['SUBSCRIPTION'] = 'free'

            # Update all elements of ENABLED_FEATURES to False
        enabled_features_object = customer_json_object['data']['ENABLED_FEATURES']
        enabled_features_object = {feature:False for feature in enabled_features_object}

        put_customer_data = requests.put(payer_endpoint_url, json=customer_json_object)
        return Response(data=customer_json_object, status=status.HTTP_200_OK)