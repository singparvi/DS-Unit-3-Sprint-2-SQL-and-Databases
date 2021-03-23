# import the library
import sqlite3

# # instantiate a connection to the database
# conn = sqlite3.connect('rpg_db.sqlite3')
# # create a cursor (pointer in the database) may have multiple cursors in the DB
# curs = conn.cursor()
# # execute a query using the cursor
# query = 'SELECT COUNT(*) FROM armory_item;'
# # query = 'tables;'
#
# curs.execute(query)

import sqlite3
conn = sqlite3.connect('rpg_db.sqlite3')
curs = conn.cursor()
query = 'SELECT COUNT(*) FROM armory_item;'
curs.execute(query )