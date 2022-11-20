from os.path import basename
from rest_framework import routers
from django.urls import path, include
from ferretic.views import *


router = routers.DefaultRouter()
router.register('user', User_view, basename='user')
router.register('employee', Employee_view, basename='employee')
router.register('vendor', Vendor_view, basename='vendor')
router.register('product', Product_view, basename='product')
router.register('order', Order_view, basename='order')
router.register('order_product', Order_product_view, basename='order_product')
router.register('invoice', Invoice_view, basename='invoice')
router.register('invoice_product', Invoice_product_view, basename='invoice_product')


urlpatterns = [
    path('', include(router.urls)),
    path('token',TokenProvider.as_view(), name = 'token'),
]