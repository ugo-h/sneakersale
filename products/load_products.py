from .models import Product
from .function.sneakerScraper import *


def refreshDatabase():
        sneakers_list = createListOfSneakers()[:30]
        products_list = Product.objects.all()
        products_list.delete()
        n=0
        for product in sneakers_list:
            n+=1
            Product.objects.create(
                title=product.title, 
                slug=n, link=product.link,
                oldPrice=product.oldPrice, 
                price=product.specialPrice, 
                img=product.image,
                 )

if __name__ == '__main__':
    refreshDatabase()
