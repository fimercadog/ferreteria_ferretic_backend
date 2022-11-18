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
    vendor = Vendor_serializer(read_only=True)
    vendor_id = serializers.PrimaryKeyRelatedField(write_only=True, queryset=Vendor.objects.all(), source='vendor')
    employee = Employee_serializer(read_only=True)
    employee_id = serializers.PrimaryKeyRelatedField(write_only=True, queryset=Employee.objects.all(), source='employee')
    class Meta:
        model = Order
        fields = '__all__'

class Purchase_serializer(serializers.ModelSerializer):
    order = Order_serializer(read_only=True)
    order_id = serializers.PrimaryKeyRelatedField(write_only=True, queryset=Order.objects.all(), source='order')
    product = Product_serializer(read_only=True)
    product_id = serializers.PrimaryKeyRelatedField(write_only=True, queryset=Product.objects.all(), source='product')
    class Meta:
        model = Purchase
        fields = '__all__'

class Invoice_serializer(serializers.ModelSerializer):
    client = Client_serializer(read_only=True)
    client_id = serializers.PrimaryKeyRelatedField(write_only=True, queryset=Client.objects.all(), source='client')
    employee = Employee_serializer(read_only=True)
    employee_id = serializers.PrimaryKeyRelatedField(write_only=True, queryset=Employee.objects.all(), source='employee')
    class Meta:
        model = Invoice
        fields = '__all__'

class Sold_serializer(serializers.ModelSerializer):
    invoice = Invoice_serializer(read_only=True)
    invoice_id = serializers.PrimaryKeyRelatedField(write_only=True, queryset=Invoice.objects.all(), source='invoice')
    product = Product_serializer(read_only=True)
    product_id = serializers.PrimaryKeyRelatedField(write_only=True, queryset=Product.objects.all(), source='product')
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

