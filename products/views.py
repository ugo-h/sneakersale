from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
from django.core.paginator import Paginator
from products.models import Product, Brand
from products.function.getImage import *
from products.function.sneakerScraper import *
from .load_products import refreshDatabase
from time import time
from .utils import objectListMixin
        


# Create your views here.

class productList(objectListMixin):
    product_model = Product.objects

    def post(self, request):
        
        refreshDatabase()
        products_list = Product.objects.all()
        return render(request, 'products/products.html', {'products_list': products_list,})


class ProductBrand(objectListMixin):
    product_model = Product.objects

    

def product_detail(request, slug):
    details = Product.objects.get(slug__iexact=slug)
    if details.detailedImage ==  '':
        # geetImageFrom = link.split('.')[1] + 'GetImage'
        try:    
            details.detailedImage = getImage(details.link)
        except:
            details.detailedImage = details.img
        details.save()
    return render(request, 'products/product_detail.html', {'details': details})
