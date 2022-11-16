from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models import PROTECT

class User(AbstractUser): # To validated users
    employee_name = models.CharField(max_length=50)
    employee_lastname = models.CharField(max_length=50)
    employee_address = models.CharField(max_length=100)
    employee_telephone = models.CharField(max_length=15)
    employee_birthday = models.CharField(max_length=15)
    employee_username = models.CharField(max_length=80)
    employee_password = models.CharField(max_length=30)
    token = models.CharField(max_length=100, default='', null=True, blank=True)

class Employee(models.Model): # Tabla de emppleado
    employee_name = models.CharField(max_length=50)
    employee_lastname = models.CharField(max_length=50)
    employee_address = models.CharField(max_length=100)
    employee_telephone = models.CharField(max_length=15)
    employee_birthday = models.CharField(max_length=15)
    employee_username = models.CharField(max_length=80)
    employee_password = models.CharField(max_length=30)
    def __str__(self):
        return self.employee_name + ' ' + self.employee_lastname

class Vendor(models.Model): # Tabla de proveedores
    vendor_name = models.CharField(max_length=80)
    vendor_address = models.CharField(max_length=100)
    vendor_telephone = models.CharField(max_length=15)
    vendor_email = models.EmailField()
    def __str__(self):
        return self.vendor_name

class Client(models.Model): # Tabla de clientes
    client_name = models.CharField(max_length=50)
    client_lastname = models.CharField(max_length=50)
    client_address = models.CharField(max_length=100)
    client_telephone = models.CharField(max_length=15)
    client_email = models.EmailField()
    def __str__(self):
        return self.client_name + ' ' + self.client_lastname

class Product(models.Model): # Tabla de productos
    product_name = models.CharField(max_length=50)
    product_description = models.TextField(max_length=80)
    product_price = models.FloatField()
    product_stock = models.IntegerField()
    def __str__(self):
        return self.product_name

class Order(models.Model): # Tabla de pedidos de productos
    vendor_id = models.ForeignKey(Vendor, on_delete=PROTECT)
    employee_id = models.ForeignKey(Employee, on_delete=PROTECT)
    order_number = models.CharField(max_length=12)
    def __str__(self):
        return self.order_number

class Purchase(models.Model): # Tabla de relacion pedidos y productos
    order_id = models.ForeignKey(Order, on_delete=PROTECT)
    order_date = models.DateTimeField(auto_now_add=True)
    product_id = models.ForeignKey(Product, on_delete=PROTECT)
    order_product_quantity = models.IntegerField()
    order_subtotal = models.IntegerField()
    order_total = models.IntegerField()
    '''def __str__(self):
        return self.order_number'''

class Invoice(models.Model): # Tabla de facturas
    client_id = models.ForeignKey(Client, on_delete=PROTECT)
    employee_id = models.ForeignKey(Employee, on_delete=PROTECT)
    invoice_number = models.CharField(max_length=12)
    def __str__(self):
        return self.invoice_number

class Sold(models.Model): # Tabla de relacion facturas y productos
    invoice_id = models.ForeignKey(Invoice, on_delete=PROTECT)
    invoice_date = models.DateTimeField(auto_now_add=True)
    product_id = models.ForeignKey(Product, on_delete=PROTECT)
    invoice_product_quantity = models.IntegerField()
    invoice_subtotal = models.IntegerField()
    invoice_total = models.IntegerField()
    '''def __str__(self):
            return self.invoice_number'''



