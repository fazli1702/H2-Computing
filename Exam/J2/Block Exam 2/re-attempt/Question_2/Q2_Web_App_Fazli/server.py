from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)

matricNo = 0


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/form', methods=['POST'])
def form():
    if request.method == 'POST':
        global matricNo
        matricNo = request.form.get('matricNo')

        # reject empty or null inputs
        if matricNo == '' or matricNo == None:
            warning = 'please enter your matriculation number'
            return render_template('index.html', warning=warning)

        db = sqlite3.connect('school.db')
        c = db.cursor()

        c.execute('''
        SELECT Student.MatricNo, Student.Name, Student.Gender, Student.CivicsClass,
        Civics.Tutor, Civics.HomeRoom, StudentCCA.CCAName, CCAInfo.TeacherIC
        FROM Student, Civics, CCAInfo, StudentCCA
        WHERE Student.MatricNo = (:mat) 
        AND Student.CivicsClass = Civics.Class
        AND StudentCCA.MatricNo = Student.MatricNo
        AND StudentCCA.CCAName = CCAInfo.Name
        ''', matricNo)
        info = c.fetchone()
        # print(info)

    return render_template('info.html', info=info)




@app.route('/cca', methods=['POST'])
def cca():
    if request.method == 'POST':

        change_cca = request.form.get('change')

        if change_cca == 'N':
            return render_template('the_end.html')

        elif change_cca == 'Y':
            db = sqlite3.connect('school.db')
            c = db.cursor()
            c.execute('''SELECT Name FROM CCAInfo''')
            data = c.fetchall()
            return render_template('cca.html', data=data)



@app.route('/update', methods=['POST'])
def update():
    if request.method == 'POST':
        global matricNo
        newCCA = request.form.get('cca')

        db = sqlite3.connect('school.db')
        c = db.cursor()

        c.execute('''UPDATE StudentCCA SET CCAName = (:newCCA) WHERE MatricNo = (:MatricNo)''', [newCCA, matricNo])
        db.commit()

        c.execute('SELECT * FROM StudentCCA WHERE MatricNo=(:MatricNo)', matricNo)
        matNo, cca = c.fetchone()
        

        return render_template('success.html', matNo=matNo, cca=cca)





app.run(debug=True, port=5000)