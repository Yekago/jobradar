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

print("\nTop-Berufe bundesweit:")
print(df.groupby("Beruf")["Anzahl_Stellen"].sum().sort_values(ascending=False))

stadt = input("\nGib einen Ort ein, um die verfügbaren Berufe dort anzuzeigen: ")
if stadt in df["Ort"].values:
    print(f"\nTop-Berufe in {stadt}:")
    print(df[df["Ort"] == stadt].groupby("Beruf")["Anzahl_Stellen"].sum().sort_values(ascending=False))
else:
    print(f"\nLeider wurden keine Daten für den Ort '{stadt}' gefunden.")

print(f"\nTop-Berufe in {stadt}:")
print(df[df["Ort"] == stadt].groupby("Beruf")["Anzahl_Stellen"].sum().sort_values(ascending=False))

import matplotlib.pyplot as plt

# Top 5 Berufe nach Stellenanzahl
top5 = df.groupby("Beruf")["Anzahl_Stellen"].sum().sort_values(ascending=False).head(5)
top5.plot(kind="bar", title="Top 5 Berufe bundesweit")
plt.xlabel("Beruf")
plt.ylabel("Anzahl Stellen")
plt.tight_layout()
plt.show()
