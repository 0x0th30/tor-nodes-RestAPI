import sqlite3
from get_ips import getAll

# realiza a conexão com o nosso banco de dados local, no diretório ""./database/address.db"
connection = sqlite3.connect('api/app/database/address.db', check_same_thread = False)          # estava apresentando erros por realizar as "queries" em outra
                                                                                              # thread, então desativei esta validação e não recebi mais erros
                                                                                              
# crio um cursor que viabiliza e possibilita a comunicação e execução de comandos e queries no nosso database                                                                                              
database = connection.cursor()


def add_ip():
    ip_list = getAll()

    for ip in ip_list:
        # nesse bloco try/catch ele verifica se foi recebido algum erro quanto a existencia de um banco de dados, caso não, ele cria um novo
        database.execute('CREATE TABLE IF NOT EXISTS ip_list (address text)')

        database.execute('INSERT OR REPLACE INTO ip_list VALUES (?)', [ip])


# este método é utilizado no arquivo "view.py" (linha 30) para receber os IP's que o usuário deseja banir
def add_ban(ip):
    # nesse bloco try/catch ele verifica se foi recebido algum erro quanto a existencia de uma tabela, caso não, ele cria uma nova
    database.execute('CREATE TABLE IF NOT EXISTS black_list (address text)')

    database.execute('INSERT OR REPLACE INTO black_list VALUES (?)', [ip])

    for row in database.execute('SELECT * FROM black_list'):
        print(row[0])


# função específica para teste
def returnAllIPs():
    show_list = list()
    for row in database.execute('SELECT * FROM ip_list'):
        show_list.append(row[0])

    return show_list


def returnAllBans():
    ban_list = list()
    for row in database.execute('SELECT * FROM black_list'):
        print(row[0])
        ban_list.append(str(row[0]))

    return ban_list
