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

app.run(debug=True, port=5000)
