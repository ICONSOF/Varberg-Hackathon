"""
Filter E-PRTR CSV files to Sweden and save as JSON in files/hackathon_data/.
Run from the repo root: python scripts/filter_eprtr_sweden.py
"""

import pandas as pd
import os

EPRTR_DIR = "files/hackathon_data/eprtr_raw"
OUT_DIR = "files/hackathon_data"

FILES = [
    ("F1_4_Air_Releases_Facilities.csv", "F1_4_Sweden.json"),
    ("F2_4_Water_Releases_Facilities.csv", "F2_4_Sweden.json"),
]

os.makedirs(OUT_DIR, exist_ok=True)

for filename, outname in FILES:
    src = os.path.join(EPRTR_DIR, filename)
    dst = os.path.join(OUT_DIR, outname)

    print(f"Reading {filename}...")
    df = pd.read_csv(src, encoding="utf-8-sig", low_memory=False)

    sweden = df[df["countryName"] == "Sweden"].copy()
    sweden.to_json(dst, orient="records", force_ascii=False)

    size_mb = os.path.getsize(dst) / 1e6
    print(f"  -> {outname}: {len(sweden):,} rows, {size_mb:.1f} MB")

print("\nDone. Files saved to", OUT_DIR)
