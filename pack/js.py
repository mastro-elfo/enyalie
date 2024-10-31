import os
import pathlib

CURRENT_DIR = os.path.dirname(os.path.realpath(__file__))

POLYLINE = ""
with open(
    pathlib.Path(CURRENT_DIR) / "javascript" / "polyline.js", "r", encoding="utf8"
) as fp:
    POLYLINE = fp.read()
