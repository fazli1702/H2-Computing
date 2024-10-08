from flask import Flask, render_template, request
import sqlite3
# my own helper function
from helper import *
import csv_db

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')



@app.route('/classes', methods=['GET', 'POST'])
def classes():
    '''DISPLAY INFORMATION FOR ALL CLASSES'''

    # form
    subjets = 'None,Math,Physics,Chemistry'
    subjets = subjets.split(',')

    locations = 'None,Jurong,Tampines,Woodlands,Yishun'
    locations = locations.split(',')

    days = 'None,Monday,Tuesday,Wednesday,Thursday,Friday,Saturday,Sunday'
    days = days.split(',')

    header = 'classID,Subject,Level,Teacher,Location,Day,Start,End,Fee'
    header = header.split(',')

    if request.method == 'POST':
        subject = request.form.get('subject')
        location = request.form.get('location')
        day = request.form.get('day')
        # print(subject, day, location)
        information = filter_class_table(subject, location, day)
        return render_template('classes.html', header=header, information=information, \
                            subjects = subjets, days = days, locations = locations)

    return render_template('classes.html', header=header, information=get_class_info(), \
                            subjects = subjets, days = days, locations = locations)







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

        # handle wrong input
        if nric not in get_nric() or password != get_password(nric):
            warning = 'Please enter the correct NRIC / Password'
            return render_template('login.html', warning = warning)

        student = get_student_info(info)
        name = student[1]

        # student perosnal info table
        header1 = 'NRIC,Name,Email,Telephone,Password'
        header1 = header1.split(',')        

        # student class information
        header2 = 'Subject,Level,Teacher,Location,Day,Start,End,Fee'
        header2 = header2.split(',')
        student_classes = get_student_class_info(nric)
        # print(student_classes)


    return render_template('welcome.html', name = name, header_student = zip(header1, student),\
                            header2 = header2, student_classes = student_classes)





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

        # hadling wrong input
        if nric in get_nric():
            warning1 = 'This is for new users, login if you are a current student'
            return render_template('register.html', warning=warning1, classID=get_classID())

        # ensure there is no blank
        elif '' in [name, nric, email, tel, classID, password]:
            warning2 = 'Please fill up all the relevant information'
            return render_template('register.html', warning=warning2, classID=get_classID())

        else:
            # add student info into db
            info = [nric, name, email, tel, password]
            add_student(info)

            # enroll student in db
            enroll = [nric, classID]
            enroll_student(enroll)

        
        student = [name, nric, email, tel, password]

        # student perosnal info table
        header1 = 'NRIC,Name,Email,Telephone,Password'
        header1 = header1.split(',')        

        # student class information
        header2 = 'Subject,Level,Teacher,Location,Day,Start,End,Fee'
        header2 = header2.split(',')
        student_classes = [get_class_info(classID)[1:]]
        # print(student_classes)


    return render_template('welcome.html', name = name, header_student = zip(header1, student),\
                            header2 = header2, student_classes = student_classes)



# ----------------- WELCOME ---------------------- #

@app.route('/register_new', methods=['GET'])
def register_new():
    pass




@app.route('/welcome', methods=['GET', 'POST'])
def welcome():
    pass






def main():
    # csv_db.main()
    app.run(debug=True, port=5000)

main()