import pymongo

client = pymongo.MongoClient('127.0.0.1', 27017)
db = client.get_database('Clinic')
col = db.get_collection('Patient')
