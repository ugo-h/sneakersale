from django.urls import path
from .views import *


urlpatterns = [
    path('', productList.as_view(), name='products_url'),
    path('/brand/<str:slug>/', ProductBrand.as_view(), name='product_brand_url'),
    path('/product_detail/<str:slug>/', product_detail, name='product_details_url'),

]
