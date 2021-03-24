import sqlite3

# Make a connection
conn = sqlite3.connect('rpg_db.sqlite3')
# Create a cursor
curs = conn.cursor()
character_count_query = """
SELECT *  
FROM charactercreator_character
WHERE name is 'Inve'
"""

# execute query
curs.execute(character_count_query)
results = curs.fetchall()

print(results)
