from flask import (
    Blueprint,
    flash,
    jsonify,
    redirect,
    render_template,
    request,
    session,
    url_for,
)
from flask_login import current_user, login_required

from .. import db
from ..models import Answer, Question

quiz = Blueprint("quiz", __name__, static_folder="static",
                 template_folder="templates")


@quiz.route("/", methods=["GET", "POST"])
@quiz.route("/home/", methods=["GET", "POST"])
@login_required
def quiz_home():
    if request.method == "POST":
        if request.form.get("link") == "rozpocznij-quiz":
            obj = [i.to_dict() for i in Question.query.filter_by(
                user_id=current_user.id).all()]
            session["questions"] = obj
            session["question_amount"] = len(obj)
            session["question_number"] = 1
            session["correct_answers"] = 0
            return redirect(url_for(".quiz_start"))
        else:
            obj = [i.to_dict() for i in Question.query.filter_by(
                user_id=current_user.id).all()]
            session["current_user_questions"] = obj
            return redirect(url_for(".quiz_add"))
    return render_template("quiz_home.html", user=current_user)


@quiz.route("/dodaj-pytanie/", methods=["POST", "GET"])
@login_required
def quiz_add():

    if request.method == "POST" and Question.query.filter_by(question=request.data.decode()).first():
        print("good")
        question = Question.query.filter_by(
            question=request.data.decode()).first()
        print(question.id)
        answers = Answer.query.filter_by(question_id=question.id).first()
        db.session.delete(answers)
        db.session.delete(question)
        db.session.commit()
        obj = [i.to_dict() for i in Question.query.filter_by(
            user_id=current_user.id).all()]
        print(obj)
        session["current_user_questions"] = obj
    elif request.method == "POST":
        print("sth")
        question = request.form.get("question")
        answer1 = request.form.get("answer1")
        answer2 = request.form.get("answer2")
        answer3 = request.form.get("answer3")
        answer4 = request.form.get("answer4")
        print(question, answer1)
        correct_answer = request.form.get("correct_answer")
        print(session["current_user_questions"])
        if Question.query.filter_by(question=question).first():

            flash("Już istnieje takie pytanie", category="info")
            return redirect(url_for(".quiz_add"))

        conditions = {"Treść pytania - to miejsce jest wymagane": question,
                      "Odpowiedź 1 - to miejsce jest wymagane": answer1,
                      "Odpowiedź 2 - to miejsce jest wymagane": answer2,
                      "Odpowiedź 3 - to miejsce jest wymagane": answer3,
                      "Odpowiedź 4 - to miejsce jest wymagane": answer4,
                      "Poprawna odpowiedź - to miejsce jest wymagane": correct_answer,
                      "Jedna z podanych odpowiedzi musi być poprawna": correct_answer in [answer1, answer2, answer3, answer4], }
        for message, condition in conditions.items():
            if not condition:
                flash(message, category="error")

        if all(conditions.values()):
            question = Question(
                question=question,
                user_id=current_user.id
            )
            db.session.add(question)
            db.session.commit()
            answer = Answer(
                answer1=answer1,
                answer2=answer2,
                answer3=answer3,
                answer4=answer4,
                correct_answer=correct_answer,
                question_id=question.id

            )
            db.session.add(answer)
            db.session.commit()

            obj = [i.to_dict() for i in Question.query.filter_by(
                user_id=current_user.id).all()]
            session["current_user_questions"] = obj

            flash("Dodano pytanie", category="success")
    return render_template("quiz_add.html", user=current_user)


@quiz.route("/start/", methods=["POST", "GET"])
@login_required
def quiz_start():
    if request.method == "POST":
        answer = request.form.get("answer")
        session["correct_answer"] = session["questions"][session["question_number"] -
                                                         1]["answers"]["correct_answer"]
        if answer == str(session["correct_answer"]):
            flash("Poprawna odpowiedź", category="success")
            session["correct_answers"] += 1
        else:
            flash("Niepoprawna odpowiedź", category="error")
        if session["question_number"] == session["question_amount"]:
            return redirect(url_for(".quiz_score"))
        session["question_number"] += 1

    session["question"] = session["questions"][session["question_number"]-1]["question"]
    ans = session["questions"][session["question_number"]-1]["answers"]
    session["answers"] = [ans["answer1"],
                          ans["answer2"], ans["answer3"], ans["answer4"]]

    return render_template("quiz_start.html", user=current_user)


@quiz.route("/wynik/", methods=["GET", "POST"])
def quiz_score():
    if request.method == 'POST':
        if request.form.get("link") == "wiedza":
            return redirect(url_for("layers.app_layer"))
        else:
            obj = [i.to_dict() for i in Question.query.filter_by(
                user_id=current_user.id).all()]
            session["current_user_questions"] = obj
            return redirect(url_for(".quiz_add"))
    return render_template("quiz_score.html", user=current_user)
