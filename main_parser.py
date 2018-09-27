import csv
import re
import time
from breed_parser import get_breed  #не используется, дергаем захардкоженный линк
from requester import get_html
from bs4 import BeautifulSoup
import sys


def get_base_info(html, breed, write_to_file='cats_avito.csv'):
    """
    parsing pages in xml format page by page and writing data to csv file
    """
    # parser working only xml format, if init BeautifulSoup with second args html.parser, then
    # we get only first element from item_table(html has a error in markup)
    soup = BeautifulSoup(html, 'lxml')
    try:
        ads = soup.find('div', class_='catalog-list').find_all('div', class_='item_table')
        for ad in ads:
            try:
                title_and_link = ad.find('div', class_='description').find('h3')
            except Exception:
                title_and_link = ''
            try:
                title = title_and_link.text.strip()
            except Exception:
                title = ''
            try:
                ad_link = 'https://avito.ru' + title_and_link.find('a').get('href')
            except Exception:
                ad_link = ''
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
            try:
                description = ad.find('meta', itemprop='description').get('content')
            except:
                description = ''
            ad_data = {
                'id':       ad_id,
                'title':    title,
                'price':    price,
                'address':  address,
                'ad_url':   ad_link,
                'thb_url':  thumb_link,
                'description': description,
                'breed':    breed,
            }
            write_to_csv(write_to_file, ad_data)
    except Exception as err:
        print("Zabanili")
        print('Error: ', err)


def get_pages_count(html):
    """
    :return: last page number from selected category"
    """
    soup = BeautifulSoup(html, 'html.parser')
    try:
        pages = soup.find('div', class_='pagination-pages').find_all('a', class_='pagination-page')[-1].get('href')
        last_page_num = pages.split('=')[1].split('&')[0]
        return int(last_page_num)
    except Exception as err:
        print('Zabanili', err)


def write_to_csv(filename, data, mode='a'):
    try:
        with open(filename, mode) as f:
            w = csv.writer(f, delimiter=';')
            w.writerow((data['id'], data['title'], data['price'], data['ad_url'], data['address'],
                        data['ad_url'], data['thb_url'], data['description'], data['breed']))
    except csv.Error as err:
        print('file {}: {}'.format(filename, err))
    except Exception as err:
        print("Unexpected error writing cvf file: ", err)


def get_cats_breed(html):
    pass


def start_sleep(request_count, seconds, message):
    if request_count % 5 == 0:
        print(message, request_count)
        print("SLEEEEP: ", seconds)
        time.sleep(seconds)


def main():
    # get breed urls
    # около 2к запроса банят, надо слипать на 1500 хз на сколько
    hardcode_dict_get_breed = {
            'Абиссинская': 'https://avito.ru/moskva/koshki/abissinskaya?p=%s',
            'Бенгальская': 'https://avito.ru/moskva/koshki/bengalskaya?p=%s',
            'Британская': 'https://avito.ru/moskva/koshki/britanskaya?p=%s',
            'Бурманская': 'https://avito.ru/moskva/koshki/burmanskaya?p=%s',
            'Девон-рекс': 'https://avito.ru/moskva/koshki/devon-reks?p=%s',
            'Европейская': 'https://avito.ru/moskva/koshki/evropeyskaya?p=%s',
            'Канадский сфинкс': 'https://avito.ru/moskva/koshki/kanadskiy_sfinks?p=%s',
            'Корниш-рекс': 'https://avito.ru/moskva/koshki/kornish-reks?p=%s',
            'Курильский бобтейл': 'https://avito.ru/moskva/koshki/kurilskiy_bobteyl?p=%s',
            'Мейн-кун': 'https://avito.ru/moskva/koshki/meyn-kun?p=%s',
            'Невская маскарадная': 'https://avito.ru/moskva/koshki/nevskaya_maskaradnaya?p=%s',
            'Ориентальная': 'https://avito.ru/moskva/koshki/orientalnaya?p=%s',
            'Персидская': 'https://avito.ru/moskva/koshki/persidskaya?p=%s',
            'Русская голубая': 'https://avito.ru/moskva/koshki/russkaya_golubaya?p=%s',
            'Сибирская': 'https://avito.ru/moskva/koshki/sibirskaya?p=%s',
            'Турецкая ангора': 'https://avito.ru/moskva/koshki/turetskaya_angora?p=%s',
            'Уральский рекс': 'https://avito.ru/moskva/koshki/uralskiy_reks?p=%s',
            'Шотландская': 'https://avito.ru/moskva/koshki/shotlandskaya?p=%s',
            'Экзотическая': 'https://avito.ru/moskva/koshki/ekzoticheskaya?p=%s',
            'Другая': 'https://avito.ru/moskva/koshki/drugaya?p=%s',
    }
    #for breed, breed_url in get_breed().items():
    req_count = 0
    for breed, breed_url in hardcode_dict_get_breed.items():
        first_breed_page = breed_url % '1'
        req_count += 1
        #sleep
        print('FIRST SLEEEP 8')
        time.sleep(8)
        #данных много, чтобы суметь за день дернуть все, будет парсить по 2-е страницы из категории
        #last_page = get_pages_count(get_html(first_breed_page))

        start_sleep(req_count, 181, 'SlEEEEEEP INCOMING')

        for page_num in range(1, 2):
            req_count += 1
            #sleep 5min
            start_sleep(req_count, 183, 'SlEEEEEEP INCOMING')
            generic_url = breed_url % page_num
            #one more sleep 10 seconds
            print('SECOND SLEEEEP 10 sec')
            time.sleep(10)
            get_base_info(get_html(generic_url), breed, write_to_file='testtest.csv')






    # get total pages count from first page
    #url = 'https://www.avito.ru/moskva/koshki/abissinskaya?p=1'
    #last_page = get_pages_count(get_html(url))

    # need add dynamic cat breed
    #default_url = 'https://www.avito.ru/moskva/koshki/abissinskaya?p=%s'

    #for page_num in range(1, last_page + 1):
    #    generic_url = default_url % page_num
    #    get_base_info(get_html(generic_url))


if __name__ == '__main__':
    main()
