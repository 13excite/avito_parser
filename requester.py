import requests
import sys


def get_html(url, timeout=5):
    headers = {
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q = 0.7',
        'referer': 'https://www.avito.ru/moskva',
        "cookie": "sessid=3544fa9d311620dce34d9531c9027d9f.1538042495; buyer_location_id=637640; u=2b47cb2v.1fc6nlr.fvo95xxz5s; v=1538042495; dfp_group=30; abp=0; cto_lwid=b99555c0-0238-460b-8d23-662b0915012b; f=5.88881e344776caaa4b5abdd419952845a68643d4d8df96e9a68643d4d8df96e9a68643d4d8df96e9a68643d4d8df96e94f9572e6986d0c624f9572e6986d0c624f9572e6986d0c62ba029cd346349f36c1e8912fd5a48d02c1e8912fd5a48d0246b8ae4e81acb9fa143114829cf33ca746b8ae4e81acb9fa46b8ae4e81acb9fae992ad2cc54b8aa858f6718e375efe92c93bf74210ee38d940e3fb81381f3591fed88e598638463b2da10fb74cac1eab2da10fb74cac1eab2da10fb74cac1eab2da10fb74cac1eab2da10fb74cac1eab2da10fb74cac1eab2da10fb74cac1eab2da10fb74cac1eab2da10fb74cac1eab2da10fb74cac1eab2da10fb74cac1eab2da10fb74cac1eabfdb229eec3b9ed9a0c79affd4e5f1d11162fe9fd7c8e9767f5298ef0d69a428d7d13591acbda872737863d73204ac566c9476b440e99bd57d5ae9dfec34a8041a0e292ff74cb61b0016d14fa319743b96028692b27942282685428d00dc691fa4b5b030516527c4378ba5f931b08c66a4817f2e578a4f4ecc1678a40dbd1753a3de19da9ed218fe23de19da9ed218fe2737d51816ba3af3b46e9537011e9226e983b6486c29270eb; rheftjdd=rheftjddVal; _ga=GA1.2.179796019.1538042500; _gid=GA1.2.14032698.1538042500; _ym_uid=1538042500447642228; _ym_d=1538042500; _dc_gtm_UA-2546784-1=1; _ym_isad=1; bltsr=1; is_adblock=true; crookie=xH8Q9lGno4jjJ5Fg2D7zqTkZcuNFtO7tVPaU5H+VQOqeEm4XBaxAi5LL13P/QO8FGOP0L9Iw7B9K6CgogUl+ORCmOX4=; cmtchd=MTUzODA0MjUwMjAxNw==",
        'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 5.1; it; rv:1.8.1.11) Gecko/20071127 Firefox/2.0.0.11',
    }
    try:
        r = requests.get(url, headers=headers, timeout=timeout)
        if str(r.status_code).startswith('5'):
            print("HTTP error code:", r.status_code)
            sys.exit(1)
        return r.text
    except requests.ConnectTimeout as err:
        print("Request error: %s" % err)
        sys.exit(1)
    except requests.ConnectionError as err:
        print("Request timeout 5 seconds with error: %s" % err)
        sys.exit(1)
