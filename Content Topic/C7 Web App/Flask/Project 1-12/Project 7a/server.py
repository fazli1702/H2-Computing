from flask import Flask, render_template
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def index():
    #is is nex year day?
    now = datetime.now()
    display = now.month == 1 and now.day == 1
    return render_template('index.html', headline=display)
    

app.run(debug=True, port=5000)
# launch web browser with url 127.0.0.1:5000
