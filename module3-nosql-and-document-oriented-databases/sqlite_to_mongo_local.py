import sqlite3
import pymongo

sl_conn = sqlite3.connect('rpg_db.sqlite3')
sl_curs = sl_conn.cursor()

character_select_query = """
SELECT * FROM charactercreator_character
"""

sl_curs.execute(character_select_query)
character_results = sl_curs.fetchall()
# get ip from docker inspect docker_network

mongo_client = pymongo.MongoClient(
    'mongodb://172.18.0.3:27017/myFirstDatabase?retryWrites=true&w=majority')

rpg_collection = mongo_client.myFirstDatabase.rpg_collection
rpg_collection.drop({})

for character in character_results:
    keys = ['name', 'level', 'exp', 'hp', 'strength', 'intelligence', 'dexterity', 'wisdom']
    doc = {}
    for key, value in zip(keys, list(character[1:])):
        doc.update({key: value})
    rpg_collection.insert_one(doc)
