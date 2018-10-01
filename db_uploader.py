import csv
from datetime import datetime, timedelta
from db.db_executor import DbExecutor, get_auth
import random
import re


def random_time_generator():
    return datetime.strptime('{} {}'.format(random.randint(1, 23), random.randint(1, 60)), '%H %M').strftime("%H:%M")


def convert_to_date_format(date_string):
    sepember_pattern = re.compile('.*сентября.*')
    today_pattern = re.compile('.*сегодня.*')
    yesterday_pattern = re.compile('.*вчера.*')

    if sepember_pattern.match(date_string):
        day = date_string.split()[0]
        try:
            date = "2018-09-%s %s" % (day, random_time_generator() )
        except ValueError as err:
            print(date_string)
            print("Error: ", err)
            date = datetime.now().strftime("%Y-%m-%d %H-%M")
        print(date)
    elif today_pattern.match(date_string):
        date = "%s %s" % (datetime.now().strftime("%Y-%m-%d"), date_string.split()[2])
        print(date)
    elif yesterday_pattern.match(date_string):
        date = "%s %s" % (datetime.strftime(datetime.now() - timedelta(1), '%Y-%m-%d'), date_string.split()[2])
        print(date)
    else:
        date = datetime.now().strftime("%Y-%m-%d %H:%M")
        print(date)


def csv_reader(file):
    try:
        with open(file, 'r') as f:
            reader = csv.reader(f, delimiter=";")
            for row in reader:
               # "INSERT INTO testtable VALUES (%s, );" % ()
                convert_to_date_format(row[2])
    except IOError as err:
        print('I/O Error: ', err)
    except Exception as err:
        print('Unexpected error: ', err)


def main():
    csv_reader('total_full_ad.csv')


if __name__ == '__main__':
    main()