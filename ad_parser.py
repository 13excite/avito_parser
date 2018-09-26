from bs4 import BeautifulSoup
from requester import get_html


def get_item_ad(url):
    """
    :return ad item's block, object has type BeautifulSoup
    """
    html = get_html(url)
    soup = BeautifulSoup(html, 'lxml')
    return soup.find('div', class_='item-view')


def get_ad_header(url):
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
    ad_date = '%s %s %s' % (dirty_date[1], dirty_date[2], dirty_date[4])

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
        'id': ad_id,
        'title': title,
        'date': ad_date,
        'image_url': ad_image,
        'price': price,
        'address': address,
        'desc': description,
    }
