import requests
import sys


def get_html(url, timeout=5):
    headers = {
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q = 0.7',
        'referer': 'https://www.avito.ru/moskva',
        'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 5.1; it; rv:1.8.1.11) Gecko/20071127 Firefox/2.0.0.11',
    }
    try:
        r = requests.get(url, timeout=timeout)
        return r.text
    except requests.ConnectTimeout as err:
        print("Request error: %s" % err)
        sys.exit(1)
    except requests.ConnectionError as err:
        print("Request timeout 5 seconds with error: %s" % err)
        sys.exit(1)
