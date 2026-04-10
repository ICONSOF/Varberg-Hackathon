# 💡 App-idéer — Hackathon Hållbarhetsdata

Välj en av dessa idéer eller använd dem som inspiration för en egen. Varje idé är uppdelad i parallella arbetsdelar (A–D) som kan utvecklas separat. **Även om ni bara hinner 2 av 4 delar har ni en visbar app.**

---

## Betygsförklaring

Varje idé är bedömd på fem faktorer (skala 1–5):

| Faktor | Betydelse |
|--------|-----------|
| 🎯 **Leadmagnet** | Hur starkt vill en användare ge sin mejl? |
| 🗺️ **Visuell punch** | Hur snygg och kartbaserad är appen? |
| 🧩 **Byggtid** | Hur realistiskt är det att hinna? (5 = enkelt) |
| 🦄 **Unikhet** | Finns detta redan? (5 = helt nytt) |
| 🔥 **Delbarhet** | Skulle folk dela detta på LinkedIn? |

---

## Idé 1: 🗺️ Grön Grannsämja — "Hur nära bor du industrin?"

> Skriv in en adress och se vilka industrianläggningar som ligger runtom dig, vad de släpper ut och vilken natur som skyddas i närheten.

| 🎯 Leadmagnet | 🗺️ Visuell punch | 🧩 Byggtid | 🦄 Unikhet | 🔥 Delbarhet |
|:---:|:---:|:---:|:---:|:---:|
| ⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐⭐ | ⭐⭐⭐⭐ |

**Datakällor:** E-PRTR (F1_4), Nominatim, OSM, Naturvårdsverket GeoJSON

| Del | Uppgift | Pers. | Fristående? |
|-----|---------|:-----:|:-----------:|
| **A. Kartan** | Leaflet med E-PRTR-anläggningar som markörer, popups med namn + utsläpp | 1–2 | ✅ Fungerande app i sig |
| **B. Sök + radie** | Adressfält (Nominatim), filtrera anläggningar inom 5/10/25 km | 1 | Förbättrar A |
| **C. Gate + rapport** | E-post-input → generera "din närområdesanalys" | 1 | Lead-funktionen |
| **D. Naturlager** | Overlay med skyddade områden (GeoJSON), kontrast industri vs natur | 1 | Wow-lager |

**MVP: A + C** → fungerande kartapp med leads. **Full build: A + B + C + D** → vinnarpotential.

---

## Idé 2: 📊 Branschduellen — "Hur ren är din bransch?"

> Välj två branscher och se dem jämförda: utsläppstrender, antal anläggningar, geografisk spridning. Interaktiva grafer.

| 🎯 Leadmagnet | 🗺️ Visuell punch | 🧩 Byggtid | 🦄 Unikhet | 🔥 Delbarhet |
|:---:|:---:|:---:|:---:|:---:|
| ⭐⭐⭐⭐ | ⭐⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ |

**Datakällor:** E-PRTR (F1_2, F1_4), SCB MCP, OECD MCP

| Del | Uppgift | Pers. | Fristående? |
|-----|---------|:-----:|:-----------:|
| **A. Branschväljare + grafer** | Dropdown × 2, stapeldiagram utsläpp per år | 1–2 | ✅ Fungerande jämförelseapp |
| **B. Kartvy** | Anläggningar på karta, färgkodade per bransch | 1 | Visuell wow |
| **C. SCB-koppling** | Hämta antal anställda per bransch, beräkna utsläpp/anställd | 1 | Smartare analys |
| **D. Gate + delning** | E-post-gate för rapport, LinkedIn med "Visste du att…" | 1 | Lead-funktionen |

**MVP: A + D.** **Full build: A + B + C + D.**

---

## Idé 3: 🌿 Hallands Naturkarta — "Upptäck vad som skyddas"

> Interaktiv karta över Hallands skyddade natur med väderlager och solinstrålning. Perfekt för kommuner och fastighetsbolag.

| 🎯 Leadmagnet | 🗺️ Visuell punch | 🧩 Byggtid | 🦄 Unikhet | 🔥 Delbarhet |
|:---:|:---:|:---:|:---:|:---:|
| ⭐⭐⭐ | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ | ⭐⭐⭐ | ⭐⭐⭐ |

**Datakällor:** halland_skyddade_omraden.geojson, NVR v3, SMHI MetObs, SMHI Strång, OSM

| Del | Uppgift | Pers. | Fristående? |
|-----|---------|:-----:|:-----------:|
| **A. Karta + GeoJSON** | Leaflet med skyddade områden, klickbara polygoner | 1–2 | ✅ Snygg kartapp |
| **B. Väderlager** | SMHI-data för närmaste station, temp/nederbörd | 1 | Mervärdeslager |
| **C. Sol-overlay** | Strång-data som heatmap per område | 1 | Visuell wow |
| **D. Gate + export** | E-post för PDF-sammanfattning, LinkedIn-knapp | 1 | Lead-funktionen |

**MVP: A + D.** Bra för grupper som gillar kartor och design.

---

## Idé 4: ☀️ Solpotential-kalkylatorn — "Hur mycket sol träffar ditt tak?"

> Ange en adress och se solinstrålning, uppskattad elproduktion och CO₂-besparing. Inte en solcellskalkylator — ett energilandskap.

| 🎯 Leadmagnet | 🗺️ Visuell punch | 🧩 Byggtid | 🦄 Unikhet | 🔥 Delbarhet |
|:---:|:---:|:---:|:---:|:---:|
| ⭐⭐⭐⭐⭐ | ⭐⭐⭐ | ⭐⭐⭐ | ⭐⭐⭐ | ⭐⭐⭐⭐ |

**Datakällor:** SMHI Strång, SMHI MetObs, Nominatim, SCB MCP

| Del | Uppgift | Pers. | Fristående? |
|-----|---------|:-----:|:-----------:|
| **A. Adress → soldata** | Input, Nominatim-geocoding, hämta Strång-data | 1–2 | ✅ Fungerande kalkylator |
| **B. Visualisering** | Månadsgrafer sol + temperatur (Recharts/Chart.js) | 1 | Wow-faktor |
| **C. Beräkningsmotor** | Uppskattad kWh, CO₂-besparing, payback | 1 | Affärsvärde |
| **D. Gate + jämförelse** | E-post för årsrapport, jämför mot rikssnitt | 1 | Lead-funktionen |

**MVP: A + C + D.** Populärt hos privatpersoner — hög leadkonvertering.

---

## Idé 5: 🚛 Logistikpulsen Halland — "E6-korridorens klimatavtryck"

> Visualisera transportflöden längs E6/E20, Halmstad hamn och Västkustbanan. Simulera: "Vad händer om vi flyttar gods från väg till tåg?"

| 🎯 Leadmagnet | 🗺️ Visuell punch | 🧩 Byggtid | 🦄 Unikhet | 🔥 Delbarhet |
|:---:|:---:|:---:|:---:|:---:|
| ⭐⭐⭐ | ⭐⭐⭐⭐⭐ | ⭐⭐ | ⭐⭐⭐⭐⭐ | ⭐⭐⭐ |

**Datakällor:** Transportstyrelsen, E-PRTR, SCB MCP, SMHI, OSM

| Del | Uppgift | Pers. | Fristående? |
|-----|---------|:-----:|:-----------:|
| **A. Kartvy E6** | Leaflet med väg/hamn/järnväg, transportstatistik som overlay | 1–2 | ✅ Visuell demo |
| **B. Scenario-slider** | "Flytta X% väg → tåg", visa CO₂-förändring live | 1 | Interaktiv wow |
| **C. Datakoppling** | Transportstyrelsen + E-PRTR + SCB godsvolymer | 1 | Trovärdighet |
| **D. Gate + rapport** | E-post för scenariorapport, LinkedIn-delning | 1 | Lead-funktionen |

**MVP: A + B + D.** Svårast att bygga men störst wow. För ambitiösa grupper.

---

## Idé 6: 🏭 Utsläppsrankingen — "Topp 10 i ditt län"

> Ranking av de största utsläpparna per län. Filtrera på ämne, se trender. Tänk "Spotify Wrapped" men för industriutsläpp.

| 🎯 Leadmagnet | 🗺️ Visuell punch | 🧩 Byggtid | 🦄 Unikhet | 🔥 Delbarhet |
|:---:|:---:|:---:|:---:|:---:|
| ⭐⭐⭐⭐ | ⭐⭐⭐ | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ |

**Datakällor:** E-PRTR (F1_4), Nominatim, SCB MCP

| Del | Uppgift | Pers. | Fristående? |
|-----|---------|:-----:|:-----------:|
| **A. Rankinglista** | Filtrera E-PRTR på län/ämne, visa topp 10 med stapeldiagram | 1–2 | ✅ Fungerande app |
| **B. Trendvy** | Klicka på anläggning → se utsläppstrend 2007–2024 | 1 | Djup |
| **C. Kartvy** | Anläggningar på karta, cirkelstorlek = utsläpp | 1 | Visuell wow |
| **D. "Wrapped"** | "Ditt läns utsläpps-wrapped 2024" som delbar bild, e-post-gate | 1 | Viral potential |

**MVP: A + D.** Enklast att bygga, högst delbarhet. **Bäst för grupper med mindre teknisk erfarenhet.**

---

## Idé 7: 💧 Vattenriskkollen — "Hur utsatt är din kommun?"

> Kombinera vattenutsläpp från industrin (E-PRTR) med hydrologisk data (SMHI VattenWeb) och skyddade vattenmiljöer. Visa risken visuellt på en karta — vilka vattendrag är mest belastade?

| 🎯 Leadmagnet | 🗺️ Visuell punch | 🧩 Byggtid | 🦄 Unikhet | 🔥 Delbarhet |
|:---:|:---:|:---:|:---:|:---:|
| ⭐⭐⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐⭐ | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐ |

**Datakällor:** E-PRTR (F2_4 Water_Releases_Facilities), SMHI VattenWeb, NVR skyddade områden, Nominatim, OSM

| Del | Uppgift | Pers. | Fristående? |
|-----|---------|:-----:|:-----------:|
| **A. Vattenutsläppskarta** | Leaflet med F2_4-anläggningar, färgkodade cirklar per utsläppsmängd | 1–2 | ✅ Fungerande kartapp |
| **B. Kommun-sök** | Sök kommun, se aggregerad bild: antal anläggningar, totalt utsläpp, trend | 1 | Personligt relevant |
| **C. Skyddade vatten** | Overlay med vattenskyddsområden från NVR — visa konfliktzoner | 1 | "Aha-moment" |
| **D. Gate + riskrapport** | E-post → "Din kommuns vattenriskprofil" som PDF, LinkedIn-knapp | 1 | Lead-funktionen |

**MVP: A + B + D.** Stark koppling till lokalpolitik och fastigheter.

---

## Idé 8: 🌡️ Klimattidsmaskinen — "Så har vädret förändrats där du bor"

> Ange en ort och se hur temperaturen har förändrats de senaste 50–100 åren, baserat på SMHI:s faktiska mätdata. Personligt, visuellt och lite skrämmande.

| 🎯 Leadmagnet | 🗺️ Visuell punch | 🧩 Byggtid | 🦄 Unikhet | 🔥 Delbarhet |
|:---:|:---:|:---:|:---:|:---:|
| ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐⭐ | ⭐⭐⭐⭐⭐ |

**Datakällor:** SMHI MetObs (historisk temperatur, parameter 1), Nominatim, SCB MCP (befolkning per ort)

| Del | Uppgift | Pers. | Fristående? |
|-----|---------|:-----:|:-----------:|
| **A. Ortsök + temperaturtrend** | Input-fält, hitta närmaste SMHI-station, visa årsmedel som linjediagram | 1–2 | ✅ Fungerande app — och redan wow |
| **B. Jämförelsevy** | Jämför två orter sida vid sida — "Stockholm vs Kiruna" | 1 | Interaktivitet |
| **C. "Ditt födelseår"** | Ange födelseår, se hur medeltemperaturen ändrats under din livstid | 1 | Personlig hook — delbart |
| **D. Gate + rapport** | E-post → "Klimatprofil för [ort]" med grafer, LinkedIn-delning | 1 | Lead-funktionen |

**MVP: A + C + D.** Extremt delbart, enkel att bygga, personlig. **Bäst viralpotential.**

---

## Idé 9: 🏗️ Avfallskartan — "Vart tar avfallet vägen?"

> Visualisera hur industriavfall transporteras mellan anläggningar och mottagare. Sankey-diagram + karta som visar flöden. Avslöjande och unikt.

| 🎯 Leadmagnet | 🗺️ Visuell punch | 🧩 Byggtid | 🦄 Unikhet | 🔥 Delbarhet |
|:---:|:---:|:---:|:---:|:---:|
| ⭐⭐⭐ | ⭐⭐⭐⭐⭐ | ⭐⭐ | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐ |

**Datakällor:** E-PRTR (F3_2 Transfers_Facilities, F4_2 WasteTransfers_Facilities), Nominatim, OSM

| Del | Uppgift | Pers. | Fristående? |
|-----|---------|:-----:|:-----------:|
| **A. Avfallslista** | Filtrera F3_2/F4_2 på Sverige, visa avsändare + mottagare + typ + mängd | 1–2 | ✅ Fungerande datatabell |
| **B. Sankey-diagram** | Visuellt flödesdiagram: bransch → avfallstyp → mottagartyp (D3.js) | 1 | Visuell wow — killer feature |
| **C. Kartvy med linjer** | Rita linjer på Leaflet mellan avsändare och mottagare | 1 | Geografisk insikt |
| **D. Gate + branschrapport** | E-post → "Avfallsflöden i [bransch/län]", LinkedIn-knapp | 1 | Lead-funktionen |

**MVP: A + B + D.** Tekniskt utmanande men visuellt spektakulärt. **Bäst portfolio-projekt.**

---

## Idé 10: 📈 Gröna Företagskortet — "Ditt företags hållbarhetsprofil på 30 sekunder"

> Sök ett företagsnamn och få ett visuellt "kort" som sammanfattar dess utsläpp, branschjämförelse och trend. Tänk baseball card men för hållbarhet.

| 🎯 Leadmagnet | 🗺️ Visuell punch | 🧩 Byggtid | 🦄 Unikhet | 🔥 Delbarhet |
|:---:|:---:|:---:|:---:|:---:|
| ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ |

**Datakällor:** E-PRTR (F1_4, F2_4 — sök på FacilityName), SCB MCP (branschdata), OECD MCP (internationell kontext)

| Del | Uppgift | Pers. | Fristående? |
|-----|---------|:-----:|:-----------:|
| **A. Sök + kort** | Sökfält, matcha mot E-PRTR FacilityName, visa kort med nyckeltal | 1–2 | ✅ Fungerande app |
| **B. Branschjämförelse** | Placera företaget i sin bransch: "Ni ligger på plats 23 av 187" | 1 | Benchmarking-hook |
| **C. Trendgraf** | Utsläppstrend 2007–2024 med sparkline på kortet | 1 | Visuell djup |
| **D. Gate + fullständig profil** | E-post → full profil med alla ämnen + branschtrender + delbar bild | 1 | Lead-funktionen |

**MVP: A + B + D.** Extremt stark lead-magnet — företag söker sig själva. **Bäst för B2B-leads.**

---

## Snabbguide: Vilken idé passar er grupp?

| Om ni vill... | Välj |
|---------------|------|
| Bygga snabbt och säkert hinna | **#6 Utsläppsrankingen** eller **#8 Klimattidsmaskinen** |
| Imponera med kartor | **#1 Grön Grannsämja** eller **#7 Vattenriskkollen** |
| Maximera delbarhet | **#8 Klimattidsmaskinen** eller **#10 Gröna Företagskortet** |
| Visa teknisk ambition | **#9 Avfallskartan** eller **#5 Logistikpulsen** |
| Generera flest leads | **#10 Gröna Företagskortet** eller **#4 Solpotential-kalkylatorn** |
| Vara unika | **#7 Vattenriskkollen** eller **#9 Avfallskartan** |
