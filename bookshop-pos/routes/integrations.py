from flask import Blueprint, render_template

from auth import current_user, require_auth
from models import AuditLog

bp = Blueprint("integrations", __name__)
bp.before_request(require_auth)


