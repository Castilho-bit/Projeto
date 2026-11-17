import os
import sqlite3
from pathlib import Path

def database_path():
    return os.getenv("DATABASE_PATH", str(Path("instance") / "uploads.db"))

def get_connection():
    path = Path(database_path())
    path.parent.mkdir(parents=True, exist_ok=True)
    connection = sqlite3.connect(path)
    connection.row_factory = sqlite3.Row
    return connection

def init_db():
    with get_connection() as connection:
        connection.execute("""
            CREATE TABLE IF NOT EXISTS uploads (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                filename TEXT NOT NULL UNIQUE,
                original_name TEXT NOT NULL,
                content_type TEXT,
                size INTEGER NOT NULL,
                created_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP
            )
        """)
