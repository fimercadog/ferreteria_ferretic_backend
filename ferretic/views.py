from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework import viewsets
from ferretic.serializer import *

class TokenProvider(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user) # To validated token, if token is not created, it must be created
        user.token = token.key
        user.save()
        user_validator = User_serializer(user)
        return Response(user_validator.data)

class User_view(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = User_serializer

class Employee_view(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = Employee_serializer


class Vendor_view(viewsets.ModelViewSet):
    queryset = Vendor.objects.all()
    serializer_class = Vendor_serializer


class Client_view(viewsets.ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = Client_serializer


class Product_view(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = Product_serializer


class Order_view(viewsets.ModelViewSet):
    queryset = Order.objects.all().order_by('vendor__vendor_name')
    serializer_class = Order_serializer


class Purchase_view(viewsets.ModelViewSet):
    queryset = Purchase.objects.all().order_by('order__order_number')
    serializer_class = Purchase_serializer


class Invoice_view(viewsets.ModelViewSet):
    queryset = Invoice.objects.all().order_by('client__client_name')
    serializer_class = Invoice_serializer


class Sold_view(viewsets.ModelViewSet):
    queryset = Sold.objects.all().order_by('invoice__invoice_number')
    serializer_class = Sold_serializer
