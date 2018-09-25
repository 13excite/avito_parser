from requester import get_html
from bs4 import BeautifulSoup


def get_items_titles(html):
    """
    :param html:
    :return: list with ads title
    """
    ads_lst = []
    soup = BeautifulSoup(html, 'html.parser')
    for el in soup.find_all("span", itemprop="name"):
        ads_lst.append(el.get_text())
    return ads_lst


def main():
    url = 'https://www.avito.ru/moskva/koshki/abissinskaya?s_trg=1007'
    print(get_items_titles(get_html(url)))


if __name__ == '__main__':
    main()