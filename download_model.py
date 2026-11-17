from database.db import get_connection

def find_upload(filename):
    with get_connection() as connection:
        row = connection.execute(
            """SELECT filename, original_name, content_type, size, created_at
               FROM uploads WHERE filename = ?""",
            (filename,)
        ).fetchone()
        return dict(row) if row else None
