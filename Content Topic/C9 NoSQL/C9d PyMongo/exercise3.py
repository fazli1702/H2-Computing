import pymongo

client = pymongo.MongoClient('127.0.0.1', 27017)
db = client.get_database('entertainment')
col = db.get_collection('movies')

display_field = {'_id':0, 'title':1, 'genre':1, 'year':1}

def genre():
    choice = input('Is there a genre (Y/N): ').upper()
    if choice == 'N':
        criteria = {'genre':{'$exists':False}}
        query = col.find(criteria, display_field)

    elif choice == 'Y':
        genre = input('What genre: ')
        criteria = {'genre':{genre}}
        query = col.find(criteria, display_field)

    for doc in query:
        print(doc)


def year():
    print()
    print('1. Greater than')
    print('2. Equal to')
    print('3. Lesser than')
    print()

    choice = int(input('Please enter your choice: '))
    year = int(input('Please enter the year: '))

    if choice == 1:
        criteria = {'year':{'$gt':year}}
        query = col.find(criteria, display_field)

    elif choice == 2:
        criteria = {'year':year}
        query = col.find(criteria, display_field)

    elif choice == 3:
        criteria = {'year':{'$lt':year}}
        query = col.find(criteria, display_field)

    for doc in query:
        print(doc)




while True:
    print('------MENU------')
    print('Please select a choice')
    print('1. Find movie based on title')
    print('2. Find movie based on genre')
    print('3. Find movie based on year')
    print('4. Display all movie')
    print('5. Quit')

    choice = int(input('Please enter your choice:'))

    # movie based on title
    if choice == 1:
        title = input('title:')
        criteria = {'title':title}
        query = col.find(criteria, display_field)
        for doc in query:
            print(doc)

    # movie based on genre
    elif choice == 2:
        genre()

    # movie based on year
    elif choice == 3:
        year()

    # sort movie in asc order
    elif choice == 4:
        query = col.find({}, display_field).sort('title', 1)
        for doc in query:
            print(doc)
    
    # quit
    elif choice == 5:
        break

    else:
        print('Please enter the correct choice')



