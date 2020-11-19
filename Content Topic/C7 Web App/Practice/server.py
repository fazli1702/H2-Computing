from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)


##def create():
##    db = sqlite3.connect('student.db')
##    c = db.cursor()
##
##    try:
##        c.execute('''CREATE TABLE student(
##                        name VARCHAR(50),
##                        class VARCHAR(5),
##                        gender CHAR(1))''')
##    except:
##        print('table exist')



@app.route('/', methods=['POST'])
def index():
    if request.method == 'POST':
        name = request.form.get('name')
        clss = request.form.get('class')
        gender = request.form.get('gender')
        info = [name, clss, gender]
        print(info)

              
    return 'hello world'


app.run(debug=True, port=5000)
