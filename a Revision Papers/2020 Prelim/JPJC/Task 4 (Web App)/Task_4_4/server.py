from flask import Flask, request, render_template
import sqlite3

app = Flask(__name__)

months = {
    1:'January',
    2:'Febraury',
    3:'March',
    4:'April',
    5:'May',
    6:'June',
    7:'July',
    8:'August',
    9:'September',
    10:'October',
    11:'November',
    12:'December'
    }

@app.route('/')
def index():
    return render_template('index.html')

def filter_date(user_year, user_month, data):
    info = []
    for ele in data:
        year, month, day = ele[-2].split('/')
        if year == user_year and month == user_month:
            info.append(ele)
    return info


def get_total_amount(info):
    db = sqlite3.connect('computercompany.db')
    c = db.cursor()
    
    total = []
    all_sid = []
    for ele in info:
        sid = ele[0]
        if sid not in all_sid:
            all_sid.append(sid)

    for sid in all_sid:
        c.execute('SELECT SUM(Amount) FROM SALE WHERE SalespersonID = ?', [sid])
        amount = c.fetchone()[0]
        total.append([amount, sid])

    total.sort()
    return total[::-1]
        

def get_top(total):
    # remove any salesperson (lower sales) who might be
    # in the same office with another (higher sales)
    db = sqlite3.connect('computercompany.db')
    c = db.cursor()
    
    data = [] # data displayed on html
    for amount, sid in total:
        seen = False
        c.execute('''SELECT OfficeID, SalesPersonName FROM SALESPERSON
                        WHERE SalesPersonID = ?''', [sid])
        info2 = c.fetchone()
        for officeID, name, a in data:
            seen = False
            if int(info2[0]) == int(officeID):
                seen = True
                break

        if not seen:
            data.append([info2[0], info2[1], amount])

    return sorted(data)

        

@app.route('/top_performer', methods=['POST', 'GET'])
def top_performer():
    global months
    if request.method == 'POST':
        user_month = request.form.get('month')
        if len(user_month) == 1: # add 0 in front e.g. 1 -> 01
            user_month = '0' + user_month
            
        user_year = request.form.get('year')

        db = sqlite3.connect('computercompany.db')
        c = db.cursor()

        c.execute('''SELECT * FROM SALE''')
        info = c.fetchall()

        filtered_info = filter_date(user_year, user_month, info)
        total = get_total_amount(filtered_info)
        data = get_top(total)
    
        return render_template('top_performer.html', month=months[int(user_month)],
                               year=user_year, data=data)
            

app.run(debug=True, port=5000)
        
