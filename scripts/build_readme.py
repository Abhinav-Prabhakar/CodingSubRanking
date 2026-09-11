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
- **[CursorBench 4.0](https://cursor.com/cursorbench)**: Cursor's empirical benchmark evaluating AI coding agents on ambiguous, multi-file software engineering tasks from real coding sessions. We extract the **output token consumption** (completion tokens per task) directly from CursorBench.

---

## 1. Why Raw Token Pricing Misleads

The original `real-api-pricing` framework compared subscriptions using:
$$\\text{{Real Unit Price}} = \\frac{{\\text{{Monthly Fee}}}}{{\\text{{Monthly Usable Tokens}}}}$$

While this was a major leap forward over comparing sticker prices, it made an implicit assumption: **that all LLMs consume an equal number of tokens to accomplish the same job.**

In real-world agentic software development, this assumption fails drastically:
- Some models are highly concise, requiring only **7,000 – 10,000 output tokens** to inspect, edit, test, and complete a complex task.
- Other models are heavily verbose or require expansive reasoning steps, consuming **120,000 – 160,000 output tokens** for the same workload — a **15× to 20× difference in token consumption**.

### The Task-Adjusted Formulation

To find the true purchasing power of an AI coding subscription, we adjust for output token consumption per task ($C_{{\\text{{task}}}}$):

1. **Monthly Task Capacity ($N_{{\\text{{tasks}}}}$)**:
   $$N_{{\\text{{tasks}}}} = \\frac{{T_{{\\text{{monthly}}}}}}{{C_{{\\text{{task}}}}}}$$
   *(How many real tasks your monthly token pool can actually solve)*

2. **Effective Cost per Task ($Cost_{{\\text{{task}}}}$)**:
   $$Cost_{{\\text{{task}}}} = \\frac{{P_{{\\text{{monthly}}}}}}{{N_{{\\text{{tasks}}}}}} = \\frac{{P_{{\\text{{monthly}}}} \\times C_{{\\text{{task}}}}}}{{T_{{\\text{{monthly}}}}}}$$
   *(What you actually pay per completed task)*

3. **Tasks per Dollar Spent ($Tasks_{{\\$}}$)**:
   $$Tasks_{{\\$}} = \\frac{{N_{{\\text{{tasks}}}}}}{{P_{{\\text{{monthly}}}}}} = \\frac{{1}}{{Cost_{{\\text{{task}}}}}}$$
   *(The true efficiency metric: completed tasks delivered per dollar)*

---

## 2. CursorBench 4.0 Token Consumption Data

Below is the complete dataset extracted directly from [CursorBench 4.0](https://cursor.com/cursorbench). For each model configuration, it records the benchmark score, average cost, steps, and specifically the **Output Tokens / Task** (median completion tokens):

{tables['cursorbench_table']}

> [!NOTE]
> For models evaluated across multiple reasoning effort tiers (Low, Medium, High, Extra High, Max), our standard baseline ranking adopts the **Medium** tier (or **Standard** tier for Composer 2.5) to ensure consistent, balanced comparisons across all subscriptions. Full breakdowns across all tiers are exported in `derived/task-ranking.json`.

---

## 3. Primary Task-Adjusted Ranking (All Benchmarked Plans)

Ranked primarily by **Effective Cost per Task ($/Task)** (cheapest task first), alongside **Tasks per Dollar** and **Monthly Task Capacity**.

The column **Shift vs Raw** indicates the ranking change compared to the traditional raw token price ($/MTok) ranking:
- **▲ +X**: Model is concise and jumped **up** X spots in cost-effectiveness.
- **▼ -X**: Model is verbose and dropped **down** X spots in cost-effectiveness.

{tables['main_ranking_table']}

---

## 4. Key Takeaways & Ranking Shifts

1. **The Verbosity Penalty**:
   - Models with large raw token allowances like `gemini-3.8-flash` offer tens of billions of tokens, ranking high on raw $/MTok charts. However, at **128,364 output tokens/task**, its effective task cost drops behind more token-efficient models.
   - Conversely, models like `gpt-5.6-luna` (**7,642 tokens/task**) and `gpt-5.6-terra` (**7,307 tokens/task**) show extreme token efficiency, providing tens of thousands of tasks per dollar.

2. **The Sweet Spot of Coding Workhorses**:
   - **ChatGPT Pro 20x / 5x / Plus (Luna & Terra)** achieve industry-leading task yields due to high monthly pools paired with low completion overhead.
   - **Composer 2.5** on Cursor Ultra / Pro+ achieves a very balanced **17,347 tokens/task**, jumping into the top tier of developer efficiency at over **5,000 tasks per dollar**.
   - **Sonnet 5** (**39,114 tokens/task**) and **Opus 5** (**45,272 tokens/task**) offer high quality at moderate token overhead, climbing past more verbose competitors.

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

The following models from the `real-api-pricing` dataset have **no CursorBench 4.0 evaluation** at all — meaning their output token consumption per task is unknown. Their ranking values are left empty (`null`) and flagged as **`[Pending CursorBench]`**:

> **Note**: API-only rows (e.g. "Claude Opus 5 API") for models that **are** in CursorBench are intentionally excluded from ranking because they carry no monthly token quota — not because the model itself is unevaluated.

{tables['unbenchmarked_table']}

> [!IMPORTANT]
> When CursorBench or community saturation benchmarks release completion token figures for DeepSeek, Kimi, GLM, Qwen, StepFun, or MiniMax, simply update `data/model-token-consumption.json` and re-run `python3 scripts/compute_task_ranking.py` to seamlessly integrate them into the ranking.

---

## 7. Project Architecture & Web Readiness

Everything has been structured so that the data pipeline is completely reproducible and ready for a web frontend when instructed:

```
CodingSubRanks/
├── README.md                      # Primary comprehensive markdown report (this file)
├── CREDITS.md                     # Formal attribution to FeiZhuLulu/real-api-pricing & Cursor
├── SOURCES.md                     # Data sources and methodology documentation
├── BUILD.md                       # Instructions to reproduce the calculations
├── LICENSE                        # MIT License
├── data/
│   ├── adopted.csv                # Upstream subscription data (196 plan × model points)
│   ├── cursorbench.json           # Raw extracted CursorBench 4.0 benchmark records
│   ├── cursorbench.csv            # Tabular CursorBench 4.0 records
│   ├── model-token-consumption.json # Canonical mapping with reasoning tiers & null placeholders
│   └── conventions.json           # Currency rates and conversion conventions
├── derived/
│   ├── task-ranking.json          # Machine-readable dataset ready for web frontend
│   ├── task-ranking.csv           # Full tabular task-adjusted ranking
│   ├── unbenchmarked-models.json  # Catalog of models awaiting eval
│   └── unbenchmarked-models.csv   # Tabular catalog of pending models
├── scripts/
│   ├── extract_cursorbench.py     # Parser for CursorBench 4.0
│   ├── build_model_consumption_map.py # Builder for canonical model mapping
│   ├── compute_task_ranking.py    # Core ranking calculation engine
│   ├── generate_markdown_report.py # Markdown table formatter
│   └── build_readme.py            # Automated README generator
└── web/
    ├── schema.json                # JSON Schema data contract for web UI
    └── README.md                  # Web frontend staging documentation
```

To regenerate the entire dataset and documentation:
```bash
python3 scripts/extract_cursorbench.py
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
