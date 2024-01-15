from flask_login import UserMixin
from sqlalchemy_serializer import SerializerMixin

from . import db


class Protocol(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), unique=True)
    description = db.Column(db.String(200))


class User(db.Model, UserMixin, SerializerMixin):
    id = db.Column(db.Integer, primary_key=True)
    login = db.Column(db.String(50))
    email = db.Column(db.String(50), unique=True)
    password = db.Column(db.String(50))
    questions = db.relationship("Question")


class Question(db.Model, SerializerMixin):
    id = db.Column(db.Integer, primary_key=True)
    question = db.Column(db.String(200))
    answers = db.relationship("Answer", uselist=False)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))


class Answer(db.Model, SerializerMixin):
    id = db.Column(db.Integer, primary_key=True)
    answer1 = db.Column(db.String(100))
    answer2 = db.Column(db.String(100))
    answer3 = db.Column(db.String(100))
    answer4 = db.Column(db.String(100))
    correct_answer = db.Column(db.String(100))
    question_id = db.Column(db.Integer, db.ForeignKey("question.id"))
