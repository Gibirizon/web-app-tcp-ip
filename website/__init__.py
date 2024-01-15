from datetime import timedelta

from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def create_app():
    app = Flask(__name__, template_folder="templates", static_folder="static")
    app.secret_key = "ahgksgkhg209523750hsdghlasdgh"
    app.config["EXPLAIN_TEMPLATE_LOADING"] = True
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.init_app(app)

    login_manager = LoginManager()
    login_manager.login_view = "auth.login"
    login_manager.init_app(app)

    from .models import Answer, Protocol, Question, User

    with app.app_context():
        db.create_all()

    from .home.view import view

    app.register_blueprint(view, url_prefix="/home")

    from .layers.layers import layers
    app.register_blueprint(layers, url_prefix="/warstwa")

    from .auth.auth import auth
    app.register_blueprint(auth, url_prefix="/uzytkownik")

    from .quiz.quiz import quiz
    app.register_blueprint(quiz, url_prefix="/quiz")

    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))

    return app
