import pymongo
import json

client = pymongo.MongoClient('127.0.0.1', 27017)
db = client.get_database('entertainment')
col = db.get_collection('games')

with open('games.json') as json_file:
    data = json.load(json_file)
    col.insert_many(data)

cursor = col.find()
for doc in cursor:
    print(doc)

client.close()


