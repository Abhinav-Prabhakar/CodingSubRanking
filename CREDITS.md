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

## 2. CursorBench by Cursor (`cursor.com/cursorbench`)
- **Website**: [https://cursor.com/cursorbench](https://cursor.com/cursorbench)
- **Publisher**: Anysphere / Cursor Team
- **Contribution**:
  - CursorBench 4.0 evaluation dataset on long-horizon, multi-file software engineering tasks from real coding sessions.
  - Crucial empirical measurements of **completion token consumption per task** (`output_tokens_per_task`) across models and reasoning effort configurations.

---

### How this project extends the prior art
While `real-api-pricing` established raw token allowances per dollar, LLMs differ drastically in their verbosity (completion tokens required to solve identical software engineering tasks). This repository factors in the CursorBench output token consumption to establish the **Task-Adjusted Value Ranking** — answering: *“How many tasks do you actually get for your subscription dollar?”*
