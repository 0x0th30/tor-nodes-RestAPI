import sqlite3

connection = sqlite3.connect('address.db')

database = connection.cursor()

database.execute('CREATE TABLE ip_list (address text)')
database.execute('INSERT INTO ip_list VALUES ("10.10.11.30")')
database.execute('INSERT INTO ip_list VALUES ("10.10.11.35")')
database.execute('INSERT INTO ip_list VALUES ("10.10.11.40")')
database.execute('INSERT INTO ip_list VALUES ("10.10.11.45")')


for row in database.execute('SELECT * FROM ip_list'):
    print(row[0])