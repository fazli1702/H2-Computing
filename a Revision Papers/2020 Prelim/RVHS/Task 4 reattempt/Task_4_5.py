from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload_image', methods=['POST'])
def upload_image():
    if request.method == 'POST':
        name = request.form.get('name')
        image = request.files.get('image')

        db = sqlite3.connect('voting_mgm.db')
        c = db.cursor()

        c.execute('''SELECT CandidateNo FROM Candidate WHERE Name=?''', [name])
        candidateNo = c.fetchone()[0]

        # format image file name
        if candidateNo < 10:
            candidateNo = '0' + str(candidateNo)
        else:
            candidateNo = str(candidateNo)

        image_name = 'potrait_' + candidateNo + '.png'
        image_link = 'static/potraits/' + image_name

        # save fsile in new folder
        image.save(image_link)

        # update PotraitLink in db
        c.execute('''UPDATE Candidate SET PotraitLink=? WHERE Name=?''',
                    [image_link, name])
        db.commit()

        # get candidate information
        c.execute('''SELECT * FROM Candidate WHERE Name=?''', [name])
        data = c.fetchone()

        return render_template('success.html', data=data)


        
app.run(debug=True, port=5000)
