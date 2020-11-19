from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/activites', methods=['POST', 'GET'])
def activities():
    db = sqlite3.connect('register.db')
    c = db.cursor()
    if request.method == 'POST':
        studentID = request.form.get('studentID')
        Type = request.form.get('Type')
        venue = request.form.get('venue')
        session = request.form.get('session')

        c.execute('''INSERT INTO Registration VALUES (?,?,?,?)''',
                          [studentID, Type, venue, session])
        db.commit()

        if Type == 'A':
            performance = request.form.get('performance')
            c.execute('INSERT INTO Arts VALUES (?,?)', [studentID, performance])
            db.commit()

        elif Type == 'C':
            race = request.form.get('race')
            c.execute('INSERT INTO Cultural VALUES (?,?)', [studentID, race])
            db.commit()

        elif Type == 'S':
            contact = request.form.get('contact')
            cost = request.form.get('cost')
            c.execute('INSERT INTO Sports VALUES (?,?,?)',
                      [studentID, contact, cost])
            db.commit()

        


    db.close()
    return render_template('index.html')


@app.route('/report', methods=['POST', 'GET'])
def report():
    db = sqlite3.connect('register.db')
    c = db.cursor()
    if request.method == 'POST':
        c.execute('''SELECT StudentID, Type FROM Registration
                    WHERE Session = "AM"''')
        data = c.fetchall()
    db.close()
    return render_template('activities.html', data=data)

app.run(debug=True, port=5000)
