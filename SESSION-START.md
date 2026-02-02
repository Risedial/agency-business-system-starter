# How to Start a New Claude Code Session

## Overview

This Agency Business System is designed for **mechanical execution** with minimal decision-making. Everything you need is in this workspace.

**System Components:**
- **CLAUDE.md** - Workspace context (auto-loads in every session)
- **Slash Commands** - `/init`, `/next`, `/validate`
- **Phase Files** - Step-by-step instructions in `.claude/rules/`
- **Prompt Generator** - Dynamic prompt creation (after Phase 3)
- **Reference Docs** - Methodology details in `.claude/rules/reference/`

---

## First Time Setup (Building the System)

### Prerequisites

- Claude Code installed and working
- Basic understanding of command line
- 30-60 minutes for initial setup

### Step 1: Initialize the System

Open Claude Code in this directory and run:

```
/init
```

**What this does:**
- Executes Phase 1: Research & Documentation
- Executes Phase 2: Workspace Foundation
- Creates all framework files in `/docs`
- Sets up state tracking (STATE.json + hooks)
- Creates reference methodology files

**Expected output:** ~20 files created in 10-15 minutes

**Watch for:**
- Files being created in `/docs`, `.claude/rules/reference`, `/system`
- STATE.json should appear in `/system` directory
- Hook should be executable (`update-state.py`)

### Step 2: Verify Initialization

After `/init` completes, check:

```
- [ ] CLAUDE.md exists (you're reading it)
- [ ] /docs directory has 6+ .md files
- [ ] /system/STATE.json exists
- [ ] .claude/hooks/update-state.py exists
- [ ] .claude/settings.json exists
- [ ] .claude/rules/reference/ has 4 .md files
```

If any are missing, re-run `/init` or check for errors.

### Step 3: Configure Your Business

Open [CLAUDE.md](CLAUDE.md) and fill in the "Current State" section:

```markdown
**Niche:** [your target industry/role]
Example: "roofing contractors in Texas"

**Offer Promise:** [specific outcome in 1-3 sentences]
Example: "50-100 qualified leads per month via Facebook ads targeting homeowners needing roof repairs"

**Price Point:** [$/month for deliverable]
Example: "$3,000/month for 50-100 qualified leads"
```

**Important:** Be specific. "Social media management" is too vague. "15-25 qualified roofing leads per month via Facebook ads" is specific.

Save [CLAUDE.md](CLAUDE.md).

### Step 4: Continue Through Phases

Run:

```
/next
```

Claude will read your current state and tell you exactly what to do next.

Follow the instructions. You'll progress through:
- Phase 3: Build prompt generator
- Phase 4: Create asset templates
- Phase 5: Set up daily operations
- Phase 6: Final validation

Each phase takes 15-30 minutes.

**Total setup time:** 1-2 hours for complete system

---

## Continuing Work (Existing Workspace)

### Quick Start (Most Common)

1. Open Claude Code in this directory
2. CLAUDE.md automatically loads (you don't need to read it manually)
3. Run: `/next`
4. Execute the recommended action

**That's it.** The system tells you what to do.

### Using the Prompt Generator (After Phase 3)

Once Phase 3 is complete, you have `/system/prompt-generator.html`:

1. Open `/system/prompt-generator.html` in your browser
2. Click **"Refresh State"** to load current workspace state
3. Read **"What Should I Do Next?"** recommendation
4. Select a prompt category (Validation, Sales Assets, Lead Gen, etc.)
5. Click **"Generate Prompt"**
6. Copy the generated prompt
7. Paste into Claude Code
8. Execute the task

### Daily Operations (After Phase 6)

Once the system is fully built:

1. Open `/daily/QUICK-REFERENCE.md` for at-a-glance checklist
2. Follow **4 daily time blocks:**
   - Morning (30-45 min): Lead generation
   - Mid-morning (30-45 min): Sales activities
   - Afternoon (variable): Client fulfillment
   - End of day (15 min): Update state

3. Use `/system/prompt-generator.html` when you need:
   - Hand raiser post templates
   - Video script variations
   - Follow-up sequences
   - Objection responses

**No improvisation needed.** Everything is templated.

---

## Understanding the Phase System

### Phase Progression

| Phase | What It Does | Time | When Complete |
|-------|--------------|------|---------------|
| **1-2** | Research + Foundation | 15 min | `/init` command |
| **3** | Build prompt generator | 20 min | HTML file created & working |
| **4** | Create asset templates | 30 min | 8+ template files in `/assets` |
| **5** | Set up daily ops | 30 min | Daily SOP created |
| **6** | Validate system | 15 min | All checklists pass |

### How to Know Which Phase You're On

**Option 1: Check CLAUDE.md**
- Open [CLAUDE.md](CLAUDE.md)
- Look at "Current State" → "Phase"

**Option 2: Run `/next`**
- Claude will tell you current phase and what to do

**Option 3: Check STATE.json**
- Open `/system/STATE.json`
- Look at `"currentPhase"` field

### Phase Files Location

Each phase has detailed instructions in `.claude/rules/phase-{X}.md`:

- `phase-1-research.md` - Research & documentation tasks
- `phase-2-foundation.md` - Workspace setup tasks
- `phase-3-generator.md` - Build prompt generator
- `phase-4-assets.md` - Create templates
- `phase-5-operations.md` - Daily operations setup
- `phase-6-validation.md` - System validation

**You don't need to read these manually.** `/next` will load and execute them for you.

---

## State Synchronization

### How State Works

The system tracks your progress in two places:

1. **CLAUDE.md** (manual updates) - "Current State" section
2. **STATE.json** (automatic updates) - Generated by hook

### Manual Updates (After Completing Tasks)

Open [CLAUDE.md](CLAUDE.md) and update:

```markdown
**Phase:** Phase 3
**Connections Built:** 25/100
**Videos Sent:** 3
**Clients Acquired:** 1
**Assets Created:**
- docs/offer-framework.md
- assets/hand-raiser-posts.md
- system/prompt-generator.html
```

### Automatic Updates (Via Hook)

Every time you use Write or Edit tools, `.claude/hooks/update-state.py` runs automatically and updates `STATE.json`.

**You don't need to edit STATE.json manually.**

### If State Gets Out of Sync

**Problem:** CLAUDE.md says "Phase 3" but STATE.json says "Phase 2"

**Solution:**
1. CLAUDE.md is the source of truth
2. Run: `python3 .claude/hooks/update-state.py` to force sync
3. STATE.json will update to match CLAUDE.md

---

## Troubleshooting

### "I ran `/init` but nothing happened"

**Check:**
- Are you in the correct directory? Run `pwd` to verify
- Is Claude Code working? Try a simple command like `ls`
- Check for error messages in output

**Fix:**
- Re-run `/init`
- If still failing, manually execute `.claude/rules/phase-1-research.md`

### "STATE.json is not updating"

**Check:**
- Does `.claude/hooks/update-state.py` exist?
- Is it executable? Run: `ls -l .claude/hooks/update-state.py`
- Does `.claude/settings.json` have the hook configured?

**Fix:**
```bash
# Make hook executable
chmod +x .claude/hooks/update-state.py

# Test hook manually
python3 .claude/hooks/update-state.py

# Check STATE.json was updated
cat system/STATE.json
```

### "Prompt generator shows old/wrong state"

**Check:**
- Did you click "Refresh State" button?
- Is STATE.json up to date?

**Fix:**
1. Update CLAUDE.md Current State section
2. Run: `python3 .claude/hooks/update-state.py`
3. In browser: Hard refresh (Ctrl+Shift+R on Windows, Cmd+Shift+R on Mac)
4. Click "Refresh State" button

### "I don't know what to do next"

**Just run:**
```
/next
```

The system will read your current state and tell you exactly what to do.

### "I'm on Phase X but the instructions don't make sense"

**Read the phase file directly:**
1. Open `.claude/rules/phase-{X}.md` (replace {X} with your phase number)
2. Read the "Prerequisites" section - make sure you completed them
3. Read the "Instructions" section step by step
4. Check the "Validation" section to verify completion

### "Claude seems to have lost context"

**CLAUDE.md auto-loads,** but if Claude seems confused:

1. Remind Claude: "Read CLAUDE.md and review current state"
2. Run: `/next` to re-orient
3. Specify current phase: "I'm on Phase 3, execute `.claude/rules/phase-3-generator.md`"

### "Phase 3 prompt generator won't load in browser"

**Check:**
- Does `/system/prompt-generator.html` exist?
- Open browser developer console (F12) for errors
- Try different browser (Chrome, Firefox, Edge)

**Fix:**
- Re-run Phase 3: "Execute `.claude/rules/phase-3-generator.md`"
- Verify STATE.json is valid: `cat system/STATE.json | python -m json.tool`

---

## Fresh Session Protocol

### When You Close and Reopen Claude Code

**What happens automatically:**
- CLAUDE.md loads into context
- All `.claude/rules/` files are available
- STATE.json is current (if you updated CLAUDE.md before closing)

**What you need to do:**
1. Run: `/next`
2. Continue where you left off

**That's it.** No manual context loading needed.

### If You Forgot Where You Were

**Check CLAUDE.md:**
1. Look at "Phase" in Current State
2. Check last entry in "Assets Created"
3. Read "Current Blockers" for reminders

**Or just run `/next`** and the system tells you.

---

## File Organization

### Where Everything Lives

```
/                           # Root - you are here
├── CLAUDE.md              # Read first - workspace context
├── SESSION-START.md       # This file - user guide
├── .claude/               # Claude Code configuration
│   ├── rules/            # Phase instructions + reference docs
│   ├── commands/         # Slash commands
│   └── hooks/            # State sync automation
├── docs/                  # Methodology documentation
├── assets/                # Templates for business operations
├── daily/                 # Daily operation SOPs
└── system/                # STATE.json + prompt generator
```

### What to Read, What to Use

**Read:**
- [CLAUDE.md](CLAUDE.md) - Workspace overview (auto-loads)
- [SESSION-START.md](SESSION-START.md) - This file, for setup help
- `/daily/QUICK-REFERENCE.md` - Daily checklist (after Phase 5)

**Use:**
- `/init` - Bootstrap system (run once)
- `/next` - What to do next (run anytime)
- `/validate` - Check completion (run after each phase)
- `/system/prompt-generator.html` - Generate prompts (after Phase 3)

**Reference (when needed):**
- `.claude/rules/reference/methodology.md` - Core principles
- `.claude/rules/reference/hand-raiser.md` - Lead gen details
- `.claude/rules/reference/video-sales.md` - Sales structure
- `.claude/rules/reference/fulfillment.md` - Delivery model
- `/docs/*` - Detailed frameworks (generated by Phase 1-2)
- `/assets/*` - Templates (generated by Phase 4)

---

## Common Workflows

### Workflow 1: Initial System Build (First Time)

1. Run `/init` → wait for completion (~15 min)
2. Open [CLAUDE.md](CLAUDE.md) → fill in Niche, Offer, Price
3. Run `/next` → execute Phase 3
4. Run `/next` → execute Phase 4
5. Run `/next` → execute Phase 5
6. Run `/next` → execute Phase 6
7. System complete → start daily operations

**Time:** 1-2 hours total

### Workflow 2: Daily Operations (System Complete)

1. Open `/daily/QUICK-REFERENCE.md`
2. Follow morning block checklist (30-45 min)
3. Follow mid-morning block checklist (30-45 min)
4. Execute client fulfillment (afternoon)
5. Update [CLAUDE.md](CLAUDE.md) Current State (end of day)

**Time:** 2-4 hours/day

### Workflow 3: Create New Asset (Need Template)

1. Open `/system/prompt-generator.html` in browser
2. Click "Refresh State"
3. Select category (e.g., "Sales Assets")
4. Click "Generate Prompt"
5. Copy prompt → paste into Claude Code
6. Execute → new asset created

**Time:** 5-10 minutes

### Workflow 4: Resume After Break (Days/Weeks Off)

1. Open Claude Code in this directory
2. Run: `/next`
3. System tells you where you left off
4. Continue from there

**Time:** Instant orientation

---

## Success Metrics

### System Build Phase (Phase 1-6)

✅ **System is ready when:**
- All 6 phases show "Complete" in CLAUDE.md
- `/validate` command shows all checks passing
- Prompt generator loads and generates valid prompts
- You can follow `/daily/QUICK-REFERENCE.md` without confusion

### Business Operations Phase (After Phase 6)

✅ **System is working when:**
- You can execute daily operations mechanically (no strategic thinking)
- Hand raiser posts generate engagement
- Video→Client conversion > 10%
- Clients are getting delivered service on time
- You're acquiring new clients weekly

---

## Next Steps

**If system is not yet built:**
1. Run: `/init`
2. Configure business in CLAUDE.md
3. Run: `/next` repeatedly until Phase 6 complete

**If system is built but not configured:**
1. Open CLAUDE.md
2. Fill in Niche, Offer Promise, Price Point
3. Save and start daily operations

**If system is built and configured:**
1. Open `/daily/QUICK-REFERENCE.md`
2. Execute morning block
3. Execute mid-morning block
4. Fulfill client work
5. Update state at end of day

**If you're stuck:**
1. Run: `/next`
2. Or read the current phase file directly
3. Or run: `/validate` to check completion

---

**Questions?** Run `/next` - the system guides you.
