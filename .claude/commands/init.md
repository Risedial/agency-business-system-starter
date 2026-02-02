# System Initialization Command

You are bootstrapping the Agency Business System workspace. This command executes Phase 1-2 automatically.

---

## What This Command Does

This initialization will create:
- Research and methodology documentation in `/docs`
- Reference materials in `.claude/rules/reference`
- Phase instruction files in `.claude/rules`
- Initial STATE.json in `/system`

**Estimated time:** 10-15 minutes

---

## PHASE 1: RESEARCH & DOCUMENTATION

### Task 1.1: Create Research Findings Document

Create `/docs/research-findings.md` with findings about:
- Beyond The Agency Box methodology (Frankie Fihn)
- Hand raiser lead generation best practices
- Async video sales systems
- 2026 social media dynamics
- No-meeting fulfillment models

Include sources, statistics, and key frameworks identified.

### Task 1.2: Create Unified Methodology Document

Create `/docs/methodology-master.md` covering:
- Complete lead-to-close pipeline (hand raiser → engagement → video → follow-up → payment → onboarding)
- Offer construction framework (outcome-focused promise formula, pricing psychology)
- Hand raiser system details (post templates, platform selection, validation signals)
- Video sales system (5-part structure, custom vs standardized phases)
- Fulfillment model (async communication protocols, update cadences)
- Scaling framework (hiring triggers, role SOPs, QC processes)

### Task 1.3: Create Core Patterns Document

Create `/docs/core-patterns.md` documenting:
- Hand raiser post psychology (why self-selection works, engagement triggers)
- Video script formulas (hook variations, outcome demonstration techniques)
- "Easy Yes" offer construction criteria
- Text-based closing sequences (timing, question handling)
- "Tried This Before" objection handling frameworks

---

## PHASE 2: WORKSPACE FOUNDATION

### Task 2.1: Create Framework Documents

Generate these 6 framework files in `/docs`:

**1. `/docs/offer-framework.md`** - Complete offer construction guide:
- Niche selection criteria (pain urgency, budget capacity, accessibility)
- 1-3 sentence offer summary formula with examples
- Promise-focused framing (outcomes NOT services)
- Pricing psychology ($1K-$10K/mo positioning)
- Contextualized price presentation scripts
- Guarantee structures (performance, time-based, satisfaction)
- Offer validation signals

**2. `/docs/hand-raiser-system.md`** - Lead generation playbook:
- Platform selection (LinkedIn vs Facebook by niche)
- 2026 organic reach reality (when to add paid amplification)
- 100-connection building strategy
- Hand raiser post templates (10+ variations)
- Post timing and frequency
- Response handling protocols
- Market validation interpretation
- Social listening for intent signals

**3. `/docs/video-sales-system.md`** - 5-minute video methodology:
- Complete 5-part structure breakdown with examples
- Hook formulas by niche
- Outcome demonstration techniques
- Price contextualization formulas
- "Tried this before" objection handling
- Explicit purchase instruction scripts
- Custom vs standardized video phases
- Message wrapper templates
- 2026 video best practices

**4. `/docs/text-closing-system.md`** - Post-video follow-up:
- Follow-up sequence timing (24h, 48h, 72h, 1-week)
- Message templates for each stage
- Question handling (situational fit, logistics)
- Objection response scripts
- Payment reminder sequences
- "Going dark" re-engagement
- Final attempt thresholds

**5. `/docs/fulfillment-system.md`** - No-meeting delivery:
- Client onboarding document template
- Expectation setting framework ("no-meeting" positioning)
- Weekly update Loom structure (3-5 minutes)
- Deliverable handoff process
- Issue resolution via async
- Client communication protocols
- Proactive update cadences
- QC checklists before handoff

**6. `/docs/scaling-system.md`** - Growth infrastructure:
- Hiring triggers (5 clients = consider, 10 = mandatory)
- Role-specific SOPs (media buyer, account manager, fulfillment)
- Job post templates by role
- Test assignment templates
- Evaluation rubrics
- Training protocols
- Video/asset library structure
- QC processes for delegated work

### Task 2.2: Initialize System Tracking

Create `/system/STATE.json` with initial state:

```json
{
  "lastUpdated": "",
  "currentPhase": "Phase 3",
  "niche": "",
  "offerPromise": "",
  "pricePoint": "",
  "metrics": {
    "connectionsBuilt": 0,
    "postsPublished": 0,
    "videosSent": 0,
    "clientsAcquired": 0,
    "offerValidated": false
  },
  "assetsCreated": [],
  "currentBlockers": []
}
```

---

## AFTER COMPLETION

1. **Update CLAUDE.md:**
   - Set Phase to "Phase 3"
   - Add created files to "Assets Created" list

2. **Tell the user:**

```
✅ System initialized successfully!

Created:
- 9 methodology documents in /docs
- 4 reference files in .claude/rules/reference
- STATE.json tracking in /system

Next steps:
1. Open CLAUDE.md
2. Configure your business:
   - Niche: [your target industry/role]
   - Offer Promise: [specific outcome in 1-3 sentences]
   - Price Point: [$/month for deliverable]
3. Save CLAUDE.md
4. Run: /next

Estimated time to complete setup: 1-2 hours total
```

---

## Quality Criteria

Before marking complete, verify:
- [ ] All 9 `/docs` files created with comprehensive content
- [ ] All 4 `.claude/rules/reference` files created
- [ ] STATE.json exists and is valid JSON
- [ ] CLAUDE.md updated with Phase 3
- [ ] All methodology content preserved from Master Prompt

---

## Error Handling

If any file creation fails:
1. Note the error
2. Continue with remaining files
3. Report all errors to user at end
4. Provide recovery instructions
