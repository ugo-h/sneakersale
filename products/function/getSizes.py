
from bs4 import BeautifulSoup as soup
from urllib.request import urlopen
import time

def getExistingSizes(url):
    sizes = getSizes(url).find(all)('span', {'class':'dropdown-box__value', 'data-alert':'true'})
    return sizes
    




def getSizes(url):
    content = openUrl(url)
    sizes = content.find_all('div', {'class':'dropdown-menu'})
    return sizes


def openUrl(url):
    '''Function returns html page from url
    ready for parsing '''
    uClient = urlopen(url)
    htmlPage = uClient.read()
    uClient.close()
    return soup(htmlPage, 'html.parser')


def findLink(text):
    '''Function finds a link in a string from html tag by dividing it into separate parts
    with ' " ' symbol and then searching in each division for 'http'  '''
    text = text.split('\"')
    for word in text:
        if word[0:4] =='http':
            return word


if __name__ == '__main__':
    timeStart = time.perf_counter()
    print(getSizes('https://ru.puma.com/sportivnye-tovary-dlja-muzhchin/obuv/krossovki/rs-9-8-ader-error-370110-01.html'))
    timeStop = time.perf_counter()
    print(timeStop - timeStart)