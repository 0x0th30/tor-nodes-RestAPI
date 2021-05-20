import sqlite3

connection = sqlite3.connect('api/app/database/address.db', check_same_thread=False)

database = connection.cursor()

try:
    database.execute('CREATE TABLE ip_list (address text)')
except sqlite3.OperationalError:
    pass

def add_ban(ip):
    database.execute(f'INSERT INTO ip_list VALUES ("{ip}")')

    for row in database.execute('SELECT * FROM ip_list'):
        print(row[0])
