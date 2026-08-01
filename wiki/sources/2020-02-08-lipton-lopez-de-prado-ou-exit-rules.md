---
type: source
source_type: paper
title: "A Closed-Form Solution for Optimal Mean-Reverting Trading Strategies"
author: "[[alexander-lipton]], [[marcos-lopez-de-prado]]"
publisher: "SSRN (later: Risk Magazine; International Journal of Theoretical and Applied Finance)"
url: https://ssrn.com/abstract=3534445
published: 2020-02-08
ingested: 2026-08-01
raw: "raw/2020-02-08-lipton-lopez-de-prado-ou-exit-rules.md"
tags: [quant, mean-reversion, ou-process, options-math, pairs-trading]
---

# Lipton & López de Prado — Optimal Mean-Reverting Trading Strategies

Academic paper, first posted to SSRN 2020-02-08. Discovered while working
through the [[statarb-strategy-lab]] pairs-trading pipeline as the natural
next tool once a pair (WTI/Brent) actually passed cointegration — see
[[ou-optimal-exit-rules]] for the full concept writeup with equations.

## TL;DR
Given a mean-reverting spread modeled as an Ornstein-Uhlenbeck process,
the paper derives a fast, semi-analytical way to find the **Sharpe-optimal
exit rule** — the stop-loss level, take-profit level, and maximum holding
time that maximize a trade's Sharpe ratio. It replaces slower Monte Carlo
simulation and extends prior analytical work (which only handled an
unrealistic infinite/perpetual horizon) to a realistic finite horizon.

## Key takeaways
- **Entry is assumed, exit is solved.** The paper doesn't optimize when to
  enter a mean-reversion trade (e.g. "spread is 2σ from its mean") — only
  what to do once you're in.
- **The exit rule has three parts**: stop-loss, take-profit, and a max
  holding time; exit at whichever triggers first. See
  [[ou-optimal-exit-rules]] for the formal stopping-time definition.
- **Method:** "heat potentials" — a technique from heat-conduction physics
  — used to solve for the trade's expected P&L and its variance (and hence
  Sharpe) as a function of the chosen exit levels, without brute-force
  simulation. Validated against Monte Carlo in the paper (small, simulation-
  noise-level discrepancy).
- **Headline practical finding:** if you entered on strong mispricing, don't
  set early stops — ride to the horizon. If mispricing was weak or ~zero at
  entry, don't bother with a stop-loss, but early profit-taking can help.
- Also extends the framework to price jumps (not just smooth diffusion) and
  to linear transaction costs (which produce a "no-trade zone" around fair
  value, a standard result in the broader transaction-cost literature).
- Multi-asset (correlated basket) extension is explicitly left as future
  work, not solved in this paper.

## Notable claims (fact-checked)
- ✅ **Paper exists as described.** SSRN abstract 3534445, posted 2020-02-08,
  authors confirmed. — [SSRN](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=3534445)
- ✅ **Later formally published**, with a retitle: *"A Closed-Form Solution
  for Optimal Ornstein–Uhlenbeck-Driven Trading Strategies,"* International
  Journal of Theoretical and Applied Finance, vol. 23(8), article 2050056,
  accepted Dec 2020 / published Jan 2021, DOI
  [10.1142/S0219024920500569](https://www.worldscientific.com/doi/abs/10.1142/S0219024920500569).
  A shorter version also ran in Risk Magazine, vol. 33(7), 2020, under the
  original title. Companion arXiv preprint: 2003.10502 (Mar 2020).
- ✅ **Both authors' affiliations verified current-ish** (as of the fact-check
  date): Lipton — ADIA (Global Head of R&D), MIT Connection Science Fellow,
  Hebrew University of Jerusalem; López de Prado — Cornell (Professor of
  Practice), ADIA (Global Head of Quant R&D), founder of True Positive
  Technologies. See their [[alexander-lipton|person]] [[marcos-lopez-de-prado|pages]]
  for sources.
- ✅ **Award:** both authors won Risk.net's 2021 Buy-Side Quant of the Year,
  largely credited to this paper. — [Risk.net](https://www.risk.net/awards/7740186/buy-side-quant-of-the-year-alex-lipton-and-marcos-lopez-de-prado)

## Agrees / contradicts
No conflicts with existing wiki content — this is the first academic
methodology paper ingested (prior sources are podcasts/interviews). It
**extends** rather than contradicts the discipline already encoded in
[[statarb-strategy-lab]]'s SKILL.md (cointegration-first, don't trust
round-number exit heuristics) by offering a principled way to derive exit
levels *after* cointegration is established — it does not replace that
precondition.

## Entities mentioned
People: [[alexander-lipton]], [[marcos-lopez-de-prado]] · Concepts:
[[ou-optimal-exit-rules]]

## Data gaps / next steps
- The paper's own numerical results (Table 1, Figures 3-5) are parameterized
  in nondimensional units specific to their scaling — applying this to a
  real pair (e.g. WTI/Brent) requires converting the pair's estimated
  $(\kappa, \theta, \sigma)$ into those units first. Not yet done.
- No position/thesis implications — this is a methodology reference, not an
  asset-specific claim.
