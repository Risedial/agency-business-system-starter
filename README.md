# Agency Business System

> A complete, self-sustaining agency operating system for running a phoneless, meetingless business through mechanical daily execution.

## Overview

The Agency Business System is a comprehensive workspace that combines proven methodologies into a complete operating system for service-based businesses. No cold outreach. No sales calls. No client meetings. Just templated execution and consistent results.

### Core Methodology

1. **Hand-Raiser Lead Generation** - Qualified leads through social posts (zero cold outreach)
2. **Async Video Sales** - Close clients via 5-minute videos (zero sales calls)
3. **No-Meeting Fulfillment** - Deliver services via async communication (zero client meetings)
4. **Mechanical Daily Operations** - Execute through checklists (zero strategic improvisation)

**Validated Results:** 800+ clients closed without a single phone conversation (Frankie Fihn, Beyond The Agency Box)

---

## Quick Start

### First Time Setup

1. **Clone and open** this repository in Claude Code
2. **Read** [SESSION-START.md](SESSION-START.md) for detailed setup instructions
3. **Run** `/init` slash command to bootstrap the system
4. **Configure** your business (Niche, Offer Promise, Price Point in CLAUDE.md)
5. **Run** `/next` to see what to do based on your current state

### Daily Operations (After Setup)

1. Open Claude Code in this directory (CLAUDE.md auto-loads)
2. Run `/next` to see your next action
3. Follow `/daily/QUICK-REFERENCE.md` for daily checklist
4. Use `/system/prompt-generator.html` for any prompt needs

---

## System Components

### 📚 Documentation (`/docs`)

Complete methodology documentation:
- Research findings from proven frameworks
- Offer construction framework
- Hand raiser lead generation system
- 5-part async video sales structure
- Text-based closing sequences
- No-meeting fulfillment model
- Scaling & hiring framework

### 🎯 Ready-to-Use Assets (`/assets`)

8+ fill-in-the-blank templates:
- Hand raiser post variations (10+ templates)
- 5-minute video sales script
- Video message wrappers
- Follow-up sequences (24h/48h/72h/1wk)
- Objection response scripts
- Client onboarding template
- Weekly update Loom scripts
- Deliverable handoff process

### 📅 Daily Operations (`/daily`)

Mechanical execution SOPs:
- Complete daily operations manual (4 time blocks)
- Quick reference card (one-page checklist)
- Pipeline tracker (prospects & clients)

### 🤖 Automation & Tools (`/system`)

- **STATE.json** - Automatic state tracking
- **prompt-generator.html** - Self-contained React app for generating prompts
- **update-state.py** - Hook for auto-syncing workspace state

---

## Business Model Summary

### Lead Generation (30-45 min/day)
- Build 100 targeted connections in your niche
- Post 1x daily asking "who needs [specific outcome]?"
- Engaged commenters = qualified leads
- **Validation signal:** 3+ engaged prospects = offer validated

### Sales (30-45 min/day)
- Send 5-minute video to all hand raisers
- 5-part structure: Hook → Outcome Demo → Price → Differentiation → Purchase Instructions
- Follow-up sequence: 24h, 48h, 72h, 1-week
- **Target conversion:** >10% video→client

### Fulfillment (Variable)
- Weekly 3-5 minute Loom progress updates
- Text communication for questions/issues
- Deliverable handoffs via Loom walkthrough
- **Zero meetings** - positioned as client benefit

### Operations (15 min/day)
- Update pipeline tracker
- Sync workspace state
- Prep tomorrow's priorities
- **Zero improvisation** - 100% templated

---

## Key Features

### ✅ Automated State Tracking
- STATE.json auto-updates via hooks
- Prompt generator reads current state
- Fresh sessions resume instantly

### ✅ Slash Commands
- `/init` - Bootstrap entire system
- `/next` - What to do based on current state
- `/validate` - Check phase completion

### ✅ Phase-Based Build System
6 phases from research to completion:
1. Research & Documentation
2. Workspace Foundation
3. Prompt Generator Tool
4. Initial Assets
5. Daily Operations Setup
6. System Validation

### ✅ Zero-Ambiguity Execution
- All recurring tasks templated
- Fill-in-the-blank format
- VA-ready from day one
- No strategic thinking required

---

## Project Structure

```
/
├── CLAUDE.md                   # Workspace context (auto-loads)
├── SESSION-START.md            # User guide
├── README.md                   # This file
├── .claude/
│   ├── settings.json           # Hook configuration
│   ├── hooks/
│   │   └── update-state.py     # Auto state sync
│   ├── commands/
│   │   ├── init.md             # Bootstrap system
│   │   ├── next.md             # Next action recommender
│   │   └── validate.md         # Validation checks
│   └── rules/
│       ├── phase-*.md          # 6 phase instructions
│       └── reference/          # Methodology details
├── docs/                       # Framework documentation (9 files)
├── assets/                     # Template library (8+ files)
├── daily/                      # Daily operations SOPs (3 files)
└── system/
    ├── STATE.json              # Current workspace state
    └── prompt-generator.html   # Self-contained prompt tool
```

---

## Methodology Sources

This system synthesizes proven frameworks:

- **Beyond The Agency Box** by Frankie Fihn - Phoneless/meetingless agency model
- **Hand Raiser Lead Generation** - Self-selection psychology, 2026 social dynamics
- **Async Video Sales System** - 5-part video structure, no-call closing
- **2026 Agency Best Practices** - Async-first fulfillment, social listening

Detailed methodology available in [.claude/rules/reference/](.claude/rules/reference/)

---

## Key Metrics Dashboard

**Lead Generation:**
- Target: 100 connections before posting
- Frequency: 1 post/day
- Validation: 3+ engaged prospects across 3 posts

**Sales:**
- Video length: 4-5 minutes
- Response time: Within 4 hours
- Target conversion: >10% video→client

**Scaling:**
- 5 clients: Consider hiring
- 10 clients: Hiring mandatory

---

## Requirements

### Software
- **Claude Code CLI** (for automated execution)
- **Python 3.x** (for state sync hooks)
- **Modern web browser** (for prompt generator)

### Skills
- Basic markdown editing
- Social media platform access (LinkedIn or Facebook)
- Loom account (for video recording)
- Stripe account (for payments)

---

## Current Status

✅ **Complete** - All 6 phases validated and ready for use

**What's Included:**
- 30+ files created and validated
- Complete methodology documentation
- Ready-to-use templates for all operations
- Automated state tracking
- Functional prompt generator
- Daily operational SOPs

**Ready For:**
- Daily business operations
- Hand raiser lead generation
- Async video sales
- Client fulfillment
- Scaling to 10+ clients

---

## Usage Example

### Day 1: Network Building
```bash
# Open workspace
cd AUTO-CLAUDE_GOALS

# Check what to do
/next
# Output: "Build your network: Add 20-30 targeted connections"

# Follow morning checklist
# - Search "[Job Title] + [Location]"
# - Send 20-30 connection requests
# - Update CLAUDE.md metrics
```

### Day 5: Start Posting
```bash
/next
# Output: "Post hand raiser content (you have 100 connections)"

# Use assets/hand-raiser-posts.md
# Select template, fill in blanks
# Post to LinkedIn/Facebook
# Track engagement
```

### Day 7: Send First Video
```bash
# Got 3 comments on post
# Use assets/video-script-template.md
# Record 5-min Loom
# Send within 4 hours
# Execute follow-up sequence
```

---

## Support & Troubleshooting

### Lost Context?
- Run `/next` - tells you exactly what to do
- Read [SESSION-START.md](SESSION-START.md) - complete user guide
- Open current phase file in `.claude/rules/`

### State Issues?
- Run hook manually: `python .claude/hooks/update-state.py`
- Check STATE.json is valid JSON
- CLAUDE.md is source of truth

### Execution Issues?
- Run `/validate` - checks if current phase is complete
- Consult `/daily/QUICK-REFERENCE.md` - one-page checklist
- Use `/system/prompt-generator.html` - generates task-specific prompts

---

## Philosophy

### Simplicity Scales
- Template-driven execution (VA-ready)
- Async communication (global reach)
- Mechanical operations (predictable results)

### Self-Selection > Persuasion
- Hand raiser posts (high intent, low resistance)
- Async video (self-qualify on their timeline)
- Clear yes/no (fast decision, no back-and-forth)

### Async > Sync
- No timezone limitations
- Scales indefinitely
- Complete documentation
- Client preference (modern buyers are busy)

---

## Contributing

This system is designed for personal use. If you find improvements or have suggestions:

1. Fork the repository
2. Create a feature branch
3. Document your changes clearly
4. Submit a pull request with detailed explanation

---

## License

This project synthesizes publicly available methodologies and best practices. Use freely for your own business operations.

**Attribution appreciated but not required.**

---

## Acknowledgments

- **Frankie Fihn** - Beyond The Agency Box methodology
- **Hand Raiser Lead Gen Community** - Self-selection psychology
- **Claude Code Team** - Workspace automation infrastructure

---

## Version

**System Version:** 1.0 Complete
**Last Updated:** 2026-02-01
**Build Time:** ~1-2 hours (automated via `/init`)
**Daily Operating Time:** 2-4 hours/day + fulfillment

---

**Ready to build a phoneless, meetingless agency?**

Start with `/init` and let the system guide you through the rest.
