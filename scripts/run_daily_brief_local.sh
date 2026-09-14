#!/bin/zsh
# Local fallback for the daily brief: runs the /daily-brief skill headlessly with Claude Code on this Mac.
# Used when the cloud routine cannot reach the open web (its egress proxy blocks sec.gov & co.).
# Install the launchd job with:  cp brief/launchd/com.mywiki.daily-brief.plist ~/Library/LaunchAgents/ && launchctl load ~/Library/LaunchAgents/com.mywiki.daily-brief.plist
set -euo pipefail
VAULT="${VAULT:-$HOME/Desktop/My_Wiki}"
MODEL="${MODEL:-opus}"
LOG="$VAULT/logs/daily-brief-$(date +%F).log"
export PATH="$HOME/.local/bin:/opt/homebrew/bin:/usr/local/bin:/usr/bin:/bin"
cd "$VAULT"
mkdir -p logs
{
  echo "=== daily-brief local run $(date '+%F %T %Z') model=$MODEL ==="
  git pull --rebase origin main || true
  # caffeinate keeps the Mac awake for the duration; -i = prevent idle sleep
  caffeinate -i claude -p \
    --model "$MODEL" \
    --permission-mode acceptEdits \
    --allowedTools "Bash,Read,Write,Edit,Glob,Grep,WebFetch,WebSearch" \
    "Run the daily-brief skill: read CLAUDE.md, then follow .claude/skills/daily-brief/SKILL.md step by step for today ($(date +%F)). Sweep brief/sources.yaml and new raw/ files, ingest with fact-check, run scripts/sec_fetch.py for the open positions and read the flagged filings, write wiki/briefs/$(date +%F).md and opportunities (with proposed edge/catalyst/invalidation), run scripts/prices.py and scripts/render_brief.py --date $(date +%F), update index.md and log.md, then commit as 'Daily brief $(date +%F): <headline>' and push to origin main (pull --rebase first if rejected). Never edit raw/, never change position numbers. Finish by printing the headline and pages touched."
  echo "=== exit $? at $(date '+%T') ==="
} >> "$LOG" 2>&1
