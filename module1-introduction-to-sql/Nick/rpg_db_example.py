import sqlite3
# from query import GET_CHARACTERS, GET_CHARACTERS_NAME

# connect to the database using a function
def connect_to_db(db_name='rpg_db.sqlite3'):
    """
    This is a function that takes in the file name and connect to the DB using sqlite3
    :param db_name:takes in the name of the database
    :return: connect object
    """
    return sqlite3.connect(db_name)


def execute_query(cursor, query):
    cursor.execute(query)
    return cursor.fetchall()


GET_CHARACTERS = """
    SELECT *
    FROM charactercreator_character;
"""
if __name__ == '__main__':
    # Connect to DB
    conn = connect_to_db()
    # Create cursor
    curs = conn.cursor()
    # Execute the query
    results = execute_query(curs, GET_CHARACTERS)
    print(results[0])
