import sqlite3
import pandas as pd


# Make a connection
conn = sqlite3.connect('rpg_db.sqlite3')
# Create a cursor
curs = conn.cursor()
character_count_query = """
SELECT *
FROM charactercreator_character
         LEFT JOIN charactercreator_character_inventory cci
                   ON charactercreator_character.character_id = cci.character_id
"""

# execute query
curs.execute(character_count_query)
results = curs.fetchall()

df = pd.DataFrame(results)

print(df.head())
