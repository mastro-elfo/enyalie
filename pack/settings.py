import json
import os


class Settings:
    _APPDATA = ""
    _DBFILE = ""
    _config = {}

    def __init__(self, appdata: str = f"{os.getenv('APPDATA')}/enyalie") -> None:
        self._APPDATA = appdata
        self._DBFILE = f"{self._APPDATA}/settings.json"
        os.makedirs(self._APPDATA, exist_ok=True)
        try:
            with open(self._DBFILE, "r", encoding="utf8") as fp:
                self._config = json.load(fp)
        except (FileNotFoundError, PermissionError):
            pass

    def get(self, key, default=None):
        return self._config.get(key, default)

    def set(self, key, value):
        self._config[key] = value
        with open(self._DBFILE, "w", encoding="utf8") as fp:
            json.dump(self._config, fp, indent=4)
