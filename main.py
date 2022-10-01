import re
import datetime

import requests
from bs4 import BeautifulSoup
from decouple import config


URL = 'https://www.kijiji.ca/b-apartments-condos/city-of-toronto/'
END = 'c37l1700273'
default_image = 'https://afs.googleusercontent.com/kijiji-ca/csa-image1-large.png'

HEADERS = {
           'user-agent': config('USER_AGENT'),
           'accept': '*/*',
}


def connect():
    session = requests.Session()
    session.headers = HEADERS
    return session


def get_date(date):
    dt = datetime.datetime.today()
    if '/' not in date:
        date = int(re.findall(r'\d+', date)[0])
        t = dt - datetime.timedelta(hours=date)
        return str(t.strftime('%d/%m/%y'))
    return date


def get_blocks():
    page = int(input('Enter the number of pages to parse(max-94): '))
    items = []
    if page and 0 < page < 94:
        for i in range(1, page+1):
            res = connect().get(f'https://www.kijiji.ca/b-apartments-condos/city-of-toronto/page-{i}/' + END)
            soup = BeautifulSoup(res.text, 'lxml')
            container = soup.find_all('div', class_='search-item')
            for i in container:
                items.append({'price': i.find('div', class_='price').text.strip(),
                              'image': i.find('img').get('data-src'),
                              'published': get_date(i.find('span', class_='date-posted').text.strip()),
                              })




