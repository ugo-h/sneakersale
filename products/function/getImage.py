
import requests
from bs4 import BeautifulSoup
import time
image_classes = {
    'allikestore':('','gallery-image visible'),
    'superstep':('https://superstep.ru/','product-slider__img js-product-current-img'),
}

def getImage(url):
    html = get_html(url)
    soup = BeautifulSoup(html, 'lxml')
    shopName = (url.split('.')[1])
    print()
    print(url)
    print()
    print(shopName)
    print()
    image =  parse_image(soup, shopName)
    print(image)
    print(image_classes[shopName][1])
    image = image_classes[shopName][0] + image
    print()
    print(image)
    print()
    return  image

def get_html(url):
    r = requests.get(url)
    return r.text

def parse_image(soup, shopName):
    if shopName == 'superstep':
        time.sleep(3)
        print( soup.find('div', class_="product-container").find_all('img') )
    else:
        return soup.find('img', class_=image_classes[shopName][1]).get('src')



if __name__ == '__main__':
    getImage()