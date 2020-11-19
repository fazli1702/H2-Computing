import pymongo

client = pymongo.MongoClient('127.0.0.1', 27017)
db = client.get_database('entertainment')
col = db.get_collection('movies')

# create variable
movie1 = 'Titanic'
genre1 = 'Romance'
year1 = 1997

# inserting value using variables
col.insert_one({'title':movie1, 'genre':genre1, 'year':year1})

client.close()
