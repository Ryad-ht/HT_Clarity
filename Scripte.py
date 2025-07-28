import pandas as pd
import numpy as np
import os

# === 1. Chargement du fichier Excel ===
file_path = "log_dataset.xlsx"

try:
    df = pd.read_excel(file_path)
    print("✅ Fichier chargé avec succès.")
except FileNotFoundError:
    print("❌ Fichier non trouvé :", file_path)
    exit()

# === 2. Aperçu initial ===
print("\n=== Aperçu des 5 premières lignes ===")
print(df.head())

print("\n=== Taille du dataset (lignes, colonnes) ===")
print(df.shape)

print("\n=== Colonnes ===")s
print(df.columns.tolist())

print("\n=== Valeurs manquantes (TOP) ===")
print(df.isnull().sum().sort_values(ascending=False).head(10))

print("\n=== Doublons ===")
print("Nombre de doublons :", df.duplicated().sum())

# === 3. Normalisation des noms de colonnes ===
df.columns = df.columns.str.strip().str.lower().str.replace(r"[^a-z0-9_]+", "_", regex=True)

# === 4. Suppression des doublons ===
df = df.drop_duplicates()

# === 5. Suppression des lignes critiques incomplètes ===
df = df.dropna(subset=["vehicle_no"])

# === 6. Conversion des types ===

# Dates à convertir
date_cols = [
    'bookingid_date', 'data_ping_time', 'planned_eta',
    'actual_eta', 'trip_start_date', 'trip_end_date'
]
for col in date_cols:
    if col in df.columns:
        df[col] = pd.to_datetime(df[col], errors='coerce')

# Valeurs numériques
if 'delay' in df.columns:
    df['delay'] = pd.to_numeric(df['delay'], errors='coerce')

# Booléens
if 'ontime' in df.columns:
    df['ontime'] = (
        df['ontime']
        .astype(str)
        .str.lower()
        .replace({'yes': True, 'no': False, 'nan': None, 'none': None})
    )

# === 7. Nettoyage facultatif des champs texte ===
text_cols = ['gpsprovider', 'vehicletype', 'suppliernamecode', 'customernamecode']
for col in text_cols:
    if col in df.columns:
        df[col] = df[col].astype(str).str.strip().str.upper()

# === 8. Export vers un fichier nettoyé ===
output_path = "log_dataset_clean.csv"
df.to_csv("log_dataset_clean.csv", index=False, encoding="utf-8-sig")
print(f"\n✅ Données nettoyées sauvegardées dans : {output_path}")

# === 9. Résumé final ===
print("\n=== Rapport final ===")
print(f"Lignes : {len(df)}")
print("Colonnes :", len(df.columns))
print("Colonnes avec NaN (non nulles) :")
print(df.isnull().sum()[df.isnull().sum() > 0])
