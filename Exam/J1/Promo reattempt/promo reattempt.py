#task 1
def population(k):
    if k == 0:
        return 18
    else:
        return population(k-1) + 0.5 - 0.001 * (population(k-1))**2


##print(population(0))
##print(population(1))
##print(population(21))



#task 2
def convert(date):
    for i in range(len(date)):
        if date[i] == '/':
            day = date[:i]
            date = date[i+1:]
            break

    for j in range(len(date)):
        if date[j] == '/':
            month = date[:j]
            date = date[j+1:]
            break

    year = date
        
    #print(day)
    #print(month)
    #print(year)

    if len(day) == 1:
        day = '0' + day
        
    if len(month) == 1:
        month = '0' + month

    if len(year) == 2:
        if int(year) >= 90:
            year = '19' + year
        elif int(year) <= 30:
            year = '20' + year

    #print(day)
    #print(month)
    #print(year)

    new = year + '-' + month + '-' + day

    return new

##print(convert('15/10/2019'))
##print(convert('3/12/2012'))
##print(convert('24/7/17'))
##print(convert('06/05/94'))






#task 3
#task 3.1
def encrypt(string):
    c1 = 0
    c2 = 0
    lst = []
    for ele in string:
        lst.append(ord(ele))
        c1 += ord(ele)
        c2 += c1

    checksum1 = c1 % 255
    #print('checksum1' , checksum1)
    checksum2 = c2 % 255
    #print('checksum2', checksum2)

    lst.append(checksum1)    
    lst.append(checksum2)

    return lst

sentence =  "Yishun Innova Junior College"
##print(encrypt(sentence))




#task 3.2
def decrypt(seq):
    sentence = ''
    c1 = 0
    c2 = 0
    for i in range(len(seq[:-2])):
        sentence += chr(seq[i])
        c1 += seq[i]
        c2 += c1

    checksum1 = c1 % 255
    #print('checksum1' , checksum1)
    checksum2 = c2 % 255
    #print('checksum2', checksum2)


    if checksum1 == seq[-2] and checksum2 == seq[-1]:
        return sentence
    else:
        return 'Error in message'


msg1 = [89, 105, 115, 104, 117, 110, 32,
        73, 110, 110, 111, 118, 97, 32,
        74, 117, 110, 105, 111, 114, 32,
        67, 111, 108, 108, 101, 103, 101,
        135, 199]

msg2 = [73, 110, 110, 111, 118, 97, 32,
        89, 105, 115, 104, 117, 110, 32,
        74, 117, 110, 105, 111, 114, 32,
        67, 111, 108, 108, 101, 103, 101,
        135, 199]

msg3 = [89, 105, 115, 104, 117, 110, 32,
        73, 110, 110, 111, 118, 97, 32,
        74, 117, 110, 105, 111, 114, 32,
        67, 111, 108, 108, 101, 103, 101, 
        32, 83, 99, 104, 111, 111, 108,
        135, 199]
        
msg4 = [84, 104, 101, 114, 101, 32, 105, 
        115, 32, 97, 110, 32, 101, 114, 
        114, 111, 114, 32, 105, 110, 32, 
        116, 104, 101, 32, 116, 114, 97, 
        110, 115, 109, 105, 116, 116, 101, 
        100, 32, 109, 101, 115, 115, 97, 
        103, 101, 46, 151, 109]

msg5 = [84, 104, 101, 114, 101, 32, 105, 
        115, 32, 110, 111, 32, 101, 114, 
        114, 111, 114, 32, 105, 110, 32, 
        116, 104, 105, 115, 32, 116, 114, 
        97, 110, 115, 109, 105, 116, 116, 
        101, 100, 32, 109, 101, 115, 115, 
        97, 103, 101, 46, 29, 74]




##print(decrypt(msg1))
##print(decrypt(msg2))
##print(decrypt(msg3))
##print(decrypt(msg4))
##print(decrypt(msg5))










#question 5
import csv
import sqlite3

#task 4.1
def create_db():
    db = sqlite3.connect('school.db')
    db.close()

def table_Civics():
    db = sqlite3.connect('school.db')
    try:
        c = db.cursor()
        c.execute('''CREATE TABLE `Civics` (
	`Class`	VARCHAR(32),
	`Tutor`	VARCAHR(50),
	`Homeroom`	VARCHAR(32),
	PRIMARY KEY(`Class`)
        );''')
    
    except:
        print('error:')

    db.commit()
    db.close()


def table_CCAInfo():
    db = sqlite3.connect('school.db')
    try:
        c = db.cursor()
        c.execute('''CREATE TABLE `CCAInfo` (
	`Name`	VARCHAR(50),
	`TeacherIC`	VARCAHR(50),
	PRIMARY KEY(`Name`)
        );''')

    except:
        print('error')

    db.commit()
    db.close()

def table_Student():
    db = sqlite3.connect('school.db')
    try:
        c = db.cursor()
        c.execute('''CREATE TABLE `Student` (
	`MatricNo`	VARCHAR(32),
	`Name`	VARCAHR(50),
	`Gender`	VARCHAR(10),
	`CivicsClass`	VARCAHR(10) REFERENCES Civis(Class),
	PRIMARY KEY(`MatricNo`)
        );''')

    except:
        print('error:')

    db.commit()
    db.close()
    
    
        
def table_StudentCCA():
    db = sqlite3.connect('school.db')
    try:
        c = db.cursor()
        c.execute('''CREATE TABLE `StudentCCA` (
	`MatricNo`	VARCHAR(10) REFERENCES Student(MatricNo),
	`CCAName`	VARCHAR(32) REFERENCES CCAInfo(Name)
        );''')

    except:
        print('error')

    db.commit()
    db.close()



##table_Civics()
##table_CCAInfo()
##table_Student()
##table_StudentCCA()






def insert_Civics():
    db = sqlite3.connect('school.db')
    c = db.cursor()

    f = open('Civics.csv')
    next(f)
    reader = csv.reader(f)

    for c, t, h in reader:
        db.execute('''INSERT INTO Civics
                    (Class, Tutor, Homeroom)
                    VALUES (:Class, :Tutor, :Homeroom)''',
                   {"Class":c, "Tutor":t, "Homeroom":h})

    db.commit()
    db.close()



    
    
def insert_CCAInfo():
    db = sqlite3.connect('school.db')
    c = db.cursor()

    f = open('CCAInfo.csv')
    next(f)
    reader = csv.reader(f)

    for n, t in reader:
        db.execute('''INSERT INTO CCAInfo
                    (Name, TeacherIC)
                    VALUES (:Name, :TeacherIC)''',
                   {"Name":n, "TeacherIC":t})

    db.commit()
    db.close()
    





def insert_Student():
    db = sqlite3.connect('school.db')
    c = db.cursor()

    f = open('Student.csv')
    next(f)
    reader = csv.reader(f)

    for m, n, g, c in reader:
        db.execute('''INSERT INTO Student
                    (MatricNo, Name, Gender, CivicsClass)
                    VALUES (:MatricNo, :Name, :Gender, :CivicsClass)''',
                  {"MatricNo":m, "Name":n, "Gender":g, "CivicsClass":c})

    db.commit()
    db.close()







def insert_StudentCCA():
    db = sqlite3.connect('school.db')
    c = db.cursor()

    f = open('StudentCCA.csv')
    next(f)
    reader = csv.reader(f)
    
    for m, c in reader:
        db.execute('''INSERT INTO StudentCCA
                    (MatricNo, CCAName)
                    VALUES (:MatricNo, :CCAName)''',
                   {"MatricNo":m, "CCAName":c})

    db.commit()
    db.close()




##insert_Civics()
##insert_CCAInfo()
##insert_Student()
##insert_StudentCCA()






#task 4.3

def menu():
    while True:
        print()
        print('1. Update Student CCA')
        print('2. Display Student Info')
        print()

        choice = input('Choice:')

        if choice == '1':
            update_CCA()

        elif choice == '2':
            display_student()

        else:
            return None


def update_CCA():
    db = sqlite3.connect('school.db')
    c = db.cursor()

    no = input('Matric No:')
    print()
    CCA = input('New CCA:')

    c .execute('''UPDATE StudentCCA SET CCAName = :CCA
                    WHERE MatricNo = :no;''',
               {"CCA":CCA, "no":no})

    db.commit()
    db.close()



def display_student():
    db = sqlite3.connect('school.db')
    c = db.cursor()

    no = input('Matric No:')

    c.execute('''SELECT Student.MatricNo, Student.Name, Student.Gender, Student.CivicsClass,
                Civics.Tutor, Civics.Homeroom, StudentCCA.CCAName, CCAInfo.TeacherIC
                FROM Student, Civics, StudentCCA,  CCAInfo 
                WHERE Student.CivicsClass = Civics.Class AND StudentCCA.MatricNo = Student.MatricNo
                AND CCAInfo.Name = StudentCCA.CCAName AND Student.MatricNo = :no;''',
                {"no":no})

    
    info = c.fetchall()
    #print(info)

    if info == None:
        print('Error: No such student.')

    elif len(info) == 2:
        print("******** Student's Info ********")
        print('Matric No: ' + info[0][0])
        print('Name: ' + info[0][1])
        print('Gender: ' + info[0][2])
        print('Civcs Class: ' + info[0][3])
        print('Civics Tutor: ' + info[0][4])
        print('Home Room: ' + info[0][5])
        print('CCA/CCA Teacher IC: ' + info[0][6] + ' / ' + info[0][7])
        print('CCA/CCA Teacher IC: ' + info[1][6] + ' / ' + info[1][7])

    else:
        print("******** Student's Info ********")
        print('Matric No: ' + info[0][0])
        print('Name: ' + info[0][1])
        print('Gender: ' + info[0][2])
        print('Civcs Class: ' + info[0][3])
        print('Civics Tutor: ' + info[0][4])
        print('Home Room: ' + info[0][5])
        print('CCA/CCA Teacher IC: ' + info[0][6] + ' / ' + info[0][7])

    


        
        
##menu()







#question 6
# Run  the following codes to import the data from psi.csv 
# into the list data

data = []

import csv
file=open('psi.csv')
lines=csv.reader(file)
for i in lines:
    data.append(tuple(i))
    
##print(data)    # run this code to see the data


#Task 5.1

def get_PSI(reading):     
    return int(reading[2])
    
    
#Task 5.2

def smallest_index(seq):
    minim = seq[0]
    index = 0
    for i in range(1, len(seq)):
        if get_PSI(minim) > get_PSI(seq[i]):
            minim = seq[i]
            index = i
    return index

def selection_sort(seq):
    minim_i = 0
    for i in range(len(seq)-1):
        minim_i = smallest_index(seq[i:]) + i
        if i != minim_i:
            seq[i], seq[minim_i] = seq[minim_i], seq[i]
    return seq
    


#Task 5.3
import math

def median(lst):
    med = (len(lst) + 1) / 2
    if len(lst) % 2 == 0:
        a = len(lst) // 2
        b = (len(lst) // 2) + 1
        return math.ceil((get_PSI(lst[a]) + get_PSI(lst[b])) / 2)
    else:
        return get_PSI(lst[med])
        

    
##print(selection_sort(data))
##print(median(data))























#question 7
#stack.py

##### Stack ADT ######

def make_stack():
    return []

def is_empty(stack):
    return stack==[]

def push(stack,item):
    stack.append(item)

def clear(stack):
    return stack.clear()
    
#Task 6.1

def pop(stack):
    if is_empty(stack):
        return None
    else:
        stack.pop()
        return stack


def peek(stack):
    if is_empty(stack):
        return None
    else:
        return stack[-1]
    

#Task 6.2

###Write the codes to initialise the following:

currentPage = make_stack()

backStack = make_stack()

forwardStack= make_stack()


def navigate(newPage):    
    global currentPage
    currentPage=newPage     

def linkClicked(page):         
    global backStack
    global forwardStack
    push(backStack,currentPage)
    clear(forwardStack)
    navigate(page)
    
#Task 6.3

def goBack():
    global currentPage
    global backStack
    global forwardStack
    #push(forwardStack, currentPage)
    forwardStack.append(currentPage)
    #navigate(pop(backStack))
    navigate(backStack.pop())
    

def goForward():
    global currentPage
    global backStack
    global forwardStack
    #push(backStack, currentPage)
    backStack.append(currentPage)
    #navigate(pop(forwardStack))
    navigate(forwardStack.pop())

#Task 6.4

def finalpage(clicks):
    global currentPage
    global backStack
    global forwardStack
    
    for i in range(len(clicks)):
        if clicks[i] == '<':
            goBack()
        elif clicks[i] == '>':
            goForward()
        else:
            if i == 0:
                navigate(clicks[i])
            else:
                linkClicked(clicks[i])
    return currentPage
            



clicks = ['Google', 'YIJC-Home', 'YIJC-News', '<']
clicks2 = ['YIJC-Home', 'YIJC-About', '<', 'YIJC-News', '<', '>']



print(finalpage(clicks))
print(finalpage(clicks2))
