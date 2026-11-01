from flask import Blueprint, jsonify, redirect, render_template, request

from extensions import db, bcrypt
from models import AuditLog, User
from auth import current_user, require_auth

bp = Blueprint("admin", __name__)
bp.before_request(require_auth)


def _require_manager():
    if current_user().role != "manager":
        return jsonify({"error": "manager role required"}), 403
    return None


