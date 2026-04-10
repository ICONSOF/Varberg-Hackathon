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
  https://geodata.naturvardsverket.se/naturvardsregistret/rest/v3/omrade?skyddstypkod=NP
  https://geodata.naturvardsverket.se/naturvardsregistret/rest/v3/omrade?skyddstypkod=NR
  https://geodata.naturvardsverket.se/naturvardsregistret/rest/v3/omrade/skyddstyper
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

### SMHI SNOW1g — Väderprognos (ersätter PMP3g)

- **Bas-URL:** `https://opendata-download-metfcst.smhi.se/api/category/snow1g/version/1`
- **Data:** Timvis prognos — temp, vind, nederbörd, molnighet m.m.
- **Format:** JSON
- **Dokumentation:** `https://opendata.smhi.se/metfcst/snow1gv1/`
- **Exempelanrop (punkt-prognos):**
  ```
  https://opendata-download-metfcst.smhi.se/api/category/snow1g/version/1/geotype/point/lon/12.0/lat/57.7/data.json
  ```

### SMHI Mesan — Interpolerad modelldata

- **Bas-URL:** `https://opendata-download-metanalys.smhi.se/api/category/mesan2g/version/2`
- **Data:** Griddata hela Sverige — temperatur, vind, nederbörd i rutnät
- **Format:** JSON
- **Dokumentation:** `https://opendata.smhi.se/metanalys/mesan2gv2/`
- **Exempelanrop:**
  ```
  https://opendata-download-metanalys.smhi.se/api/category/mesan2g/version/2/geotype/point/lon/12.0/lat/57.7/data.json
  ```

### SMHI Strång — Solinstrålning

- **Bas-URL:** `https://opendata-download-metanalys.smhi.se/api/category/strang1g/version/1`
- **Data:** Global och direkt solinstrålning per koordinat, historisk data
- **Format:** JSON
- **Dokumentation:** `https://opendata.smhi.se/metanalys/strang/`
- **Exempelanrop:**
  ```
  https://opendata-download-metanalys.smhi.se/api/category/strang1g/version/1/geotype/point/lon/12.0/lat/57.7/parameter/116/data.json
  ```

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

MCP-servrar kopplas in i Claude (och andra AI-klienter) via MCP-protokollet och ger direkt åtkomst till stora statistikdatabaser.

| Server | Data | MCP-URL |
|--------|------|---------|
| **SCB** | 1 200+ statistiktabeller — befolkning, ekonomi, miljö, arbetsmarknad, utbildning m.m. Data från 1950-talet, 312+ regioner. | `https://scb-mcp.onrender.com/mcp` |
| **OECD** | 5 000+ dataset, 38 OECD-länder, 17 kategorier: ekonomi, hälsa, miljö, utbildning, energi, handel m.m. | `https://oecd-mcp.onrender.com/mcp` |

**Fullständig guide med alla verktyg, promptmallar och installationsinstruktioner finns i MCP-repot:**
**https://github.com/ICONSOF/MCP**

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
| CO₂-utsläpp nya fordon | `https://www.transportstyrelsen.se/sv/om-oss/statistik-och-analys/statistik-inom-vagtrafik/statistik-over-koldioxidutslapp/` |
| Skrotningsstatistik | `https://www.transportstyrelsen.se/sv/om-oss/statistik-och-analys/statistik-inom-vagtrafik/skrotningsstatistik/` |
| Öppna data per trafikslag | `https://www.transportstyrelsen.se/sv/om-oss/statistik-och-analys/oppna-data/oppna-data-utifran-trafikslag/` |

### SMHI VattenWeb — Hydrologi

- **URL:** `https://vattenweb.smhi.se`
- **Innehåll:** Vattenföring, avrinning, framtida hydrologiska scenarier. Nedladdning utan registrering.

---

## 4. Lokala filer (i detta repo)

Alla lokala datafiler ligger under mappen `files/`.

### files/hackathon_data/

| Dataset | Format | Beskrivning |
|---------|--------|-------------|
| `halland_skyddade_omraden.geojson` | GeoJSON | Skyddade naturområden i Hallands län (naturreservat, Natura 2000 m.m.) |
| `DVO/` + `DVO.zip` | Shapefile | Djur- och växtskyddsområden (polygoner) |
| `NM/` + `NM.zip` | Shapefile | Naturminnen (punkter och polygoner) |
| `NP/` + `NP.zip` | Shapefile | Nationalparker (polygoner) |
| `NR/` + `NR.zip` | Shapefile | Naturreservat (polygoner) |
| `NVO/` + `NVO.zip` | Shapefile | Naturvårdsområden (polygoner) |

Shapefiler kan öppnas i QGIS, ArcGIS, eller bearbetas med Python/GeoPandas. GeoJSON fungerar direkt i Leaflet.js.

### files/eea_t_ied-eprtr_p_2007-2024_v16_r00/

EU:s industriutsläppsdata (IED/E-PRTR) version 16, februari 2026. Utsläppsdata 2007–2024. 33 000+ namngivna industrianläggningar i EU med adress, koordinater, branschkod (NACE) och utsläppsdata.

**Källa:** [EEA Industrial Emissions Data](https://sdi.eea.europa.eu/data/3bbf28cb-70e8-4073-8fe9-8c1d9c513f52)

#### Dokumentation

| Fil | Beskrivning |
|-----|-------------|
| `EEA_Industrial_Reporting_Metadata_v16.pdf` | Metadata-dokumentation |
| `README.md` | Datasetbeskrivning med käll-länk |

#### CSV-filer (tillgängliga i repot)

Följande CSV-filer finns tillgängliga direkt. De större filerna har förfiltrerats till Norden (Sverige, Norge, Danmark, Finland) för att vara hanterbara.

| Fil | Innehåll | Storlek | Nyckelkolumner |
|-----|----------|---------|----------------|
| `F1_2_Air_Releases_Sector` | Luftutsläpp per branschsektor | 3.5 MB | Sektor, ämne, år, mängd |
| `F1_4_Air_Releases_Facilities` | Luftutsläpp per anläggning — namn, adress, koordinater, utsläpp | 70 MB | FacilityName, CountryCode, Lat, Long, PollutantName, TotalQuantity, ReportingYear |
| `F2_4_Water_Releases_Facilities` | Vattenutsläpp per anläggning — samma struktur som F1_4 | 49 MB | FacilityName, CountryCode, Lat, Long, PollutantName, TotalQuantity, ReportingYear |
| `F3_2_Transfers_Facilities` | Avfallstransporter per anläggning — avsändare, mottagare, typ, mängd | 14 MB | FacilityName, WasteHandlerName, Quantity, ReportingYear |
| `F4_2_WasteTransfers_Facilities` | Avfallstransporter per anläggning — typ, mängd, mottagare | 4.6 MB | FacilityName, CountryCode, Quantity, ReportingYear |

> **Tips:** `F1_4` och `F2_4` är de mest användbara filerna — de innehåller koordinater och utsläpp per anläggning och fungerar som en färdig lead-lista över industriföretag.

---

## Snabbreferens — Alla API-endpoints

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

# Kartbilder
https://tile.openstreetmap.org/{z}/{x}/{y}.png

# MCP-servrar
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
