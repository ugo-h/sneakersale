from urllib.request import urlopen
from bs4 import BeautifulSoup as soup
import time




def createListOfSneakers():
    ''' return a list of Sneakers class objects, each of them has a title, a price, a description, a link to the product in original website, and an image of itself '''
    list_of_products = []
    urls = loopThroughPages()

    for url in urls:
        #grab the page
        page_soup = openUrl(url)
        containers = page_soup.find_all('div', {'class': 'product-item'})

        for container in containers:
            product = Sneakers(container)
            if product.oldPrice - product.specialPrice != 0:
                list_of_products.append(product)

    return list_of_products


def loopThroughPages():
    ''' we can have all information nesessary on different pages, so this function loops through pages and returns list of urls of each page '''
    urls = []
    for index in range(6):
        urls.append('https://ru.puma.com/sportivnye-tovary-dlja-muzhchin/obuv/krossovki.html?p={}'.format(index))
    return urls


def openUrl(url):
    '''Function returns html page from url
    ready for parsing '''
    uClient = urlopen(url)
    htmlPage = uClient.read()
    uClient.close()
    return soup(htmlPage, 'html.parser')


class Sneakers(object):
    def __init__(self, container):
        self.container = container
        # self.priceContainer = self.container.find_all('div', {'class': 'price-box price-final_price'}, limit=1)[0]
    
        self.titlePlusLink = self.container.find_all('a', {'class': 'product-item__name'},  limit=1)[0]
        self.title = self.titlePlusLink.text
        self.link = findLink('{}'.format(self.titlePlusLink))

        self.specialPrice = self.container.find_all('span', {'class': 'special-price'}, limit=1)[0].text
        self.specialPrice = transformPriceToNumber(self.specialPrice)

        self.oldPrice = self.container.find_all('span', {'class': 'old-price sly-old-price no-display'}, limit=1)[0].text
        self.oldPrice = transformPriceToNumber(self.oldPrice)

        self.image = findLink('{}'.format(self.container.find_all('img', limit=1)[0]))

        



    def __str__(self):
        return "{}".format(self.title)


def transformPriceToNumber(price):
    ''' Cuts of everything redundant from the price and returns an integer '''
    return transformToInt(''.join(price.strip().split()[2:4]))


def transformToInt(number):
    '''numbers in html are represented by strings and instead of the floating point may contain a coma. So in order to
    sucsessfuly transform them to integers this function cuts off  symbols after the floating point if needed '''
    try:
        number = int(number)
    except(ValueError):
        number= int(number[:-3])
    return number


def findLink(text):
    '''Function finds a link in a string from html tag by dividing it into separate parts
    with ' " ' symbol and then searching in each division for 'http'  '''
    text = text.split('\"')
    for word in text:
        if word[0:4] =='http':
            return word




if __name__ == "__main__":
    timeStart = time.perf_counter()
    list_of_products = createListOfSneakers()
    print(len(list_of_products))
    print(list_of_products[100])
    print(list_of_products[100].specialPrice)
    print(list_of_products[100].oldPrice)
    print(list_of_products[100].link)
    print(list_of_products[100].image)
    timeStop = time.perf_counter()
    print(timeStop - timeStart)
  


