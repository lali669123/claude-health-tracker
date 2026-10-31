<div align="center">

# claude-health-tracker

[简体中文](README.md) | **English**

Turn an AI coding agent into your personal health logger. Say a sentence or send a photo, and your meals, weight, training and wearable data land in local spreadsheets, with an evidence-based daily health report every night.

[![Claude Code](https://img.shields.io/badge/Claude_Code-supported-D97757)](https://code.claude.com/docs/en/setup)
[![Codex](https://img.shields.io/badge/Codex-supported-10A37F)](https://github.com/openai/codex)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)

</div>

> The skills and rules are written in Chinese. Both agents follow them fine and will reply in whatever language you write in.

---

## Why use AI for health management

Most people don't lack health knowledge. What they lack is **consistent, accurate, connected data**, and someone willing to look at it every day.

Traditional tools have three problems:
- **Logging is tedious.** Nutrition apps make you search each food and enter grams. Few people keep it up.
- **Data lives in silos.** Your wristband knows how you slept, your food app knows what you ate, your scale knows your weight. Nothing looks at them together.
- **Advice is generic.** Everyone knows "sleep more, eat more protein". The hard part is "how much am I short today, and what do I eat tomorrow?"

An AI agent fills those gaps:

| Capability | What it looks like |
|------------|--------------------|
| **Low-effort logging** | Send a photo or a sentence and the agent estimates portions, calories and protein. For home cooking, tell it how many eggs and how much flour, and it recalculates. |
| **Cross-metric links** | Sleep, HRV, resting heart rate, training and diet sit in one table. Did short sleep lower today's HRV? Was protein enough on training days? |
| **Proactive checks** | A nightly check spots protein short several days running, sleep under 7 hours, or a stalled 7-day weight average, and tells you. |
| **Personal next steps** | Advice based on your own numbers, e.g. "add two eggs at lunch, about 12 g more protein". |
| **Honest about gaps** | The rules require it: missing data is reported as missing, every estimate gets a range and a confidence level, and no made-up comparisons like "better than 90% of your peers". |

### What it can track

- **Weight and body composition**: trend from the 7-day average, which filters out the normal 0.5–1 kg daily swing from water and salt.
- **Energy balance**: basal metabolic rate (Mifflin-St Jeor) + wearable active calories − intake, as a daily deficit estimate.
- **Nutrition**: protein against 1.6–2.2 g per kg body weight; vegetables, fruit, oil and salt.
- **Sleep and recovery**: night sleep, deep sleep share, awakenings, HRV and resting heart rate.
- **Training progress**: weight and reps per exercise compared with last time, with progressive-overload suggestions.
- **Stress and mood**: if your wearable records them, they go into the log next to sleep and diet.

### Ideas for extension

These are **not implemented yet**. The structure is built to grow this way, and PRs are welcome:
- Smart scale / body-fat scale exports for body fat and muscle mass.
- Parsing medical checkup reports (lipids, glucose, uric acid) and tying diet advice to them.
- Menstrual cycle tracking and its effect on weight, sleep and training.
- Continuous glucose monitor (CGM) data to see how foods actually affect blood sugar.
- Profiles for family members, e.g. tracking blood pressure, medication and meals for parents.
- Monthly and quarterly reports against phase goals.

> ⚠️ **This is not a medical device.** The agent logs, organizes and suggests lifestyle changes based on your data. It does not diagnose. See a doctor if numbers stay abnormal.

---

## Setup

### 1. Install an agent (either one, or both)

| | Claude Code | Codex |
|---|---|---|
| Docs | [code.claude.com/docs](https://code.claude.com/docs/en/setup) | [github.com/openai/codex](https://github.com/openai/codex) |
| macOS / Linux | `curl -fsSL https://claude.ai/install.sh \| bash` | `curl -fsSL https://chatgpt.com/codex/install.sh \| sh` |
| Windows PowerShell | `irm https://claude.ai/install.ps1 \| iex` | `powershell -ExecutionPolicy ByPass -c "irm https://chatgpt.com/codex/install.ps1 \| iex"` |
| npm | `npm install -g @anthropic-ai/claude-code` | `npm install -g @openai/codex` |
| Account | Claude Pro / Max or API | ChatGPT Plus / Pro or API |
| GUI | [Claude desktop app](https://claude.com/download) | ChatGPT desktop app / IDE extension |

### 2. Clone and initialize your data

```bash
git clone https://github.com/lali669123/claude-health-tracker.git
cd claude-health-tracker
cp -r template data
```

On Windows PowerShell use `Copy-Item -Recurse template data`.

Fill in `data/config/profile.json` (height, birth date, sex) and `data/config/goals.json`.

### 3. Start

```bash
claude   # Claude Code
codex    # Codex
```

Both agents read the same rules (`AGENTS.md`), the same skills and the same data, so you can switch between them.

---

## Daily use

Just talk to it:

| You say | The agent |
|---------|-----------|
| "Morning weight 70.5" | Logs weight, updates your profile |
| "Breakfast: a glass of milk and two eggs" or a photo | Estimates calories and protein, logs the meal, tells you what's left for the day |
| Before and after photos | Subtracts leftovers |
| A wearable screenshot + "sync" | Extracts sleep, heart rate, HRV, steps, active calories |
| "Push day, bench 60 kg 8/8/7" | Logs training, compares with last time, suggests next step |
| "Daily report" / "weekly report" | Generates and saves the report |
| "Was my protein enough this week?" | Answers from your tables |

Or call a skill directly:

| Skill | Claude Code | Codex |
|-------|-------------|-------|
| Log a meal | `/record-meal` | `$record-meal` |
| Sync wearable | `/sync-wearable` | `$sync-wearable` |
| Log training | `/record-training` | `$record-training` |
| Daily report | `/daily-report` | `$daily-report` |
| Weekly report | `/weekly-report` | `$weekly-report` |

### Scheduled reports (optional)

- **Claude desktop app**: create a scheduled task in the sidebar, paste a prompt from `routines/`, and replace `<DATA_DIR>` with the absolute path of your `data` folder.
- **Codex**: run `codex exec "<prompt from routines>"` from Windows Task Scheduler or cron. We haven't fully tested this path yet.

The nightly check covers today and the two days before, fills in any day that has wearable data but no report, and never overwrites existing reports. Keep your daily logging in one conversation so a meal isn't recorded twice.

---

## Layout

```
AGENTS.md              shared rules (Codex reads it; Claude Code imports it via CLAUDE.md)
CLAUDE.md              one line: @AGENTS.md
.agents/skills/        skills for Codex (edit skills here)
.claude/skills/        copy for Claude Code (sync with sync_skills.py)
routines/              prompts for scheduled daily and weekly reports
scripts/stats.py       quick N-day averages without the agent
scripts/sync_skills.py copy .agents/skills to .claude/skills
template/              starting layout for data/: sample config and header-only CSVs
data/                  your data (gitignored, never uploaded)
```

## Data files

| File | Contents |
|------|----------|
| `structured/daily_metrics.csv` | One row per day: weight, intake range, protein, sleep, heart rate, HRV, steps, active calories |
| `structured/meals.csv` | One row per meal: foods, calories, protein, confidence, notes |
| `structured/training.csv` | One row per session, exercises in notes |
| `structured/wearable.csv` | Raw wearable metrics |

Plain CSV files: open them in Excel or any analysis tool. Your data stays on your computer.

```bash
python scripts/stats.py --days 7      # last 7 days, standard library only
python scripts/sync_skills.py --check # check both skill folders match
```

## Limitations

- Calorie estimates from photos can be off by 20–40%. Weighing food or reading labels helps a lot.
- Energy expenditure is an estimate. Judge fat loss by the change in your 7-day average weight.
- Screenshot parsing was tested with Huawei Health. Other apps have similar fields but haven't been verified one by one.

## License

[MIT](LICENSE)
