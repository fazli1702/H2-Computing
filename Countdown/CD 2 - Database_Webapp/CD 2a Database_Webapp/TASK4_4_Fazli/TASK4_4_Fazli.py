from flask import Flask, request, render_template
import sqlite3

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def process():
    # process given information
    #  display a table showing the SerialNumber and Type

    if request.method == 'POST':
        location = request.form.get('location')

        db = sqlite3.connect('equipment.db')
        c = db.cursor()
        c.execute('''SELECT SerialNumber, Type FROM Device WHERE Location = (:location)''', [location])
        data = c.fetchall()

        return render_template('TASK4_4_Fazli.html', Data=data)

app.run(port=5000, debug=True)
