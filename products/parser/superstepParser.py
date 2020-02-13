import requests
from bs4 import BeautifulSoup
import csv
from time import time, sleep
from multiprocessing import Pool
import sys
from os import path

data_list = []


def get_html(url):
    r = requests.get(url) #Response
    return r.text         # Возвращает HTML-код страницы (url)

def get_all_data(html):
    url = 'https://www.superstep.ru'
    soup = BeautifulSoup(html, 'lxml')
    divs = soup.find('div', class_="list-content").find_all('div', itemtype="https://schema.org/Product")
    data = {}
    for div in divs:
        name = div.find('p', class_='product-name').find('a').text
        if not 'кроссовки' in name:
            continue
        a = div.find('a')
        link = url + a.get('href')
        img = url+ a.find('img').get('src')
        price = div.find('p', class_="product-double-price")
        meta = div.find_all('meta', limit=2)
        brand = meta[1].get('content')
        name = brand + ' ' + meta[0].get('content')
        old_price = price.find('span', class_='product-list-price').text.strip()
        old_price = (transformPriceToNumber(old_price))
        new_price = price.find('span', class_='product-sale-price').text.strip()
        new_price = (transformPriceToNumber(new_price)) 
        data = {
            'name': name,
            'old price': old_price,
            'special price': new_price,
            'link': link,
            'img': img,
            'brand': brand,
                }
        data_list.append(transfer(data))


# def get_page_data(html):
#     soup = BeautifulSoup(html, 'lxml')
#     try:
#         name = soup.find('h1').text.strip()
#         if name == 'Please turn JavaScript on and reload the page.':
#             name = soup.find('h1').text.strip()
#     except: 
#         name = ''
#         print('not_found')
#     try:
#         price = soup.find_all('span', class_='price')
#         old_price = price[1].text.strip()
#         special_price = price[0].text.strip()
#     except:
#         price = ''
#         print('not_found')
#     data = {'name': name,
#             'old price': old_price,
#             'special price':special_price}
#     return data

def transfer(data):
    cell = (
        data['name'],
        data['old price'],
        data['special price'],
        data['link'],
        data['img'],
        data['brand'],
                )
    print(cell[0], cell[1], '/',cell[2])
    return cell

# def make_all(url):
#     html = get_html(url)
#     data = get_page_data(html)
#     try:
#         write_csv(data)
#     except(UnicodeEncodeError):
#         data['name'] = 'empty'
#         print(url)
#         write_csv(data)

def loopUrls(url):
    urls = []
    for i in range(25):
        urls.append(url + str(i+1))
    return urls

def transformPriceToNumber(price):
    return int(''.join(price.strip().split(' ')[:2]))

def main():
    timerStart = time()
    url = 'https://superstep.ru/sale/?arrFilter_107_95876792=Y&set_filter=4&PAGEN_1='
    urls = loopUrls(url)
    all_links = []
    for u in urls:
        get_all_data(get_html(u))
    timerEnd = time()
    total = timerEnd - timerStart
    print(total)
    print(len(data_list))
    return data_list






if __name__ == '__main__':
    main()