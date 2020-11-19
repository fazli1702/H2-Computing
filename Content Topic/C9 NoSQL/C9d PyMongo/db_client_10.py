import pymongo

client = pymongo.MongoClient('127.0.0.1', 27017)
db = client.get_database('entertainment')
col = db.get_collection('movies')


field_display = {'_id':0, 'title':1, 'genre':1, 'year':1}

query1 = col.find({'genre':'Sci-fi'}, field_display)
print('All Sci-fi movies:')
for doc in query1:
    print(doc)

print(f'There are {query1.count()} Sci-fi movies')
print('\n\n\n')

criteria = {'$and':[{'genre':'Sci-fi'}, {'year':{'$gt':2015}}]}

query2 = col.find(criteria, field_display)
print('All Sci-fi moveis later than 2015:')
for doc in query2:
    print(doc)

client.close()
