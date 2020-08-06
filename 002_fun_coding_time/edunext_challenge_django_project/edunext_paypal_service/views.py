import datetime
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

# Manipulate POST request on this API
@api_view(['POST'])
def ipnNotif_create(request):
    # Verify that user exists on CustomerAPI
    if customer_exists(request):

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
                json_error = {
                    'error': 'Payment status is not completed. All features are disabled.'
                }
                return Response(status=status.HTTP_406_NOT_ACCEPTABLE, data=json_error)

        # If the request is not valid, return a HTTP error
        else:
            json_error = {
                'error': 'Invalid request.'
            }
            return Response(data=json_error, status=status.HTTP_406_NOT_ACCEPTABLE)
    
    # Else, if user does not exists on the CustomerAPI
    else:
        json_error = {
            'error': 'The user (payer_id) does not exist on the CustomerAPI.'
        }
        return Response(data=json_error, status=status.HTTP_406_NOT_ACCEPTABLE)


# Retrieve existing customers, just in case the user sends a weird payer_id argument
def customer_exists(request):
    # Retrieve ID users from database
    customers_data = requests.get(CUSTOMER_API_ENDPOINT).json()['results']
    customers_ids = [customer['id'] for customer in customers_data]
    
    # Verify that payer_id exists on CustomerAPI
    if request.data['payer_id'] in customers_ids:
        return True
    # Else, if user does not exists
    else:
        return False


# Update data on Customer API
def customerAPI_update(request, payment_is_completed:bool):
    # Dict with items values for ordering them
    items = {
        'free': 0,
        'basic': 1,
        'premium': 2
    }

    # Customer request data
    new_item_name = request.data['item_name']
    new_item_value = items[new_item_name]
    payer_id = request.data['payer_id']
    payer_endpoint_url = CUSTOMER_API_ENDPOINT + payer_id + '/'

    # Get json object from Customer request
    customer_json_object = requests.get(payer_endpoint_url).json()

    # Get previous item_name from customer_json_object
    previous_item_name = customer_json_object['data']['SUBSCRIPTION']
    previous_item_value = items[previous_item_name]

    # IF payment_status IS Completed:
    if payment_is_completed:
        # Update info on the Customer API
        print(f"[+] REQUEST FROM PAYER {payer_id} RECEIVED, UPDATING DATA ON CUSTOMER API...")

        # Update data of Customer
        customer_json_object['data']['SUBSCRIPTION'] = new_item_name
        if new_item_name == 'basic' or new_item_name == 'premium':
            # Enable all features
            enabled_features_object = customer_json_object['data']['ENABLED_FEATURES']
            customer_json_object['data']['ENABLED_FEATURES'] = {feature:True for feature in enabled_features_object}

        # If user UPGRADE his current plan
        if previous_item_value < new_item_value:
            # Try dumping DOWNGRADE_DATE from the Customer data
            if 'DOWNGRADE_DATE' in customer_json_object['data']: customer_json_object['data'].pop('DOWNGRADE_DATE')

            # Add UPGRADE_DATE to Customer json object
            customer_json_object['data']['UPGRADE_DATE'] = str(datetime.datetime.now())

            # Update LAST_PAYMENT_DATE from Customer json object
            customer_json_object['data']['LAST_PAYMENT_DATE'] = str(datetime.datetime.now())

        # ELSE, IF user DOWNGRADES his current plan
        elif previous_item_value > new_item_value: 
            # Try dumping UPGRADE_DATE from the Customer data
            if 'UPGRADE_DATE' in customer_json_object['data']: customer_json_object['data'].pop('UPGRADE_DATE')

            # Update LAST_PAYMENT_DATE only IF user DOWNGRADES from premium to basic
            if new_item_name == 'basic' and previous_item_name == 'premium':
                customer_json_object['data']['LAST_PAYMENT_DATE'] = str(datetime.datetime.now())

            # Add DOWNGRADE_DATE to Customer json object
            customer_json_object['data']['DOWNGRADE_DATE'] = str(datetime.datetime.now())

        # Send the modified JSON object to the Customer API
        put_customer_data = requests.put(payer_endpoint_url, json=customer_json_object)
        print(put_customer_data.json())

        return Response(data=customer_json_object, status=status.HTTP_200_OK)
        
    # ELSE IF payment_status IS DIFFERENT THAN completed
    else:
        # Update SUBSCRIPTION field to free
        customer_json_object['data']['SUBSCRIPTION'] = 'free'
        customer_json_object['data']['DOWNGRADE_DATE'] = str(datetime.datetime.now())

        # If there is an UPGRADE_DATE, remove it
        if 'UPGRADE_DATE' in customer_json_object['data']: customer_json_object['data'].pop('UPGRADE_DATE')

        # Update all elements of ENABLED_FEATURES to False
        enabled_features_object = customer_json_object['data']['ENABLED_FEATURES']
        customer_json_object['data']['ENABLED_FEATURES'] = {feature:False for feature in enabled_features_object}

        # Send modified JSON object to the Customer API
        put_customer_data = requests.put(payer_endpoint_url, json=customer_json_object)
        print(put_customer_data)

        # Return JSON object, explaining the exception
        json_error = {
            'error': 'Payment status is not completed. All features are disabled.'
        }
        return Response(data=json_error, status=status.HTTP_406_NOT_ACCEPTABLE)