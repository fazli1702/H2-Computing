import pymongo
'''
The program displays only the first occurence documents
in the "movies" collection"
'''


client = pymongo.MongoClient('127.0.0.1', 27017)
db = client.get_database('entertainment')
col = db.get_collection('movies')

cursor = col.find()

for doc in cursor:
    print(doc)

client.close()
