from os.path import basename
from rest_framework import routers
from django.urls import path, include
from ferretic.views import *


router = routers.DefaultRouter()
router.register('user', User_view, basename='user')
router.register('employee', Employee_view, basename='employee')
router.register('vendor', Vendor_view, basename='vendor')
router.register('client', Client_view, basename='client')
router.register('product', Product_view, basename='product')
router.register('order', Order_view, basename='order')
router.register('purchase', Purchase_view, basename='purchase')
router.register('invoice', Invoice_view, basename='invoice')
router.register('sold', Sold_view, basename='sold')


urlpatterns = [
    path('', include(router.urls)),
    path('token',TokenProvider.as_view(), name = 'token'),
]