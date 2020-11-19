import pymongo

client = pymongo.MongoClient('127.0.0.1', 27017)
db = client.get_database('entertainment')
col = db.get_collection('movies')

#insert one document
col.insert_one({'title':'Star Wars', 'genre':'Sci-fi'})

#show dbs
databases = client.database_names()
print('The databases in the MonogDB server are:')
print(databases)

#show collections
collections = db.collection_names('entertainment')
print('The collections in the entertainment db are:')
print(collections)


client.close()
