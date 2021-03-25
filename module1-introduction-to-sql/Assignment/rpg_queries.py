import sqlite3
from queries import *

# connect with the DB
conn = sqlite3.connect('rpg_db.sqlite3')
# send a cursor
curs = conn.cursor()
# query
# query = '''SELECT *
# FROM charactercreator_character'''

# execute the query
curs.execute(TOTAL_CHARACTERS)
# fetch all and store in an object to get results
results = curs.fetchall()
print(results[0][0])



