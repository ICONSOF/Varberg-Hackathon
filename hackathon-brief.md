# 🚀 Hackathon Brief — Sustainability Data as Business Value

## Your Mission

Build a web app that makes sustainability data **interesting, useful, and shareable**. The app should be so compelling that a business leader, environmental manager, or curious person voluntarily tests it — and wants more.

**Format:** 5–10 minute presentation + live demo, followed by Q&A. In total 20 min for each group. 

## Why?

Companies sit on enormous amounts of open data about their environmental impact, but few know about it or use it. Your app should make that data accessible, understandable, and valuable. You don't need to be sustainability experts — you need to make data **interesting to ordinary people**.

## Goals

| Goal | Description |
|-----|-------------|
| **Primary** | Generate leads — get users to want to share their work email in exchange for added value |
| **Secondary** | Drive traffic to Icons Of's LinkedIn page |

---

## Requirements (all must be met)

### 1. Free Value First
Users should be able to test the app and see something interesting **without** providing any information. Make them curious first.

### 2. Email Gate for Premium Features
A deeper function — report, export, comparison, personalized analysis — unlocks when users provide their **work email**. 

**Key:** Make the free value so good that users *want* the premium unlock. Examples:
- **"See your neighborhood's emissions for free. Enter your email for a detailed risk report + recommendations."**
- **"Compare two industries instantly. Enter your email to benchmark your company against peers."**
- **"See your solar potential on a map. Enter your email for a 30-year ROI forecast."**

The gate should feel like a natural upgrade path, not a dark pattern.

**Important:** For this hackathon, storing the email in browser `localStorage` is completely fine. You do **not** need to build a backend, webhook, database, or real CRM flow unless you want to.

### 3. LinkedIn Share Button (mandatory)
Every app **must** have a visible "Share on LinkedIn" button for the app URL. Also include:
- a short suggested post text users can copy

Don't spend hours trying to force custom text into LinkedIn's share dialog — that behavior is limited and can change.

### 4. Ambition to have at Least 2 Meaningful Data Sources
Have an ambition to combine at least two meaningful data sources. Geocoding (Nominatim) and map tiles (OSM) don't count — they're infrastructure. The goal is finding an insight that neither source could give you alone.

### 5. Working Demo
The app should be able to be demonstrated live during the presentation. It doesn't need to be production-ready but should work.

---

## Branding Guidance

These apps should be **lightly co-branded** by Icons Of, not heavily branded as if they were a finished company product.

- Use a small `Built with Icons Of` or `Built for the Icons Of hackathon` label in the UI.
- Add a link to https://www.iconsof.se or https://www.linkedin.com/company/iconsof
- Include Icons Of in the LinkedIn share text, preview metadata, and README.
- Keep the app name and visual identity centered on the problem or use case, not the company logo.
- Avoid large hero-branding unless it helps the demo; the idea should feel useful first, promotional second.

### Branding Assets

Logos, icons, and favicons are available in the `branding/` folder.

---

## Data Sources Available

All API endpoints, file paths, and example calls are in `open-data-guide.md`. Here's what's available:

### APIs (no key needed)
- **Naturvårdsverket NVR** — National parks, nature reserves, protected areas
- **SMHI MetObs** — Historical temperature, wind, precipitation (~700 stations, data from 1800s)
- **SMHI Strång** — Solar radiation per coordinate, historical
- **SMHI Forecast / Mesan** — Hourly forecasts and interpolated grid data
- **Nominatim** — Address → coordinates (and reverse)
- **OSM Tiles** — Background maps for Leaflet

### SCB & OECD
- **SCB** — official Swedish statistics via `PxWebApi v2`, including population, labour market, income, prices, transport, trade, energy, environment, and more.
- **OECD** — international datasets and indicators via OECD Data Explorer and SDMX API, including employment, trade, emissions, climate policy, health, and macroeconomics.
- Both are useful when you want benchmark or context data around a company, municipality, industry, or country, not just raw environmental measurements.
- See `open-data-guide.md` for example links, dataset pages, and API entry points.

### E-PRTR — Industrial Emissions Data
33,000+ EU industrial facilities with coordinates, emissions by substance, and data from 2007–2024. **Your most valuable data source.** Pre-filtered Sweden files are ready to use in `files/hackathon_data/`.

### Other downloadable sources
Transportstyrelsen (vehicle/CO₂ stats), SMHI VattenWeb (hydrology), Naturvårdsverket geodata — all free, no registration.

---

## Meet Your Judges

Your judges bring diverse perspectives. Knowing their background helps you pitch effectively:

| Judge | Background | What They're Looking For |
|-------|-----------|--------------------------|
| **Birger Löfgren** | Sustainability PhD, 15+ years in private/public sector (SKF, Chalmers, RISE) | Does this reveal something meaningful about environmental impact? Is the data insight real and actionable? |
| **Hans Andrée** | 10+ years Microsoft partnerships + 10+ years operational leadership in industrial companies | Would a real company want to use this? Is this thinking about actual users and business value? |
| **Lucas Hadin** | Senior AI & Data Engineer, 14 years in analytics (gaming, EA) | Show how you combined your data sources. What was the unique insight that drove your design? |

---

## Judging Criteria

| Criterion | Weight | The jury asks themselves | What this means |
|-----------|--------|--------------------------|-----------------|
| 🎯 **Lead Power** | 30% | Would I give my work email for this? | The email gate unlocks genuine value. Users see benefit immediately (free tier) and want more (premium). |
| 🔀 **Data Mashup** | 25% | How creatively are data sources combined? | You didn't just combine random data—you found *why* these sources together reveal something new. |
| ✨ **Wow Factor** | 25% | Is this beautiful, interactive, and shareable? | Visual design, smooth interaction, and something someone would actually send to a colleague. |
| 🔧 **Polish** | 20% | How close to a real product did the team get? | Features work end-to-end. UI is intuitive. If given 2 more weeks, this could launch. |

**Scoring rubric anchors:**
- **5/5:** Exactly what the criterion describes
- **3/5:** Meets expectation but with rough edges
- **1/5:** Missing or poorly executed

---

## App Ideas

Not sure what to build? A separate document (`hackathon-app-ideas.md`) lists 10 ready-made ideas with ratings and data sources. Pick one, remix it, or ignore it entirely — it's just inspiration, not a requirement.

---

## Deliverables

### 1. Working App
- Demonstrable live (local or deployed)
- Has email gate that works
- Browser `localStorage` is completely acceptable for the email gate
- Has LinkedIn share button
- Doesn't need to be production-ready; it needs to work

### 2. Presentation (5–10 minutes + Q&A)

**Suggested structure for a 7-minute talk:**
1. **1 min:** What problem does your app solve? Why does it matter?
2. **3–4 min:** Live demo walk-through (show the happy path, hit the email gate, point out one "wow" moment)
3. **2 min:** How you combined your data sources. What was the unique insight? 

**Pro tips:**
- Have a backup screenshot or 30-second video demo on your phone in case live demo fails
- Be ready to answer: "Show how you combined your data sources. What was the unique insight?"
- The best presentations show, don't tell — let judges try the app themselves

### 3. Source Code
- Push to GitHub (private is fine, or public for portfolio)
- Include a README explaining: what the app does, which data sources you used, how to run it
- The code will be handed over to Icons Of for potential future use

---


## Tips

### 💡 Tip 1: Use AI Tools
The best builders today use Claude, ChatGPT, and Copilot as a core part of how they work. Load `open-data-guide.md` alongside this brief and ask: *"What API calls do I need to build [your idea]?"* Use it to explain data structures, write boilerplate, and debug faster.

### 💡 Tip 2: Start with the Data
Before writing a single line of code — paste an API URL into your browser and see what comes back. Understand the shape of the data first, build second.

### 💡 Tip 3: Use the Pre-filtered E-PRTR Files
The raw E-PRTR CSV files cover all of EU and are large. Pre-filtered Sweden-only JSON files are ready to use in `files/hackathon_data/` — start there.

### 💡 Tip 4: MVP First, Polish Later
Build the simplest version that works — a map with dots, a list with numbers. Make it beautiful *afterward*. You only have ~1.5 days.

### 💡 Tip 5: Divide the Work
Each idea splits into parallel tracks (map, data, email gate, design). Decide early who owns what — don't work serially.

### 💡 Tip 6: LinkedIn Button is Easy
```javascript
const shareUrl = `https://www.linkedin.com/sharing/share-offsite/?url=${encodeURIComponent(appUrl)}`;
```
Add it on Day 1 — it's a requirement and takes 5 minutes. Pair it with a visible "Copy suggested LinkedIn post" button or text box. To control how your app looks when shared, set Open Graph tags in your HTML:
```html
<meta property="og:title" content="Your compelling result headline" />
<meta property="og:description" content="What your app does — built by Icons Of" />
```

### 💡 Tip 7: Scrape if You Want
You're not limited to the provided sources. If you find useful sustainability data elsewhere — use it. Just make sure to have an ambition on at least 2 sources.

### 💡 Tip 8: Think Shareability
The app people *want* to show others wins. Ask: *"Would I send this to a colleague?"*

### 💡 Tip 9: Local Demo is Fine
Don't stress about deployment. Run it on your laptop during the presentation. If you finish early and want a live URL, Vercel (frontend) or Replit (Python/Node) both deploy for free in minutes.

---




## Red Flags to Avoid

🚩 **"I built a data dashboard"** — Data alone isn't a lead magnet. Users need to see personal value.

🚩 **"The email gate is hidden"** — Make it obvious and enticing. The gate *is* your core feature.

🚩 **"It only works on desktop"** — Test on phone. Many users preview on mobile.

🚩 **"We ran out of time for design"** — A working ugly app beats a beautiful broken one. Finish features, skip polish if you must.

🚩 **"Only our team tested it"** — Get a few people to try it during the hackathon. Judges want to see people actually wanted to use it.

---

**Good luck! 🎉**
