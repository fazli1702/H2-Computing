def menu():
    while True:
        print()
        print('***** ABC Tuition Centre *****')
        print()
        print('INFORMATION')
        print(' 1. Tuition Centre')
        print(' 2. Tuiton Class')
        print(' 3. Student Info')
        print(' 4. Teachers Info')
        print()
        print('ADMIN')
        print(' 5. Enroll for a class')
        print(' 6. Drop Class')
        print(' 7. Pay Fees')
        print(' 8. Update Fees ')
        print(' 9. Update student grade')
        print()
        print(' 10. Delete Data')
        print()
        print(' R. RESET DATABASE ')
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
            drop()

        elif choice == '7':
            fee()

        elif choice == '8':
            update_fee()

        elif choice == '9':
            update_grade()

        elif choice == '10':
            delete_data()

        elif choice.upper() == 'R':
            reset_db()

        else:
            print('Plase enter a valid choice')

















######################################################################################
######################################################################################

            

import sqlite3


def tuition_centre():
    print()
    print()
    print('*** centre information ***')
    print()
    print()
    
    db = sqlite3.connect('tuition.db')
    c = db.cursor()

    c.execute('''SELECT * from centres;''')
    
    centres = c.fetchall()

    for centre in centres:
        print('*****')
        print()
        print(centre[0], '.', centre[1])
        print(centre[2])
        print(centre[3])
        print('Opening:', centre[4])
        print('Closing:', centre[5])
        print('Telephone:', centre[6])
        print()
        print()




##tuition_centre()
















######################################################################################
######################################################################################


        
def tuition_class():
    
    db = sqlite3.connect('tuition.db')
    c = db.cursor()
    
    print()
    print()
    print('*** class information ***')
    print()
    print()
    print(' 1. JC')
    print(' 2. SEC')
    print(' 3. ALL')
    print()
    print(' 4. Number of students')
    print()
    print(' X. Quit')
    pass

    choice = input('Enter your choice:')

    if choice.upper() == 'X':
        return None

    #############    JC CLASS    ###############

    elif choice == '1':
        print('*** JC CLASS ***')
        print()
        print(' 1. H1')
        print(' 2. H2')
        print(' 3. All')
        print()
        print()
        print('X. Quit')

        choice_2 = input('Enter your choice:')

        if choice_2.upper() == 'X':
            return None


        ######### H1 ##########
        elif choice_2 == '1':
            c.execute('''SELECT class.ClassID, subjects.subject, subjects.level,subjects.type, teachers.name, centres.location,
                        class.day, class.start, class.end, fee.fee
                        FROM class, subjects, teachers, centres, fee
                        WHERE class.CentreID = centres.LocationID AND class.TeacherID = teachers.TeacherID
                        AND  class.SubjectID = subjects.SubjectID AND subjects.level = "JC"
                        AND fee.type = "H1" AND subjects.type = fee.type;''')

            classes = c.fetchall()

            for c in classes:
                print('*****')
                print()
                print(c[0])
                print(c[2])
                print(c[3], c[1])
                print('Teacher:', c[4])
                print('Centre:', c[5])
                print(c[6], c[7], 'to', c[8])
                print('Fee: $', c[9], '/ month')
                print()


                
        ######## H2 #########
        elif choice_2 == '2':
            c.execute('''SELECT class.ClassID, subjects.subject, subjects.level,subjects.type, teachers.name, centres.location,
                        class.day, class.start, class.end, fee.fee
                        FROM class, subjects, teachers, centres, fee
                        WHERE class.CentreID = centres.LocationID AND class.TeacherID = teachers.TeacherID
                        AND  class.SubjectID = subjects.SubjectID AND subjects.level = "JC"
                        AND fee.type = "H2" AND subjects.type = fee.type;''')

            classes = c.fetchall()

            for c in classes:
                print('*****')
                print()
                print(c[0])
                print(c[2])
                print(c[3], c[1])
                print('Teacher:', c[4])
                print('Centre:', c[5])
                print(c[6], c[7], 'to', c[8])
                print('Fee: $', c[9], '/ month')
                print()
                


        ###### ALL  H1/H2 #########
        elif choice_2 == '3':
            c.execute('''SELECT class.ClassID, subjects.subject, subjects.level, subjects.type, teachers.name, centres.location,
                        class.day, class.start, class.end, fee.fee
                        FROM class, subjects, teachers, centres, fee
                        WHERE class.CentreID = centres.LocationID AND class.TeacherID = teachers.TeacherID
                        AND  class.SubjectID = subjects.SubjectID AND subjects.level = "JC" AND subjects.type = fee.type;''')
                        

            classes = c.fetchall()

            for c in classes:
                print('*****')
                print()
                print(c[0])
                print(c[2])
                print(c[3], c[1])
                print('Teacher:', c[4])
                print('Centre:', c[5])
                print(c[6], c[7], 'to', c[8])
                print('Fee: $', c[9], '/ month')
                print()

        else:
            print('*** ERROR ***')
                    

    ###########    SEC CLASS     ###################

    elif choice == '2':
        print('*** SEC CLASS ***')
        print()
        print('MATH')
        print(' 1. ADDITIONAL')
        print(' 2. ELEMENTARY')
        print(' 3. All')
        print()
        print()
        print('SCIENCE')
        print(' 4. PURE')
        print(' 5. COMBINED')
        print(' 6. All')
        print()
        print(' 7. All subjects')
        print()
        print()
        print('X. Quit')

                      

        choice_3 = input('Enter your choice:')


        if choice.upper() == 'X':
            return None
        
        ######## A MATH ###########
        elif choice_3 == '1':
            c.execute('''SELECT class.ClassID, subjects.subject, subjects.level ,subjects.type, teachers.name, centres.location,
                        class.day, class.start, class.end, fee.fee
                        FROM class, subjects, teachers, centres, fee
                        WHERE class.CentreID = centres.LocationID AND class.TeacherID = teachers.TeacherID
                        AND  class.SubjectID = subjects.SubjectID AND subjects.level = "SEC"
                        AND fee.type = "ADDITIONAL" AND subjects.type = fee.type;''')

            classes = c.fetchall()

            for c in classes:
                print('*****')
                print()
                print(c[0])
                print(c[2])
                print(c[3], c[1])
                print('Teacher:', c[4])
                print('Centre:', c[5])
                print(c[6], c[7], 'to', c[8])
                print('Fee: $', c[9], '/ month')
                print()

        ######## E MATH ###########
        elif choice_3 == '2':
            c.execute('''SELECT class.ClassID, subjects.subject, subjects.level ,subjects.type, teachers.name, centres.location,
                        class.day, class.start, class.end, fee.fee
                        FROM class, subjects, teachers, centres, fee
                        WHERE class.CentreID = centres.LocationID AND class.TeacherID = teachers.TeacherID
                        AND  class.SubjectID = subjects.SubjectID AND subjects.level = "SEC"
                        AND fee.type = "ELEMENTARY" AND subjects.type = fee.type;''')

            classes = c.fetchall()

            for c in classes:
                print('*****')
                print()
                print(c[0])
                print(c[2])
                print(c[3], c[1])
                print('Teacher:', c[4])
                print('Centre:', c[5])
                print(c[6], c[7], 'to', c[8])
                print('Fee: $', c[9], '/ month')
                print()



        ####### ALL MATH ##########
        elif choice_3 == '3':
            c.execute('''SELECT class.ClassID, subjects.subject, subjects.level ,subjects.type, teachers.name, centres.location,
                        class.day, class.start, class.end, fee.fee
                        FROM class, subjects, teachers, centres, fee
                        WHERE class.CentreID = centres.LocationID AND class.TeacherID = teachers.TeacherID
                        AND  class.SubjectID = subjects.SubjectID AND subjects.level = "SEC"
                        AND subjects.subject = "MATH" AND subjects.type = fee.type;''')

            classes = c.fetchall()

            for c in classes:
                print('*****')
                print()
                print(c[0])
                print(c[2])
                print(c[3], c[1])
                print('Teacher:', c[4])
                print('Centre:', c[5])
                print(c[6], c[7], 'to', c[8])
                print('Fee: $', c[9], '/ month')
                print()



        ###### PURE SCIENCE ######
        elif choice_3 == '4':
            c.execute('''SELECT class.ClassID, subjects.subject, subjects.level ,subjects.type, teachers.name, centres.location,
                        class.day, class.start, class.end, fee.fee
                        FROM class, subjects, teachers, centres, fee
                        WHERE class.CentreID = centres.LocationID AND class.TeacherID = teachers.TeacherID
                        AND  class.SubjectID = subjects.SubjectID AND subjects.level = "SEC"
                        AND fee.type = "PURE" AND subjects.type = fee.type;''')
            

            classes = c.fetchall()

            for c in classes:
                print('*****')
                print()
                print(c[0])
                print(c[2])
                print(c[3], c[1])
                print('Teacher:', c[4])
                print('Centre:', c[5])
                print(c[6], c[7], 'to', c[8])
                print('Fee: $', c[9], '/ month')
                print()


        ######## COMBINED SCIENCE #########
        elif choice_3 == '5':
            c.execute('''SELECT class.ClassID, subjects.subject, subjects.level ,subjects.type, teachers.name, centres.location,
                        class.day, class.start, class.end, fee.fee
                        FROM class, subjects, teachers, centres, fee
                        WHERE class.CentreID = centres.LocationID AND class.TeacherID = teachers.TeacherID
                        AND  class.SubjectID = subjects.SubjectID AND subjects.level = "SEC"
                        AND fee.type = "COMBINED" AND subjects.type = fee.type;''')
            
            classes = c.fetchall()

            for c in classes:
                print('*****')
                print()
                print(c[0])
                print(c[2])
                print(c[3], c[1])
                print('Teacher:', c[4])
                print('Centre:', c[5])
                print(c[6], c[7], 'to', c[8])
                print('Fee: $', c[9], '/ month')
                print()



        ########## ALL SCIENCE #########
        elif choice_3 == '6':
            c.execute('''SELECT class.ClassID, subjects.subject, subjects.level ,subjects.type, teachers.name, centres.location,
                        class.day, class.start, class.end, fee.fee
                        FROM class, subjects, teachers, centres, fee
                        WHERE class.CentreID = centres.LocationID AND class.TeacherID = teachers.TeacherID
                        AND  class.SubjectID = subjects.SubjectID AND subjects.level = "SEC"
                        AND subjects.subject != "MATH" AND subjects.type = fee.type;''')

            classes = c.fetchall()

            for c in classes:
                print('*****')
                print()
                print(c[0])
                print(c[2])
                print(c[3], c[1])
                print('Teacher:', c[4])
                print('Centre:', c[5])
                print(c[6], c[7], 'to', c[8])
                print('Fee: $', c[9], '/ month')
                print()



        ######## ALL SEC SUBJECTS #########
        elif choice_3 == '7':
            c.execute('''SELECT class.ClassID, subjects.subject, subjects.level ,subjects.type, teachers.name, centres.location,
                        class.day, class.start, class.end, fee.fee
                        FROM class, subjects, teachers, centres, fee
                        WHERE class.CentreID = centres.LocationID AND class.TeacherID = teachers.TeacherID
                        AND  class.SubjectID = subjects.SubjectID AND subjects.level = "SEC"
                        AND subjects.type = fee.type;''')

            classes = c.fetchall()

            for c in classes:
                print('*****')
                print()
                print(c[0])
                print(c[2])
                print(c[3], c[1])
                print('Teacher:', c[4])
                print('Centre:', c[5])
                print(c[6], c[7], 'to', c[8])
                print('Fee: $', c[9], '/ month')
                print()
                    

        else:
            print('*** ERROR ***')



    ############       ALL SUBJECTS JC/SEC       ################
            
    elif choice == '3':
        c.execute('''SELECT class.ClassID, subjects.subject, subjects.level ,subjects.type, teachers.name, centres.location,
                        class.day, class.start, class.end, fee.fee
                        FROM class, subjects, teachers, centres, fee
                        WHERE class.CentreID = centres.LocationID AND class.TeacherID = teachers.TeacherID
                        AND  class.SubjectID = subjects.SubjectID AND fee.type = subjects.type;''')

        classes = c.fetchall()

        for c in classes:
            print('*****')
            print()
            print(c[0])
            print(c[2])
            print(c[3], c[1])
            print('Teacher:', c[4])
            print('Centre:', c[5])
            print(c[6], c[7], 'to', c[8])
            print('Fee: $', c[9], '/ month')
            print()




    ####### COUNT STUDENTS ########
    elif choice == '4':
        print()
        print(' 1. Total number of students')
        print(' 2. Total number of JC students')
        print(' 3. Total number of SEC students')
        print(' 4. Total number of students in class')
        print(' 5. Total number of students in centre')
        print()
        print()
        print(' X. Quit')
        print()

        choice_4 = input('Enter your choice:')

        if choice_4.upper() == 'X':
            return None

        
        ##### TOTAL STUDENTS #####
        elif choice_4 == '1':
            c.execute('''SELECT COUNT(*) FROM students;''')
            no = c.fetchone()
            print('Total students:', no)

        ##### TOTAL JC STUDENTS #####
        elif choice_4 == '2':
            c.execute('''SELECT COUNT(*) FROM students WHERE level = "JC";''')
            no = c.fetchone()
            print('Total JC students:', no)

        ##### TOTAL SEC STUDENTS #####
        elif choice_4 == '3':
            c.execute('''SELECT COUNT(*) FROM students WHERE level = "SEC";''')
            no = c.fetchone()
            print('Total JC students:', no)

        ##### STUDENTS FROM CLASS #####
        elif choice_4 == '4':
            print()
            cid = input('Enter ClassID:')
            c.execute('''SELECT COUNT(*) FROM enrollment WHERE ClassID = :cid;''',
                      {"cid":cid.upper()})
            no = c.fetchone()
            print('Total students from', cid.upper(), ':', no)

        ##### STUDENTS FROM CENTRE #####
        elif choice_4 == '5':
            print()
            lid = input('Enter LocationID:')
            c.execute('''SELECT COUNT(*) FROM centres WHERE LocationID = :lid;''',
                      {"lid":lid.upper()})
            no = c.fetchone()
            print('Total students from', lid.upper(), ':', no)

        else:
            print('*** ERROR ***')


    
    else:
        print('*** ERROR ***')
            
            
            

        
        
                            
                              


##tuition_class()

















######################################################################################
######################################################################################




def student_info():
    
    db = sqlite3.connect('tuition.db')
    c = db.cursor()
    
    print()
    print('***Student Information***')
    print()
    print()
    print('1. List all')
    print('2. List all JC students info')
    print('3. List all SEC studets info')
    print('4. List students from specific class')
    print('5. List specific student')
    print()
    print()
    print('X. Quit')

    choice = input('Enter your choice:')

    if choice.upper() == 'X':
        return None



    ##### LIST ALL #####
    elif choice == '1':
        c.execute('''SELECT * FROM students;''')
        students = c.fetchall()
        for student in students:
            print(student)
        db.commit()
        db.close()



        
    ##### JC STUDENTS #####
    elif choice == '2':
        c.execute('''SELECT * FROM students WHERE level="JC";''')
        students = c.fetchall()
        for student in students:
            print(student)
        db.commit()
        db.close()




        
    ##### SEC STUDENTS #####
    elif choice == '3':
        c.execute('''SELECT * FROM students WHERE level="SEC";''')
        students = c.fetchall()
        for student in students:
            print(student)
        db.commit()
        db.close()




    ##### STUDENTS IN CLASS ####
    elif choice == '4':
        class_1 = input('Enter class ID:')
        c.execute('''SELECT students.nric, students.name, students.gender,
                    students.level, students.email
                    FROM students, enrollment
                    WHERE students.nric = enrollment.StudentID
                    AND enrollment.ClassID = :class;''',
                    {"class":class_1.upper()})

        students = c.fetchall()

        if students == None:
            print()
            print()
            print('***ERROR***')
            print('No such nric')
            print()

        else:
            for student in students:
                print(student)

                  

        
    ##### SPECIFIC STUDENT #####
    elif choice == '5':
        nric = input('Enter nric:')
        c.execute('''SELECT * FROM students WHERE nric = :ic;''',
                {"ic":nric.upper()})

        student = c.fetchone()

        if student == None:
            print()
            print()
            print('***ERROR***')
            print('No such nric')
            print()

        else:
            print(student)


    else:
        print('***ERROR***')

        
            

##print(student_info())















######################################################################################
######################################################################################


def teacher_info():

    db = sqlite3.connect('tuition.db')
    c = db.cursor()
    
    print()
    print('***Teacher Information***')
    print()
    print()
    print('1. List all')
    print('2. List MATH teachers info')
    print('3. List PYHSICS teachers info')
    print('4. List CHEMISTRY teachers info')
    print('5. List BIOLOGY teachers info')
    print('6. List ECONOMICS teachers info')
    print('7. List specific teacher')
    print()
    print()
    print('X. Quit')

    choice = input('Enter your choice:')

    if choice.upper() == 'X':
        return None


    
    #### ALL TEACHER ####
    elif choice == '1':
        c.execute('''SELECT subjects.subject, teachers.TeacherID, teachers.name, teachers.PhoneNo, teachers.email
                    FROM teachers, subjects, class
                    WHERE teachers.TeacherID = class.TeacherID and subjects.SubjectID = class.SubjectID
                    ORDER BY subject ASC;''')
        
        teachers = c.fetchall()
        
        for teacher in teachers:
            print(teacher)
            
        db.commit()
        db.close()


        

    #### MATH TEACHER ####
    elif choice == '2':
        c.execute('''SELECT subjects.subject, teachers.TeacherID, teachers.name, teachers.PhoneNo, teachers.email
                    FROM teachers, subjects, class
                    WHERE teachers.TeacherID = class.TeacherID and subjects.SubjectID = class.SubjectID
                    AND subject = "MATH";''')

        teachers = c.fetchall()
        for teacher in teachers:
            print(teacher)
        
        db.commit()
        db.close()


        

    #### PHYSICS TEACHER ####
    elif choice == '3':
        c.execute('''SELECT subjects.subject, teachers.TeacherID, teachers.name, teachers.PhoneNo, teachers.email
                    FROM teachers, subjects, class
                    WHERE teachers.TeacherID = class.TeacherID and subjects.SubjectID = class.SubjectID
                    AND subject = "PHYSICS";''')

        teachers = c.fetchall()
        for teacher in v:
            print(teacher)
        
        db.commit()
        db.close()


        

    #### CHEM TEACHER ####
    elif choice == '4':
        c.execute('''SELECT subjects.subject, teachers.TeacherID, teachers.name, teachers.PhoneNo, teachers.email
                    FROM teachers, subjects, class
                    WHERE teachers.TeacherID = class.TeacherID and subjects.SubjectID = class.SubjectID
                    AND subject = "CHEMISTRY";''')

        teachers = c.fetchall()
        for teacher in teachers:
            print(teacher)
        
        db.commit()
        db.close()



        
    #### BIO TEACHER ####
    elif choice == '5':
        c.execute('''SELECT subjects.subject, teachers.TeacherID, teachers.name, teachers.PhoneNo, teachers.email
                    FROM teachers, subjects, class
                    WHERE teachers.TeacherID = class.TeacherID and subjects.SubjectID = class.SubjectID
                    AND subject = "BIOLOGY";''')

        teachers = c.fetchall()
        for teacher in teachers:
            print(teacher)
        
        db.commit()
        db.close()


        

    #### ECONS TEACHER ####
    elif choice == '6':
        c.execute('''SELECT subjects.subject, teachers.TeacherID, teachers.name, teachers.PhoneNo, teachers.email
                    FROM teachers, subjects, class
                    WHERE teachers.TeacherID = class.TeacherID and subjects.SubjectID = class.SubjectID
                    AND subject = "ECONOMICS";''')

        teachers = c.fetchall()
        
        for teacher in teachers:
            print(teacher)
        
        db.commit()
        db.close()



        
    #### SPECIFIC TEACHER ####
    elif choice == '7':
        teacher_id = input('Enter teacher ID:')
        
        c.execute('''SELECT subjects.subject, teachers.TeacherID, teachers.name, teachers.PhoneNo, teachers.email
                    FROM teachers, subjects, class
                    WHERE teachers.TeacherID = class.TeacherID and subjects.SubjectID = class.SubjectID
                    AND teachers.TeacherID = :ic;''',
                  {"ic":teacher_id.upper()})

        teacher = c.fetchone()

        if teacher == None:
            print()
            print()
            print('***ERROR***')
            print('No such ID')
            print()

        else:
            print(teacher)

    else:
        print('***ERROR***')


        
        
##teacher_info()
















######################################################################################
######################################################################################




def enrollment():

    db = sqlite3.connect('tuition.db')
    c = db.cursor()
    
    print()
    print('*** ENROLLMENT ***')
    print()
    print(' Are you a current student? ')
    print('1. Yes')
    print('2. No')
    print()
    print()
    print('X. Quit')

    choice = input('Enter your choice:')

    if choice.upper() == 'X':
        return None

    ########### CURRENT STUDENT ##########
    elif choice == '1':
        print()
        class_id = input('Please enter classID:')

        c.execute('''SELECT class.ClassID, subjects.subject, subjects.level,subjects.type, teachers.name, centres.location,
                        class.day, class.start, class.end, subjects.fee
                        FROM class, subjects, teachers, centres
                        WHERE class.CentreID = centres.LocationID AND class.TeacherID = teachers.TeacherID
                        AND  class.SubjectID = subjects.SubjectID AND class.ClassID = :cid;''',
                          {"cid":class_id.upper()})

        classes = c.fetchall()

        for cl in classes:
            print('*****')
            print()
            print(cl[0])
            print(cl[2])
            print(cl[3], cl[1])
            print('Teacher:', cl[4])
            print('Centre:', cl[5])
            print(cl[6], cl[7], 'to', cl[8])
            print('Fee: $', cl[9], '/ month')
            print()

        c.execute('''SELECT COUNT(status = "ACTIVE") FROM enrollment
                    WHERE classID = :cid;''',
                    {"cid":class_id.upper()})

        no = c.fetchone()
        num = no[0]
        
        if num == 5:
            print('Sorry, there is no vacancy')

        elif num < 5:
            print()
            nric = input('Please enter your nric:')
            c.execute('''INSERT INTO enrolllment
                        VALUES (:sid, :cid, NULL, ACTIVE, 0);''',
                      {"sid":nric.upper(), "cid":class_id.upper()})

            print('Thank You!')
            print('You have succesfully enrolled for our class')
            print('See you soon!')




    ######## NEW STUDENT ##############
    elif choice == '2':
        print()
        class_id = input('Please enter classID:')

        c.execute('''SELECT class.ClassID, subjects.subject, subjects.level,subjects.type, teachers.name, centres.location,
                        class.day, class.start, class.end, subjects.fee
                        FROM class, subjects, teachers, centres
                        WHERE class.CentreID = centres.LocationID AND class.TeacherID = teachers.TeacherID
                        AND  class.SubjectID = subjects.SubjectID AND class.ClassID = :cid;''',
                          {"cid":class_id.upper()})

        classes = c.fetchall()

        for cl in classes:
            print('*****')
            print()
            print(cl[0])
            print(cl[2])
            print(cl[3], cl[1])
            print('Teacher:', cl[4])
            print('Centre:', cl[5])
            print(cl[6], cl[7], 'to', cl[8])
            print('Fee: $', cl[9], '/ month')
            print()

        c.execute('''SELECT COUNT(status = "ACTIVE") FROM enrollment
                    WHERE classID = :cid;''',
                    {"cid":class_id.upper()})

        no = c.fetchone()
        num = no[0]

        if num == 5:
            print('Sorry, there is no vacancy')

        elif num < 5:
        
            print()
            nric = input('Please enter your nric:')
            print()
            name = input('Please enter your full name:')
            print()
            email = input('Please enter your email:')
            print()
            gender = input('Gender [M/F]:')
            print()
            level = input('Level [JC/SEC]:')
            print()

            c.execute('''INSERT INTO students
                        VALUES (:nric, :name, :gender, :level, :email);''',
                        {"nric":nric.upper(), "name":name, "gender":gender.upper(), "level":level.upper(), "email":email})

            db.commit()
            db.close()

        
    else:
        print('*** ERROR ***') 
        
        
            

        


##enrollment()













######################################################################################
######################################################################################


def drop():
    
    db = sqlite3.connect('tuition.db')
    c = db.cursor()

    print()
    print('*** DROP CLASS ***')
    print()
    print()
    print('Are you sure?')
    print()
    print('1. Yes')
    print()
    print('X. Quit')

    choice = input('Enter your choice:')

    if choice == '1':
        nric = input('Please enter your NRIC:')
        print()
        class_id = input('Please enter your classID:')
        print()

        c.execute('''UPDATE enrollment SET status = "STOP"
                WHERE StudentID = :sid AND ClassID = :cid;''',
                  {"sid":nric.upper(), "cid":class_id.upper()})

        print('Thank You!')

    elif choice.upper() == 'X':
        return None
        
    else:
        print('*** ERROR ***') 
    














                 

######################################################################################
######################################################################################

def fee():
    db = sqlite3.connect('tuition.db')
    c = db.cursor()

    print()
    print('*** FEES ***')
    print()
    print()
    print('Do you want to pay your fees?')
    print()
    print('1. Yes')
    print()
    print('X. Quit')

    choice = input('Enter your choice:')

    if choice == '1':
        nric = input('Please enter your NRIC:')
        print()
        class_id = input('Please enter your classID:')
        print()
        num = input('I am paying: $')

        c.execute('''UPDATE enrollment SET OutstandingFee = OutstandingFee - :num
                    WHERE StudentID = :sid AND ClassID = :cid;''',
                  {"sid":nric.upper(), "cid":class_id.upper(), "num":int(num)})

        c.execute('''SELECT COUNT(OutstandingFee) FROM enrollment
                    WHERE StudentID = :sid;''',
                  {"sid":nric.upper(), "cid":class_id.upper()})

        remain = c.fetchone()
        print('You owe: $', remain[0])

        db.commit()
        db.close()


    elif choice.upper() == 'X':
        return None
        
    else:
        print('*** ERROR ***')   
    
##fee()















######################################################################################
######################################################################################


def update_fee():

    db = sqlite3.connect('tuition.db')
    c = db.cursor()
    
    print()
    print('*** UPDATE FEES ***')
    print()
    print('Update fees for all student for the last month')
    print()
    print('Are you sure?')
    print()
    print('1. Yes')
    print()
    print('X. Quit')

    choice = input('Please enter your choice:')
    
    if choice == 1:
    
        c.execute('''SELECT subjects.SubjectID, fee.fee, class.ClassID 
                    FROM subjects, class, fee
                    WHERE subjects.SubjectID = class.SubjectID AND subjects.type = fee.type;''')

        info = c.fetchall()

        for sid, fee, cid in info:
            #print('sid:', sid)
            #print('fee:', fee)
            #print('cid:', cid)
            c.execute('''UPDATE enrollment SET OutstandingFee = OutstandingFee + :fee
                        WHERE ClassID = :cid;''',
                      {"cid":cid, "fee":fee})

        db.commit()
        db.close()

    elif choice.upper() == 'X':
        return None

    else:
        print('*** ERROR ***')        
        

    

##update_fee()


















######################################################################################
######################################################################################


def update_grade():

    db = sqlite3.connect('tuition.db')
    c = db.cursor()
    
    print()
    print('***** UPDATE STUDENT GRADE *****')
    print()
    print()
    classid = input('Enter classID:')
    print()
    nric = input('Enter student NRIC:')
    print()
    grade = input('Updated grade:')

    c.execute('''UPDATE enrollment SET grade = :grade
                WHERE ClassID = :cid AND StudentID = :sid;''',
                {"grade":grade.upper(), "cid":classid.upper(), "sid":nric.upper()})

    c.execute('''SELECT students.name, enrollment.ClassID ,enrollment.grade 
                FROM students, enrollment
                WHERE  students.nric = enrollment.StudentID AND 
                enrollment.ClassID = :cid AND
                enrollment.StudentID = :sid;''',
                {"grade":grade.upper(), "cid":classid.upper(), "sid":nric.upper()})

    u = c.fetchone()
    
    print()
    print('*****')
    print(u[1])
    print(u[0])
    print('Updated grade:', u[2])
    print()
    print('*****')
    

    db.commit()
    db.close()

    print('Thank You!')

    




##update_grade()














######################################################################################
######################################################################################


def delete_data():

    db = sqlite3.connect('tuition.db')
    c = db.cursor()

    print()
    print(' ***** DELETE DATA *****')
    print()
    print()
    print('Delete data of all inactive student')
    print()
    print('Are you sure?')
    print()
    print('1. Yes')
    print()
    print()
    print('X. Quit')
    print()



    choice = input('Enter your choice:')

    if choice == '1':
        c.execute('''DELETE FROM enrollment WHERE status = "STOP";''')
        
        print('Thank You!')

    elif choice.upper() == 'X':
        return None

    else:
        print('*** ERROR ***')
                  
    















######################################################################################
######################################################################################

from creating_tuition_database  import *

from centres_table import * 
from class_table import * 
from enrollment_table import * 
from students_table import * 
from subjects_table import *
from fee_table import *
from teachers_table import * 

from import_class import * 
from import_enrollment import * 
from import_centres import * 
from import_students import * 
from import_subjects import *
from import_fee import *
from import_teachers import * 

def reset_db():

    print()
    print('*** RESET DATABSE ***')
    print()
    print()
    print('Are you sure?')
    print()
    print('1. Yes')
    print()
    print('X. Quit')

    choice = input('Please enter your choice:')

    if choice == '1':
    
        #create db
        create_tuition_db()

        #create table
        add_table_students()
        add_table_teachers()
        add_table_subjects()
        add_table_centres()
        add_table_class()
        add_table_fee()
        add_table_enrollment()

        #import csv
        import_csv_students()
        import_csv_teachers()
        import_csv_subjects()
        import_csv_centres()
        import_csv_class()
        import_csv_fee()
        import_csv_enrollment()

    elif choice.upper() == 'X':
        return None

    else:
        print('*** ERROR ***')




######################################################################################
######################################################################################






