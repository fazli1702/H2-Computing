from flask import Flask, render_template, request
from datetime import datetime

bookInfo = (
    ("Beginner's Step-by-Step Coding Course",42.80),
    ("Algorithms to Live by",22.47),
    ("Data Science for Dummies",44.89),
    ("Must Know High School Computer Programming",21.50),
    ("Networking All-in-one for Dummies",59.87),
    ("Learn Python 3 the Hard Way",70.17),
    ("Computer Coding Projects for Kids",28.89),
    ("Data Science Programming All-in-One for Dummies",59.87),
    ("Artificial Intelligence for Dummies",44.89),
    ("Web Coding & Development All-in-one for Dummies",59.87)
)


#####################################


app = Flask(__name__)

'''
User input:
1) name and email
2) 3 books of choice (cannot repeat)


Information shown:
1) date of the order;   
2) name and email address;
3) three books which he has chosen and their prices;
4) total cost
'''

#variables
orders = []
name, email = '', ''
currDate = datetime.today().strftime('%d/%m/%Y')



@app.route('/' , methods=['GET', 'POST']) 
def index():
    total = 0
    b = []
    if request.method == 'POST': 
        name = request.form.get('name').upper()
        email = request.form.get('email')
        index = request.form.getlist('BookOrder')
        print(index)
        for i in index:
            i = int(i)
            title = bookInfo[i][0]
            price = float(bookInfo[i][1])
            b.append((title, price))
            total += price

        orders.append((currDate, name, email, b, total))
        #print(orders)   

     

    return render_template('index.html', books=bookInfo , orders=orders)


app.run(debug=True, port=5000)
