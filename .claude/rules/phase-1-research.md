# Phase 1: Research & Documentation

## Prerequisites
- None (this is the starting phase)
- Will be executed automatically by `/init` command

## Deliverables
- `/docs/research-findings.md` - Research sources and findings
- `/docs/methodology-master.md` - Unified methodology document
- `/docs/core-patterns.md` - Replicable patterns and formulas

## Instructions

### Task 1: Create Research Findings Document

Create `/docs/research-findings.md` with:

**Content Structure:**
```markdown
# Agency Business System - Research Findings

## Sources Reviewed
1. Beyond The Agency Box - Frankie Fihn
2. Hand Raiser Lead Generation Systems (2026)
3. Async Video Sales Best Practices
4. No-Meeting Agency Fulfillment Models
5. Social Media Marketing Dynamics (2026)

## Key Findings

### Hand Raiser Lead Generation
- Why it works: Inverts discovery dynamic (prospects believe they found you)
- 2026 reality: Organic reach limited, requires 100+ targeted connections first
- Platform choice: LinkedIn for B2B, Facebook for local services/B2C
- Validation signal: 3+ engaged prospects across 3 posts = offer validated
- Execution: Build 100 connections → post 1x daily → send video to responders

### Async Video Sales
- Real-world data: 800 clients closed in one year without calls (Frankie Fihn)
- 5-part structure: Hook → Outcome Demo → Price → Differentiation → Purchase Instructions
- Length: 4-5 minutes maximum for optimal engagement
- 2026 best practices: Captions enabled, mobile-optimized, "Video" in subject line
- Phases: Custom videos (first 10-20 prospects) → Standardized (post-validation)

### No-Meeting Fulfillment
- Communication: Weekly 3-5 min Loom updates + text for questions
- Positioning: "No-meeting" model is a BENEFIT (client time isn't wasted)
- Tools: Loom, email/Slack, shared dashboards, annotated screenshots
- Benefits: Global client base, higher capacity, documentation trail

### Pricing & Offers
- Sweet spot: $1K-$10K/month for service businesses
- Always contextualize: "$X/month AND 50-100 [deliverable]" (never price alone)
- Promise format: Specific, measurable outcome (not service description)
- Bad: "Social media management"
- Good: "50-100 qualified leads per month via Facebook ads"

### Social Media Dynamics (2026)
- Organic reach on Meta platforms near-zero without existing engagement
- Hand raiser posts work when: Combined with targeted network building OR high-engagement audiences
- LinkedIn organic still viable for B2B with strategic connections
- Best times: LinkedIn 7-9am or 5-6pm, Facebook 1-3pm or 7-9pm

## Statistics & Case Studies
- 800 clients closed without calls: Frankie Fihn, Beyond The Agency Box
- 60%+ watch videos on mobile: Optimize for mobile viewing
- "Video" in subject line: 19%+ open rate boost
- 150-200 instructions: Reliable LLM instruction-following limit

## Tools & Platforms
- Video: Loom (with captions)
- Lead gen: LinkedIn OR Facebook
- Payments: Stripe
- Communication: Email + Loom
- Project management: Notion/Asana (optional)
```

### Task 2: Create Unified Methodology Document

Create `/docs/methodology-master.md` with:

**Content Structure:**
```markdown
# Agency Business System - Complete Methodology

## Lead-to-Close Pipeline

```
flowchart:
Hand Raiser Post → Engagement (comment/DM) → Video Send → Follow-Up Sequence → Payment → Onboarding
```

### Stage 1: Hand Raiser Post
- Build 100 connections in target niche first
- Post 1x daily asking "who needs [specific outcome]?"
- Focus on PROMISE (what they get), not MECHANISM (what you do)
- Rotate template variations (don't repeat same post within 7 days)
- Track engagement (comments + DMs)

### Stage 2: Engagement Response
- Send video within 4 hours of engagement
- Custom video (validation phase) OR standardized video (post-validation)
- Use personalized message wrapper even with standardized video
- Log in pipeline tracker: Name, date, video sent, platform

### Stage 3: Follow-Up Sequence
- 24h: Check-in ("Did you get a chance to watch?")
- 48h: Value-add (additional proof point or case study)
- 72h: Soft close ("Ready to move forward?")
- 1 week: Final attempt ("Closing this opportunity Friday...")
- Mark cold after 1 week of no response to final attempt

### Stage 4: Payment
- Send Stripe link immediately when prospect says YES
- Template: "Here's the payment link: [link]. You'll get onboarding email within 2 hours."
- Confirm payment received
- Trigger onboarding

### Stage 5: Onboarding
- Send onboarding document (expectations, timeline, access requirements)
- Set calendar reminder for first deliverable deadline
- Set calendar reminder for first weekly update
- Log in client tracker

## Offer Construction Framework

### 1-3 Sentence Formula
[Target Niche] gets [Specific, Measurable Outcome] in [Timeframe] for [$Price/month]

**Examples:**
- "Roofing contractors get 50-100 qualified leads per month via Facebook ads for $3,000/month"
- "E-commerce brands get 15-25% revenue increase through email marketing optimization for $5,000/month"
- "Local service businesses get 20-30 booked appointments per month via Google Ads for $2,500/month"

### Pricing Psychology
- Never state price alone: Always "$X AND [deliverable]"
- Anchor to value: "50 calls at $2,000/month = $40 per call"
- Scale matters: $3K/mo feels accessible, $10K+ needs stronger proof

### Guarantee Structures
- Performance-based: "If we don't deliver 50 leads, we work for free next month"
- Time-based: "First results within 7 days or full refund"
- Satisfaction-based: "30-day money-back guarantee if not satisfied"

## Hand Raiser System Details

### Platform Selection
- **LinkedIn:** B2B services, professional services, SaaS
- **Facebook:** Local services, B2C, e-commerce

### Connection Building (Phase 1)
- Target: 100 connections before posting
- Search: "[Job Title] + [Location/Industry]"
- No custom message on connection request (higher acceptance rate)
- Add 20-30 per day until target reached

### Post Templates
- Direct question: "Who needs [outcome] without [pain point]?"
- Time-bound urgency: "Looking for 3 [niche] who need [outcome] this month"
- Specific result: "Who wants [X number] of [deliverable] for $[budget]?"
- Rotate daily, avoid repeating same template within 7 days

### Validation Signals
- **Validated:** 3+ engaged prospects across 3 posts
- **Not validated:** 0 engagement after 3 posts → pivot offer promise
- **Pivot:** Change the OUTCOME you promise, not the niche

## Video Sales System (5 Parts)

### Part 1: Hook (10-15 seconds)
- Reference their specific comment/DM
- "Hey [Name], I saw you're looking to [their goal]..."

### Part 2: Outcome Demonstration (60-90 seconds)
- Show what happens AFTER they work with you
- Screen record: Lead dashboard, example calls, metric dashboards
- Play 10-second example if possible
- Visual proof > verbal description

### Part 3: Contextualized Price (20-30 seconds)
- Formula: "$[PRICE] per [TIME] and you get [SPECIFIC DELIVERABLE]"
- Example: "$3,000/month and you get 50-100 calls like the one I just showed you"
- NEVER say price without deliverable

### Part 4: Differentiation (30-45 seconds)
- Address "tried this before" objection preemptively
- Focus on ONE key differentiator:
  - Speed: "First calls within 7 days" vs "Most agencies take 60 days"
  - Process: "We target X instead of Y" (explain unique method)
  - Guarantee: "We're the only ones who [unique guarantee]"

### Part 5: Purchase Instructions (20-30 seconds)
- Exact steps to buy: "Click the Stripe link below, enter your info, you'll get an onboarding email within 2 hours"
- Remove ALL friction from "yes" to "paid"

## Fulfillment Model

### Communication Structure
- **Onboarding:** Written doc + video walkthrough
- **Weekly updates:** 3-5 min Loom (progress, metrics, next steps)
- **Issue resolution:** Text/video response within 4 hours
- **Deliverables:** Loom walkthrough + written summary
- **No status calls:** Eliminated entirely

### Client Expectation Setting
- Explicitly state "no-meeting" model in onboarding
- Position as benefit: "Your time isn't wasted on status calls"
- Provide clear response time commitments
- Over-communicate proactively via Loom

## Scaling Framework

### Hiring Triggers
- **5 clients:** Consider hiring (optional)
- **10 clients:** Hiring mandatory (quality suffers without delegation)

### First Hire Priority
- Fulfillment specialist (frees you for acquisition + QC)
- Account manager (client communication)
- Media buyer (if service is ad management)

### Delegation Approach
- Document current process via Loom
- Create SOP from recorded process
- Test candidate with assignment
- Train via recorded processes + live shadowing
```

### Task 3: Create Core Patterns Document

Create `/docs/core-patterns.md` with:

**Content Structure:**
```markdown
# Agency Business System - Core Patterns

## Hand Raiser Post Psychology

**Why Self-Selection Works:**
- Psychological reversal: Prospect believes they found YOU (not being sold to)
- Lower resistance: Commenting/DMing is low commitment
- Intent signal: Those who engage have active need (not passive curiosity)
- Social proof: Public engagement encourages more engagement

**Engagement Triggers:**
- Specificity: "50-100 calls" beats "more leads"
- Outcome focus: "Emergency plumbing calls" beats "PPC services"
- Budget anchor: "$3K budget" pre-qualifies financially
- Question format: "Who needs X?" invites response

**Validation Interpretation:**
- 3+ engagements = market pull exists, offer validated
- 0 engagements after 3 posts = pivot offer promise (not niche)
- Engagement but no video responses = offer clarity issue (refine messaging)

## Video Script Formulas

**Hook Variations by Niche:**
- **B2B:** "Hey [Name], I saw you're trying to [business goal]..."
- **Local service:** "Hey [Name], noticed you need [outcome]..."
- **E-commerce:** "Hey [Name], saw you're looking to [revenue goal]..."

**Outcome Demonstration Techniques:**
- **Lead gen:** Show lead dashboard with real numbers
- **Service delivery:** Show before/after or process screenshots
- **Coaching:** Show testimonial clip or result screenshot
- **SaaS:** Show product demo of key outcome

**Price Contextualization Templates:**
- "$X/month and you get Y [deliverables]"
- "Y [deliverables] for $X/month" (swap order for emphasis)
- "At $X per [deliverable], you're getting [value comparison]"

## "Easy Yes" Offer Construction Criteria

1. **Specific outcome:** "50-100 leads" NOT "lead generation"
2. **Measurable:** Can be counted/tracked
3. **Timeline:** "Per month" or "within 7 days"
4. **Price contextualized:** Always paired with deliverable
5. **Target niche clear:** "Roofing contractors" NOT "businesses"

## Text-Based Closing Sequences

**Follow-Up Timing:**
- 24h: Gentle check-in
- 48h: Add value (case study, extra proof)
- 72h: Soft close (ask for decision)
- 1 week: Final attempt (create urgency)

**Question Handling:**
- **Situational fit:** "Does this work for [my situation]?" → 95% yes with minor calibration
- **Logistics:** "How long does setup take?" → Specific answer with timeline
- **Objections:** See objection frameworks below

**Going Cold Protocol:**
- After 1 week of no response to final attempt: Mark as COLD
- Remove from active follow-up
- Optional: Re-engagement campaign at 90 days

## "Tried This Before" Objection Framework

**Step 1: Acknowledge**
- "I totally get that. A lot of [niche] have tried [thing] before."

**Step 2: Probe**
- "What specifically didn't work about it?"

**Step 3: Differentiate**
- Identify their past failure point
- Explain how your approach differs AT THAT SPECIFIC POINT
- "The reason that didn't work is [X]. We handle that by [Y]."

**Step 4: Proof**
- "Here's an example of a client who had the same issue..." (show result)

**Differentiation Angles:**
- **Speed:** "Most take 60 days. We deliver first results in 7 days."
- **Targeting:** "They targeted [X]. We target [Y] instead."
- **Guarantee:** "They had no guarantee. We guarantee [outcome] or work free."
```

## Validation
- [ ] All 3 files created
- [ ] research-findings.md covers all 5 methodology sources
- [ ] methodology-master.md has complete pipeline + all frameworks
- [ ] core-patterns.md has actionable formulas and templates
- [ ] Content is comprehensive (each file 500+ words minimum)

## Next Phase
After completion, proceed to Phase 2: Workspace Foundation
(This phase is typically combined with Phase 2 in `/init` command)
