import requests
from bs4 import BeautifulSoup
import csv
from time import time, sleep
from multiprocessing import Pool
import sys
from os import path

superstep_csv = path.join('products', 'parser', 'superstep.csv')


def get_html(url):
    r = requests.get(url) #Response
    return r.text         # Возвращает HTML-код страницы (url)

def get_all_data(html):
    url = 'https://superstep.ru'
    soup = BeautifulSoup(html, 'lxml')
    divs = soup.find('div', class_="list-content").find_all('div', itemtype="https://schema.org/Product")
    data = {}
    for div in divs:
        name = div.find('p', class_='product-name').find('a').text.strip()
        if not 'кроссовки' in name:
            continue
        a = div.find('a')
        link = url + a.get('href')
        img = url+ a.find('img').get('src')
        price = div.find('p', class_="product-double-price")
        old_price = price.find('span', class_='product-list-price').text.strip()
        old_price = (transformPriceToNumber(old_price))
        new_price = price.find('span', class_='product-sale-price').text.strip()
        new_price = (transformPriceToNumber(new_price)) 
        data = {'name': name,
                'old price': old_price,
                'special price': new_price,
                'link': link,
                'img': img,}
        write_csv(data)

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

def write_csv(data):
    with open(superstep_csv, 'a') as f:
        writer = csv.writer(f)
        writer.writerow((data['name'],
                        data['old price'],
                        data['special price'],
                        data['link'],
                        data['img'],))
        print(data['name'], data['old price'],'-', data['special price'], ' parsed')

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
    f = open(superstep_csv, 'w')
    f.close()
    timerStart = time()
    url = 'https://superstep.ru/sale/?arrFilter_107_95876792=Y&set_filter=4&PAGEN_1='
    urls = loopUrls(url)
    all_links = []
    for u in urls:
        # print(u)
        get_all_data(get_html(u))
    # with Pool(10) as p:
    #     p.map(make_all, all_links)
    timerEnd = time()
    total = timerEnd - timerStart
    print(total)






if __name__ == '__main__':
    main()