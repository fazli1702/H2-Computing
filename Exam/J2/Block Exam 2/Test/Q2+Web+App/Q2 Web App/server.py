from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)

mat_no = 0

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/form', methods=['POST'])
def form():
    if request.method == 'POST':
        global mat_no
        mat_no = request.form.get('mat_no')

        # connect to db
        db = sqlite3.connect('school.db')
        c = db.cursor()

        # reject empty/null input
        if mat_no == None or mat_no == '':
            warning = 'Please enter your Matriculation  number'
            return render_template('index.html', warning=warning)


        c.execute('''SELECT Student.MatricNo, Student.Name, Student.Gender,
                Student.CivicsClass, Civics.Tutor, Civics.HomeRoom,
                CCAInfo.Name, CCAInfo.TeacherIC
                FROM Student, StudentCCA, Civics, CCAInfo 
                WHERE Student.MatricNo = (:matric_no) AND StudentCCA.MatricNo = Student.MatricNo
                AND StudentCCA.CCAName = CCAInfo.Name
                AND Civics.Class = Student.CivicsClass''', {'matric_no':mat_no})
        info = c.fetchone()

    return render_template('info.html', info=info)


@app.route('/cca', methods=['POST'])
def cca():
    change_cca = request.form.get('change')
    if change_cca == 'N':
        return render_template('the_end.html')
    elif change_cca == 'Y':
        db = sqlite3.connect('school.db')
        c = db.cursor()
        c.execute('''SELECT name FROM CCAInfo''')
        data = c.fetchall()
        return render_template('cca.html', data=data)


@app.route('/update', methods=['POST'])
def update():
    if request.method == 'POST':
        global mat_no
        cca = request.form.get('cca')
        print(cca)

        db = sqlite3.connect('school.db')
        c = db.cursor()

        c.execute('''UPDATE StudentCCA SET CCAName = (:cca) WHERE MatricNo = (:mat_no)
                    ''', {'cca':cca, 'mat_no':mat_no})
        db.commit()

        return render_template('success.html', mat_no=mat_no, new_cca=cca)
        

app.run(debug=True, port=5000)
