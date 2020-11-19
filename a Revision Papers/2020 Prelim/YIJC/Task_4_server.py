from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/checkin', methods=['POST'])
def checkin():
    if request.method == 'POST':
        postalCode = request.form.get('postalCode')
        date = request.form.get('date')
        checkinTime = request.form.get('checkInTime')
        nric = request.form.get('NRIC').upper()
        handphone = request.form.get('handphone')

        db = sqlite3.connect('covid.db')
        c = db.cursor()

        c.execute('''SELECT MAX(Id) FROM event''')
        Id = c.fetchone()[0]
        Id += 1

        info = [Id, nric, handphone, postalCode, checkinTime, ' ', date]
        
        if '' in info:
            warning = 'Please enter all the information required'
            return render_template('index.html', warning=warning)

        info[5] = ''
        c.execute('''INSERT INTO event VALUES (?,?,?,?,?,?,?)''', info)
        db.commit()
        db.close()

        return render_template('checkout.html')


@app.route('/checkout', methods=['POST', 'GET'])
def checkout():
    if request.method == 'GET':
        return render_template('checkout.html')
    
    elif request.method == 'POST':
        postalCode = request.form.get('postalCode')
        date = request.form.get('date')
        checkOutTime = request.form.get('checkOutTime')
        nric = request.form.get('NRIC').upper()
        handphone = request.form.get('handphone')

        info = [nric, handphone, postalCode, checkOutTime, date]
        
        if '' in info:
            warning = 'Please enter all the information required'
            return render_template('checkout.html', warning=warning)

        db = sqlite3.connect('covid.db')
        c = db.cursor()

        # check if record exist
        c.execute('''SELECT * FROM event WHERE
                    PostalCode = ? AND NRIC = ?
                    AND Phone = ? AND Date = ?''',
                  [postalCode, nric, handphone, date])
        data = c.fetchall()

        if len(data) == 0:
            warning = 'Please enter the correct information'
            return render_template('checkout.html', warning=warning)
        
        elif len(data) > 1:
            for ele in data:
                if ele[5] == '':
                    Id = ele[0]
                    break
        else:
            Id = data[0][0]

        c.execute('''UPDATE event SET CheckOut = ? WHERE Id = ?''', [checkOutTime, Id])
        db.commit()
        db.close()

        return 'You have checked out succesfully'

app.run(debug=True, port=5000)
