---
type: concept
category: model
aliases: [optimal mean-reversion exit, OU exit optimization, heat-potential trading rule]
tags: [quant, mean-reversion, ou-process, options-math, exit-rules]
created: 2026-08-01
updated: 2026-08-01
---

# OU-optimal exit rules (stop-loss / take-profit / horizon)

## Definition
A framework for choosing the **exit** side of a mean-reversion trade — not
when to enter, but where to set the take-profit level, the stop-loss level,
and the maximum holding time — to maximize the trade's Sharpe ratio, given
the spread follows a mean-reverting (Ornstein-Uhlenbeck) process. Introduced
by [[alexander-lipton]] and [[marcos-lopez-de-prado]]
([[2020-02-08-lipton-lopez-de-prado-ou-exit-rules]]).

**What it is *not*:** an entry-signal rule. Entry (e.g. "go long when the
spread is 2σ below its mean") is assumed as given; this framework only
optimizes what happens *after* you're in.

## How it works

### 1. Model the spread as an OU process
The spread $X_t$ is assumed to follow the standard Ornstein-Uhlenbeck SDE:

$$
dX_t = \kappa(\theta - X_t)\,dt + \sigma\,dW_t
$$

- $\theta$ — the long-run equilibrium level the spread reverts to
- $\kappa > 0$ — speed of mean reversion
- $\sigma$ — volatility of the noise
- $W_t$ — a standard Brownian motion

This is the same object [[replacement-cost-investing|cointegrated-pair]]
half-life estimation already relies on: half-life $= \ln 2 / \kappa$.

### 2. Estimate the parameters from data
Discretizing and rearranging gives a simple linear regression: regress the
change in the spread on its lagged level,

$$
X_t - X_{t-1} = \kappa(\theta - X_{t-1})\,\Delta t + \sigma\sqrt{\Delta t}\,\varepsilon_t,
\qquad \varepsilon_t \sim \mathcal{N}(0,1)
$$

An OLS fit of $\Delta X_t$ on $X_{t-1}$ recovers $\hat\kappa$ (from the
slope) and $\hat\theta$; the residual standard deviation gives $\hat\sigma$.
This is the *same* OLS estimation the statarb toolkit's cointegration/half-life
tests are already built on — this framework is the natural next step once a
pair passes cointegration, not a replacement for it.

### 3. Define the exit rule
A trading rule is a triple $R = \{\underline\pi, \bar\pi, T\}$: a stop-loss
level $\underline\pi < 0$, a take-profit level $\bar\pi > 0$, and a maximum
holding time $T$. Exit at the **first** of three events:

$$
\iota = \inf\{\, t : \pi_t \geq \bar\pi \ \text{ or } \ \pi_t \leq \underline\pi \ \text{ or } \ t = T \,\}
$$

where $\pi_t$ is the mark-to-market P&L of the position at time $t$. This is
a standard double-barrier-plus-horizon stopping rule — the same structural
idea used across the broader first-passage-time trading literature (Bertram,
Elliott et al., and others the paper builds on), not unique to this paper.

### 4. Maximize the Sharpe ratio over the exit levels
The objective is the Sharpe ratio of the trade's terminal, per-period P&L:

$$
SR(\underline\pi, \bar\pi, T) \;=\;
\frac{\mathbb{E}\!\left[\pi_\iota / \iota\right]}
{\sqrt{\mathbb{E}\!\left[\pi_\iota^2/\iota^2\right] - \big(\mathbb{E}[\pi_\iota/\iota]\big)^2}}
$$

$$
(\underline\pi^{*}, \bar\pi^{*}) \;=\; \arg\max_{\underline\pi < 0 < \bar\pi} \; SR(\underline\pi, \bar\pi, T)
$$

**Why this is hard to compute:** $\mathbb{E}[\pi_\iota/\iota]$ and
$\mathbb{E}[\pi_\iota^2/\iota^2]$ are expectations of an OU process stopped
at a random first-passage time — getting them requires solving a
boundary-value problem in the same mathematical family as the heat
(diffusion) equation. Prior work either (a) estimated $SR$ by Monte Carlo
simulation (slow, noisy, no formula), or (b) solved it analytically only for
a **perpetual** strategy (no time limit — mathematically convenient but
unrealistic). This paper's contribution is a fast, semi-analytical solution
for a **finite** horizon $T$, using an integral-equation technique
("the method of heat potentials," borrowed from heat-conduction physics) —
the specific numerical machinery isn't reproduced here; see the paper.

## The headline practical finding
Across their numerical results, one clear, low-math takeaway emerges:
- **If you entered when the spread was already far from equilibrium**
  (strong mispricing) → don't set an early stop-loss or take-profit; hold to
  the max horizon. The reversion pull is strong enough that early exits cost
  more than they protect.
- **If the mispricing was weak or near-zero at entry** → a stop-loss isn't
  worth setting (losses are mostly noise around a near-fair level), but
  taking profits early *can* help, since there's little pull left to keep
  pushing the trade further your way.

## Pros / cons
- **Pro:** replaces round-number exit heuristics (e.g. "exit at 1σ, or after
  20 days" — the kind of rule used elsewhere in this wiki's own strategy
  tests) with a Sharpe-optimal rule derived from the pair's *own* estimated
  OU parameters.
- **Pro:** handles a realistic finite trading horizon, unlike older
  "perpetual strategy" analytical results.
- **Con — the precondition is everything:** this only means something if the
  spread genuinely IS a stationary OU process. Applying it to a
  non-cointegrated spread optimizes exits around an equilibrium that doesn't
  exist. Cointegration testing (ADF / CADF / Johansen) must come first — this
  is downstream tooling, not a substitute for it.
- **Con:** requires reliable OU parameter estimates; $\kappa$, $\theta$,
  $\sigma$ are themselves noisy statistical estimates, not known constants —
  the paper explicitly cautions that using these rules "with confidence"
  requires a highly reliable parameter estimation.

## Who uses it
[[alexander-lipton]] and [[marcos-lopez-de-prado]] — both quant researchers
also known for other mean-reversion/statistical-arbitrage and backtest-
rigor work (deflated Sharpe ratio, meta-labeling). Positioned as a tool for
liquidity providers (market makers) setting quote/exit levels, and for
statistical arbitrage traders optimizing execution of an already-identified
pairs trade.

## Related
**Tested, not just candidate:** applied to the [[bz-cl-pairs-trade|BZ/CL
(Brent/WTI) pair]], including a from-scratch implementation of the paper's
own Volterra/heat-potential numerical method (validated to ~0.1–0.6% against
the paper's own published Table 1 in two of three test cases). Result: it
**underperformed a plain Bollinger Band (rolling z-score) rule** on real
data. See [[bz-cl-pairs-trade]] for the full writeup and the best-supported
reasons why (objective mismatch between per-trade time-normalized Sharpe and
portfolio-level annualized Sharpe; frozen training-period parameters vs. a
rule that adapts daily).

## Sources
- [[2020-02-08-lipton-lopez-de-prado-ou-exit-rules]]
- [[bz-cl-pairs-trade]] — empirical test against real data
