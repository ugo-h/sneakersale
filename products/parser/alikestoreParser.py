# 1 Однопоточный парсер
# 2 Замер времени
# 3 multiprocessing pool
# 4 Замер времени
# 5 Экспорт в csv

import requests
from bs4 import BeautifulSoup
import csv
from time import time, sleep
from multiprocessing import Pool
import sys
from os import path

alikestore_csv  = path.join('products', 'parser', 'alikestore.csv')


def get_html(url):
    r = requests.get(url) #Response
    return r.text         # Возвращает HTML-код страницы (url)

def get_all_links(html):
    soup = BeautifulSoup(html, 'lxml')

    divs = soup.find('ul', class_='products-grid').find_all('a', class_='product-image')
    links = []
    for div in divs:
        a = div.get('href')
        link = a
        links.append(link)
    return links

def get_page_data(html):
    soup = BeautifulSoup(html, 'lxml')
    try:
        name = soup.find('h1').text.strip()
        if name == 'Please turn JavaScript on and reload the page.':
            name = soup.find('h1').text.strip()
    except: 
        name = ''
        print('not_found')
    try:
        price = soup.find_all('span', class_='price')
        old_price = price[1].text.strip()
        old_price = transformPriceToNumber(old_price)
        special_price = price[0].text.strip()
        special_price = transformPriceToNumber(special_price)
    except:
        old_price = 0
        special_price = 0
        print('not_found')
    try:
        img = soup.find('img', id="image-0").get('src')
    except:
        img = '#'
    data = {'name': name,
            'old price': old_price,
            'special price': special_price,
            'img': img}
    return data

def write_csv(data):
    with open(alikestore_csv, 'a') as f:
        writer = csv.writer(f)
        writer.writerow((data['name'],
                        data['old price'],
                        data['special price'],
                        data['link'],
                        data['img'],))
        print(data['name'], data['old price'],'-', data['special price'], ' parsed')

def make_all(url):
    html = get_html(url)
    data = get_page_data(html)
    data['link'] = url
    try:
        write_csv(data)
    except(UnicodeEncodeError):
        data['name'] = 'empty'
        print(url)
        write_csv(data)

def transformPriceToNumber(price):
    return int(price[1:])

def main():
    f = open(alikestore_csv, 'w')
    f.close()
    timerStart = time()
    url = 'https://www.allikestore.com/default/sale/footwear-men.html?limit=all'
    all_links = get_all_links(get_html(url))
    # for index, url in enumerate(all_links):
    #     html = get_html(url)
    #     data = get_page_data(html)
    #     print(index)
    #     write_csv(data)

    with Pool(10) as p:
        p.map(make_all, all_links)
    timerEnd = time()
    total = timerEnd - timerStart
    print(total)






if __name__ == '__main__':
    main()