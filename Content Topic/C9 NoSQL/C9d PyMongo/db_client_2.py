import pymongo

client = pymongo.MongoClient('127.0.0.1', 27017)

db = client.get_database('entertainment')
col = db.get_collection('movies')

collections = db.collection_names('entertainment')
print('The collections in the entertainment db are:')
print(collections)

client.close()
