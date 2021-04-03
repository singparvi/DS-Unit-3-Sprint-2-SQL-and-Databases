
# -- How many passengers survived, and how many died? ok
survived = """SELECT SUM("Survived") FROM  titanic"""

# -- How many passengers were in each class? ok
each_class = """select count("Pclass") from titanic group by "Pclass";"""

# -- How many passengers survived/died within each class? ok
each_class_survived_or_died = '''SELECT "Survived"      as Survived,
       "Pclass"        as Class,
       count("Pclass") as count
FROM titanic
GROUP BY "Survived",
         "Pclass";'''

# -- What was the average age of survivors vs nonsurvivors? ok
each_class_survived_or_died ="""SELECT "Survived", avg("Age") as "Average Age" from titanic group by "Survived";"""

# -- What was the average age of each passenger class?
average_age_each_passenger_class = """SELECT "Pclass", avg("Age") as "Average Age" from titanic group by "Pclass";"""

# -- What was the average fare by passenger class? By survival?
average_fare_by_passenger_class_by_survival ="""SELECT "Pclass", avg("Fare") as "Average Fare" from titanic group by "Pclass";"""

# -- How many siblings/spouses aboard on average, by passenger class? By survival?
siblingsspouses_aboard_on_average_by_passenger_class_survival = """SELECT "Survived", "Pclass", avg("Siblings/Spouses Aboard") as "Average Siblings/Spouses Aboard" from titanic group by "Pclass", "Survived";"""


# -- How many parents/children aboard on average, by passenger class? By survival?
parentschildren_aboard_on_average_by_passenger_class_survival = """SELECT "Survived", "Pclass", avg("Parents/Children Aboard") as "Average Siblings/Spouses Aboard" from titanic group by "Pclass", "Survived";"""

# -- Do any passengers have the same name?
same_name = """select "Name" from titanic ou
where (select count(*) from titanic inr
where inr."Name" = ou."Name") > 1"""

# -- (Bonus! Hard, may require pulling and processing with Python) How many married couples were aboard the Titanic? Assume that two people (one Mr. and one Mrs.) with the same last name and with at least 1 sibling/spouse aboard are a married couple.