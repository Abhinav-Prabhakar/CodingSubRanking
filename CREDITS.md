# Credits and Attributions

This project builds directly on data, research, and insights from foundational community initiatives in AI economics. We extend our sincere gratitude and credit to the following original creators:

## 1. Real API Pricing (`FeiZhuLulu/real-api-pricing`)
- **Repository**: [https://github.com/FeiZhuLulu/real-api-pricing](https://github.com/FeiZhuLulu/real-api-pricing)
- **Author**: FeiZhuLulu and community contributors
- **License**: MIT License
- **Contribution**:
  - Pioneered the concept of *Real Unit Price* (`subscription fee ÷ usable tokens`).
  - Comprehensive empirical data on monthly token quotas, saturation tests, subscription tiers, and standard token workload normalization (`97.5% cache read, 2.15% fresh input, 0.35% output`).
  - Curated baseline mappings for 196 subscription and API points across major providers (OpenAI, Anthropic, Cursor, xAI, Google, StepFun, Zhipu, Kimi, Alibaba, DeepSeek, etc.).

## 2. DeepSWE by Datacurve (`deepswe.datacurve.ai`)
- **Website**: [https://deepswe.datacurve.ai](https://deepswe.datacurve.ai)
- **Publisher**: [Datacurve](https://datacurve.ai) (benchmark tasks Apache-2.0 licensed at [datacurve-ai/deep-swe](https://github.com/datacurve-ai/deep-swe))
- **Contribution**:
  - DeepSWE v1.1: a contamination-free, long-horizon software engineering benchmark — 113 original tasks across 91 repositories and 5 languages, every model run on the same open-source mini-swe-agent harness.
  - Public [leaderboard artifact](https://deepswe.datacurve.ai/artifacts/v1.1/leaderboard-live.json) with per-configuration **median output tokens per task**, cost, steps, and Pass@1 across 70 configurations (28 models × reasoning effort tiers) — the consumption figures this project is built on.

---

### How this project extends the prior art
While `real-api-pricing` established raw token allowances per dollar, LLMs differ drastically in their verbosity (output tokens required to solve identical software engineering tasks). This repository factors in the DeepSWE output token consumption to establish the **Task-Adjusted Value Ranking** — answering: *“How many tasks do you actually get for your subscription dollar?”*

### Historical note
Versions of this project prior to September 2026 used CursorBench 4.0 (Cursor / Anysphere) as the token-consumption source. The pivot to DeepSWE v1.1 brought exact per-configuration medians, a single unified harness, and near-double model coverage; earlier CursorBench-derived figures remain retrievable from the git history.
