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