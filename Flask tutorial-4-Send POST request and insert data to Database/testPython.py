from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask import request

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

@app.route('/insert_user', methods=['POST'])
def insertUser():
    newFirstName = request.form['first_name']
    newLastName = request.form['last_name']
    newEmail = request.form['email']
    user = Person(newFirstName, newLastName, newEmail)
    db.session.add(user)
    db.session.commit()
    return "<p>Data is updated</p>"

if __name__ == '__main__':
    app.run()

