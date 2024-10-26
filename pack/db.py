import os
import sqlite3


class Database:
    _APPDATA = ""
    _DBFILE = ""

    def __init__(self, appdata: str = f"{os.getenv('APPDATA')}/enyalie"):
        self._APPDATA = appdata
        self._DBFILE = f"{self._APPDATA}/enyalie.db"
        os.makedirs(self._APPDATA, exist_ok=True)
        with sqlite3.connect(f"{self._APPDATA}/enyalie.db") as connection:
            cursor = connection.cursor()
            cursor.execute(
                """
                CREATE TABLE IF NOT EXISTS "path" (
                    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                    title TEXT,
                    file TEXT NOT NULL
                );"""
            )

    def is_connected(self):
        with sqlite3.connect(f"{self._DBFILE}"):
            return True
        return False

    def get_all_paths(self):
        print("get all paths", self._DBFILE)
        with sqlite3.connect(f"{self._DBFILE}") as connection:
            cursor = connection.cursor()
            cursor.execute("SELECT id, title, file FROM path")
            return [
                {"id": x[0], "title": x[1], "file": x[2]} for x in cursor.fetchall()
            ]
