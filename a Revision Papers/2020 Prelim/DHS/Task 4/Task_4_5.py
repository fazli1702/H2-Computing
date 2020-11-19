import pymongo

client = pymongo.MongoClient('127.0.0.1', 27017)
db = client.get_database('Clinic')
col = db.get_collection('Patient')

names = []
repeated_names = []

for ele in col.find():
    name = ele['Name']
    if name in names:
        repeated_names.append(name)
    else:
        names.append(name)


for ele in col.find():
    name = ele['Name']
    if name in repeated_names:
        print(ele['PatientID'])
