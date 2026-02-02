# What Should I Do Next?

This command reads your current workspace state and recommends the next action.

---

## How This Works

1. Read `STATE.json` to determine current phase and metrics
2. Read `CLAUDE.md` Current State section
3. Apply decision logic to determine next action
4. Provide specific, actionable recommendation

---

## Decision Logic

### Check 1: System Initialization

Read STATE.json. If file doesn't exist or currentPhase is "Not Started":
- **Recommendation:** "Run `/init` to bootstrap the system (this takes 10-15 minutes)"
- **Stop here**

### Check 2: Phase Completion Status

Read STATE.json currentPhase field.

**If Phase = "Phase 1" or "Phase 2":**
- **Recommendation:** "Phase 1-2 should be completed by `/init` command. If you haven't run it yet, run `/init` now."
- **Stop here**

**If Phase = "Phase 3":**
- **Recommendation:** "Build the prompt generator tool. Execute: `.claude/rules/phase-3-generator.md`"
- **Details:** "This creates `/system/prompt-generator.html` which you'll use for all future prompt generation."
- **Stop here**

**If Phase = "Phase 4":**
- **Recommendation:** "Create asset templates. Execute: `.claude/rules/phase-4-assets.md`"
- **Details:** "This creates 8+ template files in `/assets` for hand raiser posts, video scripts, follow-ups, etc."
- **Stop here**

**If Phase = "Phase 5":**
- **Recommendation:** "Set up daily operations system. Execute: `.claude/rules/phase-5-operations.md`"
- **Details:** "This creates `/daily/DAILY-SOP.md` with your complete operational checklist."
- **Stop here**

**If Phase = "Phase 6":**
- **Recommendation:** "Run final validation. Execute: `.claude/rules/phase-6-validation.md`"
- **Details:** "This verifies all system components are working correctly."
- **Stop here**

### Check 3: Business Configuration (If Phase = "Complete" or "Phase 3+")

Read CLAUDE.md Current State section.

**If Niche is empty or contains template text "(define your target...)":**
- **Recommendation:**
```
Configure your business in CLAUDE.md:

1. Open CLAUDE.md
2. In the "Current State" section, replace:
   - Niche: [your specific target market]
     Example: "roofing contractors in Texas"

   - Offer Promise: [specific outcome, 1-3 sentences]
     Example: "50-100 qualified leads per month via Facebook ads targeting homeowners needing roof repairs"

   - Price Point: [$/month and deliverable]
     Example: "$3,000/month for 50-100 qualified leads"

3. Save CLAUDE.md
4. Run /next again

Be specific. "Social media management" is too vague. "15-25 roofing leads per month via Facebook ads" is specific.
```
- **Stop here**

### Check 4: Daily Operations (Phase Complete, Business Configured)

Read metrics from STATE.json.

**If connectionsBuilt < 100:**
- **Recommendation:** "Build your network. Add 20-30 targeted connections daily until you reach 100."
- **How:** "Search LinkedIn/Facebook for '[Job Title] + [Location/Industry]'. Send connection requests. No custom message needed (higher acceptance rate)."
- **Track:** "Update CLAUDE.md → Connections Built: [number]/100"
- **Stop here**

**If postsPublished < 3 AND offerValidated = false:**
- **Recommendation:** "Post hand raiser content to validate your offer."
- **How:**
```
1. Open /assets/hand-raiser-posts.md
2. Choose a template variation
3. Fill in your offer details
4. Post to LinkedIn/Facebook
5. Update CLAUDE.md → Posts Published: [number]
6. Track engagement (comments, DMs)
```
- **Details:** "Validation criteria: 3+ engaged prospects across 3 posts means your offer is validated."
- **Stop here**

**If postsPublished >= 3 AND offerValidated = false:**
- **Recommendation:** "Review engagement and pivot if needed."
- **Analysis:**
```
If NO engagement on 3+ posts:
- Audit: Is your offer promise outcome-focused and specific?
- Audit: Are connections actual target prospects?
- Audit: Is platform correct? (LinkedIn for B2B, Facebook for local/B2C)

Action: Pivot your offer PROMISE (not niche)
- Use /system/prompt-generator.html → "Generate alternative offer angles"
- Test new promise with next 3 posts

If you HAVE engagement (3+ people commented/DMed):
- Update CLAUDE.md → Offer Validated: Yes
- Run /next again
```
- **Stop here**

**If offerValidated = true AND videosSent = 0:**
- **Recommendation:** "Record your first sales video and send to engaged prospects."
- **How:**
```
1. Open /assets/video-script-template.md
2. Use the 5-part structure (Hook, Outcome Demo, Price, Differentiation, Purchase Instructions)
3. Customize for first prospect
4. Record via Loom (5 minutes max, enable captions)
5. Send video with personalized wrapper (see /assets/video-message-wrappers.md)
6. Update CLAUDE.md → Videos Sent: 1
```
- **Stop here**

**If videosSent > 0 AND clientsAcquired = 0:**
- **Recommendation:** "Execute follow-up sequence on all video recipients."
- **How:**
```
1. Open /assets/follow-up-sequence.md
2. For each prospect, check time since video sent:
   - 24h: Send check-in message
   - 48h: Send value-add message
   - 72h: Send soft close message
   - 1 week: Send final attempt message
3. Track responses
4. When someone says YES → send payment link
5. Update CLAUDE.md → Clients Acquired: [number]
```
- **Stop here**

**If clientsAcquired < 3:**
- **Recommendation:** "Focus on acquisition. Post hand raisers daily and send videos to all responders."
- **Daily routine:**
```
Morning (30-45 min):
- Post 1 hand raiser (rotate templates from /assets/hand-raiser-posts.md)
- Respond to yesterday's engagers with video

Mid-morning (30-45 min):
- Execute follow-up sequences
- Handle questions/objections (use /assets/objection-responses.md)
- Process any payments

Target: 3 clients before building fulfillment systems
```
- **Stop here**

**If clientsAcquired >= 3 AND currentPhase != "Complete":**
- **Recommendation:** "Finalize system setup if not already complete."
- **Check:** "Run `/validate` to ensure all phases are complete, then continue with business operations."
- **Stop here**

**If clientsAcquired >= 3 AND currentPhase = "Complete":**
- **Recommendation:** "Continue daily operations (see `/daily/QUICK-REFERENCE.md`)."
- **Daily blocks:**
```
Morning: Lead generation (30-45 min)
- Add connections (if < 100)
- Post hand raiser (if >= 100)
- Respond to engagers with video

Mid-morning: Sales activities (30-45 min)
- Send videos
- Execute follow-ups
- Handle objections
- Process payments

Afternoon: Client fulfillment (variable)
- Deliver services
- Weekly updates via Loom
- Handle issues

End of day: Update state (15 min)
- Update CLAUDE.md metrics
- STATE.json auto-syncs
```
- **Stop here**

**If clientsAcquired >= 5:**
- **Additional note:** "Consider hiring (optional at 5 clients, mandatory at 10). Use /system/prompt-generator.html → 'Generate job post for [role]'"

**If clientsAcquired >= 10:**
- **Warning:** "Hiring is mandatory at 10+ clients. Quality will suffer without delegation. Generate hiring materials immediately."

---

## Output Format

Present recommendation in this format:

```
## 📋 NEXT ACTION

[Clear, specific recommendation]

### Why This Matters
[1-2 sentences explaining priority]

### How to Execute
[Step-by-step instructions or reference to specific file]

### Success Criteria
[How to know you're done]

### Update State
[What to update in CLAUDE.md after completion]
```

---

## Error Handling

If STATE.json cannot be read:
- Fall back to reading CLAUDE.md Current State section
- Recommend: "STATE.json seems to be missing. Run `python .claude/hooks/update-state.py` to regenerate it."

If both STATE.json and CLAUDE.md are unclear:
- Recommend: "Run `/validate` to check system integrity, then run `/next` again."
