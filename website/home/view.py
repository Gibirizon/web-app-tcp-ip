from flask import Blueprint, render_template
from flask_login import current_user

view = Blueprint("view", __name__, static_folder="static",
                 template_folder="templates")


@view.route("/home")
@view.route("/")
def home():
    return render_template("home.html", user=current_user)
