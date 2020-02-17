from django.views import View
from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from django.core.paginator import Paginator
from products.models import Product, Brand
from products.function.getImage import *
from products.function.sneakerScraper import *
from .load_products import refreshDatabase
from time import time
        
class objectListMixin(View):
    product_model = None

    def get(self, request, slug=None):
        
        order = request.GET.get('order')
        if order == None:
            order = 'title'

        
        if order[0] == '-':
                print('- YOS')
                order = order[1:]
                order_type = ''
        else:    
                order = f'-{order}'
                order_type = '-'

        print(order, order[1:])
        brandList = Brand.objects.all()
        if not slug:
            products_list = self.product_model.order_by(order)
        else: 
            products_list = self.product_model.filter(brand__iexact=slug).order_by(order)


        paginator = Paginator(products_list, 20)
        page_number = request.GET.get('page')

        page_obj = paginator.get_page(page_number)
        is_paginated = page_obj.has_other_pages()

        context = {
        'page_object':  page_obj,
        'is_paginated': is_paginated,
        'previous': self.get_previous(page_obj),
        'next': self.get_next(page_obj),
        'order': order,
        'brandList': brandList,
        'order_type':order_type,
        }
        print(order)
        return render(request, 'products/products.html', context)


    def get_previous(self, page_obj):
        if page_obj.has_previous():
            previous_url = f'?page={page_obj.previous_page_number()}'
        else:
            previous_url = ''
        return previous_url

    def get_next(self, page_obj):
        if page_obj.has_next():
            next_url = f'?page={page_obj.next_page_number()}'
        else:
            next_url = ''
        return next_url