from flask import Flask, render_template, request

app = Flask(__name__)

import sqlite3
db = sqlite3.connect('pricelist.db')

@app.route('/')
def index():
    db = sqlite3.connect('pricelist.db')
    c = db.cursor()
    c.execute('''SELECT id, description, price FROM components''')
    data = c.fetchall()
    return render_template("index.html", data=data)

@app.route('/order', methods=['POST'])
def order():
    if request.method == 'POST':
        order = request.form.get('order')
        quantity = request.form.get('quantity')

        db = sqlite3.connect('pricelist.db')
        c = db.cursor()

        c.execute('''INSERT INTO myorder(item, qty) VALUES(:item, :qty)''',
                  {'item':order, 'qty':quantity})
        db.commit()
        

    return render_template('success.html', item=order, quantity=quantity)

app.run(debug=True, port=5000)
