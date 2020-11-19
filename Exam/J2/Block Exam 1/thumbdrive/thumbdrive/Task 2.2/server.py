from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")
	
@app.route('/form', methods=['POST'])
def form():
    if request.method == 'POST':
        name = request.form.get('name')
        print(f'name: {name}')
        email = request.form.get('email')
        print(f'email: {email}')

        if name == None or name == '':
            return render_template('index.html')

        if email == None or email == '':
            return render_template('index.html')

            
    return render_template('success.html', name = name, email = email)

app.run(debug=True, port=5000)
