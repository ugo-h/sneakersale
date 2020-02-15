from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
from django.core.paginator import Paginator
from products.models import Product
from products.function.getImage import *
from products.function.sneakerScraper import *
from .load_products import refreshDatabase
from time import time



# Create your views here.

class productList(View):

    def get(self, request):
        products_list = Product.objects.all()
        paginator = Paginator(products_list, 20)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        is_paginated = page_obj.has_other_pages()
        if page_obj.has_previous():
            previous_url = f'?page={page_obj.previous_page_number()}'
        else:
            previous_url = ''
        if page_obj.has_next():
            next_url = f'?page={page_obj.next_page_number()}'
        else:
            next_url = ''
        context = {
        'page_object':  page_obj,
        'is_paginated': is_paginated,
        'previous': previous_url,
        'next': next_url,
        # 'page': page_obj,
        }
        return render(request, 'products/products.html', context)

    def post(self, request):
        
        refreshDatabase()
        products_list = Product.objects.all()
        return render(request, 'products/products.html', {'products_list': products_list,})


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
