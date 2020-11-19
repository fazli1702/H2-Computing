from flask import Flask, request, render_template
import sqlite3

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process', methods=['POST', 'GET'])
def process():
    if request.method == 'POST':
        Class = request.form.get('Class').upper()

        db = sqlite3.connect('result_mgm.db')
        c = db.cursor()

        c.execute('''SELECT Class, IndexNo, Name, Gender, MatricNo 
                    FROM Student WHERE Class = :class''', {'class':Class})
        info = c.fetchall()


    return render_template('Task_4_4.html', info=info)


app.run(debug=True, port=5000)
