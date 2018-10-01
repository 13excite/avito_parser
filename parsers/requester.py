import requests


def get_html(url, timeout=5):
    headers = {
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q = 0.7',
        'referer': 'https://www.avito.ru/moskva',
        "cookie": "sessid=cb6448715ea06dfce96856f81d65d0e5.1538088674; buyer_location_id=637640; u=2b47v9xn.uimb20.fvoverrxe0; v=1538088675; dfp_group=89; abp=0; cto_lwid=b395e19c-7b75-4700-94d3-0ae9c4df85ee; rheftjdd=rheftjddVal; _ga=GA1.2.124710004.1538088678; _gid=GA1.2.1151927620.1538088678; _ym_uid=1538088678652055538; _ym_d=1538088678; _dc_gtm_UA-2546784-1=1; f=5.0c4f4b6d233fb90636b4dd61b04726f147e1eada7172e06c47e1eada7172e06c47e1eada7172e06c47e1eada7172e06cb59320d6eb6303c1b59320d6eb6303c1b59320d6eb6303c147e1eada7172e06c8a38e2c5b3e08b898a38e2c5b3e08b890df103df0c26013a0df103df0c26013a2ebf3cb6fd35a0ac0df103df0c26013a8b1472fe2f9ba6b9b0c8390560c7eb9e433be0669ea77fc059c9621b2c0fa58f897baa7410138ead3de19da9ed218fe23de19da9ed218fe23de19da9ed218fe23de19da9ed218fe23de19da9ed218fe23de19da9ed218fe23de19da9ed218fe23de19da9ed218fe23de19da9ed218fe23de19da9ed218fe23de19da9ed218fe23de19da9ed218fe207b7a18108a6dcd6f8ee35c29834d631c9ba923b7b327da7b1df3c26d9ecabd3ec88e9b07619d3955e61d702b2ac73f79bc9e600674c16dc2ccc198612346d2f762e952a876cf423a3ec383b8904a3be8732de926882853a9d9b2ff8011cc827c4d07ec9665f0b70915ac1de0d03411203fba73019678b1ebc12ae8a54d9afc82da10fb74cac1eab2da10fb74cac1eabac3d5e3f056ea51e93519700b0b0e7d789c0e3d5ba80b84c; _ym_isad=1; bltsr=1; is_adblock=true",
        'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 5.1; it; rv:1.8.1.11) Gecko/20071127 Firefox/2.0.0.11',
    }
    try:
        r = requests.get(url, headers=headers, timeout=timeout)
        if str(r.status_code).startswith('5'):
            print("HTTP error code:", r.status_code)
        return r.text
    except requests.ConnectTimeout as err:
        print("Request error: %s" % err)
    except requests.ConnectionError as err:
        print("Request timeout 5 seconds with error: %s" % err)
