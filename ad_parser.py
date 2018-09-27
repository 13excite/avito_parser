import argparse
import csv
import time
from bs4 import BeautifulSoup
from requester import get_html


def get_item_ad(url):
    """
    :return ad item's block, object has type BeautifulSoup
    """
    html = get_html(url)
    try:
        soup = BeautifulSoup(html, 'lxml')
        return soup.find('div', class_='item-view')
    except Exception as err:
        print('Errror ', err)
        print('one more try')
        get_html(url)


def get_ad_info(url, breed):
    view_header_html = get_item_ad(url)
    try:
        price = view_header_html.find('div', class_='price-value').text.strip()
    except Exception:
        price = ''
    title = view_header_html.find('div', class_='title-info-main').text.strip()

    # parse and convert date and id
    ad_info = view_header_html.find('div', class_='title-info-metadata-item').text.strip()
    ad_id = ad_info.split(', ')[0].strip('№ ')
    dirty_date = ad_info.split(', ')[1].split(' ')
    try:
        ad_date = '%s %s %s' % (dirty_date[1], dirty_date[2], dirty_date[4])
    except Exception:
        ad_date = ''

    ad_image = 'https:%s' % view_header_html.find('div', class_='gallery-img-frame').get('data-url')
    try:
        address = view_header_html.find('span', class_='item-map-address').text
    except Exception:
        address = ''
    try:
        description = view_header_html.find('div', class_='item-description-text').find('p').text
    except Exception:
        description = ''
    return {
        'id':           ad_id,
        'title':        title,
        'date':         ad_date,
        'image_url':    ad_image,
        'price':        price,
        'address':      address,
        'desc':         description,
        'breed':        breed
    }


def write_to_csv(data, filename='parser_ad.csv', mode='a'):
    try:
        with open(filename, mode) as f:
            w = csv.writer(f, delimiter=';')
            w.writerow((data['id'],  data['title'], data['date'], data['image_url'],
                        data['price'], data['address'], data['desc'], data['breed']))
            print('write data')
    except csv.Error as err:
        print('file {}: {}'.format(filename, err))
    except Exception as err:
        print("Unexpected error writing cvf file: ", err)

    return "Error opening file"


def start_sleep(request_count, seconds, message):
    if request_count % 7 == 0:
        print(message, request_count)
        print("SLEEEEP: ", seconds)
        time.sleep(seconds)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-f', '--file', required=True, help='usage -f file.txt for reading file')
    args = parser.parse_args()
    try:
        with open(args.file, 'r') as f:
            reader = csv.reader(f, delimiter=";")
            req_count = 0
            for row in reader:
                req_count += 1
                start_sleep(req_count, 181, 'SLEEEEEP')
                write_to_csv(get_ad_info(row[1], row[3]))
                print("SLEEP 1sec")
                time.sleep(2)

    except IOError:
        return "Error opening file"


if __name__ == '__main__':
    main()

