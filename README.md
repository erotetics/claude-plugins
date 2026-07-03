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
