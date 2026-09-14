# brief/ — rendered daily briefs

- `YYYY-MM-DD.html` — one self-contained page per weekday (open directly in any browser).
- `index.html` — overview: brief list, cumulative opportunities board, positions board, institutions.
- `sources.yaml` — the watchlist the sweep follows (edit freely). `config.yaml` — human-owned account settings.

Regenerate locally: `python3 scripts/prices.py && python3 scripts/render_brief.py`.
The cloud routine `daily-us-brief` runs `.claude/skills/daily-brief/SKILL.md` weekdays 07:00 America/Toronto
and pushes to `main`; pull (`git pull`, or the Obsidian Git plugin) to see new pages in Obsidian.
Wiki links in the HTML use `obsidian://` URLs and open the page in the `My_Wiki` vault.

## Local fallback (launchd)
The cloud routine's sandbox blocks direct HTTPS to sec.gov and the institution sites (verified 2026-09-13: only
WebSearch works there). Until that environment allows outbound network access, run the same skill on this Mac:

```bash
cp brief/launchd/com.mywiki.daily-brief.plist ~/Library/LaunchAgents/ && launchctl load ~/Library/LaunchAgents/com.mywiki.daily-brief.plist
```
Runs weekdays 07:00 local via `scripts/run_daily_brief_local.sh` (Claude Code headless, model opus, `caffeinate` keeps the Mac awake).
Logs: `logs/daily-brief-<date>.log`. Manual run: `scripts/run_daily_brief_local.sh`. Unload: `launchctl unload ~/Library/LaunchAgents/com.mywiki.daily-brief.plist`.

## GitHub Actions (recommended runner)
`.github/workflows/daily-brief.yml` runs the same skill on a GitHub-hosted runner (full outbound network, `GITHUB_TOKEN` can push
to `main`) weekdays 11:00 UTC, or on demand via **Actions → daily-us-brief → Run workflow**. One repository secret is required:
`CLAUDE_CODE_OAUTH_TOKEN` (run `claude setup-token` on your Mac and paste the token into Settings → Secrets → Actions) — or
`ANTHROPIC_API_KEY` for pay-per-token API billing. The rendered HTML is also attached to each run as an artifact.
