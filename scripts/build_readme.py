#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Generate the comprehensive README.md for the repository."""

from pathlib import Path
from generate_markdown_report import build_markdown_tables

ROOT = Path(__file__).resolve().parent.parent


def generate_readme():
    tables = build_markdown_tables()

    readme_content = f"""# Task-Adjusted AI Coding Subscription Rankings

> **Real Coding Value = Monthly Subscription Fee ÷ (Usable Tokens ÷ Output Tokens Consumed per Task)**
>
> **Effective Cost per Task ($/Task) = Monthly Fee ÷ Monthly Usable Tasks**

---

### Attributions & Upstream Credits
This project directly builds upon and extends the empirical work of:
- **[FeiZhuLulu/real-api-pricing](https://github.com/FeiZhuLulu/real-api-pricing)**: The original project that pioneered real AI subscription economics, documenting monthly token quotas, saturation tests, and dollar-per-token metrics across dozens of AI providers. Full credit to [FeiZhuLulu](https://github.com/FeiZhuLulu) and community contributors. See [CREDITS.md](CREDITS.md) and [SOURCES.md](SOURCES.md).
- **[DeepSWE v1.1](https://deepswe.datacurve.ai/) ([Datacurve](https://datacurve.ai))**: A contamination-free, long-horizon software engineering benchmark (113 original tasks across 91 repos, 5 languages, all models run on the same mini-swe-agent harness). We extract the **median output tokens per task** directly from the public [leaderboard artifact](https://deepswe.datacurve.ai/artifacts/v1.1/leaderboard-live.json).

---

## 1. Why Raw Token Pricing Misleads

The original `real-api-pricing` framework compared subscriptions using:
$$\\text{{Real Unit Price}} = \\frac{{\\text{{Monthly Fee}}}}{{\\text{{Monthly Usable Tokens}}}}$$

While this was a major leap forward over comparing sticker prices, it made an implicit assumption: **that all LLMs consume an equal number of tokens to accomplish the same job.**

In real-world agentic software development, this assumption fails drastically:
- Some model configurations are highly concise, requiring only **3,000 – 19,000 output tokens** to inspect, edit, test, and complete a complex task.
- Other configurations are heavily verbose or require expansive reasoning steps, consuming **115,000 – 204,000 output tokens** for the same workload — up to a **~65× difference in token consumption** (DeepSWE v1.1 medians: `gpt-5.6-luna` Low = 3,059 vs `claude-sonnet-5` Max = 203,918).

### The Task-Adjusted Formulation

To find the true purchasing power of an AI coding subscription, we adjust for output token consumption per task ($C_{{\\text{{task}}}}$):

1. **Monthly Task Capacity ($N_{{\\text{{tasks}}}}$)**:
   $$N_{{\\text{{tasks}}}} = \\frac{{T_{{\\text{{monthly}}}}}}{{C_{{\\text{{task}}}}}}$$
   *(How many real tasks your monthly token pool can actually solve)*

2. **Effective Cost per Task ($Cost_{{\\text{{task}}}}$)**:
   $$Cost_{{\\text{{task}}}} = \\frac{{P_{{\\text{{monthly}}}}}}{{N_{{\\text{{tasks}}}}}} = \\frac{{P_{{\\text{{monthly}}}} \\times C_{{\\text{{task}}}}}}{{T_{{\\text{{monthly}}}}}}$$
   *(What you actually pay per completed task)*

3. **Tasks per Dollar Spent ($Tasks_{{\\textdollar}}$)**:
   $$Tasks_{{\\textdollar}} = \\frac{{N_{{\\text{{tasks}}}}}}{{P_{{\\text{{monthly}}}}}} = \\frac{{1}}{{Cost_{{\\text{{task}}}}}}$$
   *(The true efficiency metric: completed tasks delivered per dollar)*

4. **Annual Billing & Discount Dynamics**:
   For providers without differentiated annual rates (e.g. OpenAI), the annual price is simply $12 \\times P_{{\\text{{monthly}}}}$ ($0\\%$ discount, same effective monthly rate). For providers offering annual commitments:
   - **Claude Pro (Anthropic)**: \\$200/year (\\$16.67/mo effective, $\\sim$16.7% discount).
   - **GLM Coding Plans (Zhipu)**: 30% annual discount on global USD plans (\\$56/mo Pro down from \\$80/mo, \\$12.60/mo Lite, \\$117.60/mo Max) and 20% on new-customer CN tiers.
   - **SuperGrok (xAI)**: \\$300/year (\\$25/mo effective, 16.7% discount).
   - **Ollama Pro**: \\$200/year (\\$16.67/mo effective, 16.7% discount).
   Effective cost per task under annual billing drops proportionally:
   $$Cost_{{\\text{{task, annual}}}} = \\frac{{P_{{\\text{{annual}}}} / 12}}{{N_{{\\text{{tasks}}}}}} = Cost_{{\\text{{task, monthly}}}} \\times (1 - \\text{{Discount}}\\%)$$

---

## 2. DeepSWE v1.1 Token Consumption Data

Below is the complete dataset extracted directly from [DeepSWE v1.1](https://deepswe.datacurve.ai/) (Datacurve). For each of the 70 evaluated configurations (28 models × reasoning effort tiers), it records the benchmark score (Pass@1), average API cost, steps, and specifically the **Output Tokens / Task** (median output tokens, the consumption figure used throughout this project):

{tables['deepswe_table']}

> [!NOTE]
> For models evaluated across multiple reasoning effort tiers (Low, Medium, High, Extra High, Max), our standard baseline ranking adopts the **Medium** tier — or the **nearest available tier** for models that were not evaluated at Medium (e.g. `glm-5.3`, `kimi-k3`, and `deepseek-v4-*` were only run at Max; `muse-spark-1.2` at Extra High; `kimi-k2.7-code` has a single Standard configuration). Full breakdowns across all tiers are exported in `derived/task-ranking.json`.

---

## 3. Primary Task-Adjusted Ranking (All Benchmarked Plans)

Ranked primarily by **Effective Cost per Task ($/Task)** (cheapest task first), alongside **Tasks per Dollar** and **Monthly Task Capacity**.

The column **Shift vs Raw** indicates the ranking change compared to the traditional raw token price ($/MTok) ranking:
- **▲ +X**: Model is concise and jumped **up** X spots in cost-effectiveness.
- **▼ -X**: Model is verbose and dropped **down** X spots in cost-effectiveness.

{tables['main_ranking_table']}

> [!NOTE]
> **Looking for all reasoning effort configurations?** We evaluate and rank all **260 plan × effort combinations** across Low, Medium, High, Extra High, and Max tiers. See the complete export in [`derived/task-ranking-all-efforts.csv`](derived/task-ranking-all-efforts.csv) and [`derived/task-ranking-all-efforts.json`](derived/task-ranking-all-efforts.json), or toggle the **"All"** effort filter in the interactive web interface (`web/index.html`).

---

## 4. Annual Pricing & Discount Comparison

When paid annually, subscriptions with discounts become significantly more cost-effective per completed task. Below are the plans offering explicit annual discounts, showing how their effective monthly fee, $/task, and rankings improve:

{tables['annual_discount_table']}

> [!TIP]
> Plans without published annual discounts (e.g. ChatGPT Plus / Pro, Command Code GOAT, OpenCode) maintain the same effective monthly fee ($12 \\times$ monthly with 0% discount). Consequently, discounted subscriptions like **Claude Pro** and **GLM Coding Plans** climb several spots under annual billing.

---

## 5. Key Takeaways & Ranking Shifts

1. **The Verbosity Penalty**:
   - Models with large raw token allowances like `gemini-3.8-flash` offer tens of billions of tokens, ranking high on raw $/MTok charts. However, at **120,488 median output tokens/task** (Medium tier), its effective task cost falls behind far more token-efficient models.
   - Conversely, `gpt-5.6-luna` (**7,918 tokens/task**) and `gpt-5.6-terra` (**11,453 tokens/task**) pair DeepSWE-grade competence with extreme token efficiency — `gpt-5.6-terra` plans climb up to **+39 spots** once verbosity is priced in, and Luna plans hold the entire top tier at **47,000 – 95,000 tasks per dollar**.

2. **The Sweet Spot of Coding Workhorses**:
   - **ChatGPT Pro 20x / 5x / Plus (Luna & Terra)** achieve industry-leading task yields due to high monthly pools paired with low completion overhead.
   - **GLM Coding Pro (`glm-5.3-flash`)** breaks into the top 10 at **67,491 tokens/task** on the strength of its enormous quota — despite mid-pack DeepSWE efficiency (63.4% Pass@1 at Max).
   - **Sonnet 5** (**50,414 tokens/task**) and **Opus 5** (**33,436 tokens/task**) offer high quality at moderate token overhead, climbing past more verbose competitors.

3. **Coverage Flip vs CursorBench**:
   - DeepSWE covers **21 model families with subscription plans** (vs 11 under CursorBench 4.0): DeepSeek V4, Kimi K3 / K2.7 Code, GLM-5.2 / 5.3, Qwen3.8 Max, Claude Opus 4.8, GPT-5.5, Grok 4.5 and Muse Spark 1.2 all enter the ranking for the first time.
   - **Composer 2.5** (Cursor) and **Muse Spark 1.3 / 1.3-contributor** have no DeepSWE evaluation yet and are now flagged `[Pending DeepSWE]` — plan rows switch from ranked to pending accordingly.

---

## 5. Rankings by Price Band

### Budget Band: $0 – $30 / month
Tailored for individual developers, students, and freelancers:

{tables['band_tables']['Budget ($0 – $30/mo)']}

### Pro Band: >$30 and ≤$100 / month
For professional software engineers and daily power users:

{tables['band_tables']['Pro ($30 – $100/mo)']}

### Power & Enterprise Band: >$100 and ≤$300 / month
For heavy agentic automation and team subscriptions:

{tables['band_tables']['Power / Enterprise ($100 – $300/mo)']}

---

## 6. Unbenchmarked Models (Marked for Future Evaluation)

The following models from the `real-api-pricing` dataset have **no DeepSWE v1.1 evaluation** at all — meaning their output token consumption per task is unknown. Their ranking values are left empty (`null`) and flagged as **`[Pending DeepSWE]`**:

> **Note**: API-only rows (e.g. "Claude Opus 5 API") for models that **are** in DeepSWE are intentionally excluded from ranking because they carry no monthly token quota — not because the model itself is unevaluated.

{tables['unbenchmarked_table']}

> [!IMPORTANT]
> When DeepSWE or community saturation benchmarks release completion token figures for Composer, Muse Spark 1.3, DeepSeek V4.1, MiniMax, StepFun, Qwen3.7, or any other pending model, simply update `data/model-token-consumption.json` and re-run `python3 scripts/compute_task_ranking.py` to seamlessly integrate them into the ranking.

---

## 7. Project Architecture & Web Readiness

Everything has been structured so that the data pipeline is completely reproducible and ready for a web frontend when instructed:

```
CodingSubRanks/
├── README.md                      # Primary comprehensive markdown report (this file)
├── CREDITS.md                     # Formal attribution to FeiZhuLulu/real-api-pricing & Datacurve
├── SOURCES.md                     # Data sources and methodology documentation
├── BUILD.md                       # Instructions to reproduce the calculations
├── LICENSE                        # MIT License
├── data/
│   ├── adopted.csv                # Upstream subscription data (196 plan × model points)
│   ├── deepswe.json               # Raw DeepSWE v1.1 leaderboard artifact (70 configs)
│   ├── deepswe-configs.json       # Normalized per-config records (tokens, score, cost, steps)
│   ├── model-token-consumption.json # Canonical mapping with reasoning tiers & null placeholders
│   └── conventions.json           # Currency rates and conversion conventions
├── derived/
│   ├── task-ranking.json          # Machine-readable dataset ready for web frontend
│   ├── task-ranking.csv           # Full tabular task-adjusted ranking
│   ├── unbenchmarked-models.json  # Catalog of models awaiting eval
│   └── unbenchmarked-models.csv   # Tabular catalog of pending models
├── scripts/
│   ├── extract_deepswe.py         # Fetcher/parser for DeepSWE v1.1 leaderboard artifact
│   ├── build_model_consumption_map.py # Builder for canonical model mapping
│   ├── compute_task_ranking.py    # Core ranking calculation engine
│   ├── generate_markdown_report.py # Markdown table formatter
│   └── build_readme.py            # Automated README generator
└── web/
    ├── index.html                 # Static showcase page (GitHub Pages)
    ├── schema.json                # JSON Schema data contract for web UI
    └── README.md                  # Web frontend staging documentation
```

To regenerate the entire dataset and documentation:
```bash
python3 scripts/extract_deepswe.py
python3 scripts/build_model_consumption_map.py
python3 scripts/compute_task_ranking.py
python3 scripts/build_readme.py
```
"""

    readme_path = ROOT / "README.md"
    with open(readme_path, "w", encoding="utf-8") as f:
        f.write(readme_content)
    print(f"README.md successfully written to {readme_path}")


if __name__ == "__main__":
    generate_readme()
