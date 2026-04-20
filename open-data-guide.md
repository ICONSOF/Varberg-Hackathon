# Swedish Open Data — Complete Guide

This guide collects all data sources that can be used directly without registration: REST APIs, downloadable datasets, and local files.

---

## 1. REST APIs (call directly, no key needed)

### Naturvårdsverket — Protected Areas

- **Base URL:** `https://geodata.naturvardsverket.se/naturvardsregistret/rest/v3/`
- **Data:** National parks, nature reserves, municipal nature reserves, water protection areas, biotope protection, natural monuments
- **Format:** JSON, GeoJSON
- **License:** CC0
- **Example calls:**
  ```
  https://geodata.naturvardsverket.se/naturvardsregistret/rest/v3/omrade?skyddstypkod=NP
  https://geodata.naturvardsverket.se/naturvardsregistret/rest/v3/omrade?skyddstypkod=NR
  https://geodata.naturvardsverket.se/naturvardsregistret/rest/v3/omrade/skyddstyper
  ```

### SMHI MetObs — Historical Weather Observations

- **Base URL:** `https://opendata-download-metobs.smhi.se/api`
- **Data:** Temperature, wind, precipitation, snow depth, humidity, air pressure (~700 stations, data from 1800s)
- **Format:** JSON, CSV, XML
- **License:** CC BY
- **Navigation:** API → version → parameter → station → period → data
- **Example calls:**
  ```
  https://opendata-download-metobs.smhi.se/api/version/latest.json
  https://opendata-download-metobs.smhi.se/api/version/latest/parameter/1.json
  ```
  Parameter 1 = air temperature. Full parameter list on base URL.

### SMHI SNOW1g — Weather Forecast (replaces PMP3g)

- **Base URL:** `https://opendata-download-metfcst.smhi.se/api/category/snow1g/version/1`
- **Data:** Hourly forecast — temperature, wind, precipitation, cloud cover, etc.
- **Format:** JSON
- **Documentation:** `https://opendata.smhi.se/metfcst/snow1gv1/`
- **Example call (point forecast):**
  ```
  https://opendata-download-metfcst.smhi.se/api/category/snow1g/version/1/geotype/point/lon/12.0/lat/57.7/data.json
  ```

### SMHI Mesan — Interpolated Model Data

- **Base URL:** `https://opendata-download-metanalys.smhi.se/api/category/mesan2g/version/2`
- **Data:** Grid data for all of Sweden — temperature, wind, precipitation in grid
- **Format:** JSON
- **Documentation:** `https://opendata.smhi.se/metanalys/mesan2gv2/`
- **Example call:**
  ```
  https://opendata-download-metanalys.smhi.se/api/category/mesan2g/version/2/geotype/point/lon/12.0/lat/57.7/data.json
  ```

### SMHI Strång — Solar Radiation

- **Base URL:** `https://opendata-download-metanalys.smhi.se/api/category/strang1g/version/1`
- **Data:** Global and direct solar radiation per coordinate, historical data
- **Format:** JSON
- **Documentation:** `https://opendata.smhi.se/metanalys/strang/`
- **Example call:**
  ```
  https://opendata-download-metanalys.smhi.se/api/category/strang1g/version/1/geotype/point/lon/12.0/lat/57.7/parameter/116/data.json
  ```

### Nominatim (OpenStreetMap) — Geocoding

- **Base URL:** `https://nominatim.openstreetmap.org`
- **Data:** Address → coordinates (and vice versa)
- **Limitation:** Max 1 request/second, requires User-Agent header
- **Example calls:**
  ```
  https://nominatim.openstreetmap.org/search?format=json&q=Halmstad,Sweden
  https://nominatim.openstreetmap.org/reverse?format=json&lat=57.49&lon=12.08
  ```

### OpenStreetMap — Map Tiles

- **URL template:** `https://tile.openstreetmap.org/{z}/{x}/{y}.png`
- **Usage:** Background map in Leaflet.js or similar
- **Requires:** Valid User-Agent header

### SCB — Statistics Sweden / Statistikdatabasen API

- **Base URL:** `https://statistikdatabasen.scb.se/api/v2`
- **Data:** Official Swedish statistics across population, labour market, income, prices, transport, trade, energy, environment, housing, public finances, and more
- **Format:** JSON / JSON-stat via API, CSV download via table pages
- **License / usage:** Open data, free to use
- **Limits:** SCB states API rate limits apply; PxWebApi v2 allows up to 30 requests per 10 seconds per IP and up to 150,000 data cells per request
- **How to work with it:** Start from a table page in Statistikdatabasen, inspect the variables, then use the table's API link or the v2 table endpoint
- **Useful pages:**
  - Open data overview: `https://www.scb.se/en/services/open-data-api/`
  - PxWebApi v2: `https://www.scb.se/en/services/open-data-api/pxwebapi/pxapi-2.0/`
  - Statistical Database start page: `https://www.statistikdatabasen.scb.se/pxweb/en/ssd/`
- **What kinds of data it has:**
  - Population by municipality / county / age / sex
  - Labour market and unemployment
  - Household income and living conditions
  - Prices and inflation
  - Trade, transport, energy, environment and national accounts
- **Example pages / calls:**
  ```
  https://statistikdatabasen.scb.se/pxweb/en/ssd/
  https://www.statistikdatabasen.scb.se/pxweb/en/ssd/START__BE__BE0101__BE0101A/BefolkningNy/
  https://statistikdatabasen.scb.se/api/v2/tables/TAB5974
  https://statistikdatabasen.scb.se/api/v2/tables/TAB5974/data?lang=sv&outputFormat=json-stat2
  ```
  `TAB5974` is a real SCB table endpoint and returns table metadata plus links to metadata and data.

### OECD — Data Explorer + SDMX API

- **Main data hub:** `https://www.oecd.org/en/data.html`
- **Datasets catalog:** `https://www.oecd.org/en/data/datasets.html`
- **Indicators catalog:** `https://www.oecd.org/en/data/indicators.html`
- **API docs:** `https://www.oecd.org/en/data/insights/data-explainers/2024/09/api.html`
- **Data:** International comparative statistics across employment, trade, emissions, climate policy, health, public finance, innovation, education, and macroeconomics
- **Format:** SDMX-based API with JSON, CSV, and XML output options
- **How to work with it:** Open a dataset in OECD Data Explorer, make a selection, then click `Developer API` to get ready-made query URLs
- **What kinds of data it has:**
  - Employment and unemployment trends
  - Trade by enterprise characteristics
  - Air emissions and greenhouse-gas footprints
  - Climate policy instruments
  - GDP, inflation, productivity and other macro indicators
- **Useful dataset pages:**
  - Employment database: `https://www.oecd.org/en/data/datasets/oecd-employment-database.html`
  - Trade by Enterprise Characteristics: `https://www.oecd.org/en/data/datasets/trade-by-enterprise-characteristics-tec.html`
  - Air Emissions Accounts: `https://www.oecd.org/en/data/datasets/air-emissions-accounts.html`
  - Greenhouse gas footprint indicators: `https://www.oecd.org/en/data/datasets/greenhouse-gas-footprint-indicators.html`
  - Environment at a Glance dashboard: `https://www.oecd.org/en/data/dashboards/environment-at-a-glance.html`
- **Example API calls:**
  ```
  https://sdmx.oecd.org/public/rest/dataflow/all
  https://sdmx.oecd.org/public/rest/data/OECD.SDD.NAD,DSD_NAAG@DF_NAAG_I/all
  https://sdmx.oecd.org/public/rest/data/OECD.SDD.NAD,DSD_NAAG@DF_NAAG_I?dimensionAtObservation=AllDimensions&format=jsondata
  https://sdmx.oecd.org/public/rest/data/OECD.SDD.NAD,DSD_NAAG@DF_NAAG_I?format=csvfile
  ```
  These are official OECD examples showing how to list dataflows and fetch data in JSON or CSV.

---

## 2. Downloadable Datasets (files, no API)

### Naturvårdsverket — Geodata as Shapefiles

- **URL:** `https://geodata.naturvardsverket.se/nedladdning/`
- **Content:** Nature reserves, land cover (NMD), wetlands, forest, areas of national interest, sound environment, green infrastructure, grazing lands, etc.
- **Format:** Shapefile, GeoPackage
- **Open catalog** — click into folders and download directly.

### Naturvårdsverket — Open Data (documents & emissions)

- **URL:** `https://oppnadata.naturvardsverket.se`
- **Content:** Emissions by sector, environmental documents

### Naturvårdsverket — Geodata Catalog (metadata + WMS/WFS)

- **URL:** `https://geodatakatalogen.naturvardsverket.se`
- **Content:** Searchable catalog with metadata and download links

### Transportstyrelsen — Statistics Files

Web pages with downloadable Excel/CSV files. Not APIs, but data sources are freely available:

| Data | URL |
|------|-----|
| Vehicle statistics | `https://www.transportstyrelsen.se/sv/om-oss/statistik-och-analys/statistik-inom-vagtrafik/fordonsstatistik/` |
| CO₂ emissions from new vehicles | `https://www.transportstyrelsen.se/sv/om-oss/statistik-och-analys/statistik-inom-vagtrafik/statistik-over-koldioxidutslapp/` |
| Scrapping statistics | `https://www.transportstyrelsen.se/sv/om-oss/statistik-och-analys/statistik-inom-vagtrafik/skrotningsstatistik/` |
| Open data by transport mode | `https://www.transportstyrelsen.se/sv/om-oss/statistik-och-analys/oppna-data/oppna-data-utifran-trafikslag/` |

### SMHI VattenWeb — Hydrology

- **URL:** `https://vattenweb.smhi.se`
- **Content:** Water flow, runoff, future hydrological scenarios. Download without registration.

---

## 3. Local Files (in this repo)

All local data files are under the `files/` folder.

The participant-facing hackathon documents are in the repo root: `hackathon-brief.md`, `hackathon-app-ideas.md`, and `open-data-guide.md`.

### files/hackathon_data/

| Dataset | Format | Description |
|---------|--------|-------------|
| `halland_skyddade_omraden.geojson` | GeoJSON | Protected natural areas in Halland (nature reserves, Natura 2000, etc.) — works directly in Leaflet |
| `F1_4_Sweden.json` | JSON | Air emissions per Swedish facility — pre-filtered from E-PRTR, ready to use |
| `F2_4_Sweden.json` | JSON | Water emissions per Swedish facility — pre-filtered from E-PRTR, ready to use |

For national parks, nature reserves, and other protected areas across all of Sweden, use the Naturvårdsverket REST API instead of shapefiles.

### files/hackathon_data/eprtr_raw/

EU industrial emissions data (IED/E-PRTR) version 16, February 2026. Emissions data 2007–2024. 33,000+ named industrial facilities in the EU with address, coordinates, industry code (NACE), and emissions data.

**Source:** [EEA Industrial Emissions Data](https://sdi.eea.europa.eu/data/3bbf28cb-70e8-4073-8fe9-8c1d9c513f52)

#### Documentation

| File | Description |
|------|-------------|
| `EEA_Industrial_Reporting_Metadata_v16.pdf` | Metadata documentation |

#### CSV Files (available in repo)

| File | Content | Size | Scope | Key Columns |
|------|---------|------|-------|-------------|
| `F1_2_Air_Releases_Sector` | Air emissions by industry sector | 3.5 MB | All EU | Sector, substance, year, amount |
| `F1_4_Air_Releases_Facilities` | Air emissions per facility — name, address, coordinates, emissions | 70 MB | All EU | facilityName, countryName, Longitude, Latitude, PollutantName, TotalQuantity, reportingYear |
| `F2_4_Water_Releases_Facilities` | Water emissions per facility — same structure as F1_4 | 49 MB | All EU | facilityName, countryName, Longitude, Latitude, PollutantName, TotalQuantity, reportingYear |
| `F3_2_Transfers_Facilities` | Waste transports per facility — sender, receiver, type, amount | 14 MB | All EU | facilityName, countryName, Quantity, reportingYear |
| `F4_2_WasteTransfers_Facilities` | Waste transports per facility — type, amount, receiver | 4.6 MB | Nordic Region | facilityName, countryName, Quantity, reportingYear |

> **Tip:** `F1_4` and `F2_4` are the most useful files — they contain coordinates and emissions per facility and work as a ready-made lead list of industrial companies.

---

## Quick Reference — All API Endpoints

```
# Naturvårdsverket
https://geodata.naturvardsverket.se/naturvardsregistret/rest/v3/

# SMHI
https://opendata-download-metobs.smhi.se/api
https://opendata-download-metfcst.smhi.se/api/category/snow1g/version/1
https://opendata-download-metanalys.smhi.se/api/category/mesan2g/version/2
https://opendata-download-metanalys.smhi.se/api/category/strang1g/version/1

# Geocoding
https://nominatim.openstreetmap.org

# Map tiles
https://tile.openstreetmap.org/{z}/{x}/{y}.png

# SCB docs + API entry points
https://www.scb.se/en/services/open-data-api/pxwebapi/pxapi-2.0/
https://www.statistikdatabasen.scb.se/pxweb/en/ssd/
https://statistikdatabasen.scb.se/api/v2/tables/TAB5974

# OECD API
https://sdmx.oecd.org/public/rest/dataflow/all
https://sdmx.oecd.org/public/rest/data/OECD.SDD.NAD,DSD_NAAG@DF_NAAG_I/all
```

---

## Map Library

**Leaflet.js** — `https://leafletjs.com`
Open source, lightweight map library for web apps. Include via CDN:
```html
<link rel="stylesheet" href="https://unpkg.com/leaflet@1.9.4/dist/leaflet.css" />
<script src="https://unpkg.com/leaflet@1.9.4/dist/leaflet.js"></script>
```

### Leaflet starter example

This is enough to show a map with a local GeoJSON layer from `files/hackathon_data/`:

```html
<div id="map" style="height: 500px;"></div>
<script>
  const map = L.map("map").setView([56.95, 12.49], 8);

  L.tileLayer("https://tile.openstreetmap.org/{z}/{x}/{y}.png", {
    maxZoom: 19,
    attribution: "&copy; OpenStreetMap contributors"
  }).addTo(map);

  fetch("files/hackathon_data/halland_skyddade_omraden.geojson")
    .then((response) => response.json())
    .then((geojson) => {
      L.geoJSON(geojson).addTo(map);
    });
</script>
```
