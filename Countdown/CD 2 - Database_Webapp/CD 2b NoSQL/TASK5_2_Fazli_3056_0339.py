import pymongo

client = pymongo.MongoClient('127.0.0.1', 27017)
db = client.get_database('all_classes')
col = db.get_collection('student_details')


display_field = {'_id':0, 'index_no':1, 'name':1}

student_class = input('Enter class:').upper()
info = col.find({'class':student_class}, display_field)

print('{:10} {:10}'.format('index_no', 'name'))
for ele in info:
    print('{0:10} {1:10}'.format(ele['index_no'], ele['name']))

while True:
    index_no = input('Enter index:')
    remarks = input('Enter remarks:')
                     
    search = {'index':index_no, 'class':student_class}
    update = {'$set':{'remarks':remarks}}
    col.update_one(search, update)
    
    choice = input('Continue adding student remarks? (y/n):').upper()
    if choice == 'N':
        display = {'_id':0, 'index_no':1, 'name':1, 'remarks':1}
        info = col.find({}, display)
        for ele in info:
            print(ele)
            
        client.close()
        break
    



