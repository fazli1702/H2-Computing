import pymongo

client = pymongo.MongoClient('127.0.0.1', 27017)

db = client.get_database('entertainment')


databases = client.database_names()
print('The databases in the MongoDB serever:')
print(databases)

client.close()
