
import requests
from bs4 import BeautifulSoup
import csv
from time import time, sleep
from multiprocessing import Pool
import sys
from os import path


BRANDS = [
        'adidas',
        'Aimé Leon Dore',
        'ASICS SportStyle',
        'Clarks Originals',
        'Converse',
        'Filling Pieces',
        'Hi-Tec',
        'Jordan Brand',
        'Karhu',
        'New Balance',
        'Nike',
        'Raised by Wolves',
        'Reebok',
        'Saucony',
        'Suicoke',
        'Vans',
        'Vans Vault',
        'Y-3',
]

def get_html(url):
    r = requests.get(url) #Response
    return r.text         # Возвращает HTML-код страницы (url)

def get_all_products(html):
    soup = BeautifulSoup(html, 'lxml')
    products = soup.find_all('li', class_='item')
    return products

def get_data(product, data_list):
    try:
        a = product.find('h2', class_="product-name").find('a')
        link = a.get('href')
        name = a.text.strip()
        brand = name.split(' ')[0]
        for br in BRANDS:
            if brand in br:
                brand = br
    except: 
        link = ''
        name = ''
        brand = ''
        print('name not_found')
    try:
        price = product.find_all('p')
        old_price = float(price[1].text.strip()[1:])
        special_price = float(price[0].text.strip()[1:])
    except:
        old_price = 0
        special_price = 0
        print('price not_found')
    try:
        img = product.find('img', class_="regular_img").get('src')
    except:
        img = '#'

    data = {
        'name': name,
        'old price': old_price,
        'special price': special_price,
        'img': img,
        'brand': brand,
        'link': link,
        }
    data_list.append(transfer(data))

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

def main():
    timerStart = time()
    data_list = []
    url = 'https://www.allikestore.com/default/sale/footwear-men.html?limit=all'
    products = get_all_products(get_html(url))
    for product in products:
        get_data(product, data_list)
    timerEnd = time()
    total = timerEnd - timerStart
    print(total)
    print(len(data_list))
    return data_list



if __name__ == '__main__':
    main()