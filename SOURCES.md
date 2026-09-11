# Data Sources and Provenance

## 1. Subscription Quotas and Pricing
- **Source**: [FeiZhuLulu/real-api-pricing](https://github.com/FeiZhuLulu/real-api-pricing) (`data/adopted.csv`, `data/conventions.json`, `data/research/`)
- **Snapshot Date**: 2026-09-09
- **Coverage**: 196 plan × model configurations, 183 subscription points, and 13 metered API baselines.
- **Conversion Convention**: Standard workload of 97.5% cache read, 2.15% fresh input, 0.35% output. Exchange rate: 1 USD = 6.7787 CNY.

## 2. Token Consumption Benchmarks
- **Source**: [DeepSWE v1.1](https://deepswe.datacurve.ai/) (published by [Datacurve](https://datacurve.ai))
- **Artifact**: [leaderboard-live.json (v1.1)](https://deepswe.datacurve.ai/artifacts/v1.1/leaderboard-live.json), cached verbatim as `data/deepswe.json`
- **Snapshot Date**: artifact generated 2026-09-03 (leaderboard updated September 3, 2026); fetched 2026-09-11
- **Extraction Scope**: `median_output_tokens` per configuration (median output tokens required to complete a benchmark task), plus Pass@1 score, mean cost, and mean agent steps.
- **Extracted Entries**: 70 model configurations across 28 models — Claude Fable 5 / Opus 4.8 / Opus 5 / Sonnet 5, GPT-5.4 / 5.5 / 5.6 Luna / Sol / Terra, GPT-6 Astra, Gemini 3.1–3.8 Flash, GLM-5.2 / 5.3 / 5.3 Flash, Grok 4.5 / 4.6, Kimi K2.7 Code / K3, DeepSeek V4 Flash / Pro, Qwen3.8 Max, Muse Spark 1.1 / 1.2 — across reasoning effort tiers (Low, Medium, High, Extra High, Max, and one Standard-only config).
- **Methodology Note**: benchmark "Cost / Task" figures are Datacurve's API-cost accounting and are shown for reference only; rankings use *median output tokens* consistently with the prior CursorBench methodology.

## 3. Unbenchmarked Models Scope
- Models present in the subscription dataset but currently unrepresented on DeepSWE v1.1 are categorized as `[Pending DeepSWE]` with null consumption values.
- These include: Composer 2.5 (Cursor), Muse Spark 1.2-contributor / 1.3, DeepSeek V4.1 series, Kimi K2.6, GLM 5.1 / 5.2-fast, Qwen 3.6–3.8 (non-max), StepFun 3.x, MiniMax M2.5–M3, Xiaomi MiMo, Tencent Hy3/Hy4, and others (see README §6).
