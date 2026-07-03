# Erotetics — reasoning lenses for Claude Code

**Better questions, better thinking.** This is the
[Erotetic Arts](https://erotetics.com) methodology for improving reasoning
under uncertainty, packaged as a Claude Code plugin: surface the hidden
assumptions behind a decision, strategy, or claim — and reframe to the
question that actually needs settling.

## Install

```
/plugin marketplace add erotetics/claude-plugins
/plugin install erotetics@erotetics
```

## Use

```
/erotetics:assumptions                       # analyse the content in context
/erotetics:assumptions <paste or describe>   # analyse a specific claim/plan
```

Point it at anything — a strategy memo, a pitch, a requirements doc, a PR
description, an article, a web capture. It runs the four-step erotetic method:

1. **Surface** — name what is taken for granted: factual givens, smuggled
   definitions, assumed causal links, the question the content is silently
   answering, success criteria, actor incentives, what must *remain* true.
2. **Examine** — separate load-bearing assumptions (what breaks if false?)
   from decorative ones, with an honest evidence status for each.
3. **Challenge** — the strongest honest counter-case for the few that matter,
   and the cheapest test that would settle each.
4. **Reframe** — converge on the question that can actually be decided.

The output is not more analysis — it is clearer closure.

## Example output

From a real run against: *"We should rewrite our backend in Rust because it
will make the product faster and help us attract better engineers."* —
[full output here](docs/example-rust-rewrite.md). The shape of the close:

> **The question to settle:** *What does profiling say is the cheapest way to
> hit our (yet-to-be-defined) performance target — and does that evidence
> point at our backend's CPU at all?* Until that's answered, the Rust rewrite
> is a solution with no confirmed problem attached.

## Evals — including the negative result

This plugin ships with eval cases and rubrics (`plugins/erotetics/evals/`),
and we publish what they found: on 2026 frontier models the lens adds **no
measurable content lift** — Claude already reasons well about assumptions —
but discriminates **4/4 vs 0/4 on artifact form**: the canonical skeleton,
the load-bearing/evidence table, the decorative dismissal, and the single
settling question appear only with the lens. What you're installing is
consistency and closure, not borrowed intelligence. A second round on
fresh, planted-assumption cases exposed a coverage cost of convergence
(21/30 vs baseline 23/30); v0.2's fix — enumerate what you dismiss —
restored parity at 23/30 with the artifact form intact, and now beats the
bare model on the most unfamiliar domain tested. Full data and known
ceilings in [the evals README](plugins/erotetics/evals/README.md). We think naming that distinction
matters more than a benchmark win; questioning our own answers is literally
the methodology.

## Why

Most bad decisions are answers to the wrong question. The expensive failures
hide in what everyone took for granted — named too late, if ever. Naming the
presuppositions early, so they can be challenged before they become expensive
surprises, is the whole practice. Read more at
[erotetics.com](https://erotetics.com).

## About

Built and maintained by [Erotetic Arts Ltd](https://erotetics.com) — a studio
applying structured inquiry to strategy, operations, and AI systems.
Questions: hello@erotetics.com

MIT licensed. More lenses will land here as they earn their place.
