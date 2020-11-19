from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/hello')
def hello():
    return render_template('hello.html')

app.run(debug=True, port=5000)
# launch web browser with url 1 27.0.0.1:5000
