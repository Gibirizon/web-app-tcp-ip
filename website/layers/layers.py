import json
import re

from flask import Blueprint, jsonify, redirect, render_template, request, url_for
from flask_login import current_user

from .. import db
from ..add_protocols import add_prot
from ..models import Protocol

layers = Blueprint("layers", __name__, static_folder="static",
                   template_folder="templates")


@layers.route("/warstwa-aplikacji")
def app_layer():
    if not Protocol.query.all():
        add_prot()
    return render_template("app_layer.html", user=current_user)


@layers.route("/warstwa-transportowa")
def transport_layer():
    if not Protocol.query.all():
        add_prot()
    return render_template("transport_layer.html", user=current_user)


@layers.route("/warstwa-internetowa")
def internet_layer():
    if not Protocol.query.all():
        add_prot()
    return render_template("internet_layer.html", user=current_user)


@layers.route("/warstwa-dostępu-do-sieci")
def network_access_layer():
    if not Protocol.query.all():
        add_prot()
    return render_template("network_access_layer.html", user=current_user)


@layers.route("/dodaj-opis", methods=["POST"])
def add_desc():
    if request.method == "POST":
        name = str(request.data)[2:-1]
        protocol = Protocol.query.filter_by(name=name).first()
        return f'<p>{protocol.description}</p><button type="button" class="description__button" onclick="close_app_layer()"><i class="bi bi-x-lg"></i></button>'
