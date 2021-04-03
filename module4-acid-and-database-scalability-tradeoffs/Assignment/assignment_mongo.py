import pymongo

# now make a connection with mongo db and test connection
mongo_client = pymongo.MongoClient(
    'mongodb+srv://singparvi:qwerty12345@cluster0.l0ldo.mongodb.net/myFirstDatabase?retryWrites=true&w=majority')
rpg_collections = mongo_client.myFirstDatabase.rpg_collections

# How many total Characters are there?
print('How many total Characters are there?: ', rpg_collections.count())
print("\n")

# How many total Items? ok
items_list = []
for document in rpg_collections.find():
    # pprint.pprint(document)
    items_list.append(document['items'])

# flatten list
flat_list = [item for sublist in items_list for item in sublist]

# get the number of unique in the items
print('How many total Items?: ', len(set(flat_list)))
print("\n")

# How many of the Items are weapons? How many are not? ok
items_list = []
for document in rpg_collections.find():
    # pprint.pprint(document)
    items_list.append(document['weapons'])

# flatten list
flat_list = [item for sublist in items_list for item in sublist]

# get the number of unique in the items
print('How many of the Items are weapons? ', len(set(flat_list)))
print("\n")

# How many Items does each character have? (Return first 20 rows)
print('How many Items does each character have? (Return first 20 rows)')
items_list = []
i = 0
for document in rpg_collections.find():
    # pprint.pprint(document)
    if i < 20:
        i = i + 1
        print('Item ', i, document['name'], 'has ', len(document['items']), 'items')
        print()

# How many Weapons does each character have? (Return first 20 rows)
print('How many Weapons does each character have? (Return first 20 rows)')
items_list = []
i = 0
for document in rpg_collections.find():
    # pprint.pprint(document)
    if i < 20:
        i = i + 1
        print('Item ', i, document['name'], 'has ', len(document['weapons']), 'items')
        print()

# On average, how many Items does each Character have?
items_list = []
i = 0
for document in rpg_collections.find():
    # pprint.pprint(document)
    items_list.append(document['items'])
# flatten the list
flat_list = [item for sublist in items_list for item in sublist]
print('On average, how many Items does each Character have? ', len(flat_list) / rpg_collections.count())

# On average, how many Weapons does each character have?
items_list = []
i = 0
for document in rpg_collections.find():
    # pprint.pprint(document)
    items_list.append(document['weapons'])
# flatten the list
flat_list = [item for sublist in items_list for item in sublist]
print('On average, how many Items does each Character have? ', len(flat_list) / rpg_collections.count())
