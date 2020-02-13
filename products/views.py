from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
from products.models import Product
from products.function.getImage import *
from .load_products import refreshDatabase
from time import time



# Create your views here.

class productList(View):
    is_activated = False
    def get(self, request):
        self.is_activated = False
        products_list = Product.objects.all()
        return render(request, 'products/products.html', {'products_list': products_list,})

    def post(self, request):
        print(request.POST)
        refreshDatabase()
        products_list = Product.objects.all()
        return render(request, 'products/products.html', {'products_list': products_list,})


def product_detail(request, slug):
    details = Product.objects.get(slug__iexact=slug)
    # if details.detailedImage ==  'n':
    #     details.detailedImage = getImage(details.link)
    #     details.save()
    # else:
    details.detailedImage = details.img
    return render(request, 'products/product_detail.html', {'details': details})
