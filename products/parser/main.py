import csv
from .alikestoreParser import main as alikestoreParser
from .superstepParser import main as superstepParser
from os import path

NAME = 0
OLD_PRICE = 1
SPECIAL_PRICE = 2
LINK = 3
IMG = 4
alikestore_csv  = path.join('products', 'parser', 'alikestore.csv')
superstep_csv = path.join('products', 'parser', 'superstep.csv')
CSVS = {alikestore_csv: alikestoreParser, superstep_csv: superstepParser}
GENERAL_CSV = path.join('products', 'parser', 'general.csv')

def main():
    '''Creates list of products by 
    joining all available csv-files. 
    If file does not exist it creates it using parsing'''
    f = open(GENERAL_CSV, 'w')
    f.close()
    listOfProducts = []
    for csv_file in list(CSVS.keys()):
        print(list(CSVS.keys()))
        print(csv_file)
        print("LOADING")
        currentList = readOrParce(csv_file, CSVS[csv_file])
        print(currentList[0:10])
        listOfProducts += currentList
        print("LOADING NEXT")

    for index, product in enumerate(listOfProducts):
         write_csv(product)

def readOrParce(file, parser):
    '''if file is emply, then function creates new file
     by parsing through the website '''
    try:
        listOfProducts = readCsv(file)
        if listOfProducts == []:
            raise(FileNotFoundError)
    except(FileNotFoundError):
        parser()
        listOfProducts = readCsv(file)

    return listOfProducts

def readCsv(file):
    '''Transforms csv-file into the list of objects of the Product class '''
    listOfProducts = []
    with open (file, 'r') as f:
        reader = csv.reader(f)
        for line in reader:
            if line:
                listOfProducts.append(Product(
                            name=line[NAME],
                            oldPrice=line[OLD_PRICE],
                            specialPrice=line[SPECIAL_PRICE],
                            link=line[LINK],
                            img=line[IMG],
                            ))
    return listOfProducts


class Product(object):
    def __init__(self, name, oldPrice, specialPrice, link, img):
        self.name = name
        self.oldPrice = oldPrice
        self.specialPrice = specialPrice
        self.link = link
        self.img = img

    def __str__(self):
        return self.name

def write_csv(data):
    with open(GENERAL_CSV, 'a') as f:
        writer = csv.writer(f)
        writer.writerow((data.name,
                        data.oldPrice,
                        data.specialPrice,
                        data.link,
                        data.img,
                        ))

if __name__ =='__main__':
    main()
                