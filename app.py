from flask import Flask, render_template, request, flash
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.dialects.postgresql import ARRAY

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:postgres@localhost:5732/postgres'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.secret_key = 'hi'

db = SQLAlchemy(app)


class Questions(db.Model):
    __tablename__ = 'Questions'

    question = db.Column(db.String(120), nullable=True)
    answers = db.Column(ARRAY(db.String(120)), unique=True, nullable=True)
    question_id = db.Column(db.Integer, primary_key=True)
    answerType = db.Column(db.Integer, nullable=False)

    def __init__(self, question, answers, answerType):
        self.question = question
        self.answers = answers
        self.answerType = answerType

    def __repr__(self):
        return '<Question Id {}>'.format(self.question_id)


@app.route('/', methods=['get'])
def home():
    return render_template("index.html")

@app.route("/login", methods=['get', 'put'])
def addperson():
    return render_template("index.html")


@app.route("/signup", methods=['get', 'put'])
def addperson():
    return render_template("index.html")

@app.route("/question", methods=['put'])
def addperson():
    return render_template("index.html")

if __name__ == '__main__':
    db.create_all()
    app.run()