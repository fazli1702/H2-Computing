import pymongo

# connect to db
client = pymongo.MongoClient('127.0.0.1', 27017)
db = client.get_database('all_classes')

# clear existing collection
col_names = db.collection_names()
if 'student_details' in col_names:
    db.drop_collection('student_details')
    
col = db.get_collection('student_details')

# read file
with open('STUDENTLIST.txt') as f:
    data = f.readlines()
    students = [ele.strip().split(',') for ele in data]

    # add to db
    students_info = []
    for Class, index_no, name in students:
        info = {'class':Class, 'index_no':index_no, 'name':name}
        students_info.append(info)

col.insert_many(students_info)

for ele in col.find():
    print(ele)
