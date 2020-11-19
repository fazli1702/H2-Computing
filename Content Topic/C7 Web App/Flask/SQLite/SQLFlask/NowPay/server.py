from flask import Flask, render_template, request
from datetime import datetime
import sqlite3

app = Flask(__name__)

db = sqlite3.connect('account.db')


#variable
currDate = datetime.today().strftime("%d/%m/%Y")
currTime = datetime.today().strftime("%H:%M:%S")
global total
total = 0

@app.route('/')
def index():
    '''display all available books'''
    db = sqlite3.connect('account.db')
    c = db.cursor()
    c.execute('''SELECT * FROM books''')
    books = c.fetchall()
    return render_template('index.html', books=books)




@app.route('/validate', methods=['POST'])
def validate():
    global total
    db = sqlite3.connect('account.db')
    c = db.cursor()
    if request.method == 'POST':
        purchase = []
        a = request.form.getlist('bookInfo')
        for i in a:
            i = int(i)
            c.execute('''SELECT Title, Price FROM  Books WHERE BookID = :id''', {"id":i})
            book = c.fetchone()
            total += book[1]
            purchase.append(book)
        return render_template('validate.html', date=currDate, time=currTime, purchase=purchase, total=total)



@app.route('/check', methods=['POST'])
def check():
    global total
    success = ''
    db = sqlite3.connect('account.db')
    c = db.cursor()
    if request.method == 'POST':
        name = request.form.get('name')
        password = request.form.get('password')
        c.execute('''SELECT balance FROM Account WHERE Name = :name''', {"name":name})
        balance = c.fetchone()
        #print('balance', type(balance), balance)
        #print(balance[0])
        #print('total', total)
        if balance[0] > total:
            success = 'successful'
        else:
            success = 'unsuccessful'   
            
    return render_template('check.html', success=success)



db.close()
app.run(debug=True, port=5000)
