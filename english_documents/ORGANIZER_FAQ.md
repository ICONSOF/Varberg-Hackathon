# ❓ Organizer FAQ — Hackathon Logistics & Questions

## Deployment & Technical Setup

### Q: Can everyone deploy for free?

**Vercel/Netlify (Frontend):** Yes, completely free tier.
- Next.js, React, Vue, static sites: Free tier is generous (100s of deployments/month)
- Suitable for ~80% of the ideas (mostly frontend + API calls)

**Python/Node Backend:** Mostly free tier, but with limitations.
- **Render.com**: Free tier for Python/Node, includes free PostgreSQL (sleeping after 15 min of inactivity)
- **Replit**: Free Python/Node hosting, instant spin-up, good for quick demos
- **Railway**: Free tier, then pay-as-you-go (~$5 for basic usage)
- **Fly.io**: Free tier for Docker containers

**Reality check:** By April 2026, free tier hosting is abundant. Any team can deploy.

---

### Q: Do we need to deploy, or can they demo locally?

**Short answer:** Local demo is totally normal and often preferred.

**Comparison:**

| Option | Pros | Cons | Best For |
|--------|------|------|----------|
| **Local demo** | Fast, no setup, always works | No live URL, can't test on phone | Most hackathons, time-pressured teams |
| **Deployed URL** | Wow factor, judges can try themselves, shareable | 30 min setup, possible deployment bugs | Teams with buffer time, or using Vercel |

**Recommendation:** 
- Default: Local demo during presentation
- Nice-to-have: If they finish features early, deploy to Vercel (5-min setup) for a live URL

**Your schedule works perfectly for this:** Day 2 morning (09:00–12:00) is plenty of time to deploy if they want.

---

### Q: What's the easiest deployment for a hackathon?

**Easiest path:**
1. **Vercel** for frontend → Takes 5 minutes, one-click from GitHub
2. **Local demo** if they're not comfortable deploying

**Easiest for Python:**
1. **Replit** → Paste code, run, get a shareable URL (takes 2 min)

**Bottom line:** Don't make deployment a requirement. Make it optional with "if you finish early" framing.

---

## AI & Tooling

### Q: Is using AI (Claude, ChatGPT, Copilot) normal in hackathons now?

**Yes, absolutely.** By April 2026, AI-assisted development is standard practice, not cheating.

**What smart teams will do:**
- Use Claude to understand SMHI API docs and write parsing code
- Use GitHub Copilot to auto-complete boilerplate
- Use ChatGPT to debug errors faster
- Use Claude to explain why their data mashup makes sense

**Your call:**
- **Option A:** Actively encourage it in the brief: *"Use AI tools to move faster—smart teams do."*
- **Option B:** Stay neutral: Mention it's allowed but don't push it
- **Option C:** Don't mention it: Teams who want to use it will; others won't

**My take:** Option A. By 2026, not using AI is the disadvantage. Frame it as a tool, like Git or a code editor.

**Draft language for brief:**

```markdown
## Tools & AI

By 2026, AI tools are standard in professional development. You're encouraged to use:
- **Claude/ChatGPT**: Explain APIs, write boilerplate, debug errors
- **GitHub Copilot**: Autocomplete for faster coding
- **AI code review**: Spot bugs and optimize

Using AI effectively is a *skill*, not cheating. Smart teams will leverage it to move faster.
```

---

## Presentation Format

### Q: Should presentations be 5–10 minutes instead of 5 minutes?

**Yes, definitely.** 5 minutes is too tight.

**Current schedule:** 20 min per group (10 min presentation + setup + Q&A)
- With 5 min talks: 3–5 min Q&A (rushed)
- With 7–10 min talks: 5–7 min Q&A (breathing room)

**Recommendation:** Frame it as "5–10 minutes + 5–7 min Q&A" so teams have flexibility.

**Your judges will benefit from:**
- 3+ min live demo (see the product, not just hear about it)
- Chance to ask follow-ups without feeling rushed

**Updated wording for brief:**

```markdown
## Presentations: 5–10 Minutes + Q&A

**Format:**
- 5–10 min: Present your app (demo, approach, insights)
- 5–7 min: Judges ask questions
- Total: ~20 min per slot (including computer setup)

**Suggested structure (for 7-min talks):**
1. **1 min:** Problem/opportunity
2. **4 min:** Live demo or walkthrough
3. **2 min:** How you combined data + one key insight
```

---

## Guidance & Handholding

### Q: How much handholding do teams really need? Data samples, preprocessing scripts, etc.?

**Honest take:** Less than you'd think.

**What they'll actually use:**
- ✅ **API examples** ("Here's a curl command to test SMHI MetObs")
- ✅ **Links to docs** (Official API docs, Leaflet tutorial)
- ✅ **Idea difficulty selector** (Help them pick the right scope)
- ✅ **Timeline** (Day 1 = MVP, Day 2 = polish)
- ✅ **Judge expectations** (What do judges actually care about?)

**What they won't use or don't need:**
- ❌ Preprocessing scripts (Good teams write their own, weak teams copy-paste and hit weird errors)
- ❌ Learning resources (They'll Google/ask Claude; they don't read 10-page guides)
- ❌ Detailed rubrics (Judges have their own rubrics)

**Recommendation:** 
- **Light touch:** API examples + links + timeline + scope guidance
- **Avoid:** Full scripts, step-by-step tutorials, pre-processed CSV files

By 2026, any hacker worth their salt will use Claude to understand docs faster than reading your guide anyway.

---

## Scheduling Questions

### Q: Does the schedule work for presentations + judging?

**Your schedule (from your email):**
- 13:00–15:00: Presentations (6 groups × 20 min = 2 hours) ✅
- 15:00–15:30: Fika break ✅
- 15:30–16:30: Presentations (2 groups × 20 min = 40 min, leaves 20 min buffer) ✅
- 16:30–17:00: Jury deliberation ✅
- 17:00–18:00: Awards + mingel ✅

**Yes, this works perfectly.**

**Pro tips:**
- Start presentations exactly on time (judges will have decided on earlier groups by then)
- Have a backup "what-if-demo-fails" video ready (30 sec per team)
- Judges can deliberate while mingel starts; results at 17:15 instead of 17:00

---

## Prize & Judge Strategy

### Q: How do we decide on prizes?

**By end of week is smart.** Here's a framework:

**Option A: Weighted scoring (what I'd recommend)**
```
🏆 1st Place: 1000 SEK + featured on Iconsoft website
🥈 2nd Place: 500 SEK
🥉 3rd Place: 250 SEK
```
Judges score on your 4 criteria (Lead Power 30%, Data Mashup 25%, Wow 25%, Polish 20%).
Highest total wins.

**Option B: Category awards (fun, many winners)**
```
🎯 Best Lead Magnet (Birger's choice)
🗺️ Best Data Mashup (Lucas's choice)
✨ Most Shareable (Hans's choice)
🔧 Most Polish (Judge consensus)
```
Each winner gets ~500 SEK. Multiple teams feel recognized.

**Option C: Single prize, runner-up mentions**
```
🏆 1st Place: 1000 SEK + featured online
Runners-up get special mention at awards
```

**My take:** **Option B is best for hackathons.** Why?
- Gives multiple teams recognition (better morale)
- Judges score in their area (Birger = sustainability insight, Lucas = tech, Hans = B2B viability)
- Aligns with your 4 judging criteria organically
- More memorable for winners ("Lucas's pick for best data mashup" vs "tied for 3rd place")

**Timeline:** Decide prize structure by Friday (end of week), announce at Day 1 opening (April 28).

---

## Communicating Judge Backgrounds

### Q: Should we introduce judges/their backgrounds?

**Yes, 100%.** Teams will tailor their pitches if they know:
- Birger looks for sustainability insight → Show they researched the *why*
- Hans looks for B2B viability → Show they thought about users
- Lucas looks for technical clarity → Show how they combined APIs

**Suggested intro (30 sec before presentations):**

```markdown
## Your Judges

- **Birger Löfgren** (Sustainability expert, PhD): "I'm looking for apps that use data to reveal something meaningful about environmental impact."

- **Hans Andrée** (B2B operations): "I want to see if this could work as a real product. Would I invest time in this?"

- **Lucas Hadin** (AI & Data Engineer): "Show me how you combined your data sources. What surprised you in the process?"

Each judge will score on all 4 criteria, but they'll bring their unique lens.
```

This takes 1 min and teams will immediately understand what to emphasize.

---

## Quick Checklist: Pre-Hackathon

- [ ] Decide on prize structure (end of week)
- [ ] Introduce judge backgrounds to brief
- [ ] Change presentation time to "5–10 min + Q&A"
- [ ] Add "AI tools are encouraged" to brief
- [ ] Emphasize "local demo is fine; deployment is optional"
- [ ] Add idea difficulty selector (prevent scope disasters)
- [ ] Test SMHI/E-PRTR APIs yourselves (so you can demo them)
- [ ] Have backup demo videos if live demo fails
- [ ] Brief judges on expected demo failures (that's normal for hackathons)

---

## What to Explicitly NOT Do

- ❌ Don't require deployment (local demos are faster)
- ❌ Don't provide preprocessed data files (teams learn more by filtering themselves)
- ❌ Don't write complex guides (teams will ask Claude instead)
- ❌ Don't dock points for using AI (it's 2026, it's normal)
- ❌ Don't be too strict on scope (some ideas are harder than they look; give grace)

---

## TL;DR — Main Decisions Needed

| Decision | Recommendation | Deadline |
|----------|-----------------|----------|
| Prizes | Option B (category awards) | End of week |
| AI tools | Encourage explicitly | Before brief release |
| Deployment | Optional; local demo is fine | Include in brief |
| Presentations | 5–10 min + Q&A | Announce Day 1 |
| Judge bios | Include in brief | Before brief release |
| Difficulty selector | Add to idea selection | Before brief release |

Once these are locked, the brief is ready to rock.
