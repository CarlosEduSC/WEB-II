# database.py - gerencia a conexao com o SQLite
import os
import sqlite3

PROJECT_DIR = os.path.dirname(os.path.realpath(__file__))
# representa o banco de dados
DB_FILE = os.path.join(PROJECT_DIR, 'manter.db')
# arquivo script para gerar o banco de dados:
DB_SCHEMA = os.path.join(PROJECT_DIR,'schema.sql')

class Database:
    @staticmethod
    def create_db():
        print('Creating database')
        connection = sqlite3.connect(DB_FILE)
        with open(DB_SCHEMA) as f:
            connection.executescript(f.read())
        connection.commit()
        connection.close()

    @staticmethod
    def get_connection():
        """ abre uma conexao com o BD """
        connection = sqlite3.connect(DB_FILE)
        return connection

    @staticmethod
    def select_clientes():
        connection = sqlite3.connect(DB_FILE)
        # executa uma query SQL:
        result = connection.execute(
            "SELECT * from cliente"
        )
        for cli in result:
            print(cli)
        connection.commit()
        connection.close()

    @staticmethod
    def select_produtos():
        connection_p = sqlite3.connect(DB_FILE)
        # executa uma query SQL:
        result_p = connection_p.execute(
            "SELECT * from produtos"
        )
        for pro in result_p:
            print(pro)
        connection_p.commit()
        connection_p.close()

    @staticmethod
    def select_fornecedor():
        connection_f = sqlite3.connect(DB_FILE)
        # executa uma query SQL:
        result_f = connection_f.execute(
            "SELECT * from fornecedor"
        )
        for forn in result_f:
            print(forn)
        connection_f.commit()
        connection_f.close()

if __name__ == '__main__':
    Database.create_db()
    Database.select_clientes()
    Database.select_produtos()
    Database.select_fornecedor()
