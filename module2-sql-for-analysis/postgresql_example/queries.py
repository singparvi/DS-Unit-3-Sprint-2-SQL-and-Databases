"""
Queries file for SQLite to PostGreSQL pipeline

"""
# PostGreSQL queries

CREATE_TABLE = '''
    CREATE TABLE test_table2new (
    id SERIAL PRIMARY KEY,
    name varchar(40) NOT NULL,
    number INTEGER
    );
'''

INSERT_DATA = '''
    INSERT INTO test_table2new(name, number)
    VALUES
    (
    'A row name', 
    6
    ),    
    (
    'Another row', 
    72
    );
'''

SELECT_ALL = '''
    SELECT * FROM test_table2new;
'''

CREATE_CHARACTER_TABLE ='''
    CREATE TABLE IF NOT EXISTS charactercreator_character(
    character_id SERIAL PRIMARY KEY,
    name varchar(30),
    level integer,
    exp integer,
    hp integer,
    strength integer,
    intelligence integer,
    dexterity integer,
    wisdom, integer)
'''

# SQLite queries

ROW_COUNTS = """
    SELECT COUNT(*) FROM charactercreator_character;
    """

GET_CHARACTERS = """
    SELECT * FROM charactercreator_character;
    """