from .models import Product
from .function.sneakerScraper import *


def refreshDatabase():
    sneakers_list = createListOfSneakers()[:30]
    return sneakers_list
if __name__ == '__main__':
    snl = refreshDatabase()
    print(snl[0])
    print(snl[1].specialPrice)
