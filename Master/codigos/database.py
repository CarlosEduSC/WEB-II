import os
import sqlite3

PROJECT_DIR = os.path.dirname(os.path.realpath(__file__))
DB_FILE = os.path.join(PROJECT_DIR, 'db/manter.db')
DB_SCHEMA = os.path.join(PROJECT_DIR,'db/schema.sql')

class Database:

    @staticmethod
    def create_db():
        print('Creating database')
        connection = sqlite3.connect(DB_FILE)
        with open(DB_SCHEMA) as f:
            connection.executescript(f.read())
        connection.commit()
        connection.close()