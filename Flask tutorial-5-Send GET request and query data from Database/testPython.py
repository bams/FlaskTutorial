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

@app.route('/list_all_users')
def listAllUsers():
    persons = Person.query.all()
    return render_template('list_all_users.html', myPersons=persons)
if __name__ == '__main__':
    app.run()

