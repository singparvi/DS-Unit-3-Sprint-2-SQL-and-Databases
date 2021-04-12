import pandas as pd
import psycopg2
import os
from dotenv import load_dotenv

load_dotenv()
USER = os.getenv('USER')
PASSWORD = os.getenv('PASSWORD')

df_titanic = pd.read_csv('titanic.csv')

# get columns names for PostGreSQL database
columns = ['Survived', 'Pclass', 'Name', 'Sex', 'Age', 'Siblings/Spouses Aboard',
           'Parents/Children Aboard', 'Fare']

# clean the names of any ' that may become an issue in passing queries
df_titanic['Name'] = df_titanic['Name'].apply(lambda x: str.replace(x, "'", ""))

# connect with Elephant PostGres DB and send a cursor
pg_conn = psycopg2.connect(dbname='mlrgffyq',
                           user=USER,
                           password=PASSWORD,
                           host='queenie.db.elephantsql.com')

# send cursor
pg_curs = pg_conn.cursor()

# check connection by sending a query to the DB and retrieve result
query = 'SELECT * FROM character_sqlite'
pg_curs.execute(query)
results = pg_curs.fetchall()
# print(results)

# connecting well. Now export create and export df_titanic line by line and ETL(Extract, Transform and Load)

# make a new table, delete if similar name table exists
query = """
        drop table IF exists titanic;
        -- All in " "  to make sure column names are capitalized
        create table titanic
        (
            "Survived"                int,
            "Pclass"                  int,
            "Name"                    varchar(90),
            "Sex"                     varchar(7),
            "Age"                     float4,
            "Siblings/Spouses Aboard" int,
            "Parents/Children Aboard" int,
            "Fare"                    float8
        );
        """
pg_curs.execute(query)

# Make a list of dataframe rows to insert line by line
new_list = []
new_list = df_titanic.values.tolist()
print(','.join(map(str, new_list[0])))

# Loop to add dataframe rows as queries
for i in range(len(df_titanic)):
    query = f"""INSERT INTO titanic ({'"' + '", "'.join(columns) + '"'}) VALUES ({"'" + "', '".join(map(str, new_list[i])) + "'"})"""
    # uncomment for verbose
    # print(f'inserting {query}')
    # print(f'OK {i} of {len(df_titanic)}')
    pg_curs.execute(query)
    pg_conn.commit()

# Test table
character_query = '''SELECT * FROM titanic'''
pg_curs.execute(character_query)
results = pg_curs.fetchall()
print(results)
print(f'COMPLETE!')

# Close connection
pg_conn.close()
print(f'CLOSED!')
