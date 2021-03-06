from bs4 import BeautifulSoup
from requester import get_html
import re


def get_breed(url='https://www.avito.ru/moskva/koshki'):
    """
    :param url: url all cat's category 'https://www.avito.ru/moskva/koshki?s_trg=3'
    :return: dict with cats breed and url
    dict description: key=cat breed(in ru-RU), value=url to cat breed from key
    """
    html = get_html(url)
    soup = BeautifulSoup(html, 'lxml')
    try:
        breed_block = soup.find('div', class_='catalog-counts__row').find_all('a')
        breed_urls_dict = {}
        for tag_a in breed_block:
            breed_url = re.search('^\/.*\?', str(tag_a.get('href'))).group()
            breed_name = tag_a.get('title')
            breed_urls_dict[breed_name] = 'https://avito.ru' + breed_url + 'p=%s'
        return breed_urls_dict
    except Exception as err:
        print("Zabanili")
        print('Error: ', err)
