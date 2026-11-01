from flask import Blueprint, jsonify, render_template

from extensions import db
from models import AuditLog, Order
from auth import current_user, require_auth

bp = Blueprint("orders", __name__)
bp.before_request(require_auth)


def _require_manager():
    if current_user().role != "manager":
        return jsonify({"error": "manager role required"}), 403
    return None


