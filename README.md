# Task-Adjusted AI Coding Subscription Rankings

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
$$\text{Real Unit Price} = \frac{\text{Monthly Fee}}{\text{Monthly Usable Tokens}}$$

While this was a major leap forward over comparing sticker prices, it made an implicit assumption: **that all LLMs consume an equal number of tokens to accomplish the same job.**

In real-world agentic software development, this assumption fails drastically:
- Some model configurations are highly concise, requiring only **3,000 – 19,000 output tokens** to inspect, edit, test, and complete a complex task.
- Other configurations are heavily verbose or require expansive reasoning steps, consuming **115,000 – 204,000 output tokens** for the same workload — up to a **~65× difference in token consumption** (DeepSWE v1.1 medians: `gpt-5.6-luna` Low = 3,059 vs `claude-sonnet-5` Max = 203,918).

### The Task-Adjusted Formulation

To find the true purchasing power of an AI coding subscription, we adjust for output token consumption per task ($C_{\text{task}}$):

1. **Monthly Task Capacity ($N_{\text{tasks}}$)**:
   $$N_{\text{tasks}} = \frac{T_{\text{monthly}}}{C_{\text{task}}}$$
   *(How many real tasks your monthly token pool can actually solve)*

2. **Effective Cost per Task ($Cost_{\text{task}}$)**:
   $$Cost_{\text{task}} = \frac{P_{\text{monthly}}}{N_{\text{tasks}}} = \frac{P_{\text{monthly}} \times C_{\text{task}}}{T_{\text{monthly}}}$$
   *(What you actually pay per completed task)*

3. **Tasks per Dollar Spent ($Tasks_{\textdollar}$)**:
   $$Tasks_{\textdollar} = \frac{N_{\text{tasks}}}{P_{\text{monthly}}} = \frac{1}{Cost_{\text{task}}}$$
   *(The true efficiency metric: completed tasks delivered per dollar)*

4. **Annual Billing & Discount Dynamics**:
   For providers without differentiated annual rates (e.g. OpenAI ChatGPT, Ollama Max, Claude Max, Command Code, OpenCode), the annual price is simply $12 \times P_{\text{monthly}}$ ($0\%$ discount, same effective monthly rate). For providers offering annual commitments:
   - **GLM Coding Plans (Zhipu / Z.ai)**: **30% annual discount** on global USD plans (\$56/mo Pro down from \$80/mo, \$12.60/mo Lite, \$117.60/mo Max) and **20% annual discount (8折)** across all Chinese CNY tiers.
   - **Cursor**: **20% annual discount** across all tiers — Cursor Pro (\$16/mo or \$192/yr down from \$20/mo), Pro+ (\$48/mo), and Ultra (\$160/mo).
   - **Kimi (Moonshot AI)**: **20% annual discount (8折)** on continuous annual memberships (Andante ¥39.2/mo, Moderato ¥79.2/mo, Allegretto ¥159.2/mo, Allegro ¥559.2/mo saving up to ¥1,680/yr).
   - **Claude Pro (Anthropic)**: \$200/year (\$16.67/mo effective, $\sim$16.7% discount; Claude Max is monthly only).
   - **Ollama Pro**: \$200/year (\$16.67/mo effective, 16.7% discount; Ollama Max has no annual discount).
   - **SuperGrok (xAI)**: \$300/year (\$25/mo effective, 16.7% discount) and SuperGrok Heavy \$3,000/year (\$250/mo).
   Effective cost per task under annual billing drops proportionally:
   $$Cost_{\text{task, annual}} = \frac{P_{\text{annual}} / 12}{N_{\text{tasks}}} = Cost_{\text{task, monthly}} \times (1 - \text{Discount}\%)$$

---

## 2. DeepSWE v1.1 Token Consumption Data

Below is the complete dataset extracted directly from [DeepSWE v1.1](https://deepswe.datacurve.ai/) (Datacurve). For each of the 70 evaluated configurations (28 models × reasoning effort tiers), it records the benchmark score (Pass@1), average API cost, steps, and specifically the **Output Tokens / Task** (median output tokens, the consumption figure used throughout this project):

| Rank | Model & Effort Tier         | DeepSWE Score (Pass@1) | Cost / Task | Output Tokens / Task (median) | Steps / Task |
| :--: | --------------------------- | ---------------------: | ----------: | ----------------------------: | -----------: |
|  #1  | GPT-6 Astra Extra High      |                  74.1% |       $4.43 |                        28,542 |           29 |
|  #2  | Gemini 3.8 Flash High       |                  73.8% |       $2.36 |                       138,377 |          166 |
|  #3  | Claude Opus 5 Max           |                  73.6% |      $11.84 |                       113,366 |           99 |
|  #4  | GPT-6 Astra High            |                  73.2% |       $3.92 |                        25,414 |           27 |
|  #5  | GPT-6 Astra Max             |                  73.2% |       $7.50 |                        58,618 |           28 |
|  #6  | Claude Opus 5 Extra High    |                  73.2% |       $9.07 |                        87,322 |           89 |
|  #7  | GPT-6 Astra Medium          |                  72.8% |       $3.08 |                        19,006 |           26 |
|  #8  | Claude Opus 5 High          |                  72.8% |       $6.08 |                        59,856 |           73 |
|  #9  | GPT-5.6 Sol Max             |                  72.7% |       $8.39 |                        58,786 |           61 |
| #10  | Gemini 3.8 Flash Medium     |                  71.0% |       $1.97 |                       120,488 |          147 |
| #11  | GPT-5.6 Sol Extra High      |                  70.7% |       $4.70 |                        39,449 |           44 |
| #12  | Claude Fable 5 Extra High   |                  69.9% |      $13.41 |                        76,036 |           68 |
| #13  | Claude Fable 5 Max          |                  69.7% |      $21.63 |                       115,631 |           88 |
| #14  | GPT-5.6 Terra Max           |                  69.6% |       $4.95 |                        70,835 |           76 |
| #15  | GPT-5.6 Sol High            |                  69.4% |       $3.47 |                        27,700 |           37 |
| #16  | GLM-5.3 Max                 |                  69.0% |       $3.99 |                        74,953 |          124 |
| #17  | Claude Opus 5 Medium        |                  68.9% |       $3.29 |                        33,436 |           52 |
| #18  | Claude Fable 5 High         |                  68.6% |       $9.18 |                        52,624 |           59 |
| #19  | Kimi K3 Max                 |                  68.5% |       $4.65 |                        75,383 |           98 |
| #20  | Grok 4.6 Medium             |                  67.5% |       $3.45 |                        48,586 |           70 |
| #21  | GPT-5.6 Luna Max            |                  67.2% |       $3.03 |                        70,253 |          102 |
| #22  | GPT-6 Astra Low             |                  67.0% |       $1.60 |                         9,488 |           20 |
| #23  | GPT-5.5 Extra High          |                  67.0% |       $7.23 |                        44,492 |           82 |
| #24  | Grok 4.6 Extra High         |                  66.7% |       $5.50 |                        71,285 |           87 |
| #25  | Gemini 3.7 Flash Medium     |                  65.5% |       $2.03 |                        87,640 |          117 |
| #26  | Claude Fable 5 Medium       |                  65.4% |       $6.09 |                        35,970 |           48 |
| #27  | Gemini 3.7 Flash High       |                  65.3% |       $2.18 |                        99,819 |          125 |
| #28  | Grok 4.6 High               |                  65.2% |       $4.38 |                        60,060 |           79 |
| #29  | GPT-5.5 High                |                  64.4% |       $5.10 |                        30,378 |           62 |
| #30  | GLM-5.3 Flash Max           |                  63.4% |       $0.48 |                        67,491 |          123 |
| #31  | DeepSeek V4 Pro Max         |                  62.8% |       $0.24 |                       101,214 |          155 |
| #32  | GPT-5.6 Sol Medium          |                  61.1% |       $1.86 |                        17,645 |           31 |
| #33  | GPT-5.6 Terra Extra High    |                  60.2% |       $2.13 |                        38,006 |           43 |
| #34  | Claude Fable 5 Low          |                  59.6% |       $3.76 |                        22,339 |           38 |
| #35  | Claude Opus 4.8 Max         |                  59.0% |      $13.22 |                       129,180 |          120 |
| #36  | Claude Opus 5 Low           |                  58.1% |       $1.66 |                        17,613 |           36 |
| #37  | Qwen3.8 Max Extra High      |                  57.5% |       $3.73 |                        89,729 |          111 |
| #38  | GPT-5.6 Luna Extra High     |                  56.9% |       $1.54 |                        42,374 |           71 |
| #39  | Muse Spark 1.2 Extra High   |                  54.9% |       $3.70 |                        81,250 |          101 |
| #40  | Claude Opus 4.8 Extra High  |                  54.4% |       $8.01 |                        77,961 |           95 |
| #41  | GPT-5.5 Medium              |                  54.0% |       $2.75 |                        18,737 |           46 |
| #42  | GPT-5.6 Terra High          |                  53.8% |       $1.13 |                        20,866 |           34 |
| #43  | Gemini 3.7 Flash Low        |                  53.8% |       $1.83 |                        73,220 |          130 |
| #44  | Grok 4.5 High               |                  53.8% |       $2.42 |                        34,250 |           61 |
| #45  | Claude Sonnet 5 Max         |                  53.8% |      $26.40 |                       203,918 |          268 |
| #46  | DeepSeek V4 Flash Max       |                  53.3% |       $0.10 |                       104,492 |          153 |
| #47  | Muse Spark 1.1 Extra High   |                  53.3% |       $2.36 |                        66,088 |           96 |
| #48  | Claude Opus 4.8 High        |                  51.8% |       $4.28 |                        44,476 |           72 |
| #49  | GPT-5.4 Extra High          |                  51.8% |       $5.65 |                        67,234 |           70 |
| #50  | Claude Sonnet 5 Extra High  |                  49.7% |      $11.89 |                       113,150 |          186 |
| #51  | Claude Opus 4.8 Medium      |                  48.7% |       $3.44 |                        36,648 |           66 |
| #52  | Claude Sonnet 5 High        |                  48.2% |       $7.43 |                        77,993 |          147 |
| #53  | Gemini 3.6 Flash High       |                  46.7% |       $4.42 |                        86,727 |          117 |
| #54  | GPT-5.6 Sol Low             |                  45.4% |       $1.07 |                        10,062 |           23 |
| #55  | GPT-5.6 Luna High           |                  44.2% |       $0.78 |                        24,818 |           49 |
| #56  | GLM-5.2 Max                 |                  43.8% |       $3.92 |                        75,760 |          129 |
| #57  | Grok 4.6 Low                |                  41.6% |       $1.04 |                        14,937 |           44 |
| #58  | Claude Opus 4.8 Low         |                  40.8% |       $2.29 |                        25,291 |           54 |
| #59  | Claude Sonnet 5 Medium      |                  39.8% |       $4.08 |                        50,414 |          108 |
| #60  | GLM-5.2 High                |                  36.3% |       $2.84 |                        48,956 |          122 |
| #61  | Gemini 3.5 Flash High       |                  36.1% |       $3.45 |                        68,910 |          105 |
| #62  | GPT-5.6 Terra Medium        |                  35.1% |       $0.58 |                        11,453 |           25 |
| #63  | Claude Sonnet 5 Low         |                  30.5% |       $2.19 |                        31,478 |           77 |
| #64  | Kimi K2.7 Code Standard     |                  30.5% |       $2.82 |                        54,054 |          149 |
| #65  | Claude Sonnet 4.6 High      |                  29.9% |       $5.52 |                        70,001 |          134 |
| #66  | GPT-5.5 Low                 |                  27.0% |       $1.20 |                         9,020 |           28 |
| #67  | GPT-5.6 Terra Low           |                  24.1% |       $0.43 |                         8,265 |           21 |
| #68  | Gemini 3.1 Pro Preview High |                  11.7% |       $2.14 |                        25,990 |           76 |
| #69  | GPT-5.6 Luna Medium         |                  11.3% |       $0.22 |                         7,918 |           24 |
| #70  | GPT-5.6 Luna Low            |                   1.5% |       $0.07 |                         3,059 |           12 |

> [!NOTE]
> For models evaluated across multiple reasoning effort tiers (Low, Medium, High, Extra High, Max), our standard baseline ranking adopts the **Medium** tier — or the **nearest available tier** for models that were not evaluated at Medium (e.g. `glm-5.3`, `kimi-k3`, and `deepseek-v4-*` were only run at Max; `muse-spark-1.2` at Extra High; `kimi-k2.7-code` has a single Standard configuration). Full breakdowns across all tiers are exported in `derived/task-ranking.json`.

---

## 3. Primary Task-Adjusted Ranking (All Benchmarked Plans)

Ranked primarily by **Effective Cost per Task ($/Task)** (cheapest task first), alongside **Tasks per Dollar** and **Monthly Task Capacity**.

The column **Shift vs Raw** indicates the ranking change compared to the traditional raw token price ($/MTok) ranking:
- **▲ +X**: Model is concise and jumped **up** X spots in cost-effectiveness.
- **▼ -X**: Model is verbose and dropped **down** X spots in cost-effectiveness.

| Rank | Shift vs Raw | Plan Name                     | Served Model      | Fee/mo  | Output Tok/Task | Tasks/Month | Cost / Task | Tasks / $1 | Raw $/MTok |
| :--: | :----------: | ----------------------------- | ----------------- | ------: | --------------: | ----------: | ----------: | ---------: | ---------: |
|  #1  |      —       | ChatGPT Pro 20x               | gpt-5.6-luna      |    $200 |           7,918 |  18,972,215 |    $0.00001 |   94,861.1 |   $0.00133 |
|  #2  |     ▲ +1     | ChatGPT Plus                  | gpt-5.6-luna      |     $20 |           7,918 |     948,598 |    $0.00002 |   47,429.9 |   $0.00266 |
|  #3  |     ▼ -1     | ChatGPT Pro 5x                | gpt-5.6-luna      |    $100 |           7,918 |   4,743,117 |    $0.00002 |   47,431.2 |   $0.00266 |
|  #4  |    ▲ +14     | ChatGPT Pro 20x               | gpt-5.6-terra     |    $200 |          11,453 |   2,178,923 |    $0.00009 |   10,894.6 |   $0.00801 |
|  #5  |    ▲ +38     | Command Code GOAT             | gpt-5.6-luna      |     $10 |           7,918 |      83,089 |    $0.00012 |    8,308.9 |   $0.01520 |
|  #6  |    ▲ +51     | OpenCode Go                   | gpt-5.6-luna      |     $10 |           7,918 |      62,314 |    $0.00016 |    6,231.4 |   $0.02027 |
|  #7  |    ▲ +41     | ChatGPT Plus                  | gpt-5.6-terra     |     $20 |          11,453 |     104,034 |    $0.00019 |    5,201.7 |   $0.01679 |
|  #8  |    ▲ +41     | ChatGPT Pro 5x                | gpt-5.6-terra     |    $100 |          11,453 |     520,161 |    $0.00019 |    5,201.6 |   $0.01679 |
|  #9  |     ▼ -5     | GLM Coding Pro (老客 ¥149) 闲时   | glm-5.3-flash     |  $21.98 |          67,491 |     111,007 |    $0.00020 |    5,050.4 |   $0.00293 |
| #10  |     ▼ -3     | Claude Pro                    | claude-sonnet-5   |     $20 |          50,414 |      93,129 |    $0.00021 |    4,656.4 |   $0.00426 |
| #11  |     ▼ -2     | Claude Max 20x (9/14+)        | claude-sonnet-5   |    $200 |          50,414 |     778,554 |    $0.00026 |    3,892.8 |   $0.00510 |
| #12  |     ▼ -2     | Claude Max 5x (9/14+)         | claude-sonnet-5   |    $100 |          50,414 |     389,277 |    $0.00026 |    3,892.8 |   $0.00510 |
| #13  |     ▼ -8     | GLM Coding Pro (老客 ¥149) 中间值  | glm-5.3-flash     |  $21.98 |          67,491 |      83,256 |    $0.00026 |    3,787.8 |   $0.00391 |
| #14  |     ▼ -8     | GLM Coding Max (老客 ¥469) 闲时   | glm-5.3-flash     |  $69.19 |          67,491 |     259,012 |    $0.00027 |    3,743.5 |   $0.00396 |
| #15  |    ▲ +29     | ChatGPT Pro 20x               | gpt-5.6-sol       |    $200 |          17,645 |     731,199 |    $0.00027 |    3,656.0 |   $0.01550 |
| #16  |    ▲ +10     | Claude Pro                    | claude-opus-5     |     $20 |          33,436 |      56,167 |    $0.00036 |    2,808.4 |   $0.01065 |
| #17  |     ▼ -4     | GLM Coding Max (老客 ¥469) 中间值  | glm-5.3-flash     |  $69.19 |          67,491 |     194,263 |    $0.00036 |    2,807.7 |   $0.00528 |
| #18  |    ▲ +38     | ChatGPT Pro 20x               | gpt-5.5           |    $200 |          18,737 |     532,748 |    $0.00038 |    2,663.7 |   $0.02004 |
| #19  |     ▲ +8     | Claude Pro                    | claude-opus-4.8   |     $20 |          36,648 |      51,244 |    $0.00039 |    2,562.2 |   $0.01065 |
| #20  |     ▼ -6     | GLM Coding Lite (老客 ¥49) 闲时   | glm-5.3-flash     |   $7.23 |          67,491 |      18,506 |    $0.00039 |    2,559.6 |   $0.00579 |
| #21  |     ▼ -6     | GLM Coding Pro (老客 ¥149) 忙时   | glm-5.3-flash     |  $21.98 |          67,491 |      55,504 |    $0.00040 |    2,525.2 |   $0.00587 |
| #22  |    ▲ +13     | Claude Max 20x (9/14+)        | claude-opus-5     |    $200 |          33,436 |     469,554 |    $0.00043 |    2,347.8 |   $0.01274 |
| #23  |    ▲ +13     | Claude Max 5x (9/14+)         | claude-opus-5     |    $100 |          33,436 |     234,777 |    $0.00043 |    2,347.8 |   $0.01274 |
| #24  |    ▲ +13     | Claude Max 20x (9/14+)        | claude-opus-4.8   |    $200 |          36,648 |     428,400 |    $0.00047 |    2,142.0 |   $0.01274 |
| #25  |     ▼ -9     | GLM Coding Lite (老客 ¥49) 中间值  | glm-5.3-flash     |   $7.23 |          67,491 |      13,868 |    $0.00052 |    1,918.2 |   $0.00772 |
| #26  |     ▼ -9     | GLM Coding Max (老客 ¥469) 忙时   | glm-5.3-flash     |  $69.19 |          67,491 |     129,499 |    $0.00053 |    1,871.6 |   $0.00792 |
| #27  |    ▼ -19     | Google AI Ultra 20x           | gemini-3.8-flash  | $199.99 |         120,488 |     371,987 |    $0.00054 |    1,860.0 |   $0.00446 |
| #28  |    ▼ -16     | Ollama Pro                    | deepseek-v4-flash |     $20 |         104,492 |      36,832 |    $0.00054 |    1,841.6 |   $0.00520 |
| #29  |    ▼ -18     | Ollama Max                    | deepseek-v4-flash |    $100 |         104,492 |     184,159 |    $0.00054 |    1,841.6 |   $0.00520 |
| #30  |    ▲ +48     | ChatGPT Plus                  | gpt-5.6-sol       |     $20 |          17,645 |      34,911 |    $0.00057 |    1,745.5 |   $0.03247 |
| #31  |    ▲ +48     | ChatGPT Pro 5x                | gpt-5.6-sol       |    $100 |          17,645 |     174,554 |    $0.00057 |    1,745.5 |   $0.03247 |
| #32  |    ▼ -13     | Command Code GOAT             | glm-5.3-flash     |     $10 |          67,491 |      16,765 |    $0.00060 |    1,676.5 |   $0.00884 |
| #33  |    ▼ -10     | GLM Coding Max (新客 ¥1078) 闲时  | glm-5.3-flash     | $159.03 |          67,491 |     259,012 |    $0.00061 |    1,628.7 |   $0.00910 |
| #34  |    ▼ -10     | GLM Coding Max ($168) 闲时      | glm-5.3-flash     |    $168 |          67,491 |     259,012 |    $0.00065 |    1,541.7 |   $0.00961 |
| #35  |    ▼ -15     | GLM Coding Pro (老客 ¥149) 闲时   | glm-5.3           |  $21.98 |          74,953 |      32,981 |    $0.00067 |    1,500.5 |   $0.00889 |
| #36  |    ▼ -11     | GLM Coding Pro (新客 ¥538) 闲时   | glm-5.3-flash     |  $79.37 |          67,491 |     111,007 |    $0.00072 |    1,398.6 |   $0.01059 |
| #37  |     ▼ -9     | GLM Coding Pro ($80) 闲时       | glm-5.3-flash     |     $80 |          67,491 |     111,007 |    $0.00072 |    1,387.6 |   $0.01068 |
| #38  |     ▼ -9     | GLM Coding Lite (老客 ¥49) 忙时   | glm-5.3-flash     |   $7.23 |          67,491 |       9,246 |    $0.00078 |    1,278.8 |   $0.01158 |
| #39  |    ▲ +46     | ChatGPT Plus                  | gpt-5.5           |     $20 |          18,737 |      25,436 |    $0.00079 |    1,271.8 |   $0.04196 |
| #40  |    ▲ +46     | ChatGPT Pro 5x                | gpt-5.5           |    $100 |          18,737 |     127,176 |    $0.00079 |    1,271.8 |   $0.04197 |
| #41  |    ▼ -10     | Ollama Pro                    | glm-5.3-flash     |     $20 |          67,491 |      25,148 |    $0.00080 |    1,257.4 |   $0.01178 |
| #42  |    ▼ -12     | Ollama Max                    | glm-5.3-flash     |    $100 |          67,491 |     125,744 |    $0.00080 |    1,257.4 |   $0.01178 |
| #43  |     ▼ -9     | GLM Coding Max (新客 ¥1078) 中间值 | glm-5.3-flash     | $159.03 |          67,491 |     194,263 |    $0.00082 |    1,221.5 |   $0.01213 |
| #44  |     ▼ -6     | GLM Coding Max ($168) 中间值     | glm-5.3-flash     |    $168 |          67,491 |     194,263 |    $0.00086 |    1,156.3 |   $0.01281 |
| #45  |    ▲ +22     | Cursor Ultra                  | grok-4.5          |    $200 |          34,250 |     225,898 |    $0.00089 |    1,129.5 |   $0.02585 |
| #46  |    ▼ -14     | GLM Coding Pro (老客 ¥149) 中间值  | glm-5.3           |  $21.98 |          74,953 |      24,736 |    $0.00089 |    1,125.4 |   $0.01186 |
| #47  |    ▼ -14     | GLM Coding Max (老客 ¥469) 闲时   | glm-5.3           |  $69.19 |          74,953 |      76,968 |    $0.00090 |    1,112.4 |   $0.01199 |
| #48  |     ▼ -9     | GLM Coding Lite (新客 ¥118) 闲时  | glm-5.3-flash     |  $17.41 |          67,491 |      18,506 |    $0.00094 |    1,063.0 |   $0.01394 |
| #49  |     ▼ -9     | GLM Coding Pro (新客 ¥538) 中间值  | glm-5.3-flash     |  $79.37 |          67,491 |      83,256 |    $0.00095 |    1,049.0 |   $0.01412 |
| #50  |     ▼ -9     | GLM Coding Pro ($80) 中间值      | glm-5.3-flash     |     $80 |          67,491 |      83,256 |    $0.00096 |    1,040.7 |   $0.01424 |
| #51  |     ▼ -9     | GLM Coding Lite ($18) 闲时      | glm-5.3-flash     |     $18 |          67,491 |      18,506 |    $0.00097 |    1,028.1 |   $0.01441 |
| #52  |    ▲ +43     | ChatGPT Pro 20x               | gpt-6-astra       |    $200 |          19,006 |     200,568 |    $0.00100 |    1,002.8 |   $0.05247 |
| #53  |    ▼ -32     | Google AI Pro                 | gemini-3.8-flash  |  $19.99 |         120,488 |      18,599 |    $0.00108 |      930.4 |   $0.00892 |
| #54  |    ▼ -32     | Google AI Ultra 5x            | gemini-3.8-flash  |  $99.99 |         120,488 |      92,997 |    $0.00108 |      930.1 |   $0.00892 |
| #55  |     ▲ +3     | Kimi 会员 699                   | kimi-k2.7-code    |     $99 |          54,054 |      87,024 |    $0.00114 |      879.0 |   $0.02105 |
| #56  |     ▼ -9     | GLM Coding Max (老客 ¥469) 中间值  | glm-5.3           |  $69.19 |          74,953 |      57,730 |    $0.00120 |      834.4 |   $0.01599 |
| #57  |     ▼ -5     | GLM Coding Max (新客 ¥1078) 忙时  | glm-5.3-flash     | $159.03 |          67,491 |     129,499 |    $0.00123 |      814.3 |   $0.01820 |
| #58  |     ▼ -5     | GLM Coding Lite (新客 ¥118) 中间值 | glm-5.3-flash     |  $17.41 |          67,491 |      13,868 |    $0.00126 |      796.6 |   $0.01860 |
| #59  |     ▲ +9     | Cursor Ultra                  | grok-4.6          |    $200 |          48,586 |     159,243 |    $0.00126 |      796.2 |   $0.02585 |
| #60  |     ▼ -6     | GLM Coding Max ($168) 忙时      | glm-5.3-flash     |    $168 |          67,491 |     129,499 |    $0.00130 |      770.8 |   $0.01922 |
| #61  |     ▼ -6     | GLM Coding Lite ($18) 中间值     | glm-5.3-flash     |     $18 |          67,491 |      13,868 |    $0.00130 |      770.5 |   $0.01923 |
| #62  |    ▼ -12     | GLM Coding Lite (老客 ¥49) 闲时   | glm-5.3           |   $7.23 |          74,953 |       5,497 |    $0.00131 |      760.3 |   $0.01754 |
| #63  |    ▼ -12     | GLM Coding Pro (老客 ¥149) 忙时   | glm-5.3           |  $21.98 |          74,953 |      16,490 |    $0.00133 |      750.2 |   $0.01778 |
| #64  |     ▲ +2     | Kimi 会员 199                   | kimi-k2.7-code    |     $39 |          54,054 |      29,008 |    $0.00134 |      743.8 |   $0.02487 |
| #65  |     ▲ +8     | Cursor Pro+                   | grok-4.6          |     $60 |          48,586 |      42,465 |    $0.00141 |      707.7 |   $0.02908 |
| #66  |     ▼ -7     | GLM Coding Pro (新客 ¥538) 忙时   | glm-5.3-flash     |  $79.37 |          67,491 |      55,504 |    $0.00143 |      699.3 |   $0.02119 |
| #67  |     ▼ -7     | GLM Coding Pro ($80) 忙时       | glm-5.3-flash     |     $80 |          67,491 |      55,504 |    $0.00144 |      693.8 |   $0.02136 |
| #68  |     ▼ -5     | OpenCode Go                   | glm-5.3-flash     |     $10 |          67,491 |       6,287 |    $0.00159 |      628.7 |   $0.02357 |
| #69  |    ▼ -24     | Ollama Pro                    | deepseek-v4-pro   |     $20 |         101,214 |      12,417 |    $0.00161 |      620.9 |   $0.01591 |
| #70  |    ▼ -24     | Ollama Max                    | deepseek-v4-pro   |    $100 |         101,214 |      62,086 |    $0.00161 |      620.9 |   $0.01591 |
| #71  |    ▼ -10     | Kimi 会员 699                   | kimi-k3           |     $99 |          75,383 |      57,745 |    $0.00171 |      583.3 |   $0.02274 |
| #72  |    ▼ -10     | GLM Coding Lite (老客 ¥49) 中间值  | glm-5.3           |   $7.23 |          74,953 |       4,123 |    $0.00175 |      570.2 |   $0.02339 |
| #73  |     ▼ -8     | GLM Coding Max (老客 ¥469) 忙时   | glm-5.3           |  $69.19 |          74,953 |      38,477 |    $0.00180 |      556.1 |   $0.02399 |
| #74  |     ▼ -3     | GLM Coding Lite (新客 ¥118) 忙时  | glm-5.3-flash     |  $17.41 |          67,491 |       9,246 |    $0.00188 |      531.1 |   $0.02790 |
| #75  |    ▲ +48     | Command Code GOAT             | gpt-5.6-sol       |     $10 |          17,645 |       5,220 |    $0.00192 |      522.0 |   $0.10858 |
| #76  |     ▼ -4     | GLM Coding Lite ($18) 忙时      | glm-5.3-flash     |     $18 |          67,491 |       9,246 |    $0.00195 |      513.6 |   $0.02885 |
| #77  |    ▲ +25     | SuperGrok Heavy               | grok-4.5          |    $300 |          34,250 |     148,613 |    $0.00202 |      495.4 |   $0.05894 |
| #78  |    ▲ +25     | SuperGrok                     | grok-4.5          |     $30 |          34,250 |      14,861 |    $0.00202 |      495.4 |   $0.05894 |
| #79  |    ▼ -10     | Kimi 会员 199                   | kimi-k3           |     $39 |          75,383 |      19,248 |    $0.00203 |      493.5 |   $0.02688 |
| #80  |     ▲ +2     | OpenCode Go                   | kimi-k2.7-code    |     $10 |          54,054 |       4,867 |    $0.00205 |      486.7 |   $0.03801 |
| #81  |     ▲ +2     | Command Code GOAT             | kimi-k2.7-code    |     $10 |          54,054 |       4,867 |    $0.00205 |      486.7 |   $0.03801 |
| #82  |    ▼ -12     | GLM Coding Max (新客 ¥1078) 闲时  | glm-5.3           | $159.03 |          74,953 |      76,968 |    $0.00207 |      484.0 |   $0.02757 |
| #83  |     ▲ +5     | Cursor Pro                    | grok-4.6          |     $20 |          48,586 |       9,674 |    $0.00207 |      483.7 |   $0.04255 |
| #84  |    ▲ +40     | ChatGPT Pro 5x                | gpt-6-astra       |    $100 |          19,006 |      47,880 |    $0.00209 |      478.8 |   $0.10989 |
| #85  |     ▲ +7     | Command Code GOAT             | glm-5.2           |     $10 |          48,956 |       4,625 |    $0.00216 |      462.5 |   $0.04417 |
| #86  |    ▼ -12     | GLM Coding Max ($168) 闲时      | glm-5.3           |    $168 |          74,953 |      76,968 |    $0.00218 |      458.1 |   $0.02912 |
| #87  |     ▲ +6     | SuperGrok Plus                | grok-4.6          |    $100 |          48,586 |      41,987 |    $0.00238 |      419.9 |   $0.04902 |
| #88  |    ▲ +37     | ChatGPT Plus                  | gpt-6-astra       |     $20 |          19,006 |       8,366 |    $0.00239 |      418.3 |   $0.12579 |
| #89  |    ▼ -13     | GLM Coding Pro (新客 ¥538) 闲时   | glm-5.3           |  $79.37 |          74,953 |      32,981 |    $0.00241 |      415.5 |   $0.03211 |
| #90  |    ▼ -26     | Command Code GOAT             | deepseek-v4-pro   |     $10 |         101,214 |       4,139 |    $0.00242 |      413.9 |   $0.02387 |
| #91  |    ▼ -14     | GLM Coding Pro ($80) 闲时       | glm-5.3           |     $80 |          74,953 |      32,981 |    $0.00243 |      412.3 |   $0.03236 |
| #92  |     ▲ +2     | OpenCode Go                   | glm-5.2           |     $10 |          48,956 |       3,963 |    $0.00252 |      396.3 |   $0.05155 |
| #93  |    ▼ -13     | GLM Coding Lite (老客 ¥49) 忙时   | glm-5.3           |   $7.23 |          74,953 |       2,748 |    $0.00263 |      380.1 |   $0.03509 |
| #94  |    ▼ -13     | GLM Coding Max (新客 ¥1078) 中间值 | glm-5.3           | $159.03 |          74,953 |      57,730 |    $0.00276 |      363.0 |   $0.03675 |
| #95  |     ▲ +9     | SuperGrok                     | grok-4.6          |     $30 |          48,586 |      10,476 |    $0.00286 |      349.2 |   $0.05894 |
| #96  |     ▲ +9     | SuperGrok Heavy               | grok-4.6          |    $300 |          48,586 |     104,763 |    $0.00286 |      349.2 |   $0.05894 |
| #97  |    ▼ -13     | GLM Coding Max ($168) 中间值     | glm-5.3           |    $168 |          74,953 |      57,730 |    $0.00291 |      343.6 |   $0.03883 |
| #98  |    ▲ +11     | Cursor Ultra (Fast)           | grok-4.6          |    $200 |          48,586 |      63,269 |    $0.00316 |      316.3 |   $0.06506 |
| #99  |    ▼ -12     | GLM Coding Lite (新客 ¥118) 闲时  | glm-5.3           |  $17.41 |          74,953 |       5,497 |    $0.00317 |      315.7 |   $0.04225 |
| #100 |    ▼ -11     | GLM Coding Pro (新客 ¥538) 中间值  | glm-5.3           |  $79.37 |          74,953 |      24,736 |    $0.00321 |      311.6 |   $0.04281 |
| #101 |    ▼ -26     | OpenCode Go                   | deepseek-v4-pro   |     $10 |         101,214 |       3,104 |    $0.00322 |      310.4 |   $0.03183 |
| #102 |    ▼ -12     | GLM Coding Pro ($80) 中间值      | glm-5.3           |     $80 |          74,953 |      24,736 |    $0.00323 |      309.2 |   $0.04315 |
| #103 |     ▲ +8     | SuperGrok Lite                | grok-4.6          |     $10 |          48,586 |       3,087 |    $0.00324 |      308.7 |   $0.06667 |
| #104 |     ▲ +2     | Kimi 会员 99                    | kimi-k2.7-code    |     $19 |          54,054 |       5,809 |    $0.00327 |      305.7 |   $0.06051 |
| #105 |    ▼ -14     | GLM Coding Lite ($18) 闲时      | glm-5.3           |     $18 |          74,953 |       5,497 |    $0.00328 |      305.4 |   $0.04369 |
| #106 |    ▲ +25     | Devin Max                     | gpt-6-astra       |    $200 |          19,006 |      58,666 |    $0.00341 |      293.3 |   $0.17937 |
| #107 |    ▲ +15     | Claude Max 5x (9/14+)         | claude-fable-5    |    $100 |          35,970 |      25,674 |    $0.00390 |      256.7 |   $0.10828 |
| #108 |     ▲ +4     | Ollama Pro                    | kimi-k2.7-code    |     $20 |          54,054 |       4,867 |    $0.00411 |      243.4 |   $0.07602 |
| #109 |     ▲ +4     | Ollama Max                    | kimi-k2.7-code    |    $100 |          54,054 |      24,337 |    $0.00411 |      243.4 |   $0.07602 |
| #110 |    ▼ -12     | GLM Coding Max (新客 ¥1078) 忙时  | glm-5.3           | $159.03 |          74,953 |      38,477 |    $0.00413 |      242.0 |   $0.05514 |
| #111 |    ▼ -12     | GLM Coding Lite (新客 ¥118) 中间值 | glm-5.3           |  $17.41 |          74,953 |       4,123 |    $0.00422 |      236.8 |   $0.05633 |
| #112 |    ▼ -12     | GLM Coding Lite ($18) 中间值     | glm-5.3           |     $18 |          74,953 |       4,123 |    $0.00437 |      229.0 |   $0.05825 |
| #113 |    ▼ -12     | GLM Coding Max ($168) 忙时      | glm-5.3           |    $168 |          74,953 |      38,477 |    $0.00437 |      229.0 |   $0.05825 |
| #114 |     ▼ -7     | GLM Coding Pro (新客 ¥538) 忙时   | glm-5.3           |  $79.37 |          74,953 |      16,490 |    $0.00481 |      207.8 |   $0.06421 |
| #115 |    ▼ -19     | Command Code GOAT             | gemini-3.7-flash  |     $10 |          87,640 |       2,070 |    $0.00483 |      207.0 |   $0.05513 |
| #116 |     ▼ -8     | GLM Coding Pro ($80) 忙时       | glm-5.3           |     $80 |          74,953 |      16,490 |    $0.00485 |      206.1 |   $0.06472 |
| #117 |     ▼ -7     | Kimi 会员 99                    | kimi-k3           |     $19 |          75,383 |       3,847 |    $0.00494 |      202.5 |   $0.06552 |
| #118 |     ▼ -2     | Kimi 会员 49                    | kimi-k2.7-code    |   $7.23 |          54,054 |       1,443 |    $0.00501 |      199.6 |   $0.09267 |
| #119 |     ▼ -1     | Ollama Max                    | glm-5.2           |    $100 |          48,956 |      19,818 |    $0.00505 |      198.2 |   $0.10307 |
| #120 |      —       | Ollama Pro                    | glm-5.2           |     $20 |          48,956 |       3,963 |    $0.00505 |      198.1 |   $0.10309 |
| #121 |     ▲ +9     | Claude Max 20x (9/14+)        | claude-fable-5    |    $200 |          35,970 |      33,575 |    $0.00596 |      167.9 |   $0.16560 |
| #122 |     ▼ -8     | GLM Coding Lite (新客 ¥118) 忙时  | glm-5.3           |  $17.41 |          74,953 |       2,748 |    $0.00634 |      157.9 |   $0.08450 |
| #123 |     ▼ -8     | GLM Coding Lite ($18) 忙时      | glm-5.3           |     $18 |          74,953 |       2,748 |    $0.00655 |      152.7 |   $0.08738 |
| #124 |    ▼ -27     | Command Code GOAT             | gemini-3.8-flash  |     $10 |         120,488 |       1,506 |    $0.00664 |      150.6 |   $0.05513 |
| #125 |     ▼ -6     | Ollama Max                    | glm-5.3           |    $100 |          74,953 |      12,944 |    $0.00773 |      129.4 |   $0.10307 |
| #126 |     ▼ -5     | Ollama Pro                    | glm-5.3           |     $20 |          74,953 |       2,588 |    $0.00773 |      129.4 |   $0.10309 |
| #127 |    ▼ -10     | Command Code GOAT             | muse-spark-1.2    |     $10 |          81,250 |       1,243 |    $0.00805 |      124.3 |   $0.09901 |
| #128 |     ▲ +7     | Command Code GOAT             | grok-4.5          |     $10 |          34,250 |       1,034 |    $0.00967 |      103.4 |   $0.28249 |
| #129 |     ▼ -3     | Ollama Pro                    | kimi-k3           |     $20 |          75,383 |       1,805 |    $0.01108 |       90.3 |   $0.14695 |
| #130 |     ▼ -3     | Ollama Max                    | kimi-k3           |    $100 |          75,383 |       9,025 |    $0.01108 |       90.2 |   $0.14699 |
| #131 |     ▼ -3     | Command Code GOAT             | glm-5.3           |     $10 |          74,953 |         863 |    $0.01158 |       86.3 |   $0.15456 |
| #132 |     ▲ +4     | Command Code GOAT             | grok-4.6          |     $10 |          48,586 |         729 |    $0.01372 |       72.9 |   $0.28249 |
| #133 |     ▼ -4     | Command Code GOAT             | qwen3.8-max       |     $10 |          89,729 |         691 |    $0.01447 |       69.1 |   $0.16129 |
| #134 |     ▼ -2     | OpenCode Go                   | glm-5.3           |     $10 |          74,953 |         647 |    $0.01545 |       64.7 |   $0.20619 |
| #135 |     ▼ -1     | Command Code GOAT             | kimi-k3           |     $10 |          75,383 |         602 |    $0.01660 |       60.2 |   $0.22026 |
| #136 |     ▲ +2     | OpenCode Go                   | grok-4.6          |     $10 |          48,586 |         545 |    $0.01833 |       54.5 |   $0.37736 |
| #137 |     ▼ -4     | OpenCode Go                   | qwen3.8-max       |     $10 |          89,729 |         518 |    $0.01930 |       51.8 |   $0.21505 |
| #138 |     ▼ -1     | OpenCode Go                   | kimi-k3           |     $10 |          75,383 |         451 |    $0.02217 |       45.1 |   $0.29412 |

> [!NOTE]
> **Looking for all reasoning effort configurations?** We evaluate and rank all **291 plan × effort combinations** across Low, Medium, High, Extra High, and Max tiers. See the complete export in [`derived/task-ranking-all-efforts.csv`](derived/task-ranking-all-efforts.csv) and [`derived/task-ranking-all-efforts.json`](derived/task-ranking-all-efforts.json), and explore all 291 combinations directly in the interactive web interface (`web/index.html`), which ranks all efforts by default.

---

## 4. Annual Pricing & Discount Comparison

When paid annually, subscriptions with discounts become significantly more cost-effective per completed task. Below are the plans offering explicit annual discounts, showing how their effective monthly fee, $/task, and rankings improve:

| Plan Name                     | Served Model      | Monthly Fee | Annual Total | Eff. Monthly | Discount | Monthly Rank | Annual Rank | Shift | Monthly $/Task | Annual $/Task |
| ----------------------------- | ----------------- | ----------: | -----------: | -----------: | :------: | :----------: | :---------: | :---: | -------------: | ------------: |
| GLM Coding Pro (老客 ¥149) 闲时   | glm-5.3-flash     |      $21.98 |      $211.01 |       $17.58 |  -20.0%  |      #9      |      #6     |  ▲ +3 |       $0.00020 |      $0.00016 |
| Claude Pro                    | claude-sonnet-5   |      $20.00 |      $200.00 |       $16.67 |  -16.7%  |     #10      |      #8     |  ▲ +2 |       $0.00021 |      $0.00018 |
| GLM Coding Pro (老客 ¥149) 中间值  | glm-5.3-flash     |      $21.98 |      $211.01 |       $17.58 |  -20.0%  |     #13      |     #11     |  ▲ +2 |       $0.00026 |      $0.00021 |
| GLM Coding Max (老客 ¥469) 闲时   | glm-5.3-flash     |      $69.19 |      $664.22 |       $55.35 |  -20.0%  |     #14      |     #12     |  ▲ +2 |       $0.00027 |      $0.00021 |
| GLM Coding Max (老客 ¥469) 中间值  | glm-5.3-flash     |      $69.19 |      $664.22 |       $55.35 |  -20.0%  |     #17      |     #16     |  ▲ +1 |       $0.00036 |      $0.00028 |
| Claude Pro                    | claude-opus-5     |      $20.00 |      $200.00 |       $16.67 |  -16.7%  |     #16      |     #17     |  ▼ -1 |       $0.00036 |      $0.00030 |
| GLM Coding Lite (老客 ¥49) 闲时   | glm-5.3-flash     |       $7.23 |       $69.41 |        $5.78 |  -20.0%  |     #20      |     #18     |  ▲ +2 |       $0.00039 |      $0.00031 |
| GLM Coding Pro (老客 ¥149) 忙时   | glm-5.3-flash     |      $21.98 |      $211.01 |       $17.58 |  -20.0%  |     #21      |     #19     |  ▲ +2 |       $0.00040 |      $0.00032 |
| Claude Pro                    | claude-opus-4.8   |      $20.00 |      $200.00 |       $16.67 |  -16.7%  |     #19      |     #20     |  ▼ -1 |       $0.00039 |      $0.00032 |
| GLM Coding Lite (老客 ¥49) 中间值  | glm-5.3-flash     |       $7.23 |       $69.41 |        $5.78 |  -20.0%  |     #25      |     #22     |  ▲ +3 |       $0.00052 |      $0.00042 |
| GLM Coding Max (老客 ¥469) 忙时   | glm-5.3-flash     |      $69.19 |      $664.22 |       $55.35 |  -20.0%  |     #26      |     #25     |  ▲ +1 |       $0.00053 |      $0.00043 |
| Ollama Pro                    | deepseek-v4-flash |      $20.00 |      $200.00 |       $16.67 |  -16.7%  |     #28      |     #26     |  ▲ +2 |       $0.00054 |      $0.00045 |
| GLM Coding Max ($168) 闲时      | glm-5.3-flash     |     $168.00 |     $1411.20 |      $117.60 |  -30.0%  |     #34      |     #27     |  ▲ +7 |       $0.00065 |      $0.00045 |
| GLM Coding Max (新客 ¥1078) 闲时  | glm-5.3-flash     |     $159.03 |     $1526.69 |      $127.22 |  -20.0%  |     #33      |     #29     |  ▲ +4 |       $0.00061 |      $0.00049 |
| GLM Coding Pro ($80) 闲时       | glm-5.3-flash     |      $80.00 |      $672.00 |       $56.00 |  -30.0%  |     #37      |     #30     |  ▲ +7 |       $0.00072 |      $0.00050 |
| GLM Coding Pro (老客 ¥149) 闲时   | glm-5.3           |      $21.98 |      $211.01 |       $17.58 |  -20.0%  |     #35      |     #31     |  ▲ +4 |       $0.00067 |      $0.00053 |
| GLM Coding Pro (新客 ¥538) 闲时   | glm-5.3-flash     |      $79.37 |      $761.95 |       $63.50 |  -20.0%  |     #36      |     #34     |  ▲ +2 |       $0.00072 |      $0.00057 |
| GLM Coding Max ($168) 中间值     | glm-5.3-flash     |     $168.00 |     $1411.20 |      $117.60 |  -30.0%  |     #44      |     #38     |  ▲ +6 |       $0.00086 |      $0.00060 |
| GLM Coding Lite (老客 ¥49) 忙时   | glm-5.3-flash     |       $7.23 |       $69.41 |        $5.78 |  -20.0%  |     #38      |     #39     |  ▼ -1 |       $0.00078 |      $0.00063 |
| GLM Coding Max (新客 ¥1078) 中间值 | glm-5.3-flash     |     $159.03 |     $1526.69 |      $127.22 |  -20.0%  |     #43      |     #40     |  ▲ +3 |       $0.00082 |      $0.00065 |
| Ollama Pro                    | glm-5.3-flash     |      $20.00 |      $200.00 |       $16.67 |  -16.7%  |     #41      |     #41     |   —   |       $0.00080 |      $0.00066 |
| GLM Coding Pro ($80) 中间值      | glm-5.3-flash     |      $80.00 |      $672.00 |       $56.00 |  -30.0%  |     #50      |     #42     |  ▲ +8 |       $0.00096 |      $0.00067 |
| GLM Coding Lite ($18) 闲时      | glm-5.3-flash     |      $18.00 |      $151.20 |       $12.60 |  -30.0%  |     #51      |     #43     |  ▲ +8 |       $0.00097 |      $0.00068 |
| Cursor Ultra                  | grok-4.5          |     $200.00 |     $1920.00 |      $160.00 |  -20.0%  |     #45      |     #44     |  ▲ +1 |       $0.00089 |      $0.00071 |
| GLM Coding Pro (老客 ¥149) 中间值  | glm-5.3           |      $21.98 |      $211.01 |       $17.58 |  -20.0%  |     #46      |     #45     |  ▲ +1 |       $0.00089 |      $0.00071 |
| GLM Coding Max (老客 ¥469) 闲时   | glm-5.3           |      $69.19 |      $664.22 |       $55.35 |  -20.0%  |     #47      |     #46     |  ▲ +1 |       $0.00090 |      $0.00072 |
| GLM Coding Lite (新客 ¥118) 闲时  | glm-5.3-flash     |      $17.41 |      $167.14 |       $13.93 |  -20.0%  |     #48      |     #47     |  ▲ +1 |       $0.00094 |      $0.00075 |
| GLM Coding Pro (新客 ¥538) 中间值  | glm-5.3-flash     |      $79.37 |      $761.95 |       $63.50 |  -20.0%  |     #49      |     #48     |  ▲ +1 |       $0.00095 |      $0.00076 |
| GLM Coding Max ($168) 忙时      | glm-5.3-flash     |     $168.00 |     $1411.20 |      $117.60 |  -30.0%  |     #60      |     #52     |  ▲ +8 |       $0.00130 |      $0.00091 |
| GLM Coding Lite ($18) 中间值     | glm-5.3-flash     |      $18.00 |      $151.20 |       $12.60 |  -30.0%  |     #61      |     #53     |  ▲ +8 |       $0.00130 |      $0.00091 |
| Kimi 会员 699                   | kimi-k2.7-code    |      $99.00 |      $950.40 |       $79.20 |  -20.0%  |     #55      |     #54     |  ▲ +1 |       $0.00114 |      $0.00091 |
| GLM Coding Max (老客 ¥469) 中间值  | glm-5.3           |      $69.19 |      $664.22 |       $55.35 |  -20.0%  |     #56      |     #55     |  ▲ +1 |       $0.00120 |      $0.00096 |
| GLM Coding Max (新客 ¥1078) 忙时  | glm-5.3-flash     |     $159.03 |     $1526.69 |      $127.22 |  -20.0%  |     #57      |     #56     |  ▲ +1 |       $0.00123 |      $0.00098 |
| GLM Coding Lite (新客 ¥118) 中间值 | glm-5.3-flash     |      $17.41 |      $167.14 |       $13.93 |  -20.0%  |     #58      |     #58     |   —   |       $0.00126 |      $0.00100 |
| Cursor Ultra                  | grok-4.6          |     $200.00 |     $1920.00 |      $160.00 |  -20.0%  |     #59      |     #59     |   —   |       $0.00126 |      $0.00101 |
| GLM Coding Pro ($80) 忙时       | glm-5.3-flash     |      $80.00 |      $672.00 |       $56.00 |  -30.0%  |     #67      |     #60     |  ▲ +7 |       $0.00144 |      $0.00101 |
| GLM Coding Lite (老客 ¥49) 闲时   | glm-5.3           |       $7.23 |       $69.41 |        $5.78 |  -20.0%  |     #62      |     #61     |  ▲ +1 |       $0.00131 |      $0.00105 |
| GLM Coding Pro (老客 ¥149) 忙时   | glm-5.3           |      $21.98 |      $211.01 |       $17.58 |  -20.0%  |     #63      |     #62     |  ▲ +1 |       $0.00133 |      $0.00107 |
| Kimi 会员 199                   | kimi-k2.7-code    |      $39.00 |      $374.40 |       $31.20 |  -20.0%  |     #64      |     #65     |  ▼ -1 |       $0.00134 |      $0.00108 |
| Cursor Pro+                   | grok-4.6          |      $60.00 |      $576.00 |       $48.00 |  -20.0%  |     #65      |     #66     |  ▼ -1 |       $0.00141 |      $0.00113 |
| GLM Coding Pro (新客 ¥538) 忙时   | glm-5.3-flash     |      $79.37 |      $761.95 |       $63.50 |  -20.0%  |     #66      |     #67     |  ▼ -1 |       $0.00143 |      $0.00114 |
| Ollama Pro                    | deepseek-v4-pro   |      $20.00 |      $200.00 |       $16.67 |  -16.7%  |     #69      |     #68     |  ▲ +1 |       $0.00161 |      $0.00134 |
| GLM Coding Lite ($18) 忙时      | glm-5.3-flash     |      $18.00 |      $151.20 |       $12.60 |  -30.0%  |     #76      |     #69     |  ▲ +7 |       $0.00195 |      $0.00136 |
| Kimi 会员 699                   | kimi-k3           |      $99.00 |      $950.40 |       $79.20 |  -20.0%  |     #71      |     #70     |  ▲ +1 |       $0.00171 |      $0.00137 |
| GLM Coding Lite (老客 ¥49) 中间值  | glm-5.3           |       $7.23 |       $69.41 |        $5.78 |  -20.0%  |     #72      |     #71     |  ▲ +1 |       $0.00175 |      $0.00140 |
| GLM Coding Max (老客 ¥469) 忙时   | glm-5.3           |      $69.19 |      $664.22 |       $55.35 |  -20.0%  |     #73      |     #72     |  ▲ +1 |       $0.00180 |      $0.00144 |
| GLM Coding Lite (新客 ¥118) 忙时  | glm-5.3-flash     |      $17.41 |      $167.14 |       $13.93 |  -20.0%  |     #74      |     #73     |  ▲ +1 |       $0.00188 |      $0.00151 |
| GLM Coding Max ($168) 闲时      | glm-5.3           |     $168.00 |     $1411.20 |      $117.60 |  -30.0%  |     #86      |     #74     | ▲ +12 |       $0.00218 |      $0.00153 |
| Kimi 会员 199                   | kimi-k3           |      $39.00 |      $374.40 |       $31.20 |  -20.0%  |     #79      |     #77     |  ▲ +2 |       $0.00203 |      $0.00162 |
| GLM Coding Max (新客 ¥1078) 闲时  | glm-5.3           |     $159.03 |     $1526.69 |      $127.22 |  -20.0%  |     #82      |     #78     |  ▲ +4 |       $0.00207 |      $0.00165 |
| Cursor Pro                    | grok-4.6          |      $20.00 |      $192.00 |       $16.00 |  -20.0%  |     #83      |     #79     |  ▲ +4 |       $0.00207 |      $0.00165 |
| SuperGrok Heavy               | grok-4.5          |     $300.00 |     $3000.00 |      $250.00 |  -16.7%  |     #77      |     #80     |  ▼ -3 |       $0.00202 |      $0.00168 |
| SuperGrok                     | grok-4.5          |      $30.00 |      $300.00 |       $25.00 |  -16.7%  |     #78      |     #81     |  ▼ -3 |       $0.00202 |      $0.00168 |
| GLM Coding Pro ($80) 闲时       | glm-5.3           |      $80.00 |      $672.00 |       $56.00 |  -30.0%  |     #91      |     #82     |  ▲ +9 |       $0.00243 |      $0.00170 |
| GLM Coding Pro (新客 ¥538) 闲时   | glm-5.3           |      $79.37 |      $761.95 |       $63.50 |  -20.0%  |     #89      |     #84     |  ▲ +5 |       $0.00241 |      $0.00193 |
| GLM Coding Max ($168) 中间值     | glm-5.3           |     $168.00 |     $1411.20 |      $117.60 |  -30.0%  |     #97      |     #85     | ▲ +12 |       $0.00291 |      $0.00204 |
| GLM Coding Lite (老客 ¥49) 忙时   | glm-5.3           |       $7.23 |       $69.41 |        $5.78 |  -20.0%  |     #93      |     #89     |  ▲ +4 |       $0.00263 |      $0.00211 |
| GLM Coding Max (新客 ¥1078) 中间值 | glm-5.3           |     $159.03 |     $1526.69 |      $127.22 |  -20.0%  |     #94      |     #91     |  ▲ +3 |       $0.00276 |      $0.00220 |
| GLM Coding Pro ($80) 中间值      | glm-5.3           |      $80.00 |      $672.00 |       $56.00 |  -30.0%  |     #102     |     #92     | ▲ +10 |       $0.00323 |      $0.00226 |
| GLM Coding Lite ($18) 闲时      | glm-5.3           |      $18.00 |      $151.20 |       $12.60 |  -30.0%  |     #105     |     #93     | ▲ +12 |       $0.00328 |      $0.00229 |
| SuperGrok                     | grok-4.6          |      $30.00 |      $300.00 |       $25.00 |  -16.7%  |     #95      |     #95     |   —   |       $0.00286 |      $0.00239 |
| SuperGrok Heavy               | grok-4.6          |     $300.00 |     $3000.00 |      $250.00 |  -16.7%  |     #96      |     #96     |   —   |       $0.00286 |      $0.00239 |
| Cursor Ultra (Fast)           | grok-4.6          |     $200.00 |     $1920.00 |      $160.00 |  -20.0%  |     #98      |     #100    |  ▼ -2 |       $0.00316 |      $0.00253 |
| GLM Coding Lite (新客 ¥118) 闲时  | glm-5.3           |      $17.41 |      $167.14 |       $13.93 |  -20.0%  |     #99      |     #101    |  ▼ -2 |       $0.00317 |      $0.00253 |
| GLM Coding Pro (新客 ¥538) 中间值  | glm-5.3           |      $79.37 |      $761.95 |       $63.50 |  -20.0%  |     #100     |     #102    |  ▼ -2 |       $0.00321 |      $0.00257 |
| Kimi 会员 99                    | kimi-k2.7-code    |      $19.00 |      $182.40 |       $15.20 |  -20.0%  |     #104     |     #103    |  ▲ +1 |       $0.00327 |      $0.00262 |
| GLM Coding Lite ($18) 中间值     | glm-5.3           |      $18.00 |      $151.20 |       $12.60 |  -30.0%  |     #112     |     #104    |  ▲ +8 |       $0.00437 |      $0.00306 |
| GLM Coding Max ($168) 忙时      | glm-5.3           |     $168.00 |     $1411.20 |      $117.60 |  -30.0%  |     #113     |     #105    |  ▲ +8 |       $0.00437 |      $0.00306 |
| GLM Coding Max (新客 ¥1078) 忙时  | glm-5.3           |     $159.03 |     $1526.69 |      $127.22 |  -20.0%  |     #110     |     #108    |  ▲ +2 |       $0.00413 |      $0.00331 |
| GLM Coding Lite (新客 ¥118) 中间值 | glm-5.3           |      $17.41 |      $167.14 |       $13.93 |  -20.0%  |     #111     |     #109    |  ▲ +2 |       $0.00422 |      $0.00338 |
| GLM Coding Pro ($80) 忙时       | glm-5.3           |      $80.00 |      $672.00 |       $56.00 |  -30.0%  |     #116     |     #110    |  ▲ +6 |       $0.00485 |      $0.00340 |
| Ollama Pro                    | kimi-k2.7-code    |      $20.00 |      $200.00 |       $16.67 |  -16.7%  |     #108     |     #112    |  ▼ -4 |       $0.00411 |      $0.00342 |
| GLM Coding Pro (新客 ¥538) 忙时   | glm-5.3           |      $79.37 |      $761.95 |       $63.50 |  -20.0%  |     #114     |     #113    |  ▲ +1 |       $0.00481 |      $0.00385 |
| Kimi 会员 99                    | kimi-k3           |      $19.00 |      $182.40 |       $15.20 |  -20.0%  |     #117     |     #115    |  ▲ +2 |       $0.00494 |      $0.00395 |
| Kimi 会员 49                    | kimi-k2.7-code    |       $7.23 |       $69.41 |        $5.78 |  -20.0%  |     #118     |     #116    |  ▲ +2 |       $0.00501 |      $0.00401 |
| Ollama Pro                    | glm-5.2           |      $20.00 |      $200.00 |       $16.67 |  -16.7%  |     #120     |     #118    |  ▲ +2 |       $0.00505 |      $0.00421 |
| GLM Coding Lite ($18) 忙时      | glm-5.3           |      $18.00 |      $151.20 |       $12.60 |  -30.0%  |     #123     |     #119    |  ▲ +4 |       $0.00655 |      $0.00458 |
| GLM Coding Lite (新客 ¥118) 忙时  | glm-5.3           |      $17.41 |      $167.14 |       $13.93 |  -20.0%  |     #122     |     #122    |   —   |       $0.00634 |      $0.00507 |
| Ollama Pro                    | glm-5.3           |      $20.00 |      $200.00 |       $16.67 |  -16.7%  |     #126     |     #124    |  ▲ +2 |       $0.00773 |      $0.00644 |
| Ollama Pro                    | kimi-k3           |      $20.00 |      $200.00 |       $16.67 |  -16.7%  |     #129     |     #128    |  ▲ +1 |       $0.01108 |      $0.00923 |

> [!TIP]
> Plans without published annual discounts (e.g. ChatGPT Plus / Pro, Command Code GOAT, OpenCode) maintain the same effective monthly fee ($12 \times$ monthly with 0% discount). Consequently, discounted subscriptions like **Claude Pro** and **GLM Coding Plans** climb several spots under annual billing.

---

## 5. Key Takeaways & Ranking Shifts

1. **The Verbosity Penalty**:
   - Models with large raw token allowances like `gemini-3.8-flash` offer tens of billions of tokens, ranking high on raw $/MTok charts. However, at **120,488 median output tokens/task** (Medium tier), its effective task cost falls behind far more token-efficient models.
   - Conversely, `gpt-5.6-luna` (**7,918 tokens/task**) and `gpt-5.6-terra` (**11,453 tokens/task**) pair DeepSWE-grade competence with extreme token efficiency — `gpt-5.6-terra` plans climb up to **+41 spots** once verbosity is priced in, and Luna plans hold the entire top tier at **~6,200 – 95,000 tasks per dollar** depending on pool size.

2. **The Sweet Spot of Coding Workhorses**:
   - **ChatGPT Pro 20x / 5x / Plus (Luna & Terra)** achieve industry-leading task yields due to high monthly pools paired with low completion overhead.
   - **GLM Coding Pro (`glm-5.3-flash`)** breaks into the top 10 at **67,491 tokens/task** on the strength of its enormous quota — despite mid-pack DeepSWE efficiency (63.4% Pass@1 at Max).
   - **Sonnet 5** (**50,414 tokens/task**) and **Opus 5** (**33,436 tokens/task**) offer high quality at moderate token overhead, climbing past more verbose competitors.

3. **Coverage Flip vs CursorBench**:
   - DeepSWE covers **22 model families with subscription plans** (vs 11 under CursorBench 4.0): DeepSeek V4, Kimi K3 / K2.7 Code, GLM-5.2 / 5.3, Qwen3.8 Max, Claude Opus 4.8 / Opus 5 / Fable 5, GPT-5.5 / 5.6 / 6 Astra, Gemini 3.1–3.8 Flash, Grok 4.5 / 4.6 and Muse Spark 1.2 all enter the ranking.
   - New-model rows without a DeepSWE evaluation — **Claude Opus 5.5 / Fable 5.1, GPT-6 Sol, Grok 4.7, MiMo v2.5/v2.6, Step-5 Preview, DeepSeek V4.1 Flash, SWE-2** — are flagged `[Pending DeepSWE]`; their plan rows carry quota/pricing data but no task-adjusted rank until evaluated.

---

## 5. Rankings by Price Band

### Budget Band: $0 – $30 / month
Tailored for individual developers, students, and freelancers:

| Tier Rank | Plan Name                     | Served Model      | Fee/mo | Output Tok/Task | Tasks/Month | Cost / Task | Tasks / $1 |
| :-------: | ----------------------------- | ----------------- | -----: | --------------: | ----------: | ----------: | ---------: |
|     #1    | ChatGPT Plus                  | gpt-5.6-luna      |    $20 |           7,918 |     948,598 |    $0.00002 |   47,429.9 |
|     #2    | Command Code GOAT             | gpt-5.6-luna      |    $10 |           7,918 |      83,089 |    $0.00012 |    8,308.9 |
|     #3    | OpenCode Go                   | gpt-5.6-luna      |    $10 |           7,918 |      62,314 |    $0.00016 |    6,231.4 |
|     #4    | ChatGPT Plus                  | gpt-5.6-terra     |    $20 |          11,453 |     104,034 |    $0.00019 |    5,201.7 |
|     #5    | GLM Coding Pro (老客 ¥149) 闲时   | glm-5.3-flash     | $21.98 |          67,491 |     111,007 |    $0.00020 |    5,050.4 |
|     #6    | Claude Pro                    | claude-sonnet-5   |    $20 |          50,414 |      93,129 |    $0.00021 |    4,656.4 |
|     #7    | GLM Coding Pro (老客 ¥149) 中间值  | glm-5.3-flash     | $21.98 |          67,491 |      83,256 |    $0.00026 |    3,787.8 |
|     #8    | Claude Pro                    | claude-opus-5     |    $20 |          33,436 |      56,167 |    $0.00036 |    2,808.4 |
|     #9    | Claude Pro                    | claude-opus-4.8   |    $20 |          36,648 |      51,244 |    $0.00039 |    2,562.2 |
|    #10    | GLM Coding Lite (老客 ¥49) 闲时   | glm-5.3-flash     |  $7.23 |          67,491 |      18,506 |    $0.00039 |    2,559.6 |
|    #11    | GLM Coding Pro (老客 ¥149) 忙时   | glm-5.3-flash     | $21.98 |          67,491 |      55,504 |    $0.00040 |    2,525.2 |
|    #12    | GLM Coding Lite (老客 ¥49) 中间值  | glm-5.3-flash     |  $7.23 |          67,491 |      13,868 |    $0.00052 |    1,918.2 |
|    #13    | Ollama Pro                    | deepseek-v4-flash |    $20 |         104,492 |      36,832 |    $0.00054 |    1,841.6 |
|    #14    | ChatGPT Plus                  | gpt-5.6-sol       |    $20 |          17,645 |      34,911 |    $0.00057 |    1,745.5 |
|    #15    | Command Code GOAT             | glm-5.3-flash     |    $10 |          67,491 |      16,765 |    $0.00060 |    1,676.5 |
|    #16    | GLM Coding Pro (老客 ¥149) 闲时   | glm-5.3           | $21.98 |          74,953 |      32,981 |    $0.00067 |    1,500.5 |
|    #17    | GLM Coding Lite (老客 ¥49) 忙时   | glm-5.3-flash     |  $7.23 |          67,491 |       9,246 |    $0.00078 |    1,278.8 |
|    #18    | ChatGPT Plus                  | gpt-5.5           |    $20 |          18,737 |      25,436 |    $0.00079 |    1,271.8 |
|    #19    | Ollama Pro                    | glm-5.3-flash     |    $20 |          67,491 |      25,148 |    $0.00080 |    1,257.4 |
|    #20    | GLM Coding Pro (老客 ¥149) 中间值  | glm-5.3           | $21.98 |          74,953 |      24,736 |    $0.00089 |    1,125.4 |
|    #21    | GLM Coding Lite (新客 ¥118) 闲时  | glm-5.3-flash     | $17.41 |          67,491 |      18,506 |    $0.00094 |    1,063.0 |
|    #22    | GLM Coding Lite ($18) 闲时      | glm-5.3-flash     |    $18 |          67,491 |      18,506 |    $0.00097 |    1,028.1 |
|    #23    | Google AI Pro                 | gemini-3.8-flash  | $19.99 |         120,488 |      18,599 |    $0.00108 |      930.4 |
|    #24    | GLM Coding Lite (新客 ¥118) 中间值 | glm-5.3-flash     | $17.41 |          67,491 |      13,868 |    $0.00126 |      796.6 |
|    #25    | GLM Coding Lite ($18) 中间值     | glm-5.3-flash     |    $18 |          67,491 |      13,868 |    $0.00130 |      770.5 |
|    #26    | GLM Coding Lite (老客 ¥49) 闲时   | glm-5.3           |  $7.23 |          74,953 |       5,497 |    $0.00131 |      760.3 |
|    #27    | GLM Coding Pro (老客 ¥149) 忙时   | glm-5.3           | $21.98 |          74,953 |      16,490 |    $0.00133 |      750.2 |
|    #28    | OpenCode Go                   | glm-5.3-flash     |    $10 |          67,491 |       6,287 |    $0.00159 |      628.7 |
|    #29    | Ollama Pro                    | deepseek-v4-pro   |    $20 |         101,214 |      12,417 |    $0.00161 |      620.9 |
|    #30    | GLM Coding Lite (老客 ¥49) 中间值  | glm-5.3           |  $7.23 |          74,953 |       4,123 |    $0.00175 |      570.2 |
|    #31    | GLM Coding Lite (新客 ¥118) 忙时  | glm-5.3-flash     | $17.41 |          67,491 |       9,246 |    $0.00188 |      531.1 |
|    #32    | Command Code GOAT             | gpt-5.6-sol       |    $10 |          17,645 |       5,220 |    $0.00192 |      522.0 |
|    #33    | GLM Coding Lite ($18) 忙时      | glm-5.3-flash     |    $18 |          67,491 |       9,246 |    $0.00195 |      513.6 |
|    #34    | SuperGrok                     | grok-4.5          |    $30 |          34,250 |      14,861 |    $0.00202 |      495.4 |
|    #35    | OpenCode Go                   | kimi-k2.7-code    |    $10 |          54,054 |       4,867 |    $0.00205 |      486.7 |
|    #36    | Command Code GOAT             | kimi-k2.7-code    |    $10 |          54,054 |       4,867 |    $0.00205 |      486.7 |
|    #37    | Cursor Pro                    | grok-4.6          |    $20 |          48,586 |       9,674 |    $0.00207 |      483.7 |
|    #38    | Command Code GOAT             | glm-5.2           |    $10 |          48,956 |       4,625 |    $0.00216 |      462.5 |
|    #39    | ChatGPT Plus                  | gpt-6-astra       |    $20 |          19,006 |       8,366 |    $0.00239 |      418.3 |
|    #40    | Command Code GOAT             | deepseek-v4-pro   |    $10 |         101,214 |       4,139 |    $0.00242 |      413.9 |
|    #41    | OpenCode Go                   | glm-5.2           |    $10 |          48,956 |       3,963 |    $0.00252 |      396.3 |
|    #42    | GLM Coding Lite (老客 ¥49) 忙时   | glm-5.3           |  $7.23 |          74,953 |       2,748 |    $0.00263 |      380.1 |
|    #43    | SuperGrok                     | grok-4.6          |    $30 |          48,586 |      10,476 |    $0.00286 |      349.2 |
|    #44    | GLM Coding Lite (新客 ¥118) 闲时  | glm-5.3           | $17.41 |          74,953 |       5,497 |    $0.00317 |      315.7 |
|    #45    | OpenCode Go                   | deepseek-v4-pro   |    $10 |         101,214 |       3,104 |    $0.00322 |      310.4 |
|    #46    | SuperGrok Lite                | grok-4.6          |    $10 |          48,586 |       3,087 |    $0.00324 |      308.7 |
|    #47    | Kimi 会员 99                    | kimi-k2.7-code    |    $19 |          54,054 |       5,809 |    $0.00327 |      305.7 |
|    #48    | GLM Coding Lite ($18) 闲时      | glm-5.3           |    $18 |          74,953 |       5,497 |    $0.00328 |      305.4 |
|    #49    | Ollama Pro                    | kimi-k2.7-code    |    $20 |          54,054 |       4,867 |    $0.00411 |      243.4 |
|    #50    | GLM Coding Lite (新客 ¥118) 中间值 | glm-5.3           | $17.41 |          74,953 |       4,123 |    $0.00422 |      236.8 |
|    #51    | GLM Coding Lite ($18) 中间值     | glm-5.3           |    $18 |          74,953 |       4,123 |    $0.00437 |      229.0 |
|    #52    | Command Code GOAT             | gemini-3.7-flash  |    $10 |          87,640 |       2,070 |    $0.00483 |      207.0 |
|    #53    | Kimi 会员 99                    | kimi-k3           |    $19 |          75,383 |       3,847 |    $0.00494 |      202.5 |
|    #54    | Kimi 会员 49                    | kimi-k2.7-code    |  $7.23 |          54,054 |       1,443 |    $0.00501 |      199.6 |
|    #55    | Ollama Pro                    | glm-5.2           |    $20 |          48,956 |       3,963 |    $0.00505 |      198.1 |
|    #56    | GLM Coding Lite (新客 ¥118) 忙时  | glm-5.3           | $17.41 |          74,953 |       2,748 |    $0.00634 |      157.9 |
|    #57    | GLM Coding Lite ($18) 忙时      | glm-5.3           |    $18 |          74,953 |       2,748 |    $0.00655 |      152.7 |
|    #58    | Command Code GOAT             | gemini-3.8-flash  |    $10 |         120,488 |       1,506 |    $0.00664 |      150.6 |
|    #59    | Ollama Pro                    | glm-5.3           |    $20 |          74,953 |       2,588 |    $0.00773 |      129.4 |
|    #60    | Command Code GOAT             | muse-spark-1.2    |    $10 |          81,250 |       1,243 |    $0.00805 |      124.3 |
|    #61    | Command Code GOAT             | grok-4.5          |    $10 |          34,250 |       1,034 |    $0.00967 |      103.4 |
|    #62    | Ollama Pro                    | kimi-k3           |    $20 |          75,383 |       1,805 |    $0.01108 |       90.3 |
|    #63    | Command Code GOAT             | glm-5.3           |    $10 |          74,953 |         863 |    $0.01158 |       86.3 |
|    #64    | Command Code GOAT             | grok-4.6          |    $10 |          48,586 |         729 |    $0.01372 |       72.9 |
|    #65    | Command Code GOAT             | qwen3.8-max       |    $10 |          89,729 |         691 |    $0.01447 |       69.1 |
|    #66    | OpenCode Go                   | glm-5.3           |    $10 |          74,953 |         647 |    $0.01545 |       64.7 |
|    #67    | Command Code GOAT             | kimi-k3           |    $10 |          75,383 |         602 |    $0.01660 |       60.2 |
|    #68    | OpenCode Go                   | grok-4.6          |    $10 |          48,586 |         545 |    $0.01833 |       54.5 |
|    #69    | OpenCode Go                   | qwen3.8-max       |    $10 |          89,729 |         518 |    $0.01930 |       51.8 |
|    #70    | OpenCode Go                   | kimi-k3           |    $10 |          75,383 |         451 |    $0.02217 |       45.1 |

### Pro Band: >$30 and ≤$100 / month
For professional software engineers and daily power users:

| Tier Rank | Plan Name                    | Served Model      | Fee/mo | Output Tok/Task | Tasks/Month | Cost / Task | Tasks / $1 |
| :-------: | ---------------------------- | ----------------- | -----: | --------------: | ----------: | ----------: | ---------: |
|     #1    | ChatGPT Pro 5x               | gpt-5.6-luna      |   $100 |           7,918 |   4,743,117 |    $0.00002 |   47,431.2 |
|     #2    | ChatGPT Pro 5x               | gpt-5.6-terra     |   $100 |          11,453 |     520,161 |    $0.00019 |    5,201.6 |
|     #3    | Claude Max 5x (9/14+)        | claude-sonnet-5   |   $100 |          50,414 |     389,277 |    $0.00026 |    3,892.8 |
|     #4    | GLM Coding Max (老客 ¥469) 闲时  | glm-5.3-flash     | $69.19 |          67,491 |     259,012 |    $0.00027 |    3,743.5 |
|     #5    | GLM Coding Max (老客 ¥469) 中间值 | glm-5.3-flash     | $69.19 |          67,491 |     194,263 |    $0.00036 |    2,807.7 |
|     #6    | Claude Max 5x (9/14+)        | claude-opus-5     |   $100 |          33,436 |     234,777 |    $0.00043 |    2,347.8 |
|     #7    | GLM Coding Max (老客 ¥469) 忙时  | glm-5.3-flash     | $69.19 |          67,491 |     129,499 |    $0.00053 |    1,871.6 |
|     #8    | Ollama Max                   | deepseek-v4-flash |   $100 |         104,492 |     184,159 |    $0.00054 |    1,841.6 |
|     #9    | ChatGPT Pro 5x               | gpt-5.6-sol       |   $100 |          17,645 |     174,554 |    $0.00057 |    1,745.5 |
|    #10    | GLM Coding Pro (新客 ¥538) 闲时  | glm-5.3-flash     | $79.37 |          67,491 |     111,007 |    $0.00072 |    1,398.6 |
|    #11    | GLM Coding Pro ($80) 闲时      | glm-5.3-flash     |    $80 |          67,491 |     111,007 |    $0.00072 |    1,387.6 |
|    #12    | ChatGPT Pro 5x               | gpt-5.5           |   $100 |          18,737 |     127,176 |    $0.00079 |    1,271.8 |
|    #13    | Ollama Max                   | glm-5.3-flash     |   $100 |          67,491 |     125,744 |    $0.00080 |    1,257.4 |
|    #14    | GLM Coding Max (老客 ¥469) 闲时  | glm-5.3           | $69.19 |          74,953 |      76,968 |    $0.00090 |    1,112.4 |
|    #15    | GLM Coding Pro (新客 ¥538) 中间值 | glm-5.3-flash     | $79.37 |          67,491 |      83,256 |    $0.00095 |    1,049.0 |
|    #16    | GLM Coding Pro ($80) 中间值     | glm-5.3-flash     |    $80 |          67,491 |      83,256 |    $0.00096 |    1,040.7 |
|    #17    | Google AI Ultra 5x           | gemini-3.8-flash  | $99.99 |         120,488 |      92,997 |    $0.00108 |      930.1 |
|    #18    | Kimi 会员 699                  | kimi-k2.7-code    |    $99 |          54,054 |      87,024 |    $0.00114 |      879.0 |
|    #19    | GLM Coding Max (老客 ¥469) 中间值 | glm-5.3           | $69.19 |          74,953 |      57,730 |    $0.00120 |      834.4 |
|    #20    | Kimi 会员 199                  | kimi-k2.7-code    |    $39 |          54,054 |      29,008 |    $0.00134 |      743.8 |
|    #21    | Cursor Pro+                  | grok-4.6          |    $60 |          48,586 |      42,465 |    $0.00141 |      707.7 |
|    #22    | GLM Coding Pro (新客 ¥538) 忙时  | glm-5.3-flash     | $79.37 |          67,491 |      55,504 |    $0.00143 |      699.3 |
|    #23    | GLM Coding Pro ($80) 忙时      | glm-5.3-flash     |    $80 |          67,491 |      55,504 |    $0.00144 |      693.8 |
|    #24    | Ollama Max                   | deepseek-v4-pro   |   $100 |         101,214 |      62,086 |    $0.00161 |      620.9 |
|    #25    | Kimi 会员 699                  | kimi-k3           |    $99 |          75,383 |      57,745 |    $0.00171 |      583.3 |
|    #26    | GLM Coding Max (老客 ¥469) 忙时  | glm-5.3           | $69.19 |          74,953 |      38,477 |    $0.00180 |      556.1 |
|    #27    | Kimi 会员 199                  | kimi-k3           |    $39 |          75,383 |      19,248 |    $0.00203 |      493.5 |
|    #28    | ChatGPT Pro 5x               | gpt-6-astra       |   $100 |          19,006 |      47,880 |    $0.00209 |      478.8 |
|    #29    | SuperGrok Plus               | grok-4.6          |   $100 |          48,586 |      41,987 |    $0.00238 |      419.9 |
|    #30    | GLM Coding Pro (新客 ¥538) 闲时  | glm-5.3           | $79.37 |          74,953 |      32,981 |    $0.00241 |      415.5 |
|    #31    | GLM Coding Pro ($80) 闲时      | glm-5.3           |    $80 |          74,953 |      32,981 |    $0.00243 |      412.3 |
|    #32    | GLM Coding Pro (新客 ¥538) 中间值 | glm-5.3           | $79.37 |          74,953 |      24,736 |    $0.00321 |      311.6 |
|    #33    | GLM Coding Pro ($80) 中间值     | glm-5.3           |    $80 |          74,953 |      24,736 |    $0.00323 |      309.2 |
|    #34    | Claude Max 5x (9/14+)        | claude-fable-5    |   $100 |          35,970 |      25,674 |    $0.00390 |      256.7 |
|    #35    | Ollama Max                   | kimi-k2.7-code    |   $100 |          54,054 |      24,337 |    $0.00411 |      243.4 |
|    #36    | GLM Coding Pro (新客 ¥538) 忙时  | glm-5.3           | $79.37 |          74,953 |      16,490 |    $0.00481 |      207.8 |
|    #37    | GLM Coding Pro ($80) 忙时      | glm-5.3           |    $80 |          74,953 |      16,490 |    $0.00485 |      206.1 |
|    #38    | Ollama Max                   | glm-5.2           |   $100 |          48,956 |      19,818 |    $0.00505 |      198.2 |
|    #39    | Ollama Max                   | glm-5.3           |   $100 |          74,953 |      12,944 |    $0.00773 |      129.4 |
|    #40    | Ollama Max                   | kimi-k3           |   $100 |          75,383 |       9,025 |    $0.01108 |       90.2 |

### Power & Enterprise Band: >$100 and ≤$300 / month
For heavy agentic automation and team subscriptions:

| Tier Rank | Plan Name                     | Served Model     | Fee/mo  | Output Tok/Task | Tasks/Month | Cost / Task | Tasks / $1 |
| :-------: | ----------------------------- | ---------------- | ------: | --------------: | ----------: | ----------: | ---------: |
|     #1    | ChatGPT Pro 20x               | gpt-5.6-luna     |    $200 |           7,918 |  18,972,215 |    $0.00001 |   94,861.1 |
|     #2    | ChatGPT Pro 20x               | gpt-5.6-terra    |    $200 |          11,453 |   2,178,923 |    $0.00009 |   10,894.6 |
|     #3    | Claude Max 20x (9/14+)        | claude-sonnet-5  |    $200 |          50,414 |     778,554 |    $0.00026 |    3,892.8 |
|     #4    | ChatGPT Pro 20x               | gpt-5.6-sol      |    $200 |          17,645 |     731,199 |    $0.00027 |    3,656.0 |
|     #5    | ChatGPT Pro 20x               | gpt-5.5          |    $200 |          18,737 |     532,748 |    $0.00038 |    2,663.7 |
|     #6    | Claude Max 20x (9/14+)        | claude-opus-5    |    $200 |          33,436 |     469,554 |    $0.00043 |    2,347.8 |
|     #7    | Claude Max 20x (9/14+)        | claude-opus-4.8  |    $200 |          36,648 |     428,400 |    $0.00047 |    2,142.0 |
|     #8    | Google AI Ultra 20x           | gemini-3.8-flash | $199.99 |         120,488 |     371,987 |    $0.00054 |    1,860.0 |
|     #9    | GLM Coding Max (新客 ¥1078) 闲时  | glm-5.3-flash    | $159.03 |          67,491 |     259,012 |    $0.00061 |    1,628.7 |
|    #10    | GLM Coding Max ($168) 闲时      | glm-5.3-flash    |    $168 |          67,491 |     259,012 |    $0.00065 |    1,541.7 |
|    #11    | GLM Coding Max (新客 ¥1078) 中间值 | glm-5.3-flash    | $159.03 |          67,491 |     194,263 |    $0.00082 |    1,221.5 |
|    #12    | GLM Coding Max ($168) 中间值     | glm-5.3-flash    |    $168 |          67,491 |     194,263 |    $0.00086 |    1,156.3 |
|    #13    | Cursor Ultra                  | grok-4.5         |    $200 |          34,250 |     225,898 |    $0.00089 |    1,129.5 |
|    #14    | ChatGPT Pro 20x               | gpt-6-astra      |    $200 |          19,006 |     200,568 |    $0.00100 |    1,002.8 |
|    #15    | GLM Coding Max (新客 ¥1078) 忙时  | glm-5.3-flash    | $159.03 |          67,491 |     129,499 |    $0.00123 |      814.3 |
|    #16    | Cursor Ultra                  | grok-4.6         |    $200 |          48,586 |     159,243 |    $0.00126 |      796.2 |
|    #17    | GLM Coding Max ($168) 忙时      | glm-5.3-flash    |    $168 |          67,491 |     129,499 |    $0.00130 |      770.8 |
|    #18    | SuperGrok Heavy               | grok-4.5         |    $300 |          34,250 |     148,613 |    $0.00202 |      495.4 |
|    #19    | GLM Coding Max (新客 ¥1078) 闲时  | glm-5.3          | $159.03 |          74,953 |      76,968 |    $0.00207 |      484.0 |
|    #20    | GLM Coding Max ($168) 闲时      | glm-5.3          |    $168 |          74,953 |      76,968 |    $0.00218 |      458.1 |
|    #21    | GLM Coding Max (新客 ¥1078) 中间值 | glm-5.3          | $159.03 |          74,953 |      57,730 |    $0.00276 |      363.0 |
|    #22    | SuperGrok Heavy               | grok-4.6         |    $300 |          48,586 |     104,763 |    $0.00286 |      349.2 |
|    #23    | GLM Coding Max ($168) 中间值     | glm-5.3          |    $168 |          74,953 |      57,730 |    $0.00291 |      343.6 |
|    #24    | Cursor Ultra (Fast)           | grok-4.6         |    $200 |          48,586 |      63,269 |    $0.00316 |      316.3 |
|    #25    | Devin Max                     | gpt-6-astra      |    $200 |          19,006 |      58,666 |    $0.00341 |      293.3 |
|    #26    | GLM Coding Max (新客 ¥1078) 忙时  | glm-5.3          | $159.03 |          74,953 |      38,477 |    $0.00413 |      242.0 |
|    #27    | GLM Coding Max ($168) 忙时      | glm-5.3          |    $168 |          74,953 |      38,477 |    $0.00437 |      229.0 |
|    #28    | Claude Max 20x (9/14+)        | claude-fable-5   |    $200 |          35,970 |      33,575 |    $0.00596 |      167.9 |

---

## 6. Unbenchmarked Models (Marked for Future Evaluation)

The following models from the `real-api-pricing` dataset have **no DeepSWE v1.1 evaluation** at all — meaning their output token consumption per task is unknown. Their ranking values are left empty (`null`) and flagged as **`[Pending DeepSWE]`**:

> **Note**: API-only rows (e.g. "Claude Opus 5 API") for models that **are** in DeepSWE are intentionally excluded from ranking because they carry no monthly token quota — not because the model itself is unevaluated.

| Served Model                 | Plans Offering This Model                                                   | DeepSWE Status       | Action Plan                                                |
| ---------------------------- | --------------------------------------------------------------------------- | :------------------: | ---------------------------------------------------------- |
| `claude-fable-5.1`           | Claude Fable 5.1 API, Claude Max 20x (9/14+), Claude Max 5x (9/14+)         | ⚠️ [Pending DeepSWE] | Awaiting evaluation in DeepSWE or community saturation run |
| `claude-opus-5.5`            | Claude Max 20x (9/14+), Claude Max 5x (9/14+), Claude Opus 5.5 API, Clau... | ⚠️ [Pending DeepSWE] | Awaiting evaluation in DeepSWE or community saturation run |
| `composer-2.5`               | Cursor Pro (Composer Fast), Cursor Pro (Standard), Cursor Pro+ (Composer... | ⚠️ [Pending DeepSWE] | Awaiting evaluation in DeepSWE or community saturation run |
| `deepseek-v4-flash-fast`     | Command Code GOAT                                                           | ⚠️ [Pending DeepSWE] | Awaiting evaluation in DeepSWE or community saturation run |
| `deepseek-v4.1-flash`        | Command Code GOAT, DeepSeek V4.1 Flash API 忙时, DeepSeek V4.1 Flash API 闲... | ⚠️ [Pending DeepSWE] | Awaiting evaluation in DeepSWE or community saturation run |
| `glm-5.1`                    | Ollama Max, Ollama Pro, OpenCode Go                                         | ⚠️ [Pending DeepSWE] | Awaiting evaluation in DeepSWE or community saturation run |
| `glm-5.2-fast`               | Command Code GOAT                                                           | ⚠️ [Pending DeepSWE] | Awaiting evaluation in DeepSWE or community saturation run |
| `gpt-6-sol`                  | ChatGPT Plus                                                                | ⚠️ [Pending DeepSWE] | Awaiting evaluation in DeepSWE or community saturation run |
| `grok-4.7`                   | Command Code GOAT, Grok 4.7 API (<200k), OpenCode Go, SuperGrok, SuperGr... | ⚠️ [Pending DeepSWE] | Awaiting evaluation in DeepSWE or community saturation run |
| `hy3`                        | Command Code GOAT, OpenCode Go                                              | ⚠️ [Pending DeepSWE] | Awaiting evaluation in DeepSWE or community saturation run |
| `hy4-preview`                | Command Code GOAT, OpenCode Go                                              | ⚠️ [Pending DeepSWE] | Awaiting evaluation in DeepSWE or community saturation run |
| `inkling`                    | Command Code GOAT                                                           | ⚠️ [Pending DeepSWE] | Awaiting evaluation in DeepSWE or community saturation run |
| `inkling-small`              | Command Code GOAT                                                           | ⚠️ [Pending DeepSWE] | Awaiting evaluation in DeepSWE or community saturation run |
| `kimi-k2.6`                  | OpenCode Go                                                                 | ⚠️ [Pending DeepSWE] | Awaiting evaluation in DeepSWE or community saturation run |
| `kimi-k2.7-code-highspeed`   | Command Code GOAT                                                           | ⚠️ [Pending DeepSWE] | Awaiting evaluation in DeepSWE or community saturation run |
| `longcat-2.0`                | OpenCode Go                                                                 | ⚠️ [Pending DeepSWE] | Awaiting evaluation in DeepSWE or community saturation run |
| `mimo-v2.5`                  | Command Code GOAT, MiMo Token Plan Lite 夜间0.8×, MiMo Token Plan Lite 日间,... | ⚠️ [Pending DeepSWE] | Awaiting evaluation in DeepSWE or community saturation run |
| `mimo-v2.5-pro`              | Command Code GOAT, MiMo Token Plan Lite 夜间0.8×, MiMo Token Plan Lite 日间,... | ⚠️ [Pending DeepSWE] | Awaiting evaluation in DeepSWE or community saturation run |
| `mimo-v2.6-flash`            | Command Code GOAT, MiMo Token Plan Lite 夜间0.8×, MiMo Token Plan Lite 日间,... | ⚠️ [Pending DeepSWE] | Awaiting evaluation in DeepSWE or community saturation run |
| `mimo-v2.6-pro`              | Command Code GOAT, MiMo Token Plan Lite 夜间0.8×, MiMo Token Plan Lite 日间,... | ⚠️ [Pending DeepSWE] | Awaiting evaluation in DeepSWE or community saturation run |
| `mimo-v2.6-pro-ultraspeed`   | Command Code GOAT, MiMo V2.6 Pro UltraSpeed API                             | ⚠️ [Pending DeepSWE] | Awaiting evaluation in DeepSWE or community saturation run |
| `minimax-m2.5`               | OpenCode Go                                                                 | ⚠️ [Pending DeepSWE] | Awaiting evaluation in DeepSWE or community saturation run |
| `minimax-m2.7`               | MiniMax Token Plan Plus, MiniMax Token Plan Plus (Global), Ollama Max, O... | ⚠️ [Pending DeepSWE] | Awaiting evaluation in DeepSWE or community saturation run |
| `minimax-m3`                 | Command Code GOAT, MiniMax Token Plan Max, MiniMax Token Plan Max (Globa... | ⚠️ [Pending DeepSWE] | Awaiting evaluation in DeepSWE or community saturation run |
| `muse-spark-1.2-contributor` | Command Code GOAT, OpenCode Go                                              | ⚠️ [Pending DeepSWE] | Awaiting evaluation in DeepSWE or community saturation run |
| `muse-spark-1.3`             | Command Code GOAT                                                           | ⚠️ [Pending DeepSWE] | Awaiting evaluation in DeepSWE or community saturation run |
| `muse-spark-1.3-contributor` | Command Code GOAT, OpenCode Go                                              | ⚠️ [Pending DeepSWE] | Awaiting evaluation in DeepSWE or community saturation run |
| `nemotron-3-ultra`           | Command Code GOAT                                                           | ⚠️ [Pending DeepSWE] | Awaiting evaluation in DeepSWE or community saturation run |
| `omen-alpha`                 | OpenCode Go                                                                 | ⚠️ [Pending DeepSWE] | Awaiting evaluation in DeepSWE or community saturation run |
| `qwen3.6-plus`               | Command Code GOAT, OpenCode Go                                              | ⚠️ [Pending DeepSWE] | Awaiting evaluation in DeepSWE or community saturation run |
| `qwen3.7-max`                | Command Code GOAT, OpenCode Go                                              | ⚠️ [Pending DeepSWE] | Awaiting evaluation in DeepSWE or community saturation run |
| `qwen3.7-plus`               | Alibaba Cloud Coding Plan Pro, Command Code GOAT, OpenCode Go, 阿里云百炼 Cod... | ⚠️ [Pending DeepSWE] | Awaiting evaluation in DeepSWE or community saturation run |
| `qwen3.8-27b`                | Command Code GOAT                                                           | ⚠️ [Pending DeepSWE] | Awaiting evaluation in DeepSWE or community saturation run |
| `qwen3.8-flash`              | Command Code GOAT, OpenCode Go                                              | ⚠️ [Pending DeepSWE] | Awaiting evaluation in DeepSWE or community saturation run |
| `qwen3.8-max-0902`           | Command Code GOAT                                                           | ⚠️ [Pending DeepSWE] | Awaiting evaluation in DeepSWE or community saturation run |
| `step-3.5-flash`             | Command Code GOAT, Step Plan Max (¥699), Step Plan Mini (¥49), Step Plan... | ⚠️ [Pending DeepSWE] | Awaiting evaluation in DeepSWE or community saturation run |
| `step-3.7-flash`             | Command Code GOAT, Step Plan Max (¥699), Step Plan Mini (¥49), Step Plan... | ⚠️ [Pending DeepSWE] | Awaiting evaluation in DeepSWE or community saturation run |
| `step-5-preview`             | Step Plan Max (¥699), Step Plan Mini (¥49), Step Plan Plus (¥99), Step P... | ⚠️ [Pending DeepSWE] | Awaiting evaluation in DeepSWE or community saturation run |
| `swe-2`                      | Devin Pro (促销至 10/31)                                                       | ⚠️ [Pending DeepSWE] | Awaiting evaluation in DeepSWE or community saturation run |

> [!NOTE]
> One row is **unmetered rather than merely unbenchmarked**: `Devin Pro × SWE-2` is free (unbounded quota) as a promotion running until **2026-10-31** — its $/MTok is ≈$0 and it cannot be given a finite tasks/month figure. It is flagged `unmetered` in the derived outputs and must be re-verified after the promo ends.
>
> Rows whose `price_usd` is an **international USD sticker** rather than CNY÷FX: `kimi_*` and `mimo_token_*` plans are merged domestic/global points priced at the international tier ($19–$99 Kimi, $6–$100 MiMo); `price`/`currency` still record the domestic CNY charge.

> [!IMPORTANT]
> When DeepSWE or community saturation benchmarks release completion token figures for Claude Opus 5.5 / Fable 5.1, GPT-6 Sol, Grok 4.7, MiMo v2.6, Step-5 Preview, SWE-2, Composer 2.5, Muse Spark 1.3, or any other pending model, simply update `data/model-token-consumption.json` and re-run `python3 scripts/compute_task_ranking.py` to seamlessly integrate them into the ranking.

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
│   ├── adopted.csv                # Upstream subscription data (284 plan × model points: 265 subscription + 19 metered API)
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
