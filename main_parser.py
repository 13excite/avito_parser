from requester import get_html
from bs4 import BeautifulSoup


def get_items_titles(html):
    """
    :param html:
    :return: list with ads title
    """
    soup = BeautifulSoup(html, 'html.parser')
    print(soup.find_all(itemprop="name"))


def main():
    url = 'https://www.avito.ru/moskva/koshki/abissinskaya?s_trg=1007'
    print(get_items_titles(get_html(url)))


if __name__ == '__main__':
    main()