# Phase 5: Daily Operations Setup

## Prerequisites
- Phase 1-4 complete
- All asset templates created
- Business operating (or ready to start operations)

## Deliverables
3 operational documents in `/daily` directory:
- DAILY-SOP.md - Complete daily operations manual
- QUICK-REFERENCE.md - One-page daily checklist
- pipeline-tracker.md - Prospect and client tracking

## Instructions

### Document 1: Complete Daily SOP

**File:** `/daily/DAILY-SOP.md`

**Content:** Comprehensive daily operations manual with 4 time blocks

**Structure:**

```markdown
# DAILY OPERATIONS SOP
## Phoneless Agency - Hand Raiser + Video Sales Model

---

## DAILY SCHEDULE OVERVIEW

| Time Block | Duration | Activity | Tools |
|------------|----------|----------|-------|
| Morning Block | 30-45 min | Lead Generation | LinkedIn/FB, hand-raiser templates |
| Mid-Morning Block | 30-45 min | Sales Activities | Loom, video scripts, follow-up templates |
| Afternoon Block | Variable | Client Fulfillment | Service tools, Loom |
| End of Day | 15 min | Pipeline Review & State Update | Tracker, CLAUDE.md |

**Total Active Work: 2-4 hours/day (excluding fulfillment)**

---

## MORNING BLOCK: Lead Generation (30-45 min)

### Daily Checklist

□ **Connection Building** (if under 100 connections)
   - Platform: [LinkedIn for B2B, Facebook for local/B2C]
   - Search: "[Job Title] + [Location/Industry]"
   - Add 20-30 targeted prospects
   - No custom message on request
   - Track in spreadsheet
   - **Stop when**: 100 connections reached

□ **Post Hand Raiser Content** (if at 100+ connections)
   - Frequency: 1 post per day
   - Source: /assets/hand-raiser-posts.md
   - Rotate variations (no repeat within 7 days)
   - Best times: LinkedIn 7-9am/5-6pm, Facebook 1-3pm/7-9pm
   - Log: Date, template used, platform
   - Track engagement (comments, DMs)

□ **Respond to Yesterday's Hand Raisers**
   - Check post comments from previous day(s)
   - Check DMs from previous day(s)
   - **For each interested response:**
     - Send video (custom if validating, standardized if validated)
     - Use wrapper from /assets/video-message-wrappers.md
     - Log in pipeline tracker

### Validation Signal Check

**If no engagement on posts (3+ days):**
1. Audit offer promise - outcome-focused and specific?
2. Audit connection quality - actual target prospects?
3. Consider pivoting offer promise (NOT niche)

**Engagement threshold:**
- 3+ engaged prospects across 3 posts = offer validated
- Update CLAUDE.md → Offer Validated: Yes

---

## MID-MORNING BLOCK: Sales Activities (30-45 min)

### Daily Checklist

□ **Record Custom Videos** (Validation Phase ONLY)
   - Use /assets/video-script-template.md
   - Personalize hook + outcome demo
   - Keep to 5 minutes max
   - Record in Loom with captions
   - Note any new objections

□ **Send Standardized Video** (Post-Validation)
   - Use ONE master video for ALL prospects
   - Personalize ONLY the wrapper message
   - Send within 4 hours of engagement
   - Log in pipeline tracker

□ **Execute Follow-Up Sequence**
   - Check pipeline tracker for follow-up timing:
     - 24h since video: Check-in message
     - 48h since video: Value-add message
     - 72h since video: Soft close
     - 1 week since video: Final attempt
   - Use /assets/follow-up-sequence.md
   - Mark cold after 1 week post-final attempt

□ **Handle Questions/Objections**
   - Respond to prospect questions within 4 hours
   - Use /assets/objection-responses.md
   - Log question type in tracker

□ **Process Payments**
   - Send payment links to "yes" prospects
   - Confirm payments received (check Stripe)
   - Trigger onboarding for new clients
   - Update CLAUDE.md → Clients Acquired: [number]

---

## AFTERNOON BLOCK: Client Fulfillment (Variable)

### Daily Checklist

□ **New Client Onboarding** (if payment received)
   - Send /assets/onboarding-template.md (customized)
   - Request required info/access
   - Set calendar reminder for first deliverable
   - Set calendar reminder for first weekly update
   - Log in client tracker

□ **Active Client Work**
   - Execute service delivery
   - Document progress for weekly update
   - Take screenshots of results
   - **Capacity check**: Struggling? Hiring trigger activated

□ **Weekly Client Updates** (scheduled days)
   - Record Loom using /assets/weekly-update-script.md
   - Include: Progress, metrics, next steps, questions
   - Send via client's preferred channel
   - Log: Date sent, client name

□ **Deliverable Handoffs**
   - Use /assets/deliverable-handoff.md template
   - Record Loom walkthrough (3-5 min)
   - Send summary + files
   - Request confirmation
   - Follow up if no response in 24h

---

## END OF DAY BLOCK: Review & Update (15 min)

### Daily Checklist

□ **Update Pipeline Tracker**
   - New leads added: [number]
   - Videos sent: [number]
   - Follow-ups completed: [number]
   - Payments received: [number]
   - Calculate conversion rates (weekly)

□ **Update CLAUDE.md Current State**
   - Connections Built: [0-100]
   - Videos Sent: [total]
   - Clients Acquired: [total]
   - Offer Validated: [Yes/No]
   - Current Blockers: [list]
   - **Auto-syncs to STATE.json via hook**

□ **Prep Tomorrow's Priorities**
   - Note custom videos needed
   - Flag urgent follow-ups (72h mark)
   - Check for needed assets (use Prompt Generator)

□ **Weekly Review** (Fridays ONLY)
   - Hand raiser → Video conversion: [%]
   - Video → Client conversion: [%] (target >10%)
   - Fulfillment on-time rate: 100%?
   - If not validated after 2 weeks: Major pivot needed

---

## DECISION TREES

### No Engagement on Hand Raiser Posts
[Flow diagram logic]
Post → 0 engagement after 24h → Wait for 2 more posts → Still none? → Audit offer/connections → Pivot promise → Test 3 more

### Video Sent, No Response
[Flow diagram logic]
Video sent → 24h check-in → 48h value-add → 72h soft close → 1 week final → Mark COLD

### Capacity Check for Hiring
[Flow diagram logic]
5+ clients → Struggling? → Yes: Hire / No: Continue
10+ clients → Hire mandatory

---

## KEY METRICS TO TRACK

| Metric | Target | Frequency | Action Threshold |
|--------|--------|-----------|------------------|
| Connections added | 20-30/day | Daily | Stop at 100 |
| Hand raiser posts | 1/day | Daily | - |
| Post engagement | >2% | Weekly | <2% for 3 posts = pivot |
| Videos sent | All engaged | Daily | - |
| Video → Client | >10% | Weekly | <10% after 20 videos = refine |
| Fulfillment on-time | 100% | Weekly | Late = hiring trigger |
```

Include weekly rhythm table, tool stack, and emergency protocols.

Reference: Original Master Prompt lines 960-1323 for complete SOP details

---

### Document 2: Quick Reference Card

**File:** `/daily/QUICK-REFERENCE.md`

**Content:** One-page daily checklist (under 100 lines)

**Structure:**

```markdown
# DAILY QUICK REFERENCE CARD

## Morning Block (30-45 min)
□ Add 20-30 connections (if < 100)
□ Post 1 hand raiser (if >= 100)
□ Respond to yesterday's engagers with video

**Validation:** 3+ engaged prospects across 3 posts = validated ✓

---

## Mid-Morning Block (30-45 min)
□ Record/send videos to new hand raisers
□ Execute follow-up sequence (24h/48h/72h/1wk)
□ Handle objections (use /assets/objection-responses.md)
□ Process payments → trigger onboarding

**Follow-Up Cadence:**
24h: Check-in | 48h: Value-add | 72h: Soft close | 1wk: Final | Mark COLD

---

## Afternoon Block (Variable)
□ Onboard new clients
□ Execute fulfillment
□ Record weekly updates (use /assets/weekly-update-script.md)
□ Deliver work (use /assets/deliverable-handoff.md)

**Capacity Trigger:** 10+ clients = hiring mandatory

---

## End of Day (15 min)
□ Update pipeline tracker
□ Update CLAUDE.md metrics
□ Prep tomorrow's priorities
□ **Friday:** Weekly metrics review

**Key Numbers:**
- 100 connections before posting
- 1 post/day
- 5 min max video
- >10% video→client conversion
- 5+ clients = consider hiring
- 10+ clients = hiring mandatory
```

---

### Document 3: Pipeline Tracker

**File:** `/daily/pipeline-tracker.md`

**Content:** Prospect and client tracking tables

**Structure:**

```markdown
# PIPELINE TRACKER TEMPLATE

## Active Prospects

| Name | Source | Date Added | Video Sent | Last Follow-up | Next Action | Status | Notes |
|------|--------|------------|------------|----------------|-------------|--------|-------|
| | | | | | | | |

**Status Options:**
- NEW - Just engaged
- VIDEO_SENT - Video delivered
- FOLLOWUP_1 - 24h sent
- FOLLOWUP_2 - 48h sent
- FOLLOWUP_3 - 72h sent
- FOLLOWUP_FINAL - 1-week sent
- QUESTIONS - Asked questions
- READY_TO_PAY - Said yes
- PAID - Payment received
- COLD - No response after final

---

## Conversion Funnel (This Week)

| Stage | Count | Conversion % |
|-------|-------|--------------|
| Hand Raisers | | - |
| Videos Sent | | [Videos/Raisers]% |
| Replies | | [Replies/Videos]% |
| Clients Closed | | [Clients/Videos]% |

**Targets:**
- Hand Raiser → Video: 100%
- Video → Reply: >30%
- Video → Client: >10%

---

## Weekly Summary

| Week Of | Hand Raisers | Videos Sent | Clients Closed | Revenue |
|---------|--------------|-------------|----------------|---------|
| | | | | |

---

## Client Tracker

| Client | Start Date | Service | Price | Status | Deliverables Owed | Next Update |
|--------|------------|---------|-------|--------|-------------------|-------------|
| | | | | ACTIVE | | |

**Status Options:**
- ONBOARDING - Just paid
- ACTIVE - Ongoing service
- PAUSED - Temporary hold
- CHURNED - Canceled

---

## Notes & Insights

**Common Objections This Week:**
- [Objection]: [Frequency]

**What's Working:**
- [Observation]

**What's Not:**
- [Observation]

**Action Items:**
- [ ] [Action based on data]
```

---

## Quality Criteria

- [ ] DAILY-SOP.md is comprehensive (all 4 time blocks detailed)
- [ ] DAILY-SOP.md has decision trees for common scenarios
- [ ] DAILY-SOP.md has metrics tracking table
- [ ] QUICK-REFERENCE.md is under 100 lines (truly quick)
- [ ] QUICK-REFERENCE.md covers all 4 time blocks
- [ ] pipeline-tracker.md has tables for prospects, funnel, weekly summary, clients
- [ ] All checklists are actionable (clear yes/no completion criteria)
- [ ] Can execute full day using only these documents + asset templates

## Validation

**Test the SOP:**
1. Can you execute morning block with just DAILY-SOP.md and asset templates?
2. Does QUICK-REFERENCE.md fit on one page when printed?
3. Does pipeline-tracker.md have all needed columns?

If "No" to any, refine before marking complete.

## After Completion

1. **Update CLAUDE.md:**
   - Set Phase to "Phase 6"
   - Add /daily/*.md to "Assets Created"

2. **User can now:**
   - Follow daily operations mechanically
   - No strategic thinking required
   - All decisions templated

## Next Phase

Proceed to Phase 6: System Validation & Completion
