import sqlite3
import pymongo

# start the connection with sqlite db and send a cursor
conn_sl = sqlite3.connect('rpg_db.sqlite3')
curs_sl = conn_sl.cursor()

# importing charactercreator_character_inventory and storing as a list
query = 'SELECT * FROM charactercreator_character'
curs_sl.execute(query)
charactercreator_character = curs_sl.fetchall()
#
# # importing charactercreator_character_inventory and storing as a list
query = 'SELECT * FROM charactercreator_character_inventory'
curs_sl.execute(query)
charactercreator_character_inventory = curs_sl.fetchall()
#
# # importing armory_item and storing as a list
query = 'SELECT * FROM armory_item'
curs_sl.execute(query)
armory_item = curs_sl.fetchall()
#
# # importing armory_weapon and storing as a list
query = 'SELECT * FROM armory_weapon'
curs_sl.execute(query)
armory_weapon = curs_sl.fetchall()

keys = ['character_id', 'name', 'level', 'exp', 'hp', 'strength', 'intelligence', 'dexterity', 'wisdom', 'items',
        'weapons', 'id', 'character_id:1', 'item_id', 'item_id:1', 'name:1', 'value', 'weight', 'item_ptr_id', 'power']

join_query = '''
SELECT *
FROM (SELECT *
      FROM (
               SELECT *
               FROM charactercreator_character AS cc
                        LEFT JOIN charactercreator_character_inventory as cci
                                  ON cc.character_id = cci.character_id) as char_inventory
               LEFT JOIN armory_item on char_inventory.item_id = armory_item.item_id) as char_inventory_item
         LEFT JOIN armory_weapon on char_inventory_item.item_id = armory_weapon.item_ptr_id
         '''

# run the query on sqlite database
curs_sl.execute(join_query)

# make a single table to see get all the relational db in one
results = curs_sl.fetchall()

# now make a connection with mongo db and test connection
mongo_client = pymongo.MongoClient(
    'mongodb+srv://singparvi:qwerty12345@cluster0.l0ldo.mongodb.net/myFirstDatabase?retryWrites=true&w=majority')

# go to the correct collection
rpg_collections = mongo_client.myFirstDatabase.rpg_collections

# drop any existing information in the collection
rpg_collections.drop({})

# required format:-

# mongo_document = {
#   "name": <VALUE>,
#   "level": <VALUE>,
#   "exp": <VALUE>,
#   "hp": <VALUE>,
#   "strength": <VALUE>,
#   "intelligence": <VALUE>,
#   "dexterity": <VALUE>,
#   "wisdom": <VALUE>,
#   "items": [
#     <ITEM NAME>,
#     <ITEM NAME>
#   ],
#   "weapons" [
#     <ITEM NAME>,
#     <ITEM NAME>
#   ]
# }
#
i = 0
character_id = 'Null'
for character in charactercreator_character:
    dict = {}
    items = []
    weapons = []

    matches = [x for x in results if x[0] == character[0]]

    # for loop to iterate, find and place the items and weapons in suitable lists
    for matches_iter in matches:
        if (matches_iter[16]) == None:
            # uncomment for verbose
            # print('Item ID: that is not None', matches_iter[16])
            items.append(matches_iter[13])
        else:
            # print(matches_iter[16], 'WEAPON!!!')
            weapons.append(matches_iter[13])

    # make a single dictionary item one by one to push to mongo
    dict.update({'name': character[1],
                 'level': character[2], 'exp': character[3],
                 'hp': character[4], 'strength': character[5],
                 'intelligence': character[6], 'dexterity': character[7],
                 'wisdom': character[8], 'items': items, 'weapons': weapons})
    # uncomment for verbose
    # print('Item', i)
    # print(dict)
    # i = i + 1

    # push to db mongo
    rpg_collections.insert_one(dict)

# close connections
conn_sl.close()
mongo_client.close()
