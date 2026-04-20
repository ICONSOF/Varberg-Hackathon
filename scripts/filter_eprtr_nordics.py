"""
Filter all E-PRTR CSV files to Sweden, Norway, and Denmark and save them as CSV.
Run from anywhere: python scripts/filter_eprtr_nordics.py
"""

from pathlib import Path

import pandas as pd

ROOT_DIR = Path(__file__).resolve().parents[1]
EPRTR_DIR = ROOT_DIR / "hackathon_data" / "eprtr_raw"
OUT_DIR = ROOT_DIR / "hackathon_data"
COUNTRIES = {"Sweden", "Norway", "Denmark"}
SUFFIX = "Nordics"

OUT_DIR.mkdir(parents=True, exist_ok=True)

csv_files = sorted(EPRTR_DIR.glob("*.csv"))

if not csv_files:
    raise FileNotFoundError(f"No CSV files found in {EPRTR_DIR}")

for src in csv_files:
    dst = OUT_DIR / f"{src.stem}_{SUFFIX}.csv"

    print(f"Reading {src.name}...")
    df = pd.read_csv(src, encoding="utf-8-sig", low_memory=False)

    if "countryName" not in df.columns:
        print("  -> skipped: missing countryName column")
        continue

    nordics = df[df["countryName"].isin(COUNTRIES)].copy()
    nordics.to_csv(dst, index=False, encoding="utf-8-sig")

    size_mb = dst.stat().st_size / 1e6
    print(f"  -> {dst.name}: {len(nordics):,} rows, {size_mb:.1f} MB")

print(f"\nDone. Files saved to {OUT_DIR}")
