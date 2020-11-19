def menu():
    while True:
        print()
        print('***** Stanford Tuition Centre *****')
        print()
        print(' 1. Tuition centres')
        print(' 2. Tuiton classes')
        print(' 3. Check Student Info')
        print(' 4. Teachers Info')
        print(' 5. Enroll for a class')
        print(' 6. Pay Fees')
        print()
        print(' X. Quit')
        print()


        choice = input('Enter your choice: ')

        if choice.upper() == 'X':
            return None

        elif choice == '1':
            tuition_centre()

        elif choice == '2':
            tuition_class()

        elif choice == '3':
            student_info()

        elif choice == '4':
            teacher_info()

        elif choice == '5':
            enrollment()

        elif choice == '6':
            fee()

        else:
            print('Plase enter a valid choice')



import sqlite3


def tuition_centre():
    db = sqlite3.connect('tuition.db')
    c = db.cursor()

    c.execute('''SELECT * from centres;''')
    
    centres = c.fetchall()

    for centre in centres:
        print(centre[0], '.', centre[1])
        print(centre[2])
        print(centre[3])
        print('Opening:', centre[4])
        print('Closing:', centre[5])
        print('Telephone:', centre[6])
        print()
        print()




##tuition_centre()
        

def tuition_class():
    
    db = sqlite3.connect('tuition.db')
    c = db.cursor()
    
    while True:
        print()
        print()
        print('1. JC')
        print('2. SEC')
        print('3. ALL')
        print()
        print()
        print('X. Quit')
        pass

        choice = input('Enter your choice:')

        if choice.upper() == 'X':
            return None


##tuition_class()







def student_info():
    
    db = sqlite3.connect('tuition.db')
    c = db.cursor()
    
    while True:
        print()
        print()
        print('1. List all')
        print('2. List all JC students info')
        print('3. List all SEC studets info')
        print('4. List specific student')
        print()
        print()
        print('X. Quit')

        choice = input('Enter your choice:')

        if choice.upper() == 'X':
            return None

        elif choice == '1':
            c.execute('''SELECT * FROM students;''')
            students = c.fetchall()
            for student in students:
                print(student)
            db.commit()
            db.close()



print(student_info())








##menu()
