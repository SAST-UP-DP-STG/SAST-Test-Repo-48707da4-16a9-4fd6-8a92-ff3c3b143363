import json

from extensions import db
from models import AuditLog, Book, Order


def _apply_message(app, data):
    return None


def register_ws(sock, app):
    @sock.route("/ws/register")
    def register_feed(ws):
        while True:
            raw = ws.receive()
            if raw is None:
                break
            try:
                data = json.loads(raw)
            except (TypeError, ValueError):
                ws.send(json.dumps({"error": "invalid json"}))
                continue
            result = _apply_message(app, data)
            ws.send(json.dumps(result))
