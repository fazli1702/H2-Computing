import pymongo

client = pymongo.MongoClient('127.0.0.1', 27017)
db = client.get_database('OUTLETS')
col = db.get_collection('GEM')


drop_list = []
for ele in col.find():
    for i in ele['Name']:
        if not(i.isalnum() or i == ' '):
            drop_list.append(ele['SerialNo'])


for ele in drop_list:
    col.delete_one({'SerialNo':ele})

            
