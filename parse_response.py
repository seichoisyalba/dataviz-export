import json
import csv
from datetime import datetime
from zoneinfo import ZoneInfo

INPUT_FILE = "response.json"
OUTPUT_FILE = "donnees.csv"

with open(INPUT_FILE, "r", encoding="utf-8") as fichier:
    payload = json.load(fichier)

series = payload["data"][0]["tag"]

nom_tag = series.get("nom", "")
description = series.get("description", "")
unite = series.get("unite", "")

lignes = []

for point in series.get("values", []):
    timestamp_ms = point["timestamp"]
    valeur = point.get("value")

    date_utc = datetime.fromtimestamp(
        timestamp_ms / 1000,
        tz=ZoneInfo("UTC")
    )

    date_paris = date_utc.astimezone(
        ZoneInfo("Europe/Paris")
    )

    lignes.append([
        nom_tag,
        description,
        unite,
        date_paris.isoformat(),
        valeur,
        timestamp_ms
    ])

with open(
    OUTPUT_FILE,
    "w",
    newline="",
    encoding="utf-8-sig"
) as fichier:
    writer = csv.writer(fichier, delimiter=";")

    writer.writerow([
        "tag",
        "description",
        "unite",
        "date",
        "valeur",
        "timestamp_ms"
    ])

    writer.writerows(lignes)

print(f"Tag : {nom_tag}")
print(f"Unité : {unite}")
print(f"Nombre de valeurs : {len(lignes)}")
print(f"Fichier créé : {OUTPUT_FILE}")

if lignes:
    print("Première ligne :", lignes[0])
    print("Dernière ligne :", lignes[-1])
