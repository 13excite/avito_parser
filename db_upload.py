import argparse
import configparser
import psycopg2
import sys


def _get_auth(file=None):
    data = {"user": "", "pass": "", "db": ""}
    if file:
        try:
            reader = configparser.ConfigParser()
            reader.read(file)
            data['user'] = reader.get('postgres', 'user')
            data['pass'] = reader.get('postgres', 'pass')
            data['db'] = reader.get('postgres', 'db')
        except configparser.NoSectionError as err:
            print("Error config parse:  %s" % err)
            sys.exit(1)
        except Exception as err:
            print("Error: %s" % err)
            sys.exit(1)
    else:
        print("Config file not set")
        sys.exit(1)
    return data


class DbExecutor:
    def __init__(self, auth_data):
        conn_string = "host=127.0.0.1 dbname=%s user=%s password=%s" % (auth_data['db'], auth_data['user'], auth_data['pass'])
        try:
            self.conn = psycopg2.connect(conn_string)
            self.cur = self.conn.cursor()
        except psycopg2.Error as err:
            print("Error %d: %s" % (err.args[0], err.args[1]))
            sys.exit(1)

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.conn:
            self.conn.close()

    def query_select(self, query):
        try:
            self.cur.execute(query)
            return self.cur.fetchall()
        except psycopg2.Error as err:
            print("Error exec query: ", err)

    def query_insert(self, query):
        try:
            self.cur.execute(query)
        except psycopg2.Error as err:
            print("Error exec query: ", err)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-c', '--config', type=str, help='usage -c /path/dbconf.ini ', required=True)
    args = parser.parse_args()

    auth_dict = _get_auth(args.config)
    db = DbExecutor(auth_dict)
    print(db.query_select('select * from testtable'))

    db.query_insert('insert into testtable VALUES (4, \'zsssszzzzz\');')
    print(db.query_select('select * from testtable'))


if __name__ == '__main__':
    main()
