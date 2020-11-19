from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/checkin', methods=['POST'])
def checkin():
    if request.method == 'POST':
        PostalCode = request.form.get('PostalCode')
        Date = request.form.get('Date')
        CheckInTime = request.form.get('CheckInTime')
        NRIC = request.form.get('NRIC')
        HandphoneNo = request.form.get('HandphoneNo')

        # connect to db
        db = sqlite3.connect('covid.db')
        c = db.cursor()

        # find next Id to add
        c.execute('SELECT MAX(Id) FROM event')
        Id = c.fetchone()[0]
        Id += 1
        
        TempCheckOutTime = '0'  # assign temporary check-out time
        info = [Id, NRIC, HandphoneNo, PostalCode, CheckInTime, TempCheckOutTime , Date]

        # return html page if null/empty input
        if '' in info:
            warning = 'Please enter all required information'
            return render_template('index.html', warning=warning)
        else:
            # set TempCheckOut to empty string
            info[5] = ''

        # check if user have check-out from previous check-in
        c.execute('''SELECT CheckOut, Date FROM event WHERE
                    NRIC = ? AND Phone = ? AND PostalCode = ?''',
                    [NRIC, HandphoneNo, PostalCode])
        info2 = c.fetchone()

        # new user  
        if info2 == None:
            pass

        else:
            userCheckOut, userDate = info2

            # if user have not check-out
            if userCheckOut == '' or userCheckOut == '0':
                # same date - check out time set to new check in time
                if userDate == Date:
                    c.execute('''UPDATE event SET CheckOut = ? WHERE
                                NRIC = ? AND Phone = ? AND PostalCode = ?''',
                              [CheckInTime, NRIC, HandphoneNo, PostalCode])
                    db.commit()

                # different date - check out time set 23:59
                else:
                    c.execute('''UPDATE event SET CheckOut = ? WHERE
                                NRIC = ? AND Phone = ? AND PostalCode = ?''',
                              ['23:59', NRIC, HandphoneNo, PostalCode])
                    db.commit()

        
        # insert user input into db
        c.execute('''INSERT INTO event VALUES (?, ?, ?, ?, ?, ?, ?)''', info)
        db.commit()
        db.close()

    return render_template('checkout.html')



@app.route('/checkout', methods=['GET'])
def checkout():
    return render_template('checkout.html')


@app.route('/processCheckOut', methods=['POST'])
def processCheckOut():
    if request.method == 'POST':
        PostalCode = request.form.get('PostalCode')
        Date = request.form.get('Date')
        CheckOutTime = request.form.get('CheckOutTime')
        NRIC = request.form.get('NRIC')
        HandphoneNo = request.form.get('HandphoneNo')
    
        info = [CheckOutTime, PostalCode, Date, NRIC, HandphoneNo]

        # return html page if null/empty input
        if '' in info:
            warning = 'Please enter all required information'
            return render_template('index.html', warning=warning)

        # connect to db
        db = sqlite3.connect('covid.db')
        c = db.cursor()

        # update CheckOut value
        c.execute('''UPDATE event SET CheckOut = ?
                    WHERE PostalCode = ? AND Date = ? AND NRIC = ?
                    AND Phone = ?''', info)
        db.commit()
        db.close()

    return render_template('index.html')



app.run(debug=True, port=5000)
