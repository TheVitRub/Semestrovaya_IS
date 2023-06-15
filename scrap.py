import requests
from bs4 import BeautifulSoup
import csv
import os
from datetime import datetime
import re
def scrape_page(soup, quotes):
    # retrieving all the quote <div> HTML element on the page
    url = []
    next_li_element = soup.find_all('div', class_='daynews__item')
    for element in next_li_element:
        href = element.find('a', href=True)['href']
        url.append(href)
    return url
def scrape_new(soup):
    try:
        h1 = soup.find('h1',class_='hdr__inner').text
        f = open('name_news', 'r', encoding="utf-8")
        i = 0
        for line in f:
            if h1 == line:
                i += 1
        f.close()
        if i != 1:

            path = os.getcwd()
            path1 = path
            path = path + '/' + 'Lib' + '/' + 'list' + '/' + 'Новости' + '/' + str(datetime.now().date())
            path1 = os.getcwd()
            path1 = path1 + '/' + 'Lib' + '/' + 'list' + '/' + 'Новости' + '/' + 'teglist'
            f = open(path1, 'r', encoding="utf-8")
            c = str(datetime.now().date())
            o = 0
            for line in f:
                if line == c:
                    o += 1
            f.close()

            if o == 0:
                f = open(path1, 'a', encoding="utf-8")
                f.write(str(datetime.now().date()) + '\n')
                f.close()
            if os.path.exists(path):
                None
            else:
                os.mkdir(path)
            if os.path.isfile(path + '/' + 'teglist'):
                f = open(path + '/' + 'teglist', 'r', encoding="utf-8")
                z = 0
                for i in f:
                    if i == h1 + '\n':
                        z += 1
                f.close()
                if z == 0:
                    f = open(path + '/' + 'teglist', 'a', encoding="utf-8")
                    f.write(h1 + '\n')
                    f.close()
            else:
                f = open(path + '/' + 'teglist', 'w', encoding="utf-8")
                f.write(h1 + '\n')
                f.close()

            opt = re.sub(r'[^\w\s]', '', h1)
            path1 = path + '/' + opt
            f = open(path1, 'w', encoding="utf-8")
            pp = soup.find_all('div', class_='article__intro meta-speakable-intro')
            res = soup.find('p').text
            f.write(res + '\n')

            dd = soup.find_all('div', class_='article__item article__item_alignment_left article__item_html')
            rest = ''
            for list in dd:
                a = list.text
                rest = rest + '\n' + a
            f.write(rest)
            f.close()
            f = open('name_news', 'r', encoding="utf-8")
            z = 0
            for i in f:
                if i == h1 + '\n':
                    z += 1
            f.close()
            f = open('name_news', 'a', encoding="utf-8")
            if z == 0:
                f.write(h1 + "\n")

            f.close()
    except AttributeError:
        print("Слажный сайт,насяльника!")

    # the url of the home page of the target website
def scrap():
    base_url = 'https://news.mail.ru'

    # defining the User-Agent header to use in the GET request below
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36'
    }

    # retrieving the target web page
    page = requests.get(base_url, headers=headers)

    soup = BeautifulSoup(page.text, 'html.parser')
    quotes = []
    url = scrape_page(soup, quotes)

    for i in url:

        page_1 = requests.get(i, headers=headers)
        soup_1 = BeautifulSoup(page_1.text, 'html.parser')
        scrape_new(soup_1)

scrap()