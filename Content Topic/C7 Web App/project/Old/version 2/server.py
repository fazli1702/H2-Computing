from flask import Flask, render_template, request
import sqlite3
import csv_db


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







@app.route('/register', methods=['GET'])
def register():
    db = sqlite3.connect('tuition.db')
    c = db.cursor()

    c.execute('''SELECT classID FROM class''')
    classID = c.fetchall()

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
    name = student[1]

    return render_template('welcome.html', name=name, header_student=zip(header, student))






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
    

    db = sqlite3.connect('tuition.db')
    c = db.cursor()

    c.execute('''SELECT * FROM student WHERE nric = :nric 
                AND password = :password''', {'nric':nric, 'password':password})
    student = c.fetchone()
    # print(student)  
    name = student[1]


    return render_template('welcome.html', name=name, header_student=zip(header, student))



# csv_db.main()
app.run(debug=True, port=5000)


