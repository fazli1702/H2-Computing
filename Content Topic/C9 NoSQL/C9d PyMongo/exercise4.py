import pymongo

client = pymongo.MongoClient('127.0.0.1', 27017)
db = client.get_database('entertainment')
col = db.get_collection('movies')

display_field = {'_id':0, 'title':1, 'genre':1, 'year':1}


def main():
    while True:
        print('------ MENU -----')
        print()
        print('1. Update movie')
        print('2. Delete movie')
        print('3. Disaplay all movie')
        print('4. Quit')

        choice = int(input('Enter your choice: '))

        if choice == 1:
            search = search_movie()
            update = update_value()
            col.update_many(search, update)


        elif choice == 2:
            search = search_movie()
            col.delete_many(search)

        elif choice == 3:
            query = col.find({}, display_field).sort('title', 1)
            for doc in query:
                print(doc)

        elif choice == 4:
            break


def search_movie():
    print('Search movie by')
    print('1. title')
    print('2. genre')
    print('3. year')

    choice = int(input('Enter your choice: '))

    if choice == 1:
        title = input('title: ')
        search = {'title':title}

    elif choice == 2:
        choice = input('Is there a genre (Y/N): ').upper()
        if choice == 'N':
            search = {'genre':{'$exists':False}}

        elif choice == 'Y':
            genre = input('What genre: ')
            search = {'genre':{genre}}


    elif choice == 3:
        print()
        print('1. Greater than')
        print('2. Equal to')
        print('3. Lesser than')
        print()

        choice = int(input('Please enter your choice: '))
        year = int(input('Please enter the year: '))

        if choice == 1:
            search = {'year':{'$gt':year}}

        elif choice == 2:
            search = {'year':year}

        elif choice == 3:
            search = {'year':{'$lt':year}}

    return search


def update_value():
    print('What do you want to update?')
    print('1. title')
    print('2. genre')
    print('3. year')

    choice = int(input('Enter your choice: '))

    if choice == 1:
        title = input('title:')
        update = {'$set':{'title':title}}
        
    elif choice == 2:
        genre = input('genre:')
        update = {'$set':{'genre':genre}}

    elif choice == 3:
        year = int(input('year:'))
        update = {'$set':{'year':year}}

    return update


main()