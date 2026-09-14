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

- **手机（网页版，推荐）**：Cloudflare Pages 私有站点，书签 `<你的站点>/latest` 永远是最新一期
  （`_redirects` 每次渲染自动更新指向）。完整 HTML：迷你图、机构徽章、可折叠原文。配置见文末。
- **手机（Markdown 版，零配置）**：直接点上面表格里的日期，GitHub App 原生渲染。仓库是私有的，只有你能看。
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

---

## Cloudflare Pages 私有站点（一次性配置，约 10 分钟）

免费：Pages 免费版不限流量/请求、每月 500 次构建（我们每月约 20 次）；Zero Trust Access 免费版含 50 个用户，你只需 1 个。

**1. 建站**
1. 注册/登录 <https://dash.cloudflare.com> → 左侧 **Workers & Pages** → **Create** → **Pages** → **Connect to Git**
2. 授权 GitHub，**只勾选 `liobulio/My_Wiki` 这一个仓库**（私有仓可用，免费版支持）
3. 构建设置——三项都要改：

   | 字段 | 填什么 |
   |---|---|
   | Framework preset | **None** |
   | Build command | **留空** |
   | Build output directory | **`brief`** |

4. **Save and Deploy**。约 1 分钟后拿到 `xxx.pages.dev` 网址。

> ⚠️ 部署完成到你配好 Access 之间，这个网址是**公开可访问**的。先别分享，立刻做第 2 步。

**2. 上锁（关键，别跳过）**
1. 左侧 **Zero Trust**（首次进入会让你起一个 team name，随便取；选 **Free** 方案）
2. **Access → Applications → Add an application → Self-hosted**
3. Application name 随意；Session Duration 建议 **1 month**（省得每天登录）
4. Public hostname 填你的 `xxx.pages.dev`（子域留空、域名选 `pages.dev`、路径留空）
5. **Add policy**：Action = **Allow**，Include = **Emails** → 填 `hengkun.zhang@mail.mcgill.ca`
6. 保存。再打开网址会先要求邮箱验证码，只有你能进。

**3. 手机上**
打开 `https://xxx.pages.dev/latest` → 收验证码登录一次 → 加到主屏幕。之后每天早上直接点，永远是最新一期。

**注意**：这等于把简报（含你的真实持仓）托管在 Cloudflare 上。`_headers` 已设 `noindex` 防搜索引擎收录，
Access 负责鉴权；但托管方本身能看到文件，这是选择 Pages 的固有取舍。不想要就删掉这个项目，GitHub Markdown 版照常可用。
