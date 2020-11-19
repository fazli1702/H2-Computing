from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/location', methods=['POST', 'GET'])
def location():
    if request.method == 'POST':
        location = request.form.get('location')

        db = sqlite3.connect('bakery.db')
        c = db.cursor()

        c.execute('''SELECT Name, Type, Price FROM Product WHERE Location=?
                     ORDER BY Price ASC''', [location])
        data = c.fetchall()

        return render_template('location.html', data=data)


app.run(debug=True, port=5000)
