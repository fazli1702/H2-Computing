import pymongo

try:
    client = pymongo.MongoClient('127.0.0.1', 27017)
    print("Connected successfully")
except:
    print("Could not connect to MongoDB")
else:
    db = client.get_database('concert')
    col = db.get_collection('information')


def main():
    while True:
        print('------ CONCERT ------')
        print()
        print('1. Insert concert information')
        print('2. Concert information - according to title')
        print('3. Delete concert - according to title')
        print('4. Quit')

        choice = int(input('Please enter your choice: '))

        if choice == 1:
            info = {}
            title = input('Title: ')
            info.update({'title':title})

            date = input('Date (dd/mm/yyyy): ')
            info.update({'date':date})

            time = input('Time (hh:mm): ')
            info.update({'time':time})

            venue = input('Venue: ')
            info.update({'venue':venue})

            price = int(input('Price: '))
            info.update({'price':price})

            try:
                col.insert(info)
                print('information added')
            except:
                print('There was an error, please try again')
            

        elif choice == 2:
            title = input('Title:')
            try:
                result = col.find({'title':title})
                print("Search")
                for document in result:
                    print(document)
            except:
                print("Error occurred while trying to search")


        elif choice == 3:
            title = input('title:')
            try:
                search = {'title':title}
                col.delete_one(search)
            except:
                print('There was an error, please try again')

        elif choice == 4:
            break

        else:
            print('Please enter the correct choice')
main()
