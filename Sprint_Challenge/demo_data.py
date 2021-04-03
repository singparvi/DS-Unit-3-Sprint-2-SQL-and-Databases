import sqlite3

# open an sqlite3 connection and connect
sl_conn = sqlite3.connect('demo_data.sqlite3')

sl_curs = sl_conn.cursor()

# Queries
drop_table = """
DROP TABLE IF EXISTS demo;
"""
sl_curs.execute(drop_table)
create_table_query = """

CREATE TABLE demo
(
    s varchar(1) PRIMARY KEY,
    x varchar(1),
    y varchar(1)

);"""
sl_curs.execute(create_table_query)

insert_query_1 = """insert into demo(s, x, y) values ("'g'", 3, 9);"""
sl_curs.execute(insert_query_1)
sl_conn.commit()
insert_query_2 = """insert into demo(s, x, y) values ("'v'", 5, 7);"""
sl_curs.execute(insert_query_2)
sl_conn.commit()
insert_query_3 = """insert into demo(s, x, y) values ("'f'", 8, 7);"""
sl_curs.execute(insert_query_3)
sl_conn.commit()

row_count = """SELECT COUNT(*) FROM demo;"""
xy_at_least_5 = """SELECT COUNT(*) FROM demo where x > 4 and y > 4;"""
unique_y = """SELECT COUNT(DISTINCT y) from demo;"""

print(sl_curs.execute(row_count).fetchall()[0][0])
print(sl_curs.execute(xy_at_least_5).fetchall()[0][0])
print(sl_curs.execute(unique_y).fetchall()[0][0])

# close connection
sl_conn.close()
