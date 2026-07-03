# Assumption analysis: "We should rewrite our backend in Rust because it will make the product faster and help us attract better engineers."

## 1. SURFACE — what's taken for granted

**Factual givens**
- A1. The product is currently too slow, and users notice or care ("make the product **faster**" presumes speed is a felt problem).
- A2. The backend is the bottleneck — not the database, network, frontend, or architecture.
- A3. Rust-curious engineers are "better engineers" and are meaningfully attracted by stack choice.

**Causal links**
- A4. Rewriting in Rust → faster product. (Language speed ≠ product speed; most latency lives in I/O, queries, and design.)
- A5. Adopting Rust → attracting better engineers → better product outcomes. Two hops, both assumed.

**Smuggled definitions**
- A6. "Faster" — undefined. p99 latency? Throughput? Time-to-interactive? Cost per request?
- A7. "Better engineers" — undefined, and conflates language enthusiasm with engineering quality.

**The question behind the answer**
- A8. The claim answers "which language should our backend be in?" — but the felt problems (performance, hiring) may not be language problems at all. The rewrite is an answer looking for its question.

**Actors & incentives**
- A9. The current team can and wants to become productive in Rust; nobody critical leaves during a multi-quarter rewrite.
- A10. The business can afford a feature freeze or slowdown while the rewrite happens.

**Temporal load**
- A11. Requirements stay stable enough that the rewrite doesn't chase a moving target (the classic second-system failure).
- A12. Rust's hiring-market halo persists for the years the codebase will live.

## 2. EXAMINE — load-bearing walls

| Assumption | Load-bearing? (what breaks if false) | Evidence status |
|---|---|---|
| A2. Backend compute is the bottleneck | **Yes** — if latency is in DB/network/design, Rust buys ~nothing | Merely assumed; no profiling cited |
| A4. Rewrite → faster product | **Yes** — the entire first justification | Merely assumed |
| A10. Business survives the rewrite cost | **Yes** — rewrites routinely take 2–3× estimates; feature velocity drops to ~zero | Merely assumed |
| A3/A5. Rust attracts better engineers who improve outcomes | **Yes** — half the justification | Merely assumed; weakly supported folk claim |
| A9. Team can/will ramp on Rust | Moderate — mitigable by hiring, but slows everything | Merely assumed |
| A6. "Faster" definition | Prerequisite — can't verify A4 without it | Undefined |

**Decorative (safe to ignore):** A12 (hiring fashion drift is slow), A11 in isolation (it's really a component of A10's cost risk), and any debate about Rust's technical merits as a language — Rust being excellent is not in dispute and doesn't settle whether *this rewrite* is justified.

## 3. CHALLENGE — the strongest counter-cases

**A2/A4 — "Rust will make the product faster"**
- *Best case it's false:* In most web backends, >80% of request time is database queries, external calls, and serialization — workloads where Go/Java/Python-with-caching perform within noise of Rust. Rewriting the language layer optimizes the 15% while paying 100% of the cost. Meanwhile, targeted fixes (query optimization, caching, hot-path extraction) capture most of the gain for ~5% of the effort.
- *Settling evidence:* A profile of production traffic showing where p95/p99 time actually goes.
- *Cheapest test:* One week of APM/flame-graph profiling on the current system. If CPU-in-app-code is a minority of request time, A4 is dead. Second-cheapest: rewrite **one** proven-hot service in Rust and measure end-to-end user-visible improvement.

**A10 — "We can afford the rewrite"**
- *Best case it's false:* Full rewrites are among the best-documented failure modes in software (Netscape being the canonical corpse). The old system keeps changing while you rewrite it; parity takes years; competitors ship. The realistic comparison isn't "Rust backend vs. current backend" but "Rust backend in 18 months vs. current backend plus 18 months of features and targeted optimization."
- *Settling evidence:* An honest parity inventory (endpoints, edge cases, integrations) with a bottom-up estimate, times the historical estimate-overrun factor.
- *Cheapest test:* Estimate the parity surface for the single hairiest existing service. If that one service alone looks like a quarter, extrapolate and decide with open eyes. The strangler-fig alternative (incrementally extract hot services) prices this risk continuously instead of betting it all upfront.

**A3/A5 — "It will attract better engineers"**
- *Best case it's false:* Strong engineers choose problems, compensation, autonomy, and team quality far more than stack. A "Rust for hiring" pitch also selects for stack-motivated candidates, who churn when the next fashionable language arrives. And the near-term effect is negative: your *current* engineers must ship in a language they don't know.
- *Settling evidence:* Your own funnel data — where past strong hires actually came from and what they cited; recruiter feedback on whether stack is a stated blocker.
- *Cheapest test:* Ask the last 10 strong candidates (hired or lost) whether backend language influenced their decision. Days, not quarters.

## 4. REFRAME

The stated question — "should we rewrite in Rust?" — bundles two unrelated problems (performance, hiring) into one dramatic solution. Unbundled, each becomes decidable:

- **Reframe 1 (performance):** "Where does our production latency/cost actually go, and what is the cheapest intervention that gets us to our target — measured against a defined target (e.g., p99 < X ms)?" Settled by one profiling sprint. Only if the answer is "CPU in our own backend code, irreducibly" does Rust re-enter — and then as a strangler-fig extraction of that hot path, not a rewrite.
- **Reframe 2 (hiring):** "What do the engineers we want actually weigh when choosing us, and where do we lose them?" Settled by funnel data and candidate interviews, not by a rewrite.

**The question to settle:** *What does profiling say is the cheapest way to hit our (yet-to-be-defined) performance target — and does that evidence point at our backend's CPU at all?* Until that's answered, the Rust rewrite is a solution with no confirmed problem attached.
