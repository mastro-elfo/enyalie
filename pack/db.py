import os
import sqlite3

APPDATA = f"{os.getenv('APPDATA')}/enyalie"
# APPDATA = "./APPDATA"
os.makedirs(APPDATA, exist_ok=True)

with sqlite3.connect(f"{APPDATA}/enyalie.db") as connection:
    cursor = connection.cursor()
    cursor.execute(
        """
    CREATE TABLE IF NOT EXISTS "path" (
        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        title TEXT,
        file TEXT NOT NULL
    );
"""
    )


def is_connected():
    with sqlite3.connect(f"{APPDATA}/enyalie.db"):
        return True
    return False


def get_all_paths():
    with sqlite3.connect(f"{APPDATA}/enyalie.db") as connection:
        cursor = connection.cursor()
        cursor.execute("SELECT id, title, file FROM path")
        return [{"id": x[0], "title": x[1], "file": x[2]} for x in cursor.fetchall()]
