#!/usr/bin/env python3
"""
Automatic state synchronization for Agency Business System workspace.
Reads CLAUDE.md "Current State" section and writes to STATE.json.
"""

import os
import json
import sys
import re
from datetime import datetime
from pathlib import Path


def extract_state_from_claude_md(project_dir):
    """Extract state information from CLAUDE.md Current State section."""
    claude_md = project_dir / 'CLAUDE.md'

    # Default state
    state = {
        "lastUpdated": datetime.utcnow().isoformat() + "Z",
        "currentPhase": "Not Started",
        "niche": "",
        "offerPromise": "",
        "pricePoint": "",
        "metrics": {
            "connectionsBuilt": 0,
            "postsPublished": 0,
            "videosSent": 0,
            "clientsAcquired": 0,
            "offerValidated": False
        },
        "assetsCreated": [],
        "currentBlockers": []
    }

    if not claude_md.exists():
        return state

    try:
        content = claude_md.read_text(encoding='utf-8')

        # Find Current State section
        current_state_pattern = r'## Current State\s*\n(.*?)(?=\n##|\Z)'
        match = re.search(current_state_pattern, content, re.DOTALL)

        if not match:
            return state

        current_state_text = match.group(1)

        # Extract phase
        phase_match = re.search(r'\*\*Phase:\*\*\s*(.+)', current_state_text)
        if phase_match:
            state["currentPhase"] = phase_match.group(1).strip()

        # Extract niche
        niche_match = re.search(r'\*\*Niche:\*\*\s*(.+)', current_state_text)
        if niche_match:
            niche_text = niche_match.group(1).strip()
            if not niche_text.startswith('('):  # Ignore template text
                state["niche"] = niche_text

        # Extract offer promise
        offer_match = re.search(r'\*\*Offer Promise:\*\*\s*(.+)', current_state_text)
        if offer_match:
            offer_text = offer_match.group(1).strip()
            if not offer_text.startswith('('):
                state["offerPromise"] = offer_text

        # Extract price point
        price_match = re.search(r'\*\*Price Point:\*\*\s*(.+)', current_state_text)
        if price_match:
            price_text = price_match.group(1).strip()
            if not price_text.startswith('('):
                state["pricePoint"] = price_text

        # Extract metrics
        connections_match = re.search(r'Connections Built:\s*(\d+)', current_state_text)
        if connections_match:
            state["metrics"]["connectionsBuilt"] = int(connections_match.group(1))

        posts_match = re.search(r'Posts Published:\s*(\d+)', current_state_text)
        if posts_match:
            state["metrics"]["postsPublished"] = int(posts_match.group(1))

        videos_match = re.search(r'Videos Sent:\s*(\d+)', current_state_text)
        if videos_match:
            state["metrics"]["videosSent"] = int(videos_match.group(1))

        clients_match = re.search(r'Clients Acquired:\s*(\d+)', current_state_text)
        if clients_match:
            state["metrics"]["clientsAcquired"] = int(clients_match.group(1))

        validated_match = re.search(r'Offer Validated:\s*(Yes|No)', current_state_text)
        if validated_match:
            state["metrics"]["offerValidated"] = (validated_match.group(1) == "Yes")

        # Extract assets created
        assets_match = re.search(r'\*\*Assets Created:\*\*\s*\n(.*?)(?=\n\*\*|\Z)', current_state_text, re.DOTALL)
        if assets_match:
            assets_text = assets_match.group(1).strip()
            if assets_text and assets_text.lower() != "none yet":
                # Parse list items
                assets_list = [line.strip('- ').strip() for line in assets_text.split('\n') if line.strip().startswith('-')]
                state["assetsCreated"] = assets_list

        # Extract blockers
        blockers_match = re.search(r'\*\*Current Blockers:\*\*\s*\n(.*?)(?=\n\*\*|\n\n##|\Z)', current_state_text, re.DOTALL)
        if blockers_match:
            blockers_text = blockers_match.group(1).strip()
            if blockers_text and blockers_text.lower() != "none":
                # Parse list items
                blockers_list = [line.strip('- ').strip() for line in blockers_text.split('\n') if line.strip().startswith('-')]
                state["currentBlockers"] = blockers_list

    except Exception as e:
        print(f"Error extracting state from CLAUDE.md: {e}", file=sys.stderr)

    return state


def write_state_json(state, state_file):
    """Write state to STATE.json atomically."""
    tmp_file = state_file.with_suffix('.json.tmp')

    try:
        # Write to temporary file
        with open(tmp_file, 'w', encoding='utf-8') as f:
            json.dump(state, f, indent=2)

        # Atomic rename
        tmp_file.replace(state_file)
        return True

    except Exception as e:
        print(f"Error writing STATE.json: {e}", file=sys.stderr)
        if tmp_file.exists():
            tmp_file.unlink()
        return False


def main():
    """Main execution function."""
    try:
        project_dir = Path(os.environ.get('CLAUDE_PROJECT_DIR', '.'))
        state_file = project_dir / 'system' / 'STATE.json'

        # Ensure system directory exists
        state_file.parent.mkdir(parents=True, exist_ok=True)

        # Extract state from CLAUDE.md
        state = extract_state_from_claude_md(project_dir)

        # Write to STATE.json
        write_state_json(state, state_file)

        # Always exit 0 to avoid blocking Claude Code
        sys.exit(0)

    except Exception as e:
        print(f"State update error: {e}", file=sys.stderr)
        sys.exit(0)  # Exit 0 even on error to avoid blocking


if __name__ == '__main__':
    main()
