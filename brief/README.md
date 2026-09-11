# brief/ — rendered daily briefs

- `YYYY-MM-DD.html` — one self-contained page per weekday (open directly in any browser).
- `index.html` — overview: brief list, cumulative opportunities board, positions board, institutions.
- `sources.yaml` — the watchlist the sweep follows (edit freely). `config.yaml` — human-owned account settings.

Regenerate locally: `python3 scripts/prices.py && python3 scripts/render_brief.py`.
The cloud routine `daily-us-brief` runs `.claude/skills/daily-brief/SKILL.md` weekdays 07:00 America/Toronto
and pushes to `main`; pull (`git pull`, or the Obsidian Git plugin) to see new pages in Obsidian.
Wiki links in the HTML use `obsidian://` URLs and open the page in the `My_Wiki` vault.
