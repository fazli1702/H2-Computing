import pymongo

client = pymongo.MongoClient('127.0.0.1', 27017)
db = client.get_database('Clinic')
col = db.get_collection('Patient')

for ele in col.find().sort('Name').limit(3):
    print('name:', ele['Name'])
    print('patientID:', ele['PatientID'])
