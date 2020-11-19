from flask import Flask

app = Flask(__name__)

@app.route('/')

def index():
    return 'Hello World!(1)'


@app.route('/fazli') # url 127.0.0.1:5000/david
def fazli():
    return 'Hello Fazli!'



app.run(debug=True, port=5000)
# launch web browser with url 127.0.0.1:5000
