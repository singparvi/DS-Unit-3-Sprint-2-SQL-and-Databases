import sqlite3

# open an sqlite3 connection and connect
sl_conn = sqlite3.connect("northwind_small.sqlite3")

sl_curs = sl_conn.cursor()

# Queries
expensive_items = (
    """SELECT * FROM Product order by UnitPrice DESC Limit 20;"""
)
avg_hire_age = (
    """SELECT avg(HireDate - Employee.BirthDate)
    as average_age from Employee;"""
)
avg_age_by_city = """SELECT city, avg(HireDate - Employee.BirthDate)
as average_age from Employee group by City"""

print(
    "What are the ten most expensive items (per unit price) in the database? ",
    sl_curs.execute(expensive_items).fetchall(),
)
print('\n')
print(
    "What is the average age of an employee at the time of their hiring? ",
    sl_curs.execute(avg_hire_age).fetchall()[0][0],
)
print('\n')
print(
    "How does the average age of employee at hire vary by city? ",
    sl_curs.execute(avg_age_by_city).fetchall(),
)
print('\n')

# With join

ten_most_expensive = """SELECT Id, ProductName, SupplierId, CategoryId, QuantityPerUnit,
       UnitPrice, UnitsInStock, UnitsOnOrder, ReorderLevel, Discontinued
from (SELECT * FROM Product
LEFT JOIN Supplier ON Product.SupplierId = Supplier.Id)
order by UnitPrice DESC Limit 10;"""

largest_category = """
SELECT CategoryName, max(frequency)
from (SELECT CategoryName, count(CategoryName)
as frequency from (SELECT * FROM Product
LEFT JOIN Category ON Product.CategoryId = Category.Id)
group by CategoryName);"""

most_territories = """select Id, firstname, lastname,
max(count_distinct_TerritoryId)
from (select *, count(count_TerritoryId)
as count_distinct_TerritoryId
from (select *, count(TerritoryId)
as count_TerritoryId
            from (SELECT *
                  FROM Employee
LEFT JOIN EmployeeTerritory ON Employee.Id = EmployeeTerritory.EmployeeId
                  group by TerritoryId)
            group by firstname, TerritoryId)
      group by firstname);"""

print(
    "What are the ten most expensive items (per unit price) "
    "in the database and their suppliers? ",
    sl_curs.execute(ten_most_expensive).fetchall(),
)
print('\n')
print(
    "What is the largest category (by number of unique products in it)? ",
    sl_curs.execute(largest_category).fetchall(),
)
print('\n')
print(
    "Who's the employee with the most territories? ",
    sl_curs.execute(most_territories).fetchall(),
)

# close connection
sl_conn.close()
