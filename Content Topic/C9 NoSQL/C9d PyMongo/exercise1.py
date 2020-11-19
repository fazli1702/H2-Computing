import pymongo

title = input('Movie title:')
year = int(input('Year of movie:'))

client = pymongo.MongoClient('127.0.0.1', 27017)
db = client.get_database('entertainment')
col = db.get_collection('movies')

col.insert_one({'title':title, 'year':year})

cursor = col.find()

for doc in cursor:
    print(doc)

client.close()


