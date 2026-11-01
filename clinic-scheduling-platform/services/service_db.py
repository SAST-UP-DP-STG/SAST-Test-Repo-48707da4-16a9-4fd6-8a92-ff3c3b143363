import os
import sqlite3
from pathlib import Path

from dotenv import load_dotenv

load_dotenv()

BASE_DIR = Path(__file__).resolve().parent.parent
DATABASE_PATH = os.environ.get("DATABASE_PATH", "data/clinic.db")


def db_file():
    return str(BASE_DIR / DATABASE_PATH)


def connect():
    conn = sqlite3.connect(db_file())
    conn.row_factory = sqlite3.Row
    return conn


def ensure_analytics_tables():
    return None


def ensure_finance_tables():
    return None
