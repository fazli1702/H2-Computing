from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/hello', methods=['GET', 'POST'])
def hello():
    if request.method == 'GET':
        return 'Please submit the form instead.'
    else:
        username = request.form.get('name')
        return render_template('hello.html', display=username)


app.run(debug=True, port=5000)
# launch web browser with url 1 27.0.0.1:5000
