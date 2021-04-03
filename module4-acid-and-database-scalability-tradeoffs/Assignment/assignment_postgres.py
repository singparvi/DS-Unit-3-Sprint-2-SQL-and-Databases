import psycopg2
from postgres_queries import *

# make the connection with the elephant postgres
pg_conn = psycopg2.connect(
    'postgres://mlrgffyq:O6SgFeUVSIUk1q0cvOhV4IM6vsyrSRmS@queenie.db.elephantsql.com:5432/mlrgffyq')

# send cursor
pg_curs = pg_conn.cursor()

# Test query
test_query = """ select * from titanic"""

pg_curs.execute(test_query)
results = pg_curs.fetchall()

pg_curs.execute(survived)
print('How many passengers survived, and how many died? ', pg_curs.fetchall()[0][0])

pg_curs.execute(each_class)
print('How many passengers were in each class? ', pg_curs.fetchall())

pg_curs.execute(each_class_survived_or_died)
print('How many passengers survived/died within each class? ', pg_curs.fetchall())

pg_curs.execute(average_age_each_passenger_class)
print('What was the average age of each passenger class? ', pg_curs.fetchall())

pg_curs.execute(average_fare_by_passenger_class_by_survival)
print('What was the average age of survivors vs nonsurvivors? ', pg_curs.fetchall())

pg_curs.execute(siblingsspouses_aboard_on_average_by_passenger_class_survival)
print('What was the average age of each passenger class? ', pg_curs.fetchall())

pg_curs.execute(parentschildren_aboard_on_average_by_passenger_class_survival)
print('What was the average fare by passenger class? By survival? ', pg_curs.fetchall())

pg_curs.execute(same_name)
print('How many siblings/spouses aboard on average, by passenger class? By survival? ', pg_curs.fetchall())
