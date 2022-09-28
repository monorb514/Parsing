import requests
from bs4 import BeautifulSoup
from decouple import config


URL = 'https://www.kijiji.ca/b-apartments-condos/city-of-toronto/'
END = 'c37l1700273'

HEADERS = {
           'user-agent': config('USER_AGENT'),
           'accept': '*/*',
}


def connect():
    session = requests.Session()
    session.headers = HEADERS
    return session


def get_page(url, page=None):
    params = {}
    if page and page > 1:
        params['page-'] = page
    res = connect().get(url+END, params=params)
    return res.text


def get_blocks():
    items = []
    text = get_page(url=URL, page=2)
    soup = BeautifulSoup(text, 'lxml')
    container = soup.find_all('div', class_='search-item')
    for i in container:
        items.append({'price': i.find('div', class_='price').text.strip(),
                      'image': i.find('img').get('data-src'),
                      'date': i.find('span', class_='date-posted').text.strip(),
                      })
    for i in items[:3]:
        print(i)


get_blocks()
