# 🚀 Hackathon Brief — Hållbarhetsdata som affärsvärde

## Ert uppdrag

Bygg en webbapp som gör hållbarhetsdata **intressant, användbar och delbar**. Appen ska vara så bra att en företagsledare, miljöansvarig eller nyfiken person frivilligt testar den — och vill ha mer.

## Varför?

Företag sitter på enorma mängder öppen data om sin miljöpåverkan, men få vet om det eller använder det. Er app ska göra den datan tillgänglig, begriplig och värdefull. Ni behöver inte vara hållbarhetsexperter — ni ska göra data **intressant för vanliga människor**.

## Mål

| Mål | Beskrivning |
|-----|-------------|
| **Primärt** | Generera leads — få användare att vilja ge sin jobbmejl i utbyte mot mervärde |
| **Sekundärt** | Driva trafik till Iconsofs LinkedIn-sida |

---

## Krav (alla måste uppfyllas)

### 1. Fritt värde först
Användaren ska kunna testa appen och se något intressant **utan** att ange några uppgifter. Gör dem nyfikna först.

### 2. E-post-gate för mervärde
En djupare funktion — rapport, export, jämförelse, personlig analys — låses upp när användaren anger sin **jobbmejl**. Tänk: *"Ange din jobbmejl så skickar vi din rapport inom 30 sekunder."*

### 3. LinkedIn-dela-knapp (obligatorisk)
Varje app **måste** ha en synlig "Dela på LinkedIn"-knapp med förifyllt budskap som inkluderar länk till appen och Iconsofs LinkedIn-profil.

### 4. Minst 2 datakällor
Kombinera minst två av de tillhandahållna datakällorna. Ju mer kreativ kombination, desto bättre.

### 5. Körbar demo
Appen ska gå att visa live vid presentationen. Den behöver inte vara produktionsklar men ska fungera.

---

## Datakällor ni har tillgång till

### REST-API:er (anropa direkt, ingen nyckel behövs)

| API | Data | Exempel |
|-----|------|---------|
| **Naturvårdsverket NVR v3** | Nationalparker, naturreservat, skyddade områden | `https://geodata.naturvardsverket.se/naturvardsregistret/rest/v3/omrade?skyddstypkod=NP` |
| **SMHI MetObs** | Historisk temperatur, vind, nederbörd (~700 stationer) | `https://opendata-download-metobs.smhi.se/api/version/latest.json` |
| **SMHI Prognos (SNOW1g)** | Timvis väderprognos för valfri koordinat | `https://opendata-download-metfcst.smhi.se/api/category/snow1g/version/1/geotype/point/lon/12.0/lat/57.7/data.json` |
| **SMHI Mesan** | Interpolerad griddata (hela Sverige) | `https://opendata-download-metanalys.smhi.se/api/category/mesan2g/version/2/geotype/point/lon/12.0/lat/57.7/data.json` |
| **SMHI Strång** | Solinstrålning per koordinat, historisk | `https://opendata-download-metanalys.smhi.se/api/category/strang1g/version/1/geotype/point/lon/12.0/lat/57.7/parameter/116/data.json` |
| **Nominatim** | Adress → koordinater (och omvänt) | `https://nominatim.openstreetmap.org/search?format=json&q=Halmstad,Sweden` |
| **OSM Tiles** | Bakgrundskarta för Leaflet | `https://tile.openstreetmap.org/{z}/{x}/{y}.png` |

### MCP-servrar (för AI-agenter)

| Server | Data | URL |
|--------|------|-----|
| **SCB** | 1 200+ statistiktabeller (befolkning, ekonomi, miljö, arbetsmarknad) | `https://scb-mcp.onrender.com/mcp` |
| **OECD** | 5 000+ dataset, 38 länder (ekonomi, hälsa, miljö, energi) | `https://oecd-mcp.onrender.com/mcp` |

### E-PRTR — Industriutsläppsdata (CSV-filer)

Industrianläggningar i Norden (Sverige, Norge, Danmark, Finland) med namn, adress, koordinater, branschkod och utsläppsdata 2007–2024. **Detta är er mest värdefulla datakälla.** Filerna är förfiltrerade till Norden och kan laddas direkt.

| Fil | Innehåll | Storlek |
|-----|----------|---------|
| `F1_4_Air_Releases_Facilities` | Luftutsläpp per anläggning — namn, koordinater, ämne, mängd, år | ~5 MB |
| `F2_4_Water_Releases_Facilities` | Vattenutsläpp per anläggning — samma struktur som F1_4 | ~4 MB |
| `F1_1_Air_Releases_National` | Luftutsläpp aggregerat per land | < 1 MB |
| `F1_2_Air_Releases_Sector` | Luftutsläpp per branschsektor | 3.5 MB |
| `F3_2_Transfers_Facilities` | Avfallstransporter per anläggning — avsändare, mottagare, typ, mängd | 13 MB |

> **Tips:** Filtrera vidare till Sverige (`CountryCode = "SE"`) om ni bara vill visa svensk data.

### Lokala filer

| Fil | Format | Beskrivning |
|-----|--------|-------------|
| `halland_skyddade_omraden.geojson` | GeoJSON | Skyddade naturområden i Halland — fungerar direkt i Leaflet |
| Shapefiler (NP, NR, NM, DVO, NVO) | Shapefile | Nationalparker, naturreservat m.m. för hela Sverige |

### Nedladdningsbara datakällor

- **Transportstyrelsen** — Fordonsstatistik, CO₂-utsläpp nya fordon, skrotningsstatistik (Excel/CSV)
- **SMHI VattenWeb** — Vattenföring, avrinning (nedladdning)
- **Naturvårdsverket geodata** — Marktäcke, skog, riksintressen m.m. (Shapefile/GeoPackage)

### Kartor

**Leaflet.js** — lägg till i er HTML:
```html
<link rel="stylesheet" href="https://unpkg.com/leaflet@1.9.4/dist/leaflet.css" />
<script src="https://unpkg.com/leaflet@1.9.4/dist/leaflet.js"></script>
```

---

## Bedömningskriterier

| Kriterium | Vikt | Frågan juryn ställer sig |
|-----------|------|--------------------------|
| 🎯 **Leadkraft** | 30% | Skulle jag ge min jobbmejl för att få detta? |
| 🔀 **Datamashup** | 25% | Hur kreativt kombineras datakällor? |
| ✨ **Wow-faktor** | 25% | Är detta snyggt, interaktivt och delbart? |
| 🔧 **Färdighetsgrad** | 20% | Hur nära en riktig produkt kom gruppen? |

---

## Tips

### 💡 Tips 1: Använd AI som medhjälpare
Om ni har tillgång till ett AI-verktyg (ChatGPT, Claude, Copilot) — ladda in `svenska-oppna-data-guide.md` tillsammans med denna brief och fråga: *"Vilka API-anrop behöver jag för att bygga [er idé]?"*. AI:n kan hjälpa er förstå API-strukturerna snabbt.

### 💡 Tips 2: Börja med datan
Innan ni skriver en enda rad kod — testa API-anropen i webbläsaren. Klistra in en URL och se vad som kommer tillbaka. Förstå datan först, bygg sen.

### 💡 Tips 3: Filtrera E-PRTR tidigt
CSV-filerna är stora. Första steget: filtrera till Sverige (och ev. ett specifikt län) och spara som en liten JSON-fil som er app kan ladda snabbt.

### 💡 Tips 4: MVP först, polish sen
Bygg den enklaste versionen som funkar — en karta med prickar, en lista med siffror. Gör det snyggt *efteråt*. Ni har bara ~1.5 dag.

### 💡 Tips 5: Stycka upp arbetet
Varje idé kan delas i parallella delar (karta, data, gate, design). Bestäm tidigt vem som gör vad så ni inte blockerar varandra.

### 💡 Tips 6: LinkedIn-knappen är enkel
```javascript
const shareUrl = `https://www.linkedin.com/sharing/share-offsite/?url=${encodeURIComponent(appUrl)}`;
```
Lägg till den tidigt — det är ett krav och tar 5 minuter.

### 💡 Tips 7: Skrapa om ni vill
Ni är inte begränsade till de tillhandahållna källorna. Om ni hittar en intressant webbsida med hållbarhetsdata — skrapa den! Men se till att minst 2 av källorna i guiden används.

### 💡 Tips 8: Tänk delbarhet
Den app som folk *vill* visa för andra vinner. Fråga er: *"Skulle jag skicka detta till en kollega?"*

---

## Leverans

- Fungerande app som kan visas live
- Kort presentation (5 min) som förklarar: vad appen gör, vilka datakällor som används, och varför någon skulle vilja använda den
- Källkod i ett repo som kan överlämnas till Iconsof

**Lycka till! 🎉**
