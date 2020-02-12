
from bs4 import BeautifulSoup as soup
from urllib.request import urlopen
import time


def getImage(url):
    content = openUrl(url)
    img = content.find_all('img', {'class':'gallery-item__img'}, limit=1)[0]
    return findLink('{}'.format(img))


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
    print(getImage('https://ru.puma.com/sportivnye-tovary-dlja-muzhchin/obuv/krossovki/rs-9-8-ader-error-370110-01.html'))
    timeStop = time.perf_counter()
    print(timeStop - timeStart)