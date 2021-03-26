# Sprint 2 Module 1 Notes

1. Sqlite 
   Learn



2. Sqlite commands:
   
      SELECT count(*)
      FROM charactercreator_character
      LIMIT 10;


   SELECT *
   FROM charactercreator_character
   WHERE name is "Inve"


   SELECT *
   FROM charactercreator_character
            LEFT JOIN charactercreator_character_inventory cci
                      ON charactercreator_character.character_id = cci.character_id



    SELECT *
    FROM (SELECT *
          FROM charactercreator_character
                   LEFT JOIN charactercreator_character_inventory cci
                             ON charactercreator_character.character_id = cci.character_id) as char_inventory
             LEFT JOIN armory_item on char_inventory.item_id = armory_item.item_id) as char_inventory_item



   -- Example for Left Join
   
    '''
   ```SELECT character_id, name , rage
    FROM charactercreator_character AS cc
    LEFT JOIN charactercreator_fighter AS cf
    ON cf.character_ptr_id = cc.character_id;

-- Example for Left Join
   
    SELECT character_id, name , rage
    FROM charactercreator_character AS cc
    LEFT JOIN charactercreator_fighter AS cf
    ON cf.character_ptr_id = cc.character_id;

--This is a new line 

    SELECT character_id, name , rage
    FROM charactercreator_character AS cc
    LEFT JOIN charactercreator_fighter AS cf
    ON cf.character_ptr_id = cc.character_id;


# Module 2

PostgreSQL Commands

1. create a table

CREATE Table test_table (
id SERIAL PRIMARY KEY,
name varchar(40) NOT NULL,
data JSONB);

2. insert some data

3. Get the schema of a table

sl_curs.execute('PRAGMA table_info(charactercreator_character);').fetchall()

4. create table characters
(
    id int,
    level int,
    hp int,
    constraint characters_pk
    primary key (id)
);

5. 



drop table characters;
create table IF NOT EXISTS characters
(
    character_id int,
    name varchar(30),
    level int,
    exp int,
    hp int,
    strength int,
    intelligence int,
    dexterity int,
    wisdom int,
    constraint characters_pk
    primary key (character_id)
);

6. 

alter table characters add column is_mage bool
https://www.postgresqltutorial.com/postgresql-alter-table/

7. 



drop table characters;
drop table character_item_map;
drop table items;
create table characters
(
    character_id int,
    name         varchar(30),
    level        int,
    exp          int,
    hp           int,
    strength     int,
    intelligence int,
    dexterity    int,
    wisdom       int,
    constraint characters_pk
        primary key (character_id)
);
create table items
(
    item_id int,
    name    varchar(30),
    value   int,
    weight  int,
    constraint item_pk
        primary key (item_id)
);
create table character_item_map
(
    map_id       int,
    character_id int,
    item_id      int,
    constraint item_map_pk
        primary key (item_id),
    constraint characters_fk
        foreign key (character_id) references characters,
    constraint item_fk
        foreign key (item_id)
            references characters
)


