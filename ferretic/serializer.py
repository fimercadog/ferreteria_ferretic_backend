from pyexpat import model

from rest_framework import serializers
from ferretic.models import *

class Employee_serializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = '__all__'

class Vendor_serializer(serializers.ModelSerializer):
    class Meta:
        model = Vendor
        fields = '__all__'

class Client_serializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = '__all__'

class Product_serializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

class Order_serializer(serializers.ModelSerializer):
    vendor_id = Vendor_serializer(read_only=True)
    vendorID = serializers.PrimaryKeyRelatedField(write_only=True, queryset=Vendor.objects.all(), source='vendor_id')
    employee_id = Employee_serializer(read_only=True)
    employeeID = serializers.PrimaryKeyRelatedField(write_only=True, queryset=Employee.objects.all(), source='employee_id')
    class Meta:
        model = Order
        fields = '__all__'

class Purchase_serializer(serializers.ModelSerializer):
    order_id = Order_serializer(read_only=True)
    orderID = serializers.PrimaryKeyRelatedField(write_only=True, queryset=Order.objects.all(), source='order_id')
    product_id = Product_serializer(read_only=True)
    productID = serializers.PrimaryKeyRelatedField(write_only=True, queryset=Product.objects.all(), source='product_id')
    class Meta:
        model = Purchase
        fields = '__all__'

class Invoice_serializer(serializers.ModelSerializer):
    client_id = Client_serializer(read_only=True)
    clientID = serializers.PrimaryKeyRelatedField(write_only=True, queryset=Client.objects.all(), source='client_id')
    employee_id = Employee_serializer(read_only=True)
    employeeID = serializers.PrimaryKeyRelatedField(write_only=True, queryset=Employee.objects.all(), source='employee_id')
    class Meta:
        model = Invoice
        fields = '__all__'

class Sold_serializer(serializers.ModelSerializer):
    invoice_id = Invoice_serializer(read_only=True)
    invoiceID = serializers.PrimaryKeyRelatedField(write_only=True, queryset=Invoice.objects.all(), source='invoice_id')
    product_id = Product_serializer(read_only=True)
    productID = serializers.PrimaryKeyRelatedField(write_only=True, queryset=Product.objects.all(), source='product_id')
    class Meta:
        model = Sold
        fields = '__all__'

class User_serializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
    def create(self, validated_data):
        user = User(
            employee_username = validated_data['employee_username'],
            employee_name = validated_data['employee_name'],
            employee_lastname=validated_data['employee_lastname'],
            employee_address=validated_data['employee_address'],
            employee_telephone=validated_data['employee_telephone'],
            employee_birthday=validated_data['employee_birthday'],
        )
        user.set_password(validated_data['employee_password'])
        user.save()
        return user