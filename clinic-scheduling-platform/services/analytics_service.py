from datetime import datetime, timezone
from typing import Optional

from fastapi import Depends, FastAPI
from pydantic import BaseModel

from .analytics_deps import get_current_user
from .service_db import connect, ensure_analytics_tables

app = FastAPI(title="Clinic Analytics Service", root_path="/svc/analytics")

ensure_analytics_tables()


class ConfigUpdate(BaseModel):
    scope: Optional[str] = None
    weight: Optional[float] = None
    refresh_minutes: Optional[int] = None
    internal_flag: Optional[int] = None


def _now():
    return datetime.now(timezone.utc).isoformat()


@app.get("/my-exports")
def my_exports(user=Depends(get_current_user)):
    conn = connect()
    cur = conn.cursor()
    cur.execute(
        "SELECT id, requested_by, requested_by_name, clinic_id, scope, row_count, created_at "
        "FROM analytics_export ORDER BY id DESC"
    )
    rows = [dict(r) for r in cur.fetchall()]
    conn.close()
    return {"exports": rows}


