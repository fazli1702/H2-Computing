from flask import Flask, request, render_template
import sqlite3

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process', methods=['POST', 'GET'])
def process():
    if request.method == 'POST':
        school = request.form.get('school')
        department = request.form.get('department')

        db = sqlite3.connect('schools.db')
        c = db.cursor()

        c.execute('''SELECT School.Name, Staff.Name, Staff.Department,
                    Staff.contact, School.Address
                    FROM School, Staff
                    WHERE School.Name LIKE :school AND
                    Staff.Department = :department''',
                  {'school':'%'+school+'%', 'department':department})
        data = c.fetchall()

        return render_template('output.html', data=data)
        
        


app.run(debug=True, port=5000)
