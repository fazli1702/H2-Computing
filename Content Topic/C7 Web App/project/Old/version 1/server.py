from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)
 
@app.route('/')
def index():
    return render_template('index.html')


@app.route('/register', methods=['GET'])
def register():
    return render_template('register.html')

	

@app.route('/login', methods=['GET'])
def login():
    return render_template('login.html')


@app.route('/validate_login', methods=['POST'])
def validate_login():
    if request.method == 'POST':
        nric = request.form.get('nric')
        password = request.form.get('password')

    return render_template('welcome.html')


@app.route('/validate_reegister', methods=['POST'])
def validate_register():
    if request.method == 'POST':
        name = request.form.get('name')
        nric = request.form.get('nric')
        email = request.form.get('email')
        tel = request.form.get('tel')
        subject = request.form.get('subject')
        password = request.form.get('password')

    return render_template('welcome.html')

	
	
app.run(debug=True, port=5000)


