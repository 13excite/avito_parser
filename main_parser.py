from requester import get_html
from bs4 import BeautifulSoup
import re


def get_ad_info(html):
    soup = BeautifulSoup(html, 'html.parser')
    ads = soup.find('div', class_='catalog-list').find_all('div', class_='item_table')
    print(ads)
    for ad in ads:
        title_and_link = ad.find('div', class_='description').find('h3')
        title = title_and_link.text.strip()
        add_link = 'https://avito.ru' + title_and_link.find('a').get('href')
        try:
            thumb_link = "https:%s" % re.findall(r"\/\/\d+.*jpg", str(ad.find('div', class_='item-slider-image')))[0]
        except Exception:
            thumb_link = ''
        try:
            price = ad.find('div', class_='about').text.strip()
        except Exception:
            price = ''
        try:
            address = ad.find('div', class_='data').find_all('p')[-1].text.strip()
        except Exception:
            address = ''
        print(title)
        print(add_link)
        print(price)
        print(address)
        print(thumb_link)


#def degug_get(html):
#   soup = BeautifulSoup(html, 'html.parser')
#    ads = soup.find('div', class_='catalog-list')
#    print(ads)

def get_pages_count(html):
    soup = BeautifulSoup(html, 'html.parser')
    pages = soup.find('div', class_='pagination-pages').find_all('a', class_='pagination-page')[-1].get('href')
    last_page_num = pages.split('=')[1].split('&')[0]
    return int(last_page_num)

def main():
    url = 'https://www.avito.ru/moskva/koshki/abissinskaya?p=1'
    page_html = get_html(url)
    print(page_html)
    #print(get_items_titles())
    #get_ad_info(page_html)
    #get_pages_count(page_html)
    #degug_get(page_html)


if __name__ == '__main__':
    main()