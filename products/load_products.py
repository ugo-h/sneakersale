from .models import Product
from .parser.main import main as parser
import csv
from os import path

NAME = 0
OLD_PRICE = 1
SPECIAL_PRICE = 2
LINK = 3
IMG = 4
GENERAL_CSV = path.join('products', 'parser', 'general.csv')

def refreshDatabase():
    f = open(GENERAL_CSV, 'w')
    f.close()
    # try:
    #     f = open(GENERAL_CSV, 'r')
    #     if f == []:
    #         f.close()
    #         raise(FileNotFoundError)
    #     f.close()
    # except(FileNotFoundError):
    parser()

    products_list = Product.objects.all()
    products_list.delete()
    n=0
    with open (GENERAL_CSV, 'r') as f:
        reader = csv.reader(f)
        for line in reader:
            if line:
                n+=1
                Product.objects.create(
                    title=line[NAME], 
                    slug=n, link=line[LINK],
                    oldPrice=line[OLD_PRICE], 
                    price=line[SPECIAL_PRICE], 
                    img=line[IMG],
                    )   

    f = open(GENERAL_CSV, 'w')
    f.close()
if __name__ == '__main__':
    refreshDatabase()
