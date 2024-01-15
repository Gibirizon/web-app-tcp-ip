from flask import Blueprint, flash, redirect, render_template, request, session, url_for
from flask_login import current_user, login_required, login_user, logout_user
from werkzeug.security import check_password_hash, generate_password_hash

from .. import db
from ..models import User
from .create_questions import create_questions

auth = Blueprint("auth", __name__, static_folder="static",
                 template_folder="templates")


@auth.route("/rejestracja/", methods=["GET", "POST"])
def sign_up():
    if request.method == "POST":
        login = request.form.get("login")
        email = request.form.get("email")
        password = request.form.get("password")
        confirm_password = request.form.get("confirm_password")

        if User.query.filter_by(email=email).first():
            flash("Już masz konto, zaloguj się", category="info")
            return redirect(url_for("auth.login"))

        conditions = {"Nazwa użytkownika - to miejsce jest wymagane": login,
                      "E-mail - to miejsce jest wymagane": email,
                      "Hasło - to miejsce jest wymagane": password,
                      "Potwierdzenie hasła - to miejsce jest wymagane": confirm_password,
                      "Nazwa użytkownika jest zbyt długa": len(login) < 50,
                      "E-mail jest zbyt długi": len(email) < 50,
                      "Hasło jest zbyt długie": len(password) < 50,
                      "Hasła nie są takie same": password == confirm_password,
                      "Hasło jest zbyt krótkie": len(password) > 5}
        for message, condition in conditions.items():

            if not condition:
                flash(message, category="error")

        if all(conditions.values()):
            user = User(login=login, email=email,
                        password=generate_password_hash(password))
            db.session.add(user)
            db.session.commit()
            flash("Pomyślnie założono konto", category="success")
            return redirect(url_for("auth.login"))
    if "email" in session:
        flash("Już jesteś zalogowany", category="info")
        return redirect(url_for("view.home"))
    return render_template("sign_up.html", user=current_user)


@auth.route("/logowanie/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")
        remember = True if request.form.get("remember") else False
        user = User.query.filter_by(email=email).first()

        if not user:
            flash("Niepoprawny e-mail", category="error")

        elif not check_password_hash(user.password, password):
            flash("Niepoprawne hasło", category="error")

        else:
            session["email"] = email
            flash("Pomyślnie zalogowano", category="success")
            login_user(user, remember=remember)
            create_questions()
            return redirect(url_for("view.home"))
    if "email" in session:
        flash("Już jesteś zalogowany", category="info")
        return redirect(url_for("view.home"))
    return render_template("login.html", user=current_user)


@auth.route("/wylogowanie/")
@login_required
def logout():
    session.pop("email", None)
    logout_user()
    flash("Pomyślnie wylogowano", category="success")
    return redirect(url_for("view.home"))
