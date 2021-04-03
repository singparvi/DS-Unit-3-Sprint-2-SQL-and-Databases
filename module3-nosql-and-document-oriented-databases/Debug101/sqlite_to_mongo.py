import sqlite3
import pymongo
import pdb

character_select_query = """
SELECT * FROM charactercreator_character"""
conn = sqlite3.connect('rpg_db.sqlite3')
curs = conn.cursor()

results = curs.execute(character_select_query)

mongo_conn = pymongo.mongo_client.MongoClient(
    'mongodb+srv://singparvi:qwerty12345@cluster0.l0ldo.mongodb.net/myFirstDatabase?retryWrites=true&w=majority')
# mongo_conn = pymongo.mongo_client.MongoClient(
#     'mongodb://localhost:27017/test?retryWrites=true&w=majority')

rpg_collection = mongo_conn.myFirstDatabase.rpg_collection
rpg_collection.drop({})

keys = ['level', 'name', 'strength', 'exp', 'wisdom', 'intelligence']
for result in results:
    result = result[1:]
    doc = {}
    for key, value in zip(keys, result):
        doc.update({key: value})
        breakpoint()
    rpg_collection.insert_one(doc)

conn.close()
mongo_conn.close()