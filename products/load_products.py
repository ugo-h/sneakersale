from .models import Product
from .parser.alikestoreParser import main as alikestoreParser
from .parser.superstepParser import main as superstepParser
import csv
from os import path

NAME = 0
OLD_PRICE = 1
SPECIAL_PRICE = 2
LINK = 3
IMG = 4
BRAND = 5


def refreshDatabase():
    products_list = Product.objects.all()
    products_list.delete()
    n=0
    alikestoreProducts = alikestoreParser()
    superstepProducts = []
    # superstepProducts = superstepParser()
    parsed_products = alikestoreProducts + superstepProducts
    for line in parsed_products:
            if line:
                n+=1
                Product.objects.create(
                    title=line[NAME], 
                    slug=n, link=line[LINK],
                    oldPrice=line[OLD_PRICE], 
                    price=line[SPECIAL_PRICE], 
                    img=line[IMG],
                    brand=line[BRAND],
                    )    


if __name__ == '__main__':
    refreshDatabase()
