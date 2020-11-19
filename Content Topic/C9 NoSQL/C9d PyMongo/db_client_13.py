import pymongo

client = pymongo.MongoClient('127.0.0.1', 27017)
db = client.get_database('entertainment')
col = db.get_collection('movies')

cursor = col.find()
for doc in cursor:
    print(doc)

print(f'There are {col.count()} movies.')

search1 = {'year':2010}
col.delete_one(search1)

search2 = {'genre':'Romance'}
col.delete_many(search2)

print(f'Now, there are {col.count()} movies.')

client.close()
