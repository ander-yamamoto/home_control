import sqlite3
import datetime

database = 'data.db'

def db_user_init():
        conn = sqlite3.connect(database)
        cursor = conn.cursor()

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS user (
                        email TEXT NOT NULL PRIMARY KEY,
                        paswword TEXT NOT NULL,
                        name TEXT NOT NULL UNIQUE,
                        last_update timestamp NOT NULL
        );
        """)

        print('user db init successful')
        conn.close()
