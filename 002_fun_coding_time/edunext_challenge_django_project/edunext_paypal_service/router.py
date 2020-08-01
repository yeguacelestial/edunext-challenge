from edunext_paypal_service.viewsets import PaypalViewset
from rest_framework import routers

router = routers.DefaultRouter()
router.register('paypal', PaypalViewset)