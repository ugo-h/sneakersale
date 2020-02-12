from django.urls import path
from .views import *


urlpatterns = [
    path('', productList.as_view(), name='products_url'),
    path('/product_detail/<str:slug>/', product_detail, name='product_details_url')

]
