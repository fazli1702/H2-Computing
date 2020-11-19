from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload_picture', methods=['POST'])
def upload_picture():
    if request.method == 'POST':
        name = request.form.get('name')
        image = request.files.get('img')

        db = sqlite3.connect('voting_mgm.db')
        c = db.cursor()

        # get candidate no
        c.execute('SELECT CandidateNo FROM Candidate WHERE Name = ?', [name])
        candidateNo = c.fetchone()[0]

        # format img name
        candidateNo = '0' + str(candidateNo) if candidateNo < 10 else str(candidateNo)
        img_name = 'portrait_' + candidateNo + '.png'
        img_link = 'static/potraits/' + img_name

        # save img
        image.save(img_link)

        # update candidate info
        c.execute('''UPDATE Candidate
                    SET PotraitLink = ?
                    WHERE CandidateNo = ?''',
                  [img_link, int(candidateNo)])
        db.commit()

        # get candidate information
        c.execute('SELECT * FROM Candidate WHERE CandidateNo=?', [int(candidateNo)])
        data = c.fetchone()
        print(data)
        db.close()

        return render_template('success.html', data=data)
    

app.run(debug=True, port=5000)
