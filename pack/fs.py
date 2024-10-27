import os
import re
import xml.etree.ElementTree as ET


def get_trkpts_from_file(filename: str):
    root = ET.parse(filename).getroot()
    match = re.search(r"(\{.*?\}).+", root.tag)
    ns = match.group(1) if match else ""

    track = []
    for trkseg in root.findall(f".//{ns}trkseg"):
        segment = []
        for trkpt in trkseg.findall(f".//{ns}trkpt"):
            lat = trkpt.get("lat")
            lon = trkpt.get("lon")
            if lat is not None and lon is not None:
                segment.append((float(lat), float(lon)))
        track.append(segment)

    return track


def is_directory(path: str):
    return os.path.isdir(path)
