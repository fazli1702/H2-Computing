from pymongo import MongoClient
import csv

try:
    client=MongoClient('127.0.0.1',27017)
    print("Connected successfully")
except:
    print("could not connect to Mongo")


db=client.get_database("all_classes")

collections=db.collection_names("all_classes")
if 'student_details' in collections:
    db.drop_collection('student_details')

col=db.get_collection('student_details')

with open('STUDENTLIST.txt') as csv_file:
    data=csv.reader(csv_file, delimiter=",")
    for row in data:
        col.insert_one({"class":row[0],"index_no":row[1],"name":row[2]})

##cursor=col.find()
##for doc in cursor:
##    print(doc)
##
##client.close()

while True:
    student_class=input('Please enter class:').upper()
    cursor=col.find({'class':student_class})
    
    print('These are the students in class:',student_class)
    print('{0:10}{1:10}'.format('index_no','name'))
    for doc in cursor:
        print('{0:10}{1:10}'.format(doc['index_no'],doc['name']))
        
    student_index=input('Please enter index_num:')
    student_remarks=input('Please enter remarks:')
    
    search={'class': student_class, 'index_no':student_index}
    update={'$set':{'remarks':student_remarks}}
    col.update_one(search, update)
    
    repeat=input('Proceed for other students? Y/N')
    if repeat.upper() == 'N':
        display = {'_id':0, 'index_no':1, 'name':1, 'remarks':1}
        info = col.find({}, display)
        for doc in info:
            print(doc)
        client.close()
        break
    
