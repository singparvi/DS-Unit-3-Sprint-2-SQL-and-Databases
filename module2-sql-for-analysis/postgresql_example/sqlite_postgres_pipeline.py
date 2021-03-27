"""
Basic SQLite to PostGreSQL Data Pipeline
"""
import psycopg2
import sqlite3
from queries import *

# Connecting to PostGresDB
conn = psycopg2.connect(dbname='mlrgffyq',
                        user='mlrgffyq',
                        password='O6SgFeUVSIUk1q0cvOhV4IM6vsyrSRmS',
                        host='queenie.db.elephantsql.com')

# create a cursor
pg_curs = conn.cursor()

# Connecting to SQLite DB
sl_conn = sqlite3.connect('rpg_db.sqlite3')
sl_curs = sl_conn.cursor()


def execute_query(curs, query):
    results = curs.execute(query)
    return results.fetchall()


def populate_pg_character_table(pg_curs, characters_list):
        for character in characters_list:
            insert_statement = """
            """



get_characters_list = execute_query(sl_curs, GET_CHARACTERS)


if __name__ == '__main__':
    execute_query(pg_curs, CREATE_CHARACTER_TABLE)
    get_characters = execute_query(sl_curs, GET_CHARACTERS)
    populate_pg_character_table(pg_curs, get_characters)



