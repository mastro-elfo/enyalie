import os
import sqlite3
from typing import Any


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
                CREATE TABLE IF NOT EXISTS paths (
                    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                    title TEXT,
                    file TEXT NOT NULL
                );
                """
            )
            cursor.execute(
                """
                CREATE TABLE IF NOT EXISTS config (
                    "key" TEXT NOT NULL,
                    integerValue INTEGER,
                    numericValue NUMERIC,
                    realValue INTEGER,
                    textValue TEXT,
                    blobValue BLOB,
                    CONSTRAINT config_pk PRIMARY KEY ("key")
                );
                """
            )

    def is_connected(self):
        with sqlite3.connect(f"{self._DBFILE}"):
            return True
        return False

    def get_all_paths(self):
        with sqlite3.connect(f"{self._DBFILE}") as connection:
            cursor = connection.cursor()
            cursor.execute("SELECT id, title, file FROM paths")
            return [self._map(x, ["id", "title", "file"]) for x in cursor.fetchall()]

    def get_config(self):
        with sqlite3.connect(f"{self._DBFILE}") as connection:
            cursor = connection.cursor()
            cursor.execute(
                "SELECT key, integerValue, numericValue, realValue, textValue, blobValue FROM config"
            )
            return {x[0]: self._not_none(x[1:]) for x in cursor.fetchall()}

    def set_config(self, key: str, value: Any):
        with sqlite3.connect(f"{self._DBFILE}") as connection:
            cursor = connection.cursor()
            cursor.execute(
                "REPLACE INTO config (key, integerValue, numericValue, realValue, textValue, blobValue) VALUES (?,?,?,?,?,?)",
                (
                    key,
                    value if isinstance(value, int) else None,
                    value if isinstance(value, (float, int)) else None,
                    value if isinstance(value, (float, int)) else None,
                    value if isinstance(value, str) else None,
                    value if isinstance(value, bytes) else None,
                ),
            )
            connection.commit()

    def _map(self, result: list[Any], fields: list[str]):
        return {
            field: result[index]
            for index, field in enumerate(fields)
            if len(result) > index
        }

    def _not_none(self, seq: list[Any]):
        for value in seq:
            if value is not None:
                return value
        return None
