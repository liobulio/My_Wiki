# brief/ — 每日美股机构简报

<!-- BRIEFS:START -->

## 每日简报（手机版）

手机上直接点日期即可阅读；网页版是同名 `.html`。

| 日期 | 头条 |
|---|---|
| [2026-09-14](2026-09-14.md) | 宏观天平明显倒向加息——8 月核心 CPI 环比 0.3% 超预期后，东海证券 称市场把 9/16 加息概率由 ~70% 推高至 80%+，国信多资产周报记录美债 10 年本周 +18BP 逼近 5%、黄金"脱敏"于利率 |
| [2026-09-11](2026-09-11.md) | 宏观分歧集中在 9 月 16 日 FOMC——Apollo 明确预期加息，大摩 称市场定价约 50/50，中银国际 反驳"单月非农不构成转向条件"；ECB 已于 9 月 10 日加息 25bp。行业主线仍是 AI 基建： |

<!-- BRIEFS:END -->

---

## 怎么看

- **手机**：直接点上面表格里的日期，GitHub 原生渲染 Markdown。仓库是私有的，只有你能看。
- **电脑**：同名 `.html` 是完整网页版（迷你图、机构徽章、可折叠原文），下载后用浏览器打开；
  `index.html` 是总览（历史简报、累积的机会看板、持仓看板）。
- **Obsidian**：`git pull` 后在 `wiki/briefs/` 看结构化原文，所有 `[[链接]]` 可跳转。

简报正文里的链接都指向 `wiki/` 下的实际页面（机构、来源、资产、论点），手机上可以一路点进去。

## 怎么跑

| | |
|---|---|
| 自动 | GitHub Actions `daily-us-brief`，工作日 11:00 UTC（= 多伦多 07:00 EDT；11 月改冬令时后需把 cron 改成 `0 12`） |
| 手动 | 仓库 Actions 页 → daily-us-brief → Run workflow（可填 `since` 日期补跑漏掉的天） |
| 本地 | `python3 scripts/prices.py && python3 scripts/render_brief.py`（只重新渲染，不抓新数据） |

流程写在 `.claude/skills/daily-brief/SKILL.md`，schema 在 `CLAUDE.md` §4.4。
巡查清单 `sources.yaml` 可随时增删机构；`config.yaml` 是你自己的账户设置，脚本不改它。

## 产出物

| 文件 | 是什么 |
|---|---|
| `YYYY-MM-DD.md` | 手机版（本目录，GitHub 直接渲染） |
| `YYYY-MM-DD.html` | 网页版，单文件自包含 |
| `index.html` | 总览页 |
| `../wiki/briefs/YYYY-MM-DD.md` | 结构化数据源（含 `brief-data` JSON 块） |
| `../wiki/sources/`、`institutions/`、`opportunities/` | 当天新增/更新的 wiki 页面 |

## 备选方案（未启用）

`launchd/com.mywiki.daily-brief.plist` + `../scripts/run_daily_brief_local.sh` 可在本机跑同一套流程
（工作日 07:00 本地时间，Claude Code headless，`caffeinate` 防休眠）。GitHub Actions 正常时不需要它。
安装：`cp brief/launchd/com.mywiki.daily-brief.plist ~/Library/LaunchAgents/ && launchctl load ~/Library/LaunchAgents/com.mywiki.daily-brief.plist`
