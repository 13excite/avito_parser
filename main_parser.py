import csv
from requester import get_html
from bs4 import BeautifulSoup
import re


def get_ad_info(html, write_to_file='cats_avito.csv'):
    """
    parsing pages in xml format page by page and writing data to csv file
    """
    # parser working only xml format, if init BeautifulSoup with second args html.parser, then
    # we get only first element from item_table(html has a error in markup)
    soup = BeautifulSoup(html, 'lxml')
    ads = soup.find('div', class_='catalog-list').find_all('div', class_='item_table')
    for ad in ads:
        title_and_link = ad.find('div', class_='description').find('h3')
        title = title_and_link.text.strip()
        ad_link = 'https://avito.ru' + title_and_link.find('a').get('href')
        try:
            # match id from ad link url
            ad_id = re.match('.*\_(\d+$)', ad_link).group(1)
        except Exception:
            ad_id = ''
        try:
            # get ad thumbs url, need for upload in storage
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
        ad_data = {
            'id':       ad_id,
            'title':    title,
            'price':    price,
            'address':  address,
            'ad_url':   ad_link,
            'ad_url':  thumb_link,
        }
        write_to_csv(write_to_file, ad_data)


def get_pages_count(html):
    soup = BeautifulSoup(html, 'html.parser')
    pages = soup.find('div', class_='pagination-pages').find_all('a', class_='pagination-page')[-1].get('href')
    last_page_num = pages.split('=')[1].split('&')[0]
    return int(last_page_num)


def write_to_csv(filename, data, mode='a'):
    try:
        with open(filename, mode) as f:
            w = csv.writer(f, delimiter=';')
            w.writerow((data['id'], data['title'], data['price'],
                       data['address'], data['ad_url'], data['ad_url']))
    except csv.Error as err:
        print('file {}: {}'.format(filename, err))
    except Exception as err:
        print("Unexpected error writing cvf file: ", err)


def main():
    # get total pages count from first page
    url = 'https://www.avito.ru/moskva/koshki/abissinskaya?p=1'
    page_html = get_html(url)
    #last_page = get_pages_count(page_html)
    get_ad_info(page_html)
    #get_pages_count(page_html)


if __name__ == '__main__':
    main()