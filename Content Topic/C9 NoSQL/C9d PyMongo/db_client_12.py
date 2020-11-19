import pymongo

client = pymongo.MongoClient('127.0.0.1', 27017)
db = client.get_database('entertainment')
col = db.get_collection('movies')

search1 = {'year':{'$exists':False}}
update1 = {'$set':{'year':'pending'}}
col.update_many(search1, update1)

search2 = {'year':{'$eq':1997}}
update2 = {'$unset':{'genre':''}}
col.update_many(search2, update2)

display_field = {'_id':0, 'title':1, 'genre':1, 'year':1}
cursor = col.find({}, display_field)
for doc in cursor:
    print(doc)


client.close()
