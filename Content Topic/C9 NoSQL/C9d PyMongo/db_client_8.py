import pymongo
import csv

client = pymongo.MongoClient('127.0.0.1', 27017)
db = client.get_database('entertainment')
col = db.get_collection('users')

with open('users.txt') as csv_file:
    data = csv.reader(csv_file, delimiter=',')
    for row in data:
        col.insert_one({'name':row[0], 'age':row[0]})

cursor = col.find()
for doc in cursor:
    print(doc)

client.close()
