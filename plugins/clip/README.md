# Clip for Claude Code

See a problem in the browser, click **Clip**, and keep talking to Claude: the
page is already in your session — scroll screenshots, the CSS selector of every
visible element, console and network errors, contrast/a11y findings, Core Web
Vitals, and your note.

## Install

Needs [uv](https://docs.astral.sh/uv/getting-started/installation/) on your
`PATH` and the **Clip** browser extension (install link on request while the
store listing is unlisted — hello@erotetics.com).

```
/plugin marketplace add erotetics/claude-plugins
/plugin install clip@erotetics
```

In the extension: **Options → Capture mode → AI agent (MCP)**.

## What you get

- **MCP server** ([clip-bridge](https://github.com/erotetics/clip-bridge)),
  launched by Claude Code for each session — nothing to install as a service.
  Tools: `get_latest_capture` (summary + screenshots), `list_recent_captures`.
- **Auto-attach hook**: after you clip, your next message carries the clip's
  URL, note, errors and selectors automatically — no "pull my capture" needed.
  It fires once per clip and does nothing when no clip is waiting.

Clips are saved to `~/.clip-bridge/captures/`. Nothing leaves your machine.

## Options (environment variables)

| Variable | Effect |
|---|---|
| `CLIP_PUNCHLIST=1` | the agent also logs each clip to `PUNCHLIST.md` in your project |
| `CLIP_AUTO_ANSWER=1` | a clip sent with a question is answered on the page by a headless `claude -p` (uses your Claude usage) |
| `CLIP_HOME` | where clips are saved (default `~/.clip-bridge`) |

**Clip before opening Claude Code?** The bridge only listens while a session is
open. For always-on capture, run clip-bridge as a service — see its
[README](https://github.com/erotetics/clip-bridge#always-on-service-optional-one-command-always-running).
