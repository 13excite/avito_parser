import argparse
import csv
from datetime import datetime, timedelta
from db.db_executor import DbExecutor, get_auth
import random
import re
import uuid


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
    elif today_pattern.match(date_string):
        date = "%s %s" % (datetime.now().strftime("%Y-%m-%d"), date_string.split()[2])
    elif yesterday_pattern.match(date_string):
        date = "%s %s" % (datetime.strftime(datetime.now() - timedelta(1), '%Y-%m-%d'), date_string.split()[2])
    else:
        date = (datetime.now() - timedelta(minutes=15)).strftime("%Y-%m-%d %H:%M")
    return date


def csv_reader(file):
    try:
        with open(file, 'r') as f:
            reader = csv.reader(f, delimiter=";")
            for row in reader:
                if row[0]:
                    id = row[0]
                else:
                    id = uuid.uuid1().fields[0]
                title = row[1]
                date = str(convert_to_date_format(row[2]))
                img_url = row[3]
                if row[4]:
                    price = row[4]
                else:
                    price = 'NULL'
                address = row[5]
                desc = row[6].replace("'", "")
                breed = row[7]
                query = "INSERT INTO items (id, title, start_date, img_url, price, address, description, breed)" \
                        "VALUES (%s, \'%s\', \'%s\', \'%s\', \'%s\', \'%s\', \'%s\', \'%s\' );" % (id, title, date, img_url, price, address, desc, breed)

                yield query
    except IOError as err:
        print('I/O Error: ', err)
    except Exception as err:
        print('Unexpected error: ', err)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-c', '--config', type=str, help='usage -c /path/dbconf.ini ', required=True)
    args = parser.parse_args()

    auth_dict = get_auth(args.config)
    db = DbExecutor(auth_dict)

    for q in csv_reader('total_full_ad.csv'):
        db.query_insert(q)


if __name__ == '__main__':
    main()
