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

dict = {}

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

# character documents --> loop through items item character match add
# run the query on sqlite database
curs_sl.execute(join_query)
results = curs_sl.fetchall()

# print(results)

# now make a connection with mongo db and test connection
mongo_client = pymongo.MongoClient(
    'mongodb+srv://singparvi:qwerty12345@cluster0.l0ldo.mongodb.net/myFirstDatabase?retryWrites=true&w=majority')
# rpg_collection = mongo_client.myFirstDatabase.rpg_collection
# # test mongodb connection by sending a query
# results = rpg_collection.find().count()
# print(results)

# go to the correct collection
rpg_collections = mongo_client.myFirstDatabase.rpg_collections

# drop any existing information in the collection
rpg_collections.drop({})

keys = ['character_id', 'name', 'level', 'exp', 'hp', 'strength', 'intelligence', 'dexterity', 'wisdom', 'items',
        'weapons', 'id', 'character_id:1', 'item_id', 'item_id:1', 'name:1', 'value', 'weight', 'item_ptr_id', 'power']

item_keys = ['item_id', 'item_id:1', 'name:1', 'value', 'weight', 'item_ptr_id', 'power']

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
# mongo_document_key = ['character_id', 'name', 'level', 'exp', 'hp', 'strength', 'intelligence', 'dexterity', 'wisdom',
#                       'items', 'weapons']
#
# character = charactercreator_character[0]
# inventory = charactercreator_character_inventory[0]
#

i = 0
character_id = 'Null'
for character in charactercreator_character:
    dict = {}
    print('Item', i)
    # see the current character_id
    # character_id = character[0]
    # for key, value in zip(keys, list(character)):
    # print(character[0])
    # character_id = -1
    # previous_id = 0
    items = []
    weapons = []
    # j = 0
    matches = [x for x in results if x[0] == character[0]]
    for matches_iter in matches:
        if (matches_iter[16]) == None:
            print('Item ID: that is not None', matches_iter[16])
            items.append(matches_iter[13])
        else:
            print(matches_iter[16], 'WEAPON!!!')
            weapons.append(matches_iter[13])


    # print(character[0], ' items are', items)

    dict.update({'character_id': character[0], 'name': character[1],
                     'level': character[2], 'exp': character[3],
                     'hp': character[4], 'strength': character[5],
                     'intelligence': character[6], 'dexterity': character[7],
                     'wisdom': character[8], 'items': items, 'weapons': weapons})
    print(dict)

    # i = i + 1
    # if i > 6:
    #     break

        # doc.update({key, value[0][j]})

    # print(dict)
    rpg_collections.insert_one(dict)
# character_id =-1
# previous_id = 0
# i = 0
# make_list = []
# for character in results:
#     # print(character[0])
#     character_id = character[0]
#     if (character_id>0) and (character_id == previous_id):
#         print('loop', i, ' match found')
#         make_list.append(character[13])
#     else:
#         print('loop:else', i )
#         make_list.append(character[13])
#
#     previous_id = character_id
#     print(make_list)
#     i = i + 1
#     if i > 5:
#         break


# test = mongo_client.test


# dict.update({'character_id': charactercreator_character[0][0], 'name': 'new',
#              'level': charactercreator_character[0][2], 'exp': charactercreator_character[0][3],
#              'hp': charactercreator_character[0][4], 'strength': charactercreator_character[0][5],
#               'intelligence': charactercreator_character[0][6], 'dexterity': charactercreator_character[0][7],
#              'wisdom': charactercreator_character[0][8], 'items': '', 'weapons': ''})
# dict.update({'character_id': 2, 'name': 'new',
#              'level': charactercreator_character[0][2], 'exp': charactercreator_character[0][3],
#              'hp': charactercreator_character[0][4], 'strength': charactercreator_character[0][5],
#              'intelligence': charactercreator_character[0][6], 'dexterity': charactercreator_character[0][7],
#              'wisdom': charactercreator_character[0][8], 'items': '', 'weapons': ''})




