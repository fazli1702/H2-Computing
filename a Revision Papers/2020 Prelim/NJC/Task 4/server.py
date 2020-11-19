from flask import Flask, render_template, request
import sqlite3
from datetime import datetime

app = Flask(__name__)


def get_date_time():
    now = datetime.now()
    curr_date = now.strftime('%Y/%m/%d')
    curr_time = now.strftime('%H:%M')
    return curr_date, curr_time

@app.route('/<string:locationID>')
def index(locationID):
    return render_template('checkin.html')


@app.route('/cancel', methods=['POST'])
def cancel():
    return render_template('checkin.html')

##app.run(debug=True, port=5000)
