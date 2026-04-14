# Data Files Audit & Recommendations

## Current Local Files in `files/hackathon_data/`

```
halland_skyddade_omraden.geojson (useful)
DVO/, NM/, NP/, NR/, NVO/ (shapefiles - questionable)
```

**Total disk usage:** ~200 MB (mostly shapefiles as unzipped folders + zips)

---

## Analysis: Do We Really Need All These?

### 1. halland_skyddade_omraden.geojson ✅ KEEP

**Status:** Essential

**Why:**
- Directly usable in Leaflet.js (no conversion needed)
- Referenced in Idea #3 (Halland Nature Map)
- Small (~2 MB uncompressed)
- Teams can copy-paste into their project immediately

**Action:** Keep. It's the perfect "starter data" for map-based ideas.

---

### 2. Shapefiles (DVO, NM, NP, NR, NVO) ❌ QUESTIONABLE

**Status:** Friction-causing, likely unused

**Why keep them:**
- Comprehensive coverage of all Sweden's protected areas
- Useful for detailed mapping projects
- Idea #1 (Green Neighborhood) mentions "Naturvårdsverket GeoJSON"

**Why NOT to include them:**
- **Format friction:** Shapefiles are complex (each is multiple files: .shp, .shx, .dbf, .prj)
- **Conversion barrier:** Teams need to convert to GeoJSON using:
  - Python (GeoPandas, fiona) — requires setup
  - Online tools (mapshaper.org) — slower, less portable
  - QGIS — not installed on all machines
- **Large:** Unzipped folders are 100+ MB total
- **Redundant:** Naturvårdsverket has a REST API that returns this data as JSON/GeoJSON
  ```
  https://geodata.naturvardsverket.se/naturvardsregistret/rest/v3/omrade?skyddstypkod=NP
  ```
- **Not mentioned in ideas:** None of the 10 app ideas specifically require shapefiles
- **Time cost:** Teams would spend 30+ min figuring out how to use them

**Better alternative:**
- Keep **just** `halland_skyddade_omraden.geojson` (already converted)
- Point teams to the **REST API** for Sweden-wide data
- Include a note: "Need national parks or reserves? Use the Naturvårdsverket API instead of converting shapefiles"

**Recommendation:** ❌ **Remove shapefiles** (NP, NR, NM, DVO, NVO folders and zips)

**Why:** Teams who truly need them can download from Naturvårdsverket's website in 2 min. The API is faster.

---

### 3. E-PRTR CSV Files (F1_2, F1_4, F2_4, F3_2, F4_2)

**Status:** Mixed feelings — valuable but problematic

#### The Problem:
- **F1_4** (70 MB) and **F2_4** (49 MB) contain ALL EU data
- Most teams only need **Sweden** (~10% of the data = ~7 MB, much more manageable)
- Loading 70 MB CSV in a browser is painful and slow
- Teams will struggle with:
  - "The file won't load"
  - "My laptop is slow"
  - "I don't know how to filter this"

#### Current Guidance:
The brief says: *"Filter to Sweden early"* — but doesn't provide HOW.

#### The Reality:
- Smart teams: Ask Claude how to filter CSV → get a Python script → create `sweden_only.json` → done (30 min)
- Less experienced teams: Stuck, spend 1+ hour trying to load full file in browser → give up

#### Better Solution:

**Option A: Pre-filter to Sweden (Recommended)**
- Create `F1_4_Sweden_only.json` (~7 MB instead of 70 MB)
- Create `F2_4_Sweden_only.json` (~5 MB instead of 49 MB)
- Keep full CSV files for completeness
- Teams get instant working data, can still explore full EU if they want

**Option B: Keep as-is, but add pre-filtering script**
- Provide a simple Node.js or Python script that reads CSV, filters, saves JSON
- Include in the brief as "Quick Start: Pre-process E-PRTR data"
- Teams run once on Day 1, get JSON file they can use all week

**Option C: Host as online JSON API**
- Convert E-PRTR to a simple REST endpoint (could be Render.com free tier)
- Teams call `/api/facilities?country=Sweden` instead of downloading huge CSV
- More production-like, but requires infrastructure

**Recommendation:** ❌ **Option A: Pre-filter to Sweden**

Why:
- Removes biggest friction point (file size)
- Teams still have full data access if curious
- Takes you 10 min to create (in Python or Node)
- Saves each team 1-2 hours of debugging

---

## Summary Table: What to Keep, What to Remove

| File | Keep? | Reasoning |
|------|:-----:|-----------|
| `halland_skyddade_omraden.geojson` | ✅ YES | Small, usable, referenced in ideas |
| `NP.zip`, `NR.zip`, `NM.zip`, `DVO.zip`, `NVO.zip` | ❌ NO | Large, needs conversion, API available instead |
| `F1_4_Air_Releases_Facilities.csv` (70 MB) | ⚠️ ADD FILTERED VERSION | Too large; create `F1_4_Sweden.json` |
| `F2_4_Water_Releases_Facilities.csv` (49 MB) | ⚠️ ADD FILTERED VERSION | Too large; create `F2_4_Sweden.json` |
| `F1_2_Air_Releases_Sector` (3.5 MB) | ✅ YES | Small, useful for Idea #2 |
| `F3_2_Transfers_Facilities` (14 MB) | ⚠️ OPTIONAL | Useful for Idea #9, but large; consider filtering |
| `F4_2_WasteTransfers_Facilities` (4.6 MB) | ⚠️ OPTIONAL | Nordic-only, useful for Idea #9; keep as-is |

---

## Action Items for Organizers

### Immediate (Before hackathon):

1. **Filter E-PRTR to Sweden**
   ```python
   import pandas as pd
   
   # Read full E-PRTR
   df = pd.read_csv('F1_4_Air_Releases_Facilities.csv')
   
   # Filter to Sweden
   sweden = df[df['countryName'] == 'Sweden']
   
   # Save as compact JSON
   sweden.to_json('F1_4_Sweden.json', orient='records')
   # Result: ~7 MB instead of 70 MB
   ```

2. **Remove shapefiles** (optional but recommended)
   - Delete: `NP/`, `NR/`, `NM/`, `DVO/`, `NVO/` folders and zips
   - Keep the `.geojson` file
   - Save ~150 MB disk space

3. **Update data guide** (in brief or separate doc)
   - Add: "For large CSV files, we've pre-filtered key datasets to Sweden for faster loading"
   - Point to Sweden-filtered versions

4. **Add preprocessing tips** (optional)
   ```markdown
   ### If you want to use full E-PRTR data:
   
   Fast option: Use the Sweden-filtered JSON we've provided.
   
   Advanced option: Process the full CSV yourself:
   ```
   Ask Claude: "Show me how to filter F1_4_Air_Releases_Facilities.csv to Sweden and save as JSON"
   ```

### Nice-to-have (if time permits):

1. Add a **preprocessing script** to the repo
   ```python
   # Filter E-PRTR to a single country
   python scripts/filter_eprtr.py --country Sweden --output sweden_facilities.json
   ```

2. Create a **quick-start README** for data files
   ```
   # Using E-PRTR Data
   - Pre-filtered: F1_4_Sweden.json (7 MB, ready to use)
   - Full: F1_4_Air_Releases_Facilities.csv (70 MB, all EU)
   - How to filter your own: python scripts/filter_eprtr.py
   ```

---

## Final Recommendation

**Do this before the hackathon:**

| Action | Time | Impact |
|--------|------|--------|
| Create `F1_4_Sweden.json` | 10 min | 🔴 **Critical** — Saves teams 1-2 hours |
| Create `F2_4_Sweden.json` | 10 min | 🔴 **Critical** |
| Remove unused shapefiles | 5 min | 🟡 Optional but good housekeeping |
| Add data preprocessing note to brief | 5 min | 🟡 Helpful guidance |
| Create filtering script (optional) | 30 min | 🟢 Nice-to-have |

**Total time: 30 min.** Saves teams hours of frustration.

---

## Disk Space Impact

**Current state:** ~200 MB
- Shapefiles (unzipped): ~150 MB
- Large CSVs: ~120 MB  
- Everything else: ~30 MB

**After cleanup + pre-filtering:**
- `halland_skyddade_omraden.geojson`: ~2 MB
- `F1_4_Sweden.json`: ~7 MB
- `F2_4_Sweden.json`: ~5 MB
- Small CSVs (F1_2, etc.): ~20 MB
- **Total: ~35 MB** (83% reduction)

Faster to clone, no file size friction for teams.

---

**Bottom line:** Pre-filter the big CSV files to Sweden. It's the single biggest win for team productivity. Remove or move the shapefiles to keep things lean.
