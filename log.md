---
type: log
---

# Log — Investment Wiki

Append-only, newest at the bottom. One entry per operation
(`ingest` · `query` · `lint` · `maintenance`). Grep the timeline with:

```
grep "^## \[" log.md | tail -5
```

---

## [2026-06-19] maintenance | Wiki initialized
- pages touched: [[CLAUDE]], [[index]], [[log]], [[overview]]
- note: Set up the schema, folder conventions, navigation files, and portfolio dashboard. Empty and ready for the first source.

## [2026-06-19] ingest | Quant Corner Ep. 47 — Does Momentum Still Work? (sample seed)
- raw: [[raw/2026-06-12-quant-corner-momentum]]
- pages touched: [[2026-06-12-quant-corner-momentum]], [[momentum-factor]], [[factor-investing]], [[mtum]], [[cliff-asness]], [[mtum-bull]], [[index]]
- stubs created (links only): [[value-factor]], [[momentum-crashes]], [[AQR]], [[dana-whitfield]]
- note: First ingest. Established baseline momentum claims (no contradictions yet). Flagged 2 data gaps on [[mtum]] (exact expense ratio, AUM/methodology) for a future lint/web-search. Position NOT created — momentum is not a real holding; proposing one to the human.

## [2026-06-19] maintenance | Removed momentum sample seed
- note: Per user request, deleted the illustrative momentum demo (raw + 6 wiki pages) and reset [[index]] to empty. Prior ingest entry above kept for history (append-only log). The MTUM watch position was never created (user declined).

## [2026-06-19] ingest | All-In Best Ideas Pitch Competition (4 picks) + fact-check
- raw: clipped via Obsidian Web Clipper (YouTube fO5sC7qS04E)
- pages touched (13): [[2026-06-12-all-in-best-ideas-pitch]], [[mgm]], [[tln]], [[akts]], [[geod]], [[aaron-cowen]], [[dan-dreyfus]], [[oleg-nodelman]], [[kyle-samani]], [[ai-power-demand]], [[radiopharmaceuticals]], [[depin]], [[all-in-best-ideas-2026-factcheck]] + [[index]]
- stubs created (links only): [[barry-diller]], [[all-in-podcast]], [[replacement-cost-investing]]
- fact-check: MGM ✅ (Diller $48.30 bid / 26.1% / Osaka 2030), TLN ✅ (~$382, AWS PPA, 2.2GW nuclear), AKTS ✅ (mostly — $318M IPO, Ac-225/nectin-4 Fast Track; "$100M Lilly" imprecise), GEOD ⚠️ revenue ~$5M actual vs ~$11M pitched (~2x overstated) + token net-inflationary + disclosed Multicoin conflict.
- ⚠️ contradiction flagged: [[geod]] pitched revenue vs reported. No positions created (none are real holdings).
