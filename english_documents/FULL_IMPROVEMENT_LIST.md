# Full Improvement List — Cross-Referenced Analysis

Fresh pass across open-data-guide, DATA_RECOMMENDATIONS, and hackathon-app-ideas.

---

## 🔴 Critical Issues (will cause teams to lose hours)

### 1. MCP Servers Are NOT REST APIs — Major Gotcha

**The problem:** The data guide lists SCB and OECD as "MCP Servers" and app ideas list them as data sources across 6 out of 10 ideas. But MCP is a protocol for AI agents (Claude, Copilot, etc.) — you cannot call `https://scb-mcp.onrender.com/mcp` with `fetch()` from a browser or Node script. It will fail. Teams that try will waste 1–2 hours confused.

**Which ideas are affected:** #2 (Industry Duel), #4 (Solar Calculator), #5 (Logistics Pulse), #6 (Emissions Ranking), #8 (Climate Time Machine), #10 (Green Company Card)

**Fix options:**
- **Option A (recommended):** Add a prominent warning in the guide: *"MCP servers require an MCP client (like Claude) to use. They are not REST APIs. Use the SCB REST API instead."*
- **Option B:** Add the SCB REST API as an alternative: `https://api.scb.se/OV0104/v1/doris/en/ssd/` — it's free, no key, returns JSON, and covers the same data
- **Option C:** Include a simple Claude API proxy example so teams can build an AI-powered backend that queries SCB MCP and returns JSON to their frontend

**In the app ideas, SCB/OECD MCP is used as if it's a normal API call in every idea. Either replace with the REST API alternative or add a clear note per idea.**

---

### 2. SMHI VattenWeb is a Download Portal, Not an API

**The problem:** Idea #7 (Water Risk Checker) lists "SMHI VattenWeb" as a data source. But VattenWeb is a web portal for manual download — there's no programmatic API. Teams cannot fetch it in code without scraping or manually downloading files.

**Affected idea:** #7 (Water Risk Checker) — segment A and B depend on this

**Fix:** Either:
- Remove VattenWeb from Idea #7 and replace with a different water data source (e.g. Naturvårdsverket water protection areas via REST API, which IS available)
- Add a warning: *"VattenWeb requires manual download — do this before the hackathon starts"*
- Revise Idea #7 to work with just E-PRTR F2_4 water releases + NVR protected water areas (both are API/file accessible)

---

### 3. Transportstyrelsen is Downloads, Not an API

**The problem:** Idea #5 (Logistics Pulse) lists "Transportstyrelsen" as a key data source, and segment C ("Data coupling") depends on it. Like VattenWeb, Transportstyrelsen stats are Excel/CSV file downloads from web pages — not APIs.

**Affected idea:** #5 (Logistics Pulse) — particularly segment C

**Fix:** Add a note that this data must be downloaded and pre-loaded before the hackathon, or scope Idea #5 to not depend on Transportstyrelsen for the MVP.

---

### 4. SMHI MetObs Navigation Is Non-Obvious

**The problem:** Unlike a simple REST API, SMHI MetObs requires a multi-step discovery process: list parameters → find station → select period → fetch data. Teams who just try to call the base URL and parse it will be stuck.

**Example of what confuses teams:**
```
# Step 1: List parameters
https://opendata-download-metobs.smhi.se/api/version/latest.json

# Step 2: Pick parameter 1 (temperature), list stations
https://opendata-download-metobs.smhi.se/api/version/latest/parameter/1.json

# Step 3: Find station ID for nearest city, e.g. Stockholm = 98210
# Step 4: Get corrected-archive data
https://opendata-download-metobs.smhi.se/api/version/latest/parameter/1/station/98210/period/corrected-archive/data.json
```

The guide documents the concept ("API → version → parameter → station → period → data") but a team that has never used this API needs to see the full chain.

**Fix:** Add a full worked example for the Climate Time Machine use case (most common) showing all four steps.

---

### 5. CORS May Block Browser API Calls

**The problem:** Not documented anywhere. Some APIs (Nominatim, SMHI Strång, Mesan) may return CORS errors when called directly from browser JavaScript. Teams using pure frontend (HTML + JS, no backend) will hit a wall with certain endpoints.

**Known issues:**
- **Nominatim:** Works from browser if you set a User-Agent header (not possible in basic fetch without backend)
- **SMHI endpoints:** Generally CORS-friendly but Mesan/Strång should be tested
- **Naturvårdsverket:** Has been known to block browser requests occasionally

**Fix:** Add a "Browser-friendly?" column to the API reference table, or a warning note: *"If you hit CORS errors, you need a simple backend proxy or a serverless function — see [example]."*

---

## 🟡 Data & File Issues

### 6. open-data-guide.md Lists Removed Files

The local files section still documents `DVO/` + `DVO.zip`, `NM/`, `NP/`, `NR/`, `NVO/` — which are being removed/archived. The file list will be wrong when participants see it.

**Fix:** After cleanup is complete, update section 4 to only list what's actually there:
```
| halland_skyddade_omraden.geojson | GeoJSON | Protected areas in Halland — use directly in Leaflet |
| F1_4_Sweden.json (pre-filtered) | JSON | Swedish air emission facilities — ready to use |
| F2_4_Sweden.json (pre-filtered) | JSON | Swedish water emission facilities — ready to use |
```

---

### 7. No Pre-filtered Sweden JSON Files Exist Yet

DATA_RECOMMENDATIONS says to create `F1_4_Sweden.json` and `F2_4_Sweden.json` — this hasn't been done. Without them, teams using E-PRTR (which is 8 out of 10 ideas) will hit the 70 MB file problem on Day 1.

**Fix:** Run the filtering script before the hackathon. This is the single highest-ROI preparation task.

```python
import pandas as pd, json

for filename, outname in [
    ('F1_4_Air_Releases_Facilities.csv', 'F1_4_Sweden.json'),
    ('F2_4_Water_Releases_Facilities.csv', 'F2_4_Sweden.json'),
]:
    df = pd.read_csv(f'files/eea_t_ied-eprtr_p_2007-2024_v16_r00/{filename}', 
                     encoding='utf-8-sig')  # handles BOM in EEA files
    sweden = df[df['countryName'] == 'Sweden']
    sweden.to_json(f'files/hackathon_data/{outname}', orient='records', force_ascii=False)
    print(f'{outname}: {len(sweden)} rows, {sweden.to_json(orient="records").__len__() / 1e6:.1f} MB')
```

Note: EEA CSV files often have a BOM (byte order mark) — use `encoding='utf-8-sig'` to avoid parse errors.

---

### 8. No Sample API Responses Anywhere

Teams learn data formats by seeing them, not by reading descriptions. The open data guide describes data types but shows no example responses.

**Fix:** Add a collapsed JSON snippet per API showing ~3 fields so teams know what they're getting. Especially for:
- SMHI MetObs temperature (what does a station object look like?)
- Naturvårdsverket NVR (what's in a protected area feature?)
- E-PRTR CSV (which column is the pollutant, which is the amount?)

Even 5 lines per API would save teams 30 min of exploration.

---

## 🟡 App Ideas Issues

### 9. Idea 8: SCB MCP Listed as a Data Source But Unused

Idea #8 (Climate Time Machine) lists "SCB MCP (population per location)" as a data source, but none of the four segments (A–D) actually uses it. It's hanging there confusing teams.

**Fix option A:** Remove SCB from the data sources list for Idea #8.

**Fix option B (better):** Add it to segment C or D explicitly:
> *Segment C enhancement: After showing temperature change, add "X people live in [location]" from SCB to frame the impact — makes the emotional punch stronger.*

---

### 10. Idea 9: D3.js Sankey Diagram Is a Hard Dependency

Segment B ("Visual wow — killer feature") is a Sankey diagram built with D3.js. D3 is powerful but has a steep learning curve. In 2026, there are much faster alternatives:

- **Plotly.js** — Has a built-in Sankey trace, much simpler API, free
- **Observable Plot** — Modern D3 wrapper, significantly faster to build with
- **Highcharts Sankey** — Commercial but free for non-profits/hackathons

**Fix:** Replace "D3.js" with "Plotly.js (easier) or D3.js (more control)" in Segment B's task description.

---

### 11. Idea 10: FacilityName Matching Is Unreliable

The Green Company Card searches by `FacilityName` in E-PRTR, but these are industrial plant names ("Stenungsunds Refinery"), not company names ("INOVYN Sverige AB"). Users searching for "Volvo" or "SSAB" are unlikely to get clean hits.

**This is a real usability problem for the lead magnet** — if the search doesn't return results for well-known companies, users give up.

**Fix:** Add a note in the idea description:
> *E-PRTR FacilityName contains plant names, not brand names. Search for plant name fragments ("unda", "refinery") or county + industry type. Consider adding a pre-built dropdown of Sweden's top 50 emitting facilities as a fallback.*

---

### 12. Idea 3: Weakest Lead Magnet — Target User Unclear

Idea #3 (Halland Nature Map) is the most beautiful and technically easiest, but has the weakest lead magnet (⭐⭐⭐). The description says "Perfect for municipalities and property companies" but doesn't explain why they'd give an email.

**What would municipality officials actually want?**
- A PDF report of protected areas overlapping their planned development zone
- A downloadable map for a planning meeting

**Fix:** Rewrite Segment D to be more specific:
> *"Enter your email to download a printable 'area overview' report for Halland (municipality + protected status + coordinates) — useful for planning meetings."*

This is a clearer, stronger lead magnet for the stated target user.

---

### 13. Ideas 2 and 10: OECD Data Not Described Concretely

Ideas #2 and #10 reference "OECD MCP (international context)" but don't specify what data to use or how. "International context" is vague — what OECD table specifically? Industrial emissions by country? Energy mix?

**Fix:** Be specific:
- **Idea #2 (Industry Duel):** "OECD ENV_NET_EMISSIONS — country-level industrial emissions for benchmarking Sweden against EU average"
- **Idea #10 (Green Company Card):** "OECD STAN industrial database — sector output and emissions intensity for international comparison"

Or, given the MCP issue (#1 above), replace OECD MCP with a concrete REST alternative.

---

### 14. No Idea Properly Uses Current/Forecast Weather

SMHI offers four weather-related APIs (MetObs, SNOW1g, Mesan, Strång) but the ideas only use MetObs (historical) and Strång (solar, for Idea #4). SNOW1g (current forecast) and Mesan (interpolated grid) are never used.

**This is a missed opportunity.** Current weather adds real-time relevance.

**Possible enhancement for existing ideas:**
- **Idea #1 (Green Neighborhood):** Add current AQI/wind direction to show "pollution dispersion risk today"
- **Idea #3 (Halland Nature Map):** Current weather at each nature reserve makes it feel live
- **Idea #7 (Water Risk):** Current rainfall from Mesan shows live flood/contamination risk

Not a blocking issue, but worth noting as an untapped angle.

---

## 🟢 Polish & Clarity Improvements

### 15. Quick Reference Table Doesn't Show What Each API Returns

The "Quick Reference — All API Endpoints" section is just a list of base URLs. Teams need to know what they're looking at before diving in.

**Fix:** Add a one-liner per API:
```
# Naturvårdsverket — returns protected area polygons (GeoJSON)
# SMHI MetObs — historical weather observations per station
# SMHI SNOW1g — hourly point forecasts for any coordinate
# SMHI Mesan — gridded model output for Sweden
# SMHI Strång — historical solar radiation per coordinate
# Nominatim — geocoding (address ↔ coordinates)
# OSM Tiles — background map images for Leaflet
```

---

### 16. Leaflet.js Section Needs Mapbox/Maptiler Alternative Mention

OSM tiles work fine but look basic. In a hackathon judged 25% on "Wow Factor," a better base map can make a significant visual difference.

**Alternatives with free tiers:**
- **Stadia Maps** — Beautiful tile styles (Alidade Smooth, Outdoors), free tier 200k tiles/month
- **Maptiler** — Free tier, professionally designed maps
- **CartoDB** (Carto) — Clean minimal styles, free for non-commercial

**Fix:** Add a "Better-looking tiles (optional)" section to the map library section.

---

### 17. MCP Section Needs Clearer "Who Is This For?" Note

The MCP section appears alongside REST APIs, making them look equivalent. Teams unfamiliar with Claude's MCP ecosystem will assume they can call these URLs like any other API.

**Fix:** Add a clear header or callout:
```markdown
> **Note:** MCP servers require an MCP client (Claude Code, Claude Desktop, etc.) to use.
> They cannot be called directly with fetch() from a browser or Node.js without an MCP client library.
> If you're building a standard web app, use the SCB REST API instead:
> https://api.scb.se/OV0104/v1/doris/en/ssd/
```

---

### 18. Nominatim Rate Limit Is a Demo Killer

1 request/second is fine for data fetching, but for a live address-search feature (as in Ideas #1, #4), users typing in a search box will trigger many requests quickly. Without debouncing, teams will hit 429 rate-limit errors during their demo.

**Fix:** Add to the Nominatim entry:
> *Hackathon tip: Add a 1-second debounce to your search input to avoid rate limiting. Do not fire a request on every keystroke.*

```javascript
// Debounce example (copy-paste ready)
let timeout;
searchInput.addEventListener('input', (e) => {
  clearTimeout(timeout);
  timeout = setTimeout(() => fetchAddress(e.target.value), 1000);
});
```

---

## Master Action List

| # | Change | Where | Effort | Priority |
|---|--------|--------|--------|----------|
| 1 | MCP servers ≠ REST APIs — add warning + SCB REST alternative | Open data guide + all 6 affected ideas | Medium | 🔴 Critical |
| 2 | VattenWeb is download-only — clarify or replace in Idea #7 | App ideas | Low | 🔴 Critical |
| 3 | Transportstyrelsen is download-only — flag in Idea #5 | App ideas | Low | 🔴 Critical |
| 4 | SMHI MetObs — add full 4-step worked example | Open data guide | Low | 🔴 Critical |
| 5 | CORS warning + "works from browser?" column | Open data guide | Low | 🔴 Critical |
| 6 | Update local files section (remove archived shapefiles) | Open data guide | Low | 🔴 Critical |
| 7 | Pre-filter E-PRTR to Sweden (create JSON files) | Repo files | Medium | 🔴 Critical |
| 8 | Add sample JSON responses per API | Open data guide | Medium | 🟡 High |
| 9 | Idea #8: Remove or use SCB MCP properly | App ideas | Low | 🟡 High |
| 10 | Idea #9: Suggest Plotly.js instead of D3 for Sankey | App ideas | Low | 🟡 High |
| 11 | Idea #10: Warn about FacilityName matching + add fallback suggestion | App ideas | Low | 🟡 High |
| 12 | Idea #3: Strengthen lead magnet — be specific about PDF export value | App ideas | Low | 🟡 High |
| 13 | Ideas #2 and #10: Specify actual OECD table or replace with REST alternative | App ideas | Low | 🟡 High |
| 14 | Note about unused current/forecast weather APIs | App ideas | Low | 🟢 Optional |
| 15 | Add one-liner descriptions to Quick Reference section | Open data guide | Low | 🟢 Optional |
| 16 | Add better tile alternatives for Wow Factor | Open data guide | Low | 🟢 Optional |
| 17 | MCP section — add "Who is this for?" callout box | Open data guide | Low | 🟢 Optional |
| 18 | Nominatim — add debounce tip and code snippet | Open data guide | Low | 🟡 High |

---

## Biggest Wins (If You Only Do 5 Things)

1. **Pre-filter E-PRTR to Sweden** (#7) — 20 min work, saves every team hours
2. **MCP warning + SCB REST alternative** (#1) — Half the ideas reference MCP incorrectly
3. **SMHI MetObs worked example** (#4) — Idea #8 (highest viral potential) depends on this
4. **Fix VattenWeb/Transportstyrelsen** (#2, #3) — Teams that pick #5 or #7 will be stuck without this
5. **Nominatim debounce tip** (#18) — Will kill demos if not handled
