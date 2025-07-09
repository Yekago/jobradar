import pandas as pd

# CSV-Datei laden
df = pd.read_csv("arbeitsmarkt.csv")

# Überblick
print("📊 Übersicht über die Arbeitsmarktdaten:\n")
print(df)

# Gruppieren nach Beruf
stellen_pro_beruf = df.groupby("Beruf")["Anzahl_Stellen"].sum()

print("\n🔎 Anzahl offener Stellen pro Beruf:\n")
print(stellen_pro_beruf)

