# 💡 App Ideas — Hackathon Sustainability Data

Use them as inspiration for your own.

---
Tip: Provide an LLM with your data sources (or a .md file listing them) and iterate toward an idea that matches your ambition.
---

## Idea 1: 🗺️ Green Neighborhood Watch — "How close do you live to industry?"

> Enter an address and see which industrial facilities are nearby, what they emit, and what protected nature is in the area.

**Why it's interesting:** Most people have no idea what's being released in their neighborhood — this makes it personal and local.

**Data Sources:** E-PRTR (F1_4), Naturvårdsverket protected areas, Nominatim, OSM

---


## Idea 2: 📊 Industry Duel — "How clean is your industry?"

> Select two industries and see them compared: emission trends, number of facilities, geographic spread. Interactive graphs.

**Why it's interesting:** Every professional wonders how their industry stacks up — and the answer is rarely flattering.

**Data Sources:** E-PRTR (F1_2, F1_4), SCB REST API or SCB MCP, OECD MCP

---

## Idea 3: 🌿 Halland Nature Map — "Discover what's protected"

> Interactive map of Halland's protected nature with weather layers and solar radiation. Perfect for municipalities and property companies.

**Why it's interesting:** Protected areas and development pressures are invisible to most people — putting them on a map makes the tension visible.

**Data Sources:** halland_skyddade_omraden.geojson, NVR v3, SMHI MetObs, SMHI Strång, OSM

---

## Idea 4: 🚛 Logistics Pulse Halland — "The E6 corridor's climate footprint"

> Visualize transport flows along E6/E20, Halmstad harbor, and the West Coast Railway. Simulate: "What if we moved goods from road to rail?"

**Why it's interesting:** The road vs. rail debate is everywhere — this lets you run the numbers yourself and see the CO₂ impact in real time.

**Data Sources:** Transportstyrelsen (download required), E-PRTR, SCB REST API, OSM

> **Note:** Transportstyrelsen data is file-based (Excel/CSV download), not an API. Pre-process the relevant files before the hackathon starts.

---

## Idea 5: 🏭 Emissions Ranking — "Top 10 in your region"

> Ranking of the largest emitters per region. Filter by substance, see trends. Think "Spotify Wrapped" but for industrial emissions.

**Why it's interesting:** People are shocked by who their biggest local polluters actually are — name recognition makes this instantly shareable.

**Data Sources:** E-PRTR (F1_4), SCB REST API, Nominatim

---

## Idea 6: 💧 Water Risk Checker — "How exposed is your municipality?"

> Combine water emissions from industry (E-PRTR) with protected water environments. Show risk visually on a map — which water bodies are most stressed?

**Why it's interesting:** Industrial water pollution is largely invisible — showing it alongside protected drinking water areas creates an immediate "aha" moment.


**Data Sources:** E-PRTR (F2_4), NVR water protection areas (REST API), Nominatim, OSM

---

## Idea 7: 🌡️ Climate Time Machine — "How weather has changed where you live"

> Enter a location and see how temperature has changed over the last 50–100 years, based on SMHI's actual measurement data. Personal, visual, and slightly unsettling.

**Why it's interesting:** Seeing climate change through the lens of your own lifetime makes it feel real, not abstract — and the "your birth year" hook is impossible not to share.

**Data Sources:** SMHI MetObs (historical temperature, parameter 1), SCB REST API, Nominatim

---

## Idea 8: 🏗️ Waste Map — "Where does the waste go?"

> Visualize how industrial waste is transported between facilities and receivers. Sankey diagram + map showing flows. Revealing and unique.

**Why it's interesting:** Industrial waste disappears from public view the moment it leaves a facility — tracing where it actually ends up is genuinely surprising.

**Data Sources:** E-PRTR (F3_2, F4_2), Naturvardsverket protected areas or SCB regional industry data, Nominatim, OSM

---

## Idea 9: 📈 Green Company Card — "Your company's sustainability profile in 30 seconds"

> Search a company name and get a visual "card" summarizing its emissions, industry comparison, and trend. Think baseball card but for sustainability.

**Why it's interesting:** Companies Google themselves constantly — giving them a sustainability scorecard they can share (or quietly act on) is a lead magnet that sells itself.


**Data Sources:** E-PRTR (F1_4, F2_4), SCB REST API, OECD MCP

> **Note:** E-PRTR uses industrial plant names (e.g. "Stenungsunds Refinery"), not brand names. Consider a pre-built dropdown of Sweden's top emitters as a fallback.

---

