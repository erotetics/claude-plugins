#!/usr/bin/env python3
"""UserPromptSubmit hook — auto-attach a freshly clipped page into the session.

On each prompt it asks the bridge whether a new clip arrived; if so, it injects
the clip's metadata as additional context so the live session sees it *without*
the user mentioning it. The bridge returns a fresh clip only once, so this fires
on the first prompt after a clip, not every turn. Bridge down / no clip → no-op.
Set CLIP_PUNCHLIST=1 to also have the agent log each clip to PUNCHLIST.md.
"""

import json
import os
import sys
import urllib.request

BRIDGE = "http://127.0.0.1:7777/pending"


def main() -> None:
    try:
        with urllib.request.urlopen(BRIDGE, timeout=2) as r:
            d = json.load(r)
    except Exception:
        sys.exit(0)  # bridge unreachable — stay invisible

    if not d.get("fresh"):
        sys.exit(0)

    lines = [
        "A page was just clipped in the browser and auto-attached for you to act on:",
        f"- url: {d.get('url')}",
        f"- title: {d.get('title')}",
    ]
    if d.get("note"):
        lines.append(f"- my note: {d['note']}")
    sel = d.get("selection")
    if sel:
        text = sel if isinstance(sel, str) else sel.get("text", "")
        lines.append(f'- my selected text (focus here): "{text}"')
        if isinstance(sel, dict) and sel.get("selector"):
            lines.append(f"  (lives in `{sel['selector']}`)")
    if d.get("dir"):
        lines.append(f"- saved to: {d['dir']} (read tileNN.png for full-res screenshots)")
    counts = d.get("audit_counts") or {}
    if counts:
        lines.append(
            "- audit findings: "
            + ", ".join(f"{v} {k}" for k, v in counts.items())
            + " — call get_latest_capture for details"
        )
    for c in d.get("console", []):
        lines.append(f"- issue: {c}")
    for e in (d.get("elements") or [])[:20]:
        lines.append(f"- element `{e.get('selector')}` — {str(e.get('text', ''))[:60]}")
    if d.get("tiles"):
        lines.append(
            f"- {d['tiles']} screenshot tile(s) available — call get_latest_capture to view them."
        )
    if os.environ.get("CLIP_PUNCHLIST") == "1":
        lines.append(
            "Action: review this clip and append a dated entry to PUNCHLIST.md "
            "(create it if missing): the issue(s) and the file or CSS selector to fix. "
            "Keep it terse."
        )
    else:
        lines.append("Treat this clip as context for my message.")

    print(
        json.dumps(
            {
                "hookSpecificOutput": {
                    "hookEventName": "UserPromptSubmit",
                    "additionalContext": "\n".join(lines),
                }
            }
        )
    )
    sys.exit(0)


if __name__ == "__main__":
    main()
