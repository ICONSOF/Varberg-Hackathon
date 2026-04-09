# Svenska Öppna Data — Komplett guide

Denna guide samlar alla datakällor som kan användas direkt utan registrering: REST-API:er, nedladdningsbara dataset, MCP-servrar och lokala filer.

---

## 1. REST-API:er (anropa direkt, ingen nyckel behövs)

### Naturvårdsverket — Skyddade områden

- **Bas-URL:** `https://geodata.naturvardsverket.se/naturvardsregistret/rest/v3/`
- **Data:** Nationalparker, naturreservat, kommunala naturreservat, vattenskyddsområden, biotopskydd, naturminnen
- **Format:** JSON, GeoJSON
- **Licens:** CC0
- **Exempelanrop:**
  ```
  https://geodata.naturvardsverket.se/naturvardsregistret/rest/v3/nationalpark
  https://geodata.naturvardsverket.se/naturvardsregistret/rest/v3/naturreservat
  ```

### SMHI MetObs — Historiska väderobservationer

- **Bas-URL:** `https://opendata-download-metobs.smhi.se/api`
- **Data:** Temperatur, vind, nederbörd, snödjup, luftfuktighet, lufttryck (~700 stationer, data från 1800-talet)
- **Format:** JSON, CSV, XML
- **Licens:** CC BY
- **Navigering:** API → version → parameter → station → period → data
- **Exempelanrop:**
  ```
  https://opendata-download-metobs.smhi.se/api/version/latest.json
  https://opendata-download-metobs.smhi.se/api/version/latest/parameter/1.json
  ```
  Parameter 1 = lufttemperatur. Full parameterlista finns på bas-URL:en.

### SMHI MetFcst — Väderprognos 10 dygn

- **Bas-URL:** `https://opendata-download-metfcst.smhi.se/api`
- **Data:** Timvis prognos, 15 parametrar (temp, vind, nederbörd, molnighet m.m.)
- **Format:** JSON
- **Exempelanrop (punkt-prognos):**
  ```
  https://opendata-download-metfcst.smhi.se/api/category/pmp3g/version/2/geotype/point/lon/12.0/lat/57.7/data.json
  ```

### SMHI Mesan — Interpolerad modelldata

- **Bas-URL:** `https://opendata-download-mesan.smhi.se/api`
- **Data:** Griddata hela Sverige — temperatur, vind, nederbörd i rutnät
- **Format:** JSON

### SMHI Strång — Solinstrålning

- **Bas-URL:** `https://opendata-download-metanalys.smhi.se/api`
- **Data:** Global och direkt solinstrålning per koordinat, historisk data
- **Format:** JSON

### Nominatim (OpenStreetMap) — Geocoding

- **Bas-URL:** `https://nominatim.openstreetmap.org`
- **Data:** Adress → koordinater (och omvänt)
- **Begränsning:** Max 1 request/sekund, kräver User-Agent-header
- **Exempelanrop:**
  ```
  https://nominatim.openstreetmap.org/search?format=json&q=Kungsbacka,Sweden
  https://nominatim.openstreetmap.org/reverse?format=json&lat=57.49&lon=12.08
  ```

### OpenStreetMap — Kartbilder (tiles)

- **URL-mall:** `https://tile.openstreetmap.org/{z}/{x}/{y}.png`
- **Användning:** Bakgrundskarta i Leaflet.js eller liknande
- **Kräver:** Giltig User-Agent-header

---

## 2. MCP-servrar (för AI-agenter och Claude)

Dessa kopplas in i Claude via MCP-protokollet och ger direkt åtkomst till stora statistikdatabaser.

### SCB — Statistiska centralbyrån

- **MCP-URL:** `https://scb-mcp.onrender.com/mcp`
- **Data:** 1 200+ statistiktabeller — befolkning, ekonomi, miljö, arbetsmarknad, utbildning, boende, hälsa, transport. Data från 1950-talet till idag. 312+ regioner.
- **Nyckelverktyg:**

| Verktyg | Vad det gör |
|---------|-------------|
| `scb_search_tables` | Sök tabeller med svenska termer ("befolkning", "utsläpp") |
| `scb_get_table_variables` | Se vilka variabler/värden en tabell har — **kör alltid detta först** |
| `scb_get_table_data` | Hämta data med filter. Använd `"TOP(5)"` för senaste 5 perioder |
| `scb_preview_data` | Förhandsgranska ~50 rader innan full hämtning |
| `scb_search_regions` | Sök regionkoder ("Lerum" → 1441). Fuzzy matching fungerar |

- **Exempelflöde:**
  ```
  1. scb_search_tables("växthusgaser")          → hitta tabell-ID
  2. scb_get_table_variables("MI0107T08")        → se struktur
  3. scb_preview_data("MI0107T08")               → kontrollera
  4. scb_get_table_data("MI0107T08", selection)  → hämta data
  ```

### OECD — Internationell statistik

- **MCP-URL:** `https://oecd-mcp.onrender.com/mcp`
- **Data:** 5 000+ dataset, 38 OECD-länder + partnerekonomier. 17 kategorier: ekonomi, hälsa, miljö, utbildning, energi, skatter, handel m.m.
- **Nyckelverktyg:**

| Verktyg | Vad det gör |
|---------|-------------|
| `search_dataflows` | Sök dataset ("GDP", "emissions", "unemployment") |
| `get_data_structure` | Se dimensioner och giltiga värden — **kör alltid detta först** |
| `query_data` | Hämta data med SDMX-filter och tidsavgränsning |
| `search_indicators` | Sök specifika indikatorer |
| `get_categories` | Lista alla 17 kategorier |

- **Landskoder:** ISO 3166-1 alpha-3 (SWE, NOR, DNK, FIN, DEU, USA)
- **Exempelflöde:**
  ```
  1. search_dataflows("greenhouse gas emissions")  → hitta dataset-ID
  2. get_data_structure("AIR_GHG")                 → se dimensioner
  3. query_data("AIR_GHG", filter: "SWE+NOR+DNK", last_n_observations: 20)
  ```

---

## 3. Nedladdningsbara dataset (filer, ingen API)

### Naturvårdsverket — Geodata som shapefiler

- **URL:** `https://geodata.naturvardsverket.se/nedladdning/`
- **Innehåll:** Naturreservat, marktäcke (NMD), våtmark, skog, riksintressen, ljudmiljö, grön infrastruktur, betesmarker m.m.
- **Format:** Shapefile, GeoPackage
- **Öppen katalog** — klicka in i mappar och ladda ner direkt.

### Naturvårdsverket — Öppna data (dokument & utsläpp)

- **URL:** `https://oppnadata.naturvardsverket.se`
- **Innehåll:** Utsläpp per bransch, miljödokument

### Naturvårdsverket — Geodatakatalog (metadata + WMS/WFS)

- **URL:** `https://geodatakatalogen.naturvardsverket.se`
- **Innehåll:** Sökbar katalog med metadata och nedladdningslänkar

### Transportstyrelsen — Statistikfiler

Webbsidor med nedladdningsbara Excel/CSV-filer. Inte API:er, men datakällorna är fritt tillgängliga:

| Data | URL |
|------|-----|
| Fordonsstatistik | `https://www.transportstyrelsen.se/sv/om-oss/statistik-och-analys/statistik-inom-vagtrafik/fordonsstatistik/` |
| CO₂-utsläpp nya fordon | `https://www.transportstyrelsen.se/sv/om-oss/statistik-och-analys/statistik-inom-vagtrafik/vaxthusgaser/` |
| Skrotningsstatistik | `https://www.transportstyrelsen.se/sv/om-oss/statistik-och-analys/statistik-inom-vagtrafik/skrotningsstatistik/` |
| Öppna data per trafikslag | `https://www.transportstyrelsen.se/sv/om-oss/statistik-och-analys/oppna-data/oppna-data-utifran-trafikslag/` |

### SMHI VattenWeb — Hydrologi

- **URL:** `https://vattenweb.smhi.se`
- **Innehåll:** Vattenföring, avrinning, framtida hydrologiska scenarier. Nedladdning utan registrering.

---

## 4. Lokala filer

### halland_skyddade_omraden.geojson

- **Innehåll:** Skyddade naturområden i Hallands län (naturreservat, Natura 2000 m.m.)
- **Format:** GeoJSON
- **Användning:** Kan laddas direkt i Leaflet.js, QGIS, eller bearbetas med Python/GeoPandas.

---

## Snabbreferens — Alla API-endpoints

```
# Naturvårdsverket
https://geodata.naturvardsverket.se/naturvardsregistret/rest/v3/

# SMHI
https://opendata-download-metobs.smhi.se/api
https://opendata-download-metfcst.smhi.se/api
https://opendata-download-mesan.smhi.se/api
https://opendata-download-metanalys.smhi.se/api

# Geocoding
https://nominatim.openstreetmap.org

# Kartbilder
https://tile.openstreetmap.org/{z}/{x}/{y}.png

# MCP-servrar (för Claude / AI-agenter)
https://scb-mcp.onrender.com/mcp
https://oecd-mcp.onrender.com/mcp
```

---

## Kartbibliotek

**Leaflet.js** — `https://leafletjs.com`
Öppen källkod, lättviktigt kartbibliotek för webbappar. Inkludera via CDN:
```html
<link rel="stylesheet" href="https://unpkg.com/leaflet@1.9.4/dist/leaflet.css" />
<script src="https://unpkg.com/leaflet@1.9.4/dist/leaflet.js"></script>
```
