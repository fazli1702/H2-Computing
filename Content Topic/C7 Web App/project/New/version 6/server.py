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






# ------------------------ ADMIN PAGE ------------------------------- #


@app.route('/admin_login', methods = ['GET'])
def admin_login():
    return render_template('admin_login.html')


@app.route('/admin', methods=['POST'])
def admin():
    if request.method == 'POST':
        password = request.form.get('password')

        if password != 'admin':
            warning = 'Please enter the correct password'
            return render_template('admin_login.html', warning = warning)

    students = [(ele[0], ele[1], ele[3]) for ele in get_all_student_info()]
    # print(students)

    return render_template('admin.html', students=students)


@app.route('/admin/<nric>')
def admin_student_info(nric):
    NRIC = nric
    info = [NRIC, get_student_password(NRIC)]
    student = get_student_info(info)

    # student perosnal info table
    header1 = 'NRIC,Name,Email,Telephone,Password'
    header1 = header1.split(',')        

    # student class information
    header2 = 'classID,Subject,Level,Teacher,Location,Day,Start,End,Fee'
    header2 = header2.split(',')
    student_classes = get_student_class_info(NRIC)
    # print(student_classes)


    return render_template('admin_student_info.html', nric = NRIC , header_student = zip(header1, student),\
                            header2 = header2, student_classes = student_classes,\
                            fees = get_student_fees(NRIC))




# ----------------------- LOGIN PAGE -------------------------- #


@app.route('/login', methods=['GET'])
def login():
    return render_template('login.html')




@app.route('/welcome-validate_login', methods=['POST'])
def validate_login():
    if request.method == 'POST':
        nric = request.form.get('nric').upper()
        password = request.form.get('password')
        info = [nric, password]

        # handle wrong input
        if nric not in get_nric() or password != get_student_password(nric):
            warning = 'Please enter the correct NRIC / Password'
            return render_template('login.html', warning = warning)

        student = get_student_info(info)
        name = student[1]

        # student perosnal info table
        header1 = 'NRIC,Name,Email,Telephone,Password'
        header1 = header1.split(',')        

        # student class information
        header2 = 'classID,Subject,Level,Teacher,Location,Day,Start,End,Fee'
        header2 = header2.split(',')
        student_classes = get_student_class_info(nric)
        # print(student_classes)


    return render_template('welcome.html', name = name, header_student = zip(header1, student),\
                            header2 = header2, student_classes = student_classes,\
                            fees = get_student_fees(nric), nric = nric, \
                            password = password)





# ----------------------- REGISTER PAGE -------------------------- #


@app.route('/register', methods=['GET'])
def register():
    classID = get_classID()
    return render_template('register.html', classID = classID)




@app.route('/welcome-validate_register', methods=['POST'])
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
        header2 = 'classID,Subject,Level,Teacher,Location,Day,Start,End,Fee'
        header2 = header2.split(',')
        student_classes = get_student_class_info(nric)
        # print(student_classes)


    return render_template('welcome.html', name = name, header_student = zip(header1, student),\
                            header2 = header2, student_classes = student_classes,\
                            fees = get_student_fees(nric), nric = nric, \
                            password = password)



# ----------------- WELCOME ---------------------- #

@app.route('/register_new', methods=['GET'])
def register_new():
    return render_template('register_new.html', classID = get_classID())




@app.route('/welcome', methods=['GET', 'POST'])
def welcome():
    '''
    same as validate login/register
    welcome.html
    '''
    if request.method == 'POST':
        nric = request.form.get('nric').upper()
        classID = request.form.get('classID')
        password = request.form.get('password')

        # check if student not already enrolled
        if check_enrollment(nric, classID):
            warning = 'Please register for a new class'
            return render_template('register_new.html', warning = warning, classID = get_classID())
        
        # check for correct nric / password
        elif nric not in get_nric() or password != get_student_password(nric):
            warning = 'Please enter the correct NRIC / Password'
            return render_template('register_new.html', warning = warning, classID = get_classID())

        enroll_student([nric, classID])

        info = [nric, password]
        student = get_student_info(info)
        name = student[1]

        # student perosnal info table
        header1 = 'NRIC,Name,Email,Telephone,Password'
        header1 = header1.split(',')        

        # student class information
        header2 = 'classID,Subject,Level,Teacher,Location,Day,Start,End,Fee'
        header2 = header2.split(',')
        student_classes = get_student_class_info(nric)

        return render_template('welcome.html', name = name, header_student = zip(header1, student),\
                            header2 = header2, student_classes = student_classes,\
                            fees = get_student_fees(nric), nric = nric, \
                            password = password)





@app.route('/welcome/payment', methods=['GET'])
def payment():
    fees = request.args.get('Fees')
    nric = request.args.get('NRIC')
    password = request.args.get('password')
    # print('welcome->payment:', fees, nric, password)
    return render_template('payment.html', fees = fees)


@app.route('/welcome-validate_payment', methods=['POST'])
def validate_payment():
    if request.method == 'POST':
        nric = request.form.get('nric').upper()
        password = request.form.get('password')
        # print('payment -> validate payment:', nric, password)
    

    info = [nric, password]
    student = get_student_info(info)
    name = student[1]

    # student perosnal info table
    header1 = 'NRIC,Name,Email,Telephone,Password'
    header1 = header1.split(',')        

    # student class information
    header2 = 'classID,Subject,Level,Teacher,Location,Day,Start,End,Fee'
    header2 = header2.split(',')
    student_classes = get_student_class_info(nric)

    return render_template('welcome.html', name = name, header_student = zip(header1, student),\
                        header2 = header2, student_classes = student_classes,\
                        fees = 0, nric = nric, \
                        password = password)




def main():
    # csv_db.main()
    app.run(debug=True, port=5000)

if __name__ == "__main__":
    main()
