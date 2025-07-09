import pandas as pd
import os

# Aktueller Pfad der Python-Datei selbst (nicht des Aufrufs)
script_dir = os.path.dirname(os.path.abspath(__file__))
csv_path = os.path.join(script_dir, "arbeitsmarkt.csv")

print("Aktueller Skript-Pfad:", script_dir)
print("Geladene Datei:", csv_path)

print("Herzlich Willkommen im Jobradar")

df = pd.read_csv(csv_path)
print(df.head())
