from flask import Flask, render_template, request
import sqlite3
import csv_db
from class_reader import display_student_class, get_classID

app = Flask(__name__)
 
@app.route('/')
def index():
    return render_template('index.html')



@app.route('/display_class')
def display_class():
    # header for html table
    header = 'classID,Subject,Level,Teacher,Location,Day,Start,End,Fee'
    header = header.split(',')

    db = sqlite3.connect('tuition.db')
    c = db.cursor()

    c.execute('''SELECT * FROM class''')
    information = c.fetchall()

    return render_template('class.html', header=header, information=information)




###### Registration Form #####


@app.route('/register', methods=['GET'])
def register():
    classID = get_classID()
    return render_template('register.html', classID=classID)


@app.route('/validate_register', methods=['POST'])
def validate_register():
    if request.method == 'POST':
        name = request.form.get('name')
        nric = request.form.get('nric').upper()
        email = request.form.get('email')
        tel = request.form.get('tel')
        classID = request.form.get('classID')
        password = request.form.get('password')

        info = [nric, name, email, tel, password]
        enroll = [nric, classID]

    # header for student info table
    header = 'NRIC,Name,Email,Telephone,Password'
    header = header.split(',')


    db = sqlite3.connect('tuition.db')
    c = db.cursor()

    # check if nric not in db
    c.execute('''SELECT * FROM student WHERE nric = :nric''', {'nric':nric})
    check = c.fetchone()
    if check != None:
        classID = get_classID()
        warning = 'This if for new users, login if you are a current student'
        return render_template('register.html', warning = warning, classID = classID)


    # add student info into student table
    c.execute('''INSERT INTO student (nric, name, email, tel, password)
            VALUES (:nric, :name, :email, :tel, :password)''', info)

    print('student info added')
    db.commit()

    # enroll student in enrollment table
    c.execute('''INSERT INTO enrollment (nric, classID) VALUES (:nric, :classID)''', enroll)
    print('student enrolled in enrollment table')
    db.commit()


    # retrieve student info
    c.execute('''SELECT * FROM student WHERE nric = :nric''', {'nric':nric})
    student = c.fetchone()

    # to display student class information
    header2 = 'Subject,Level,Teacher,Location,Day,Start,End,Fee'
    header2 = header2.split(',')
    
    student_class = display_student_class(nric)
    # print(student_class)

    return render_template('welcome.html', name=name, header_student=zip(header, student), 
                            header2 = header2, class_information = student_class)








##### Login Form #####


@app.route('/login', methods=['GET'])
def login():
    return render_template('login.html')


@app.route('/validate_login', methods=['POST'])
def validate_login():
    if request.method == 'POST':
        nric = request.form.get('nric').upper()
        password = request.form.get('password')

    # header for student info table
    header = 'NRIC,Name,Email,Telephone,Password'
    header = header.split(',')

    # connect to db
    db = sqlite3.connect('tuition.db')
    c = db.cursor()

    c.execute('''SELECT * FROM student WHERE nric = :nric 
                AND password = :password''', {'nric':nric, 'password':password})
    student = c.fetchone()
    # print(student)  

    if student == None:
        warning = 'Please enter the correct NRIC / Password'
        return render_template('login.html', warning = warning)

    else:
        name = student[1]

    # to display student class information
    header2 = 'Subject,Level,Teacher,Location,Day,Start,End,Fee'
    header2 = header2.split(',')
    
    student_class = display_student_class(nric)
    # print(student_class)


    return render_template('welcome.html', name=name, header_student=zip(header, student), 
                            header2 = header2, class_information = student_class)



@app.route('/register_new', methods=['POST', 'GET'])
def register_new():
    classID = get_classID()
    return render_template('register_new.html', classID = classID)


@app.route('/validate_register_new', methods=['POST'])
def validate_register_new():
    if request.method == 'POST':
        nric = request.form.get('nric')
        classID = request.form.get('classID')
        info = [nric, classID]
    
    print('---------- VALIDATING INFORMATION ----------')
    print()
    print()

    db = sqlite3.connect('tuition.db')
    c = db.cursor()

    c.execute('''INSERT INTO enrollment (nric, classID) VALUES (:nric, :classID)''', info)
    db.commit()

    classID = get_classID()

    return render_template('register_new.html', classID = classID, \
                            registered = 'You have succesfully registered')


# csv_db.main()
app.run(debug=True, port=5000)

