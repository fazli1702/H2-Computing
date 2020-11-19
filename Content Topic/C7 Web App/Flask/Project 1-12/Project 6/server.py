from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    display ='Hello World! (using jinja code in html)'
    return render_template('index.html', headline=display)

@app.route('/goodbye') # 127.0.0.1:5000/goodbye
def goodbye():
    display = 'Goodbye!'
    return render_template('index.html', headline=display)
    

app.run(debug=True, port=5000)
# launch web browser with url 127.0.0.1:5000
