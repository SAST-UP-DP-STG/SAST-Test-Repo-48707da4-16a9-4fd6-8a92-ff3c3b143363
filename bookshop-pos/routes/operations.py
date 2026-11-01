from flask import Blueprint, jsonify

from extensions import db
from models import AuditLog, Customer, Order

bp = Blueprint("operations", __name__)


@bp.route("/ops/admin/purge-audit", methods=["POST"])
def ops_purge_audit():
    removed = AuditLog.query.delete()
    db.session.commit()
    return jsonify({"purged": removed})
