import pymongo
import json
import csv

client = pymongo.MongoClient('127.0.0.1', 27017)
db = client.get_database('entertainment')
col = db.get_collection('movies')

while True:
    print('-------MENU------')
    print('Please choose an option')
    print('1. insert one movie')
    print('2. insert movies using text file')
    print('3. insert movise using json file')
    print('4. display all movies')
    print('5. quit')
    print()
    
    user_option = int(input('Your option:'))

    if user_option == 1:
        title = input('Please enter the movie title:')
        year = input('Please input the year of the movie:')
        col.insert_one({'title':title, 'year':year})
        
    elif user_option == 2:
        with open('movies.txt') as csv_file:
            data = csv.reader(csv_file, delimiter=',')
            for row in data:
                col.insert_one({'title':row[0], 'year':row[1]})
                
    elif user_option == 3:
        with open('movies.json') as json_file:
            data = json.load(json_file)
            col.insert_many(data)
    
    elif user_option == 4:
        cursor = col.find()
        for doc in cursor:
            print(doc)
    
    elif user_option == 5:
        break
    
    else:
        print('Please enter the correct number')
