from flask import Blueprint, jsonify, make_response, redirect, render_template, request

from extensions import bcrypt
from models import User
from auth import issue_token

bp = Blueprint("auth", __name__)


def _credentials():
    if request.is_json:
        body = request.get_json(silent=True) or {}
        return body.get("username"), body.get("password")
    return request.form.get("username"), request.form.get("password")


@bp.route("/logout")
def logout():
    response = make_response(redirect("/login"))
    response.delete_cookie("session_token")
    return response
