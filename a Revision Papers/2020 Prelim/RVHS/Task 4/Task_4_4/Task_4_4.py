from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/voted_for', methods=['POST'])
def voted_for():
    if request.method == 'POST':
        matricNo = request.form.get('matricNo')

        db = sqlite3.connect('voting_mgm.db')
        c = db.cursor()

        c.execute('''SELECT Vote.CandidateNo, Candidate.Name
                    FROM Candidate, Student, Vote
                    WHERE Student.MatricNo = ?
                    AND Student.MatricNo = Vote.MatricNo
                    AND Vote.CandidateNo = Candidate.CandidateNo''', [matricNo])
        data = c.fetchall()

        return render_template('voted_for.html', data=data)



app.run(debug=True, port=5000)
