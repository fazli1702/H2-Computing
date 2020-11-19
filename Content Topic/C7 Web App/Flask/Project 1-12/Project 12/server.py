from flask import Flask, render_template, request

app = Flask(__name__)

notes = []  #list to keep notes

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        note = request.form.get('note')
        notes.append(note)
    return render_template('index.html', display=notes)

app.run(debug=True, port=5000)
# launch web browser with url 127.0.0.1:5000
