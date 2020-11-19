import json
import pymongo

try:
    client = pymongo.MongoClient('127.0.0.1', 27017)
    print('Connected successfully')
except:
    print('Could not connect to MongoDB')


    

## task 1

db = client.get_database('superheroes') # connect to db
collections = db.collection_names('superheroes')

for col in collections:
    if col == 'heroes':
        db.drop_collection('heroes') # delete if collection exists


col = db.get_collection('heroes')

# load json data into collection
with open('heroes.json') as f:
    data = json.load(f)
    col.insert_many(data)

# print content of heores collection
cursor = col.find()
for doc in cursor:
    print(doc)








## task 2

# find and print name whose publisher - Marvel Comics
display_field = {'_id': 0, 'name':1, 'Publisher':1}
criteria = {'Publisher':'Marvel Comics'}
query = col.find(criteria, display_field)
for doc in query:
    print(doc)


# find and print name - women and weight < 0
display_field = {'_id': 0, 'name':1, 'Gender':1, 'Weight':1}
criteria = {'$and':[{'Gender':'Female'}, {'Weight':{'$lt':0}}]}
query = col.find(criteria, display_field)
for doc in query:
    print(doc)





## task 3

# search superheroes with '-' race and remove it
criteria = {'Race':'-'}
update = {'$unset':{'Race':''}}
col.update_many(criteria, update)

# print name and race
display_field = {'_id':0, 'name':1, 'Race':1}
cursor = col.find({}, display_field)
for doc in cursor:
    print(doc)



    
