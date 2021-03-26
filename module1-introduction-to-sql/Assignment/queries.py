

'''
TOTAL_CHARACTERS: How many total Characters are there?
TOTAL_SUBCLASS: How many of each specific subclass?
TOTAL_ITEMS: How many total Items?
WEAPONS: How many of the Items are weapons?
NON_WEAPONS: How many of the items are not weapons?
CHARACTER_ITEMS: How many Items does each character have? (Return first 20 rows)
CHARACTER_WEAPONS: How many Weapons does each character have? (Return first 20 rows)
AVG_CHARACTER_ITEMS: On average, how many Items does each Character have?
AVG_CHARACTER_WEAPONS: On average, how many Weapons does each character have?
'''

TOTAL_CHARACTERS = '''
SELECT COUNT(name)
FROM charactercreator_character;'''
# 302

TOTAL_SUBCLASS = '''
SELECT * from
(SELECT COUNT(has_pet) as count
FROM charactercreator_mage
UNION ALL
SELECT COUNT(is_sneaking) as count
FROM charactercreator_thief
UNION ALL
SELECT COUNT(using_shield) as count
FROM charactercreator_cleric
UNION ALL
SELECT COUNT(using_shield) as count
FROM charactercreator_fighter);
'''
# 302

TOTAL_ITEMS = '''
SELECT COUNT(item_id)
FROM armory_item;
'''
# 174

WEAPONS = '''
SELECT COUNT(item_ptr_id)
FROM armory_weapon
'''


NON_WEAPONS = '''
SELECT COUNT(*)
FROM (SELECT item_ptr_id
      FROM armory_item ai
               LEFT JOIN armory_weapon aw
                         ON aw.item_ptr_id = ai.item_id
      WHERE aw.power IS NULL)
'''

# CHARACTER_ITEMS = '''
# SELECT COUNT(*)
# FROM (SELECT item_ptr_id
#       FROM armory_item ai
#                LEFT JOIN armory_weapon aw
#                          ON aw.item_ptr_id = ai.item_id
#       WHERE aw.power IS NULL)

CHARACTER_ITEMS = '''SELECT COUNT (*)
FROM (SELECT *
      FROM charactercreator_character_inventory cci
               INNER JOIN charactercreator_character cc
                          ON cci.character_id = cc.character_id)
GROUP BY character_id LIMIT 20'''


CHARACTER_WEAPONS = '''SELECT COUNT (*), character_id
FROM (SELECT *
      FROM (SELECT *
            FROM (SELECT *
                  FROM charactercreator_character_inventory cci
                           INNER JOIN charactercreator_character cc
                                      ON cci.character_id = cc.character_id) as char_inventory
                     INNER JOIN armory_item ai ON char_inventory.item_id = ai.item_id) as char_inventory_armory
               INNER JOIN armory_weapon aw ON char_inventory_armory.item_id = aw.item_ptr_id) GROUP BY character_id ORDER BY 1 DESC'''

AVG_CHARACTER_ITEMS = '''


'''

