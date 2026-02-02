# System Validation Command

This command checks your workspace for completeness and identifies any issues.

---

## What This Command Does

Runs validation checks appropriate for your current phase:
- File existence verification
- Content completeness checks
- State synchronization verification
- Functional testing (where applicable)

---

## Validation Checks

### Phase 1-2 Validation (Foundation)

**Required Files:**
- [ ] CLAUDE.md exists in root
- [ ] SESSION-START.md exists in root
- [ ] `.claude/settings.json` exists
- [ ] `.claude/hooks/update-state.py` exists and is executable
- [ ] `/system/STATE.json` exists

**Required Documentation (9 files in `/docs`):**
- [ ] research-findings.md
- [ ] methodology-master.md
- [ ] core-patterns.md
- [ ] offer-framework.md
- [ ] hand-raiser-system.md
- [ ] video-sales-system.md
- [ ] text-closing-system.md
- [ ] fulfillment-system.md
- [ ] scaling-system.md

**Required Reference Files (4 files in `.claude/rules/reference`):**
- [ ] methodology.md
- [ ] hand-raiser.md
- [ ] video-sales.md
- [ ] fulfillment.md

**Content Checks:**
- [ ] Each `/docs` file contains > 100 lines (not just stubs)
- [ ] STATE.json is valid JSON (test: `cat system/STATE.json | python -m json.tool`)
- [ ] update-state.py is executable (test: `ls -l .claude/hooks/update-state.py`)

**Result:** If all pass → Ready for Phase 3
**If failures:** List missing files and recommend actions

---

### Phase 3 Validation (Prompt Generator)

**Required Files:**
- [ ] All Phase 1-2 files present (run above checks)
- [ ] `/system/prompt-generator.html` exists

**Functional Tests:**
- [ ] Open prompt-generator.html in browser → loads without errors
- [ ] Browser console (F12) shows no JavaScript errors
- [ ] STATE.json loads successfully (check for "State loaded" or similar confirmation)
- [ ] "Refresh State" button works
- [ ] Can select a prompt category
- [ ] "Generate Prompt" button produces output
- [ ] "Copy to Clipboard" button works

**Content Checks:**
- [ ] prompt-generator.html contains > 500 lines
- [ ] Contains React CDN link
- [ ] Contains state loading logic
- [ ] Contains all 7 prompt categories (Validation, Offer Development, Sales Assets, Lead Generation, Fulfillment, Scaling, Custom)

**Result:** If all pass → Ready for Phase 4
**If failures:** List specific issues and recommend re-generation or fixes

---

### Phase 4 Validation (Asset Templates)

**Required Files (8+ files in `/assets`):**
- [ ] hand-raiser-posts.md
- [ ] video-script-template.md
- [ ] video-message-wrappers.md
- [ ] follow-up-sequence.md
- [ ] objection-responses.md
- [ ] onboarding-template.md
- [ ] weekly-update-script.md
- [ ] deliverable-handoff.md

**Content Checks:**
- [ ] hand-raiser-posts.md contains 10+ template variations
- [ ] video-script-template.md has all 5 parts (Hook, Outcome Demo, Price, Differentiation, Purchase Instructions)
- [ ] follow-up-sequence.md has templates for 24h, 48h, 72h, 1-week cadence
- [ ] objection-responses.md covers "Tried before", "Too expensive", "Need to think", etc.
- [ ] All templates use fill-in-the-blank format [like this]

**Result:** If all pass → Ready for Phase 5
**If failures:** List missing or incomplete templates

---

### Phase 5 Validation (Daily Operations)

**Required Files (3 files in `/daily`):**
- [ ] DAILY-SOP.md
- [ ] QUICK-REFERENCE.md
- [ ] pipeline-tracker.md

**Content Checks:**
- [ ] DAILY-SOP.md contains all 4 time blocks (Morning, Mid-morning, Afternoon, End of day)
- [ ] DAILY-SOP.md has decision trees for common scenarios
- [ ] DAILY-SOP.md has metrics tracking table
- [ ] QUICK-REFERENCE.md is < 100 lines (quick reference, not comprehensive)
- [ ] pipeline-tracker.md has tables for: Active Prospects, Conversion Funnel, Weekly Summary, Client Tracker

**Result:** If all pass → Ready for Phase 6
**If failures:** List missing or incomplete operational documents

---

### Phase 6 Validation (Complete System)

**Full System Check:**

Run all previous validation checks (Phase 1-5).

**Additional Checks:**
- [ ] Can execute morning block using only system assets (no improvisation)
- [ ] Can execute mid-morning block using only system assets
- [ ] Can execute afternoon block using only system assets
- [ ] Can execute end-of-day block using only system assets

**State Synchronization Test:**
1. Update CLAUDE.md Current State (change any metric)
2. Run: `python .claude/hooks/update-state.py`
3. Check STATE.json reflects the change
4. Result: [ ] Pass / [ ] Fail

**Fresh Session Test:**
1. Close and reopen Claude Code in this directory
2. CLAUDE.md should auto-load (verify with /memory command)
3. Run: `/next`
4. System should provide correct guidance
5. Result: [ ] Pass / [ ] Fail

**Prompt Generator Integration Test:**
1. Open `/system/prompt-generator.html`
2. Click "Refresh State"
3. Verify current phase and metrics display correctly
4. Generate a test prompt from any category
5. Verify prompt includes current state context
6. Result: [ ] Pass / [ ] Fail

**Completeness Check:**
- [ ] Total file count: 30+ files created
- [ ] All methodology from Master Prompt preserved (spot-check key concepts)
- [ ] Zero ambiguity in daily execution path (can follow checklists mechanically)
- [ ] Only one-time decisions: niche, offer, price (all other work is templated)

**Result:** If all pass → System Complete and Ready for Use
**If failures:** List issues and recommend remediation

---

## Output Format

Present validation results in this format:

```
# VALIDATION RESULTS

## Current Phase: [Phase from STATE.json]

## ✅ PASSED (X/Y checks)
- [List passed checks]

## ❌ FAILED (X/Y checks)
- [List failed checks with details]

## ⚠️ WARNINGS (X issues)
- [List non-critical issues]

---

## Overall Status: [PASS / FAIL / PARTIAL]

[If PASS]:
✅ Phase [X] validation complete. Ready to proceed.
Run `/next` to continue.

[If FAIL]:
❌ Found [X] critical issues that must be resolved.

Recommended actions:
1. [Action to fix issue 1]
2. [Action to fix issue 2]
...

[If PARTIAL]:
⚠️ System mostly complete but has [X] warnings.

You can proceed, but be aware of:
- [Warning 1]
- [Warning 2]

Run `/next` to continue or address warnings first.
```

---

## Error Handling

If validation script itself fails (e.g., cannot read files):
- Report the error clearly
- Recommend: "Check file paths and permissions"
- Suggest: "Try running validation checks manually"

If STATE.json is corrupted or invalid:
- Recommend: "Run `python .claude/hooks/update-state.py` to regenerate"
- Provide: "Or manually fix JSON syntax issues"

---

## Manual Validation (If Automated Checks Fail)

If you cannot run automated validation, check manually:

1. **File Count:** `find . -type f -name "*.md" | wc -l` (should be 25+)
2. **STATE.json:** `cat system/STATE.json | python -m json.tool` (should be valid JSON)
3. **Prompt Generator:** Open in browser, check console for errors
4. **Templates:** Open a few asset files, verify they contain actual content (not stubs)

Report findings and I'll help diagnose issues.
