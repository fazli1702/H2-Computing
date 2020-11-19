from flask import Flask, render_template, request
import sqlite3
from helper import *
import csv_db

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')



@app.route('/classes', methods=['GET'])
def classes():
    '''DISPLAY INFORMATION FOR ALL CLASSES'''
    header = 'classID,Subject,Level,Teacher,Location,Day,Start,End,Fee'
    header = header.split(',')

    db = sqlite3.connect('tuition.db')
    c = db.cursor()

    c.execute('''SELECT * FROM class''')
    information = c.fetchall()

    return render_template('classes.html', header=header, information=information)







# ----------------------- LOGIN PAGE -------------------------- #


@app.route('/login', methods=['GET'])
def login():
    return render_template('login.html')

@app.route('/validate_login', methods=['POST'])
def validate_login():
    if request.method == 'POST':
        nric = request.form.get('nric').upper()
        password = request.form.get('password')
        info = [nric, password]
        
        student = get_student_info(info)
        print(student)
        name = student[1]

    return render_template('welcome.html', name = name)







# ----------------------- REGISTER PAGE -------------------------- #


@app.route('/register', methods=['GET'])
def register():
    classID = get_classID()
    return render_template('register.html', classID = classID)

@app.route('/validate_register', methods=['POST'])
def validate_register():
    if request.method == 'POST':
        name = request.form.get('name')
        nric = request.form.get('nric').upper()
        email = request.form.get('email')
        tel = request.form.get('tel')
        classID = request.form.get('classID')
        password = request.form.get('password')

        # add student info into db
        info = [nric, name, email, tel, password]
        add_student(info)

        # enroll student in db
        enroll = [nric, classID]
        enroll_student(enroll)



    return render_template('welcome.html', name=name)


def main():
    csv_db.main()
    app.run(debug=True, port=5000)

main()