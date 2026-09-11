# Data Sources and Provenance

## 1. Subscription Quotas and Pricing
- **Source**: [FeiZhuLulu/real-api-pricing](https://github.com/FeiZhuLulu/real-api-pricing) (`data/adopted.csv`, `data/conventions.json`, `data/research/`)
- **Snapshot Date**: 2026-09-09
- **Coverage**: 196 plan × model configurations, 183 subscription points, and 13 metered API baselines.
- **Conversion Convention**: Standard workload of 97.5% cache read, 2.15% fresh input, 0.35% output. Exchange rate: 1 USD = 6.7787 CNY.

## 2. Token Consumption Benchmarks
- **Source**: [CursorBench 4.0](https://cursor.com/cursorbench) (published by Cursor / Anysphere)
- **Snapshot Date**: September 2026
- **Extraction Scope**: `output_tokens_per_task` (median completion tokens required to complete real multi-file coding sessions).
- **Extracted Entries**: 43 model configurations spanning Fable 5.1, Opus 5, Sonnet 5, GPT-5.6 Sol, GPT-5.6 Terra, GPT-5.6 Luna, Grok 4.6, Gemini 3.8 Flash, Muse Spark 1.3, and Composer 2.5 across various reasoning effort tiers (Low, Medium, High, Extra High, Max).

## 3. Unbenchmarked Models Scope
- Models present in the subscription dataset but currently unrepresented on CursorBench 4.0 are categorized as `[Pending CursorBench]` with null consumption values.
- These include: DeepSeek V4 series, Kimi K2.7 / K3, GLM 5.x, Qwen 3.x, StepFun 3.x, MiniMax M2.5–M3, Xiaomi MiMo, and Tencent Hy3/Hy4.
