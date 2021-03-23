import sqlite3


# connect to the database using a function
def connect_to_db(db='rpg_db.sqlite3'):
    """
    This is a function that takes in the file name and connect to the DB using sqlite3
    :param db:
    :return:
    """
    return sqlite3.connect(db)
