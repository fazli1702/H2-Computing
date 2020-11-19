import pymongo

client = pymongo.MongoClient('127.0.0.1', 27017)
db = client.get_database('entertainment')
col = db.get_collection('movies')

display_field = {'_id':0, 'title':1, 'genre':1, 'year':1}
criteria = {'$and':[{'genre':'Horror'}, {'year':{'$lt':2000}}]}
query3 = col.find(criteria, display_field)

print('All the movies before 2000:')
for doc in query3:
    print('Title:', doc.get('title'))
    print('Genre:', doc.get('genre'))
    print('Year:', doc.get('year'))

print(f'There are {query3.count()} movies.')

client.close()
