# Evals — and what they honestly found

Cases live in `<case>/prompt.md` with two rubrics each in `<case>/graders/`:
`rubric.md` (content: did the analysis catch what matters?) and `form.md`
(artifact: is the output a consistent decision document?). They are written
for `claude plugin eval` (early access as of July 2026); until that ships
broadly, the manual protocol below reproduces the ablation.

## Manual ablation protocol

1. `claude plugin disable erotetics@erotetics` → run each `prompt.md` via
   `claude -p` → baseline arm.
2. Re-enable, run again (the skill auto-invokes on these natural prompts) →
   with-lens arm.
3. Grade both arms against both rubrics (`claude -p --model haiku` with the
   rubric + response; or apply `form.md` by inspection — its criteria are
   mechanical).

## Findings (July 2026, three-run ablation on the rust-rewrite case)

**Content rubric: saturated — no measurable lift.** Frontier Claude scored
6/6 with the lens, without the lens, and even on a lazy one-word-question
prompt. The model has internalised this genre of analysis; we publish that
result rather than hide it.

**Form rubric: full discrimination.** With-lens 4/4 on the mechanical form
criteria (canonical skeleton, examine table with evidence status, explicit
decorative dismissal, single settling question); both baselines 0/4 —
well-reasoned *essays*, differently shaped every run.

**Honest positioning, therefore:** on strong 2026 models this lens does not
make Claude smarter about assumptions — it makes the output a *standardised,
comparable, skimmable decision artifact*, produced identically every time,
triggered even by lazy phrasing (the skill auto-invokes on natural "check
this plan" requests). Consistency of form, zero prompt-craft, and a
convergent close are the product. That is what the erotetic method promises:
not more analysis — clearer closure.

## Round 2 — planted-assumption recall (fresh domains)

Three non-folklore cases (`planted-*/`), each with 10 assumptions embedded by
design (`key.txt`), several subtle: a hidden technical killer (Postgres has no
native TTL), an adversarial actor (submission-farming fraud), a transfer trap
(Google's monorepo needs Google's tooling). Grading = strict recall against
the key, both arms, same lazy prompt.

**Result: baseline 23/30, lens 21/30.** No content lift on fresh domains, and
mildly negative — with an instructive split: the lens *won* the case where an
actor-incentive plant needed the category sweep (it alone caught the fraud
vector), and *lost* where its top-walls-only convergence discarded plants a
free essay had simply enumerated (failure coupling, marginal ops cost,
onboarding impact).

**The finding behind the finding: form and closure cost coverage.** The lens
is a decision-focuser; recall punishes curation. v0.2 addresses the honest
part of that trade: the EXAMINE step now requires an exhaustive one-line
"noted, not load-bearing" enumeration instead of a silent discard — keep the
focus, stop paying for it with blindness. (Re-measurement pending.)

*Caveats, stated plainly: n=1 per arm per case; single LLM judge pass; cases
and keys authored with the same model family that generated the answers —
keys are published for human audit. Directional conclusions only.*
