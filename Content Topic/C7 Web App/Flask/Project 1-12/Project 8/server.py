from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    names = ['Alice', 'Bob', 'Charlie']
    return render_template('index.html', namelist=names)

    

app.run(debug=True, port=5000)
# launch web browser with url 127.0.0.1:5000
