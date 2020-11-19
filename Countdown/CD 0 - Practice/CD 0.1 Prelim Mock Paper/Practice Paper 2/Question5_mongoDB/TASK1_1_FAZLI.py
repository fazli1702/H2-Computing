import pymongo

client = pymongo.MongoClient('127.0.0.1', 27017)


# Task 1.1
db = client.get_database('library')
col = db.get_collection('books')

books = [
{"book_id": 234, "title": "Father Night", "author": "Kurt",
 "publisher": "APress", "page_count": 433, "year": "2018"},
{"book_id": 134, "title": "Mother Night", "author": ["Kurt", "Dan"],
 "publisher": "APress", "year": "2015"},
{"book_id": 334, "title": "Programming C## 6.0", "author": ["Andrew", "Dan"],
 "page_count": 300, "year": "2000"},
{"book_id": 534, "title": "Introduction to Python", "publisher": "MPH",
 "year": "1999"},
{"book_id": 434, "title": "Travel with Dogs", "author": "Andy",
 "publisher": "APress", "page_count": 100, "year": "2017"}
]
        
##col.insert_many(books)
##
##for book in col.find():
##    print(book)


# Task 1.2
display = {'_id':0, 'book_id':1, 'title':1, 'author':1}
query1 = {'year':'2015'}
##print('Display 2015 books:')
##for book in col.find(query1, display):
##    print(book)
##print()

query2 = {'page_count':{'$gte':100, '$lt':400}}
##print('100 <= page count < 400:')
##for book in col.find(query2):
##    print(book)
##print()

search = {'page_count':{'$exists':False}}
update = {'$set':{'page_count':'Less Than 100 Pages'}}
col.update_many(search, update)

display2 = {'_id':0, 'book_title':1, 'page_count':1, 'year':1}
##print('sort by year, descending:')
##for book in col.find({}, display2).sort('year', -1):
##    print(book)

