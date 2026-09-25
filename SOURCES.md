# Data Sources and Provenance

## 1. Subscription Quotas and Pricing
- **Source**: [FeiZhuLulu/real-api-pricing](https://github.com/FeiZhuLulu/real-api-pricing) (`data/adopted.csv`, `data/conventions.json`, `data/research/`, `scripts/build_adopted.py`)
- **Snapshot Date**: 2026-09-24 (upstream `conventions.updatedAt`; ~100 upstream commits since the previous 2026-09-09 snapshot)
- **Coverage**: 284 plan × model rows — 266 synced verbatim from upstream (247 subscription + 19 metered API) plus 18 local-only GLM Coding Plan global USD rows (Z.ai $18/$80/$168).
- **Conversion Convention**: standard workload revised 2026-09-23 to **97% cache read / 2.5% fresh input / 0.5% output** (was 97.5/2.15/0.35); additional tiers `lowCache` (85/14.5/0.5, StepFun) and `anthropic` (cache-write-based, Anthropic API rows). Exchange rate: 1 USD = 6.7787 CNY.
- **New schema fields**: `plan_name_en`, `unmetered`, `promo_until`, `plan_gen`, `workload` — see `data/README.md`. One unmetered promo row exists (`Devin Pro × SWE-2`, until 2026-10-31).

## 2. Token Consumption Benchmarks
- **Source**: [DeepSWE v1.1](https://deepswe.datacurve.ai/) (published by [Datacurve](https://datacurve.ai))
- **Artifact**: [leaderboard-live.json (v1.1)](https://deepswe.datacurve.ai/artifacts/v1.1/leaderboard-live.json), cached verbatim as `data/deepswe.json`
- **Snapshot Date**: artifact regenerated 2026-09-22 (refetched 2026-09-25); scores/token figures unchanged since 2026-09-03 — the regeneration repriced GPT-6 Astra cost fields to current pricing only.
- **Extraction Scope**: `median_output_tokens` per configuration (median output tokens required to complete a benchmark task), plus Pass@1 score, mean cost, and mean agent steps.
- **Extracted Entries**: 70 model configurations across 28 models — Claude Fable 5 / Opus 4.8 / Opus 5 / Sonnet 5, GPT-5.4 / 5.5 / 5.6 Luna / Sol / Terra, GPT-6 Astra, Gemini 3.1–3.8 Flash, GLM-5.2 / 5.3 / 5.3 Flash, Grok 4.5 / 4.6, Kimi K2.7 Code / K3, DeepSeek V4 Flash / Pro, Qwen3.8 Max, Muse Spark 1.1 / 1.2 — across reasoning effort tiers (Low, Medium, High, Extra High, Max, and one Standard-only config).
- **Methodology Note**: benchmark "Cost / Task" figures are Datacurve's API-cost accounting and are shown for reference only; rankings use *median output tokens* consistently with the prior CursorBench methodology.

## 3. Unbenchmarked Models Scope
- Models present in the subscription dataset but currently unrepresented on DeepSWE v1.1 are categorized as `[Pending DeepSWE]` with null consumption values.
- These include: Claude Opus 5.5 / Fable 5.1, GPT-6 Sol, Grok 4.7, MiMo v2.5 / v2.6 series, Step-5 Preview, DeepSeek V4.1 series, SWE-2 (unmetered promo), Composer 2.5 (Cursor), Muse Spark 1.2-contributor / 1.3, Kimi K2.6 / K2.7-highspeed, GLM 5.1 / 5.2-fast, Qwen 3.6–3.8 (non-max), StepFun 3.x, MiniMax M2.5–M3, Xiaomi MiMo older gens, Tencent Hy3/Hy4, LongCat, Nemotron, Omen, Inkling, and others (see README §6).
