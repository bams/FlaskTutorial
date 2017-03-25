from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask import render_template

app = Flask("__name_")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SQLALCHEMY_DATABASE_URI"] = 'postgresql://hoangnd:123456@localhost:5432/postgresdemo'
db = SQLAlchemy(app)

class Person(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    firstName = db.Column(db.String(120), unique=False)
    lastName = db.Column(db.String(120), unique=False)
    email = db.Column(db.String(220), unique=False)

    def __init__(self, firstName, lastName, email):
        self.firstName = firstName
        self.lastName = lastName
        self.email = email

@app.route('/find_person/<email>')
def findUser(email):
    person = Person.query.filter_by(email=email).first()
    return render_template('detail_user.html', myPerson=person)
#http://127.0.0.1:5000/find_person/test2@yahoo.com
if __name__ == '__main__':
    app.run()

