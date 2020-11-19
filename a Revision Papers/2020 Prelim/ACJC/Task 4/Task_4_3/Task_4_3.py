from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/service_status', methods=['POST', 'GET'])
def service_status():
    if request.method == 'POST':
        status = request.form.get('status')  # user input
        
        db = sqlite3.connect('records.db')
        c = db.cursor()

        c.execute('''SELECT Employee_name FROM Employee
                    WHERE Service_Status = ?
                    ORDER BY Employee_name ASC''', [status])
        names = c.fetchall()

        return render_template('status.html', names=names)
        

app.run(debug=True, port=5000)
