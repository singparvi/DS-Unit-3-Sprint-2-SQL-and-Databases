import os

import pymongo
import sqlite3

# from dotenv import load_dotenv
#
# load_dotenv()
#
# MONGO_DB_USER =
# MONGO_DB_PASS =

client = pymongo.MongoClient('mongodb+srv://singparvi:qwerty12345@cluster0.l0ldo.mongodb.net/myFirstDatabase?retryWrites=true&w=majority')

db = client.test