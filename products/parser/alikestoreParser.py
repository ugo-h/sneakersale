
import requests
from bs4 import BeautifulSoup
import csv
from time import time, sleep
from multiprocessing import Pool
import sys
from os import path

data_list = []
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
        brand = name.split(' ')[0]
        for br in BRANDS:
            if brand in br:
                brand = br
    except: 
        name = ''
        brand = ''
        print('name not_found')
    try:
        price = soup.find_all('span', class_='price')
        old_price = float(price[1].text.strip()[1:])
        special_price = float(price[0].text.strip()[1:])
    except:
        old_price = 0
        special_price = 0
        print('price not_found')
    try:
        img = soup.find('img', id="image-0").get('src')
    except:
        img = '#'

    data = {
        'name': name,
        'old price': old_price,
        'special price': special_price,
        'img': img
        }
    return data

def transfer(data):
    cell = (
        data['name'],
        data['old price'],
        data['special price'],
        data['link'],
        data['img']
        )
    print(cell[0], cell[1], '/',cell[2])
    return cell

def make_all(url):
    html = get_html(url)
    data = get_page_data(html)
    data['link'] = url
    try:
        data_list.append(transfer(data))
    except(UnicodeEncodeError):
        data['name'] = 'empty'
        print(url)
        data_list.append(transfer(data))

def main():
    global data_list
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
    return data_list


if __name__ == '__main__':
    main()