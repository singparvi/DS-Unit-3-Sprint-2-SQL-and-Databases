import sqlite3
import pandas as pd

df = pd.read_csv('buddymove_holidayiq.csv')

conn = sqlite3.connect('buddymove_holidayiq.sqlite3')

# uncomment
# df.to_sql('review', con=conn)

curs = conn.cursor()

query1 = 'SELECT COUNT(*) FROM review'

curs.execute(query1)
results = curs.fetchall()
print('Number of rows: ', results[0][0])

query2 = '''SELECT COUNT(*)
FROM review
WHERE (Nature > 100) and (Shopping > 100)'''

curs.execute(query2)
results = curs.fetchall()
print('Number of review with Nature and Shopping more than 100: ', results[0][0])
