from database.db import get_connection

def register_upload(filename, original_name, content_type, size):
    with get_connection() as connection:
        connection.execute(
            """INSERT INTO uploads (filename, original_name, content_type, size)
               VALUES (?, ?, ?, ?)""",
            (filename, original_name, content_type, size)
        )

def list_uploads():
    with get_connection() as connection:
        rows = connection.execute(
            "SELECT id, filename, original_name, content_type, size, created_at FROM uploads ORDER BY id DESC"
        ).fetchall()
        return [dict(row) for row in rows]
