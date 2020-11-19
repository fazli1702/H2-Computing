import pymongo

info = []
with open('STUDENTLIST.txt') as f:
    data = f.readlines()
    for student in data:
        student = tuple(student.strip().split(','))
        clss, index, name = student
        info.append({'class':clss, 'index':index, 'name':name})


##for ele in info:
##    print(ele)



# task 3.1
client = pymongo.MongoClient('127.0.0.1', 27017)
db = client.get_database('all_classes')
collections = db.collection_names()

# check for duplicate
for col in collections:
    if col == 'student_details':
        db.drop_collection('student_details')

# insert into collection
col = db.get_collection('student_details')
col.insert_many(info)
# for ele in col.find():
#     print(ele)


# task 3.2
display_field = {'_id':0, 'class':1, 'index':1, 'name':1}
while True:
    # input class
    clss = input('Enter class:').upper()
    print(clss)

    # display all student
    print('------------ STUDENTS -------------')
    query = col.find({'class':clss}, display_field)
    for student in query:
        print(student)
    print('-----------------------------------')

    # input index
    index = input('Index:')

    #input remarks
    remarks = input('Remarks:')

    search = {'$and':[{'class':clss}, {'index':index}]}
    if col.find({'$and':[search, {'remarks':None}]}):
        # no remarks in document
        update = {'$set':{'remarks':remarks}}
        col.update_one(search, update)

    else:
        col.insert_one({'remarks':remarks})

    choice = input('Do you want to continue adding remarks?(y/n):').upper()

    if choice == 'N':
        display_field = {'_id':0, 'class':1, 'index':1, 'name':1, 'remarks':remarks}
        query = col.find({}, display_field)
        for student in query:
            print(student)
        break
