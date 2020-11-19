import pymongo

client = pymongo.MongoClient('127.0.0.1', 27017)
db = client.get_database('entertainment')
col = db.get_collection('movies')

# create variable
movie1 = 'Titanic'
genre1 = 'Romance'
year1 = 1997

# inserting value using variables
##col.insert_one({'title':movie1, 'genre':genre1, 'year':year1})


list_to_add = []
list_to_add.append({'title':'Inception', 'genre':'Thiller', 'year':2010})
list_to_add.append({'title':'Avengers', 'genre':'Action', 'year':2012})
list_to_add.append({'title':'Jaws', 'genre':'Horro', 'year':1975})

col.insert_many(list_to_add)

client.close()
