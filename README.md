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
|  #1  | GPT-6 Astra Extra High      |                  74.1% |       $6.52 |                        28,542 |           29 |
|  #2  | Gemini 3.8 Flash High       |                  73.8% |       $2.36 |                       138,377 |          166 |
|  #3  | Claude Opus 5 Max           |                  73.6% |      $11.84 |                       113,366 |           99 |
|  #4  | GPT-6 Astra High            |                  73.2% |       $5.72 |                        25,414 |           27 |
|  #5  | Claude Opus 5 Extra High    |                  73.2% |       $9.07 |                        87,322 |           89 |
|  #6  | GPT-6 Astra Max             |                  73.2% |      $12.37 |                        58,618 |           28 |
|  #7  | GPT-6 Astra Medium          |                  72.8% |       $4.38 |                        19,006 |           26 |
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
| #22  | GPT-6 Astra Low             |                  67.0% |       $2.19 |                         9,488 |           20 |
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
|  #2  |      —       | ChatGPT Plus                  | gpt-5.6-luna      |     $20 |           7,918 |     948,598 |    $0.00002 |   47,429.9 |   $0.00266 |
|  #3  |      —       | ChatGPT Pro 5x                | gpt-5.6-luna      |    $100 |           7,918 |   4,743,117 |    $0.00002 |   47,431.2 |   $0.00266 |
|  #4  |    ▲ +13     | ChatGPT Pro 20x               | gpt-5.6-terra     |    $200 |          11,453 |   2,097,616 |    $0.00010 |   10,488.1 |   $0.00833 |
|  #5  |    ▲ +33     | Command Code GOAT             | gpt-5.6-luna      |     $10 |           7,918 |      90,212 |    $0.00011 |    9,021.2 |   $0.01400 |
|  #6  |    ▲ +44     | OpenCode Go                   | gpt-5.6-luna      |     $10 |           7,918 |      67,656 |    $0.00015 |    6,765.6 |   $0.01867 |
|  #7  |    ▲ +37     | ChatGPT Plus                  | gpt-5.6-terra     |     $20 |          11,453 |     104,881 |    $0.00019 |    5,244.0 |   $0.01665 |
|  #8  |    ▲ +37     | ChatGPT Pro 5x                | gpt-5.6-terra     |    $100 |          11,453 |     524,404 |    $0.00019 |    5,244.0 |   $0.01665 |
|  #9  |     ▼ -5     | GLM Coding Pro (老客 ¥149) 闲时   | glm-5.3-flash     |  $21.98 |          67,491 |     114,074 |    $0.00019 |    5,189.9 |   $0.00285 |
| #10  |     ▼ -1     | Claude Pro                    | claude-sonnet-5   |     $20 |          50,414 |      78,748 |    $0.00025 |    3,937.4 |   $0.00504 |
| #11  |     ▼ -6     | GLM Coding Pro (老客 ¥149) 中间值  | glm-5.3-flash     |  $21.98 |          67,491 |      85,552 |    $0.00026 |    3,892.3 |   $0.00381 |
| #12  |     ▼ -2     | Claude Max 20x (9/14+)        | claude-sonnet-5   |    $200 |          50,414 |     778,554 |    $0.00026 |    3,892.8 |   $0.00510 |
| #13  |     ▼ -2     | Claude Max 5x (9/14+)         | claude-sonnet-5   |    $100 |          50,414 |     389,277 |    $0.00026 |    3,892.8 |   $0.00510 |
| #14  |     ▼ -8     | GLM Coding Max (老客 ¥469) 闲时   | glm-5.3-flash     |  $69.19 |          67,491 |     266,184 |    $0.00026 |    3,847.1 |   $0.00385 |
| #15  |    ▲ +28     | ChatGPT Pro 20x               | gpt-5.6-sol       |    $200 |          17,645 |     698,215 |    $0.00029 |    3,491.1 |   $0.01623 |
| #16  |     ▼ -4     | GLM Coding Max (老客 ¥469) 中间值  | glm-5.3-flash     |  $69.19 |          67,491 |     199,627 |    $0.00035 |    2,885.2 |   $0.00514 |
| #17  |     ▼ -4     | GLM Coding Lite (老客 ¥49) 闲时   | glm-5.3-flash     |   $7.23 |          67,491 |      19,010 |    $0.00038 |    2,629.3 |   $0.00563 |
| #18  |     ▼ -4     | GLM Coding Pro (老客 ¥149) 忙时   | glm-5.3-flash     |  $21.98 |          67,491 |      57,045 |    $0.00038 |    2,595.3 |   $0.00571 |
| #19  |    ▲ +38     | ChatGPT Pro 20x               | gpt-5.5           |    $200 |          18,737 |     512,868 |    $0.00039 |    2,564.3 |   $0.02081 |
| #20  |    ▲ +12     | Claude Max 20x (9/14+)        | claude-opus-5     |    $200 |          33,436 |     469,554 |    $0.00043 |    2,347.8 |   $0.01274 |
| #21  |    ▲ +12     | Claude Max 5x (9/14+)         | claude-opus-5     |    $100 |          33,436 |     234,777 |    $0.00043 |    2,347.8 |   $0.01274 |
| #22  |     ▲ +9     | Claude Pro                    | claude-opus-4.8   |     $20 |          36,648 |      43,331 |    $0.00046 |    2,166.6 |   $0.01259 |
| #23  |    ▲ +11     | Claude Max 20x (9/14+)        | claude-opus-4.8   |    $200 |          36,648 |     428,400 |    $0.00047 |    2,142.0 |   $0.01274 |
| #24  |    ▼ -17     | Ollama Pro                    | deepseek-v4-flash |     $20 |         104,492 |      41,414 |    $0.00048 |    2,070.7 |   $0.00462 |
| #25  |    ▼ -17     | Ollama Max                    | deepseek-v4-flash |    $100 |         104,492 |     207,070 |    $0.00048 |    2,070.7 |   $0.00462 |
| #26  |    ▼ -11     | GLM Coding Lite (老客 ¥49) 中间值  | glm-5.3-flash     |   $7.23 |          67,491 |      14,254 |    $0.00051 |    1,971.5 |   $0.00751 |
| #27  |    ▼ -11     | GLM Coding Max (老客 ¥469) 忙时   | glm-5.3-flash     |  $69.19 |          67,491 |     133,084 |    $0.00052 |    1,923.5 |   $0.00770 |
| #28  |    ▲ +46     | ChatGPT Plus                  | gpt-5.6-sol       |     $20 |          17,645 |      34,911 |    $0.00057 |    1,745.5 |   $0.03247 |
| #29  |    ▲ +46     | ChatGPT Pro 5x                | gpt-5.6-sol       |    $100 |          17,645 |     174,554 |    $0.00057 |    1,745.5 |   $0.03247 |
| #30  |    ▼ -12     | Command Code GOAT             | glm-5.3-flash     |     $10 |          67,491 |      17,316 |    $0.00058 |    1,731.6 |   $0.00856 |
| #31  |    ▼ -11     | GLM Coding Max (新客 ¥1078) 闲时  | glm-5.3-flash     | $159.03 |          67,491 |     266,184 |    $0.00060 |    1,673.8 |   $0.00885 |
| #32  |    ▼ -11     | GLM Coding Max ($168) 闲时      | glm-5.3-flash     |    $168 |          67,491 |     266,184 |    $0.00063 |    1,584.4 |   $0.00935 |
| #33  |    ▼ -14     | GLM Coding Pro (老客 ¥149) 闲时   | glm-5.3           |  $21.98 |          74,953 |      33,888 |    $0.00065 |    1,541.8 |   $0.00865 |
| #34  |    ▼ -12     | GLM Coding Pro (新客 ¥538) 闲时   | glm-5.3-flash     |  $79.37 |          67,491 |     114,074 |    $0.00070 |    1,437.2 |   $0.01031 |
| #35  |    ▼ -12     | GLM Coding Pro ($80) 闲时       | glm-5.3-flash     |     $80 |          67,491 |     114,074 |    $0.00070 |    1,425.9 |   $0.01039 |
| #36  |    ▼ -12     | GLM Coding Lite (老客 ¥49) 忙时   | glm-5.3-flash     |   $7.23 |          67,491 |       9,512 |    $0.00076 |    1,315.7 |   $0.01126 |
| #37  |    ▼ -12     | Ollama Pro                    | glm-5.3-flash     |     $20 |          67,491 |      25,975 |    $0.00077 |    1,298.8 |   $0.01141 |
| #38  |    ▼ -12     | Ollama Max                    | glm-5.3-flash     |    $100 |          67,491 |     129,877 |    $0.00077 |    1,298.8 |   $0.01141 |
| #39  |    ▲ +43     | ChatGPT Plus                  | gpt-5.5           |     $20 |          18,737 |      25,644 |    $0.00078 |    1,282.2 |   $0.04162 |
| #40  |    ▲ +43     | ChatGPT Pro 5x                | gpt-5.5           |    $100 |          18,737 |     128,217 |    $0.00078 |    1,282.2 |   $0.04163 |
| #41  |    ▼ -12     | GLM Coding Max (新客 ¥1078) 中间值 | glm-5.3-flash     | $159.03 |          67,491 |     199,627 |    $0.00080 |    1,255.3 |   $0.01180 |
| #42  |    ▼ -12     | GLM Coding Max ($168) 中间值     | glm-5.3-flash     |    $168 |          67,491 |     199,627 |    $0.00084 |    1,188.3 |   $0.01247 |
| #43  |    ▼ -16     | GLM Coding Pro (老客 ¥149) 中间值  | glm-5.3           |  $21.98 |          74,953 |      25,416 |    $0.00086 |    1,156.3 |   $0.01154 |
| #44  |    ▼ -16     | GLM Coding Max (老客 ¥469) 闲时   | glm-5.3           |  $69.19 |          74,953 |      79,063 |    $0.00088 |    1,142.7 |   $0.01168 |
| #45  |    ▲ +19     | Cursor Ultra                  | grok-4.5          |    $200 |          34,250 |     225,898 |    $0.00089 |    1,129.5 |   $0.02585 |
| #46  |    ▼ -11     | GLM Coding Lite (新客 ¥118) 闲时  | glm-5.3-flash     |  $17.41 |          67,491 |      19,010 |    $0.00092 |    1,091.9 |   $0.01357 |
| #47  |    ▼ -11     | GLM Coding Pro (新客 ¥538) 中间值  | glm-5.3-flash     |  $79.37 |          67,491 |      85,552 |    $0.00093 |    1,077.9 |   $0.01375 |
| #48  |    ▼ -11     | GLM Coding Pro ($80) 中间值      | glm-5.3-flash     |     $80 |          67,491 |      85,552 |    $0.00093 |    1,069.4 |   $0.01386 |
| #49  |    ▼ -10     | GLM Coding Lite ($18) 闲时      | glm-5.3-flash     |     $18 |          67,491 |      19,010 |    $0.00095 |    1,056.1 |   $0.01403 |
| #50  |     ▲ +3     | Kimi 会员 199                   | kimi-k2.7-code    |  $29.36 |          54,054 |      29,008 |    $0.00101 |      988.0 |   $0.01872 |
| #51  |     ▼ -9     | GLM Coding Max (老客 ¥469) 中间值  | glm-5.3           |  $69.19 |          74,953 |      59,304 |    $0.00117 |      857.1 |   $0.01557 |
| #52  |     ▲ +7     | Kimi 会员 699                   | kimi-k2.7-code    | $103.12 |          54,054 |      87,024 |    $0.00119 |      843.9 |   $0.02192 |
| #53  |     ▼ -5     | GLM Coding Max (新客 ¥1078) 忙时  | glm-5.3-flash     | $159.03 |          67,491 |     133,084 |    $0.00120 |      836.9 |   $0.01771 |
| #54  |     ▼ -5     | GLM Coding Lite (新客 ¥118) 中间值 | glm-5.3-flash     |  $17.41 |          67,491 |      14,254 |    $0.00122 |      818.7 |   $0.01810 |
| #55  |    ▲ +10     | Cursor Ultra                  | grok-4.6          |    $200 |          48,586 |     159,243 |    $0.00126 |      796.2 |   $0.02585 |
| #56  |     ▼ -5     | GLM Coding Max ($168) 忙时      | glm-5.3-flash     |    $168 |          67,491 |     133,084 |    $0.00126 |      792.2 |   $0.01870 |
| #57  |     ▼ -5     | GLM Coding Lite ($18) 中间值     | glm-5.3-flash     |     $18 |          67,491 |      14,254 |    $0.00126 |      791.9 |   $0.01871 |
| #58  |    ▼ -12     | GLM Coding Lite (老客 ¥49) 闲时   | glm-5.3           |   $7.23 |          74,953 |       5,644 |    $0.00128 |      780.6 |   $0.01709 |
| #59  |    ▼ -12     | GLM Coding Pro (老客 ¥149) 忙时   | glm-5.3           |  $21.98 |          74,953 |      16,944 |    $0.00130 |      770.9 |   $0.01731 |
| #60  |     ▼ -5     | GLM Coding Pro (新客 ¥538) 忙时   | glm-5.3-flash     |  $79.37 |          67,491 |      57,045 |    $0.00139 |      718.7 |   $0.02061 |
| #61  |     ▼ -5     | GLM Coding Pro ($80) 忙时       | glm-5.3-flash     |     $80 |          67,491 |      57,045 |    $0.00140 |      713.1 |   $0.02078 |
| #62  |     ▲ +9     | Cursor Pro+                   | grok-4.6          |     $60 |          48,586 |      42,465 |    $0.00141 |      707.7 |   $0.02908 |
| #63  |    ▼ -23     | Ollama Pro                    | deepseek-v4-pro   |     $20 |         101,214 |      13,925 |    $0.00144 |      696.2 |   $0.01419 |
| #64  |    ▼ -23     | Ollama Max                    | deepseek-v4-pro   |    $100 |         101,214 |      69,627 |    $0.00144 |      696.3 |   $0.01419 |
| #65  |    ▼ -11     | Kimi 会员 199                   | kimi-k3           |  $29.36 |          75,383 |      19,248 |    $0.00153 |      655.6 |   $0.02023 |
| #66  |     ▼ -5     | OpenCode Go                   | glm-5.3-flash     |     $10 |          67,491 |       6,494 |    $0.00154 |      649.4 |   $0.02282 |
| #67  |     ▼ -7     | GLM Coding Lite (老客 ¥49) 中间值  | glm-5.3           |   $7.23 |          74,953 |       4,229 |    $0.00171 |      585.0 |   $0.02280 |
| #68  |     ▼ -6     | GLM Coding Max (老客 ¥469) 忙时   | glm-5.3           |  $69.19 |          74,953 |      39,531 |    $0.00175 |      571.3 |   $0.02335 |
| #69  |    ▲ +48     | Command Code GOAT             | gpt-5.6-sol       |     $10 |          17,645 |       5,667 |    $0.00177 |      566.7 |   $0.10000 |
| #70  |     ▼ -7     | Kimi 会员 699                   | kimi-k3           | $103.12 |          75,383 |      57,745 |    $0.00179 |      560.0 |   $0.02369 |
| #71  |     ▼ -4     | GLM Coding Lite (新客 ¥118) 忙时  | glm-5.3-flash     |  $17.41 |          67,491 |       9,512 |    $0.00183 |      546.4 |   $0.02711 |
| #72  |     ▼ -4     | GLM Coding Lite ($18) 忙时      | glm-5.3-flash     |     $18 |          67,491 |       9,512 |    $0.00189 |      528.5 |   $0.02804 |
| #73  |     ▲ +5     | OpenCode Go                   | kimi-k2.7-code    |     $10 |          54,054 |       5,052 |    $0.00198 |      505.2 |   $0.03662 |
| #74  |     ▲ +5     | Command Code GOAT             | kimi-k2.7-code    |     $10 |          54,054 |       5,052 |    $0.00198 |      505.2 |   $0.03662 |
| #75  |     ▼ -9     | GLM Coding Max (新客 ¥1078) 闲时  | glm-5.3           | $159.03 |          74,953 |      79,063 |    $0.00201 |      497.2 |   $0.02684 |
| #76  |    ▲ +23     | SuperGrok Heavy               | grok-4.5          |    $300 |          34,250 |     148,613 |    $0.00202 |      495.4 |   $0.05894 |
| #77  |    ▲ +23     | SuperGrok                     | grok-4.5          |     $30 |          34,250 |      14,861 |    $0.00202 |      495.4 |   $0.05894 |
| #78  |     ▲ +8     | Cursor Pro                    | grok-4.6          |     $20 |          48,586 |       9,674 |    $0.00207 |      483.7 |   $0.04255 |
| #79  |     ▲ +9     | Command Code GOAT             | glm-5.2           |     $10 |          48,956 |       4,782 |    $0.00209 |      478.2 |   $0.04272 |
| #80  |    ▼ -11     | GLM Coding Max ($168) 闲时      | glm-5.3           |    $168 |          74,953 |      79,063 |    $0.00213 |      470.6 |   $0.02835 |
| #81  |    ▼ -23     | Command Code GOAT             | deepseek-v4-pro   |     $10 |         101,214 |       4,642 |    $0.00215 |      464.2 |   $0.02129 |
| #82  |    ▼ -10     | GLM Coding Pro (新客 ¥538) 闲时   | glm-5.3           |  $79.37 |          74,953 |      33,888 |    $0.00234 |      427.0 |   $0.03125 |
| #83  |    ▼ -10     | GLM Coding Pro ($80) 闲时       | glm-5.3           |     $80 |          74,953 |      33,888 |    $0.00236 |      423.6 |   $0.03150 |
| #84  |     ▲ +6     | SuperGrok Plus                | grok-4.6          |    $100 |          48,586 |      41,987 |    $0.00238 |      419.9 |   $0.04902 |
| #85  |     ▲ +6     | OpenCode Go                   | glm-5.2           |     $10 |          48,956 |       4,100 |    $0.00244 |      410.0 |   $0.04983 |
| #86  |     ▲ +3     | Kimi 会员 99                    | kimi-k2.7-code    |  $14.60 |          54,054 |       5,809 |    $0.00251 |      397.9 |   $0.04651 |
| #87  |    ▼ -11     | GLM Coding Lite (老客 ¥49) 忙时   | glm-5.3           |   $7.23 |          74,953 |       2,828 |    $0.00256 |      391.2 |   $0.03410 |
| #88  |    ▼ -11     | GLM Coding Max (新客 ¥1078) 中间值 | glm-5.3           | $159.03 |          74,953 |      59,304 |    $0.00268 |      372.9 |   $0.03578 |
| #89  |     ▼ -9     | GLM Coding Max ($168) 中间值     | glm-5.3           |    $168 |          74,953 |      59,304 |    $0.00283 |      353.0 |   $0.03780 |
| #90  |    ▲ +11     | SuperGrok                     | grok-4.6          |     $30 |          48,586 |      10,476 |    $0.00286 |      349.2 |   $0.05894 |
| #91  |    ▲ +11     | SuperGrok Heavy               | grok-4.6          |    $300 |          48,586 |     104,763 |    $0.00286 |      349.2 |   $0.05894 |
| #92  |    ▼ -22     | OpenCode Go                   | deepseek-v4-pro   |     $10 |         101,214 |       3,482 |    $0.00287 |      348.2 |   $0.02838 |
| #93  |    ▼ -12     | GLM Coding Lite (新客 ¥118) 闲时  | glm-5.3           |  $17.41 |          74,953 |       5,644 |    $0.00309 |      324.2 |   $0.04115 |
| #94  |    ▼ -10     | GLM Coding Pro (新客 ¥538) 中间值  | glm-5.3           |  $79.37 |          74,953 |      25,416 |    $0.00312 |      320.2 |   $0.04166 |
| #95  |    ▼ -10     | GLM Coding Pro ($80) 中间值      | glm-5.3           |     $80 |          74,953 |      25,416 |    $0.00315 |      317.7 |   $0.04199 |
| #96  |     ▲ +9     | Cursor Ultra (Fast)           | grok-4.6          |    $200 |          48,586 |      63,269 |    $0.00316 |      316.3 |   $0.06506 |
| #97  |    ▼ -10     | GLM Coding Lite ($18) 闲时      | glm-5.3           |     $18 |          74,953 |       5,644 |    $0.00319 |      313.5 |   $0.04255 |
| #98  |     ▲ +8     | SuperGrok Lite                | grok-4.6          |     $10 |          48,586 |       3,087 |    $0.00324 |      308.7 |   $0.06667 |
| #99  |     ▼ -7     | Kimi 会员 99                    | kimi-k3           |  $14.60 |          75,383 |       3,847 |    $0.00380 |      263.5 |   $0.05036 |
| #100 |    ▲ +18     | Claude Max 5x (9/14+)         | claude-fable-5    |    $100 |          35,970 |      25,674 |    $0.00390 |      256.7 |   $0.10828 |
| #101 |     ▲ +6     | Ollama Max                    | kimi-k2.7-code    |    $100 |          54,054 |      25,266 |    $0.00396 |      252.7 |   $0.07322 |
| #102 |     ▲ +6     | Ollama Pro                    | kimi-k2.7-code    |     $20 |          54,054 |       5,052 |    $0.00396 |      252.6 |   $0.07323 |
| #103 |     ▼ -8     | GLM Coding Max (新客 ¥1078) 忙时  | glm-5.3           | $159.03 |          74,953 |      39,531 |    $0.00402 |      248.6 |   $0.05367 |
| #104 |     ▼ -8     | GLM Coding Lite (新客 ¥118) 中间值 | glm-5.3           |  $17.41 |          74,953 |       4,229 |    $0.00412 |      242.9 |   $0.05491 |
| #105 |     ▼ -8     | GLM Coding Max ($168) 忙时      | glm-5.3           |    $168 |          74,953 |      39,531 |    $0.00425 |      235.3 |   $0.05670 |
| #106 |     ▼ -8     | GLM Coding Lite ($18) 中间值     | glm-5.3           |     $18 |          74,953 |       4,229 |    $0.00426 |      235.0 |   $0.05678 |
| #107 |    ▼ -14     | Command Code GOAT             | gemini-3.7-flash  |     $10 |          87,640 |       2,230 |    $0.00449 |      223.0 |   $0.05118 |
| #108 |     ▼ -5     | GLM Coding Pro (新客 ¥538) 忙时   | glm-5.3           |  $79.37 |          74,953 |      16,944 |    $0.00468 |      213.5 |   $0.06249 |
| #109 |     ▼ -5     | GLM Coding Pro ($80) 忙时       | glm-5.3           |     $80 |          74,953 |      16,944 |    $0.00472 |      211.8 |   $0.06299 |
| #110 |     ▲ +3     | Ollama Pro                    | glm-5.2           |     $20 |          48,956 |       4,100 |    $0.00488 |      205.0 |   $0.09965 |
| #111 |     ▲ +4     | Ollama Max                    | glm-5.2           |    $100 |          48,956 |      20,494 |    $0.00488 |      204.9 |   $0.09967 |
| #112 |     ▼ -1     | Kimi 会员 49                    | kimi-k2.7-code    |   $7.23 |          54,054 |       1,443 |    $0.00501 |      199.6 |   $0.09267 |
| #113 |    ▲ +10     | Claude Max 20x (9/14+)        | claude-fable-5    |    $200 |          35,970 |      33,575 |    $0.00596 |      167.9 |   $0.16560 |
| #114 |     ▼ -5     | GLM Coding Lite (新客 ¥118) 忙时  | glm-5.3           |  $17.41 |          74,953 |       2,828 |    $0.00615 |      162.5 |   $0.08211 |
| #115 |    ▼ -21     | Command Code GOAT             | gemini-3.8-flash  |     $10 |         120,488 |       1,622 |    $0.00617 |      162.2 |   $0.05118 |
| #116 |     ▼ -6     | GLM Coding Lite ($18) 忙时      | glm-5.3           |     $18 |          74,953 |       2,828 |    $0.00636 |      157.1 |   $0.08491 |
| #117 |     ▼ -3     | Ollama Pro                    | glm-5.3           |     $20 |          74,953 |       2,678 |    $0.00747 |      133.9 |   $0.09965 |
| #118 |     ▼ -2     | Ollama Max                    | glm-5.3           |    $100 |          74,953 |      13,386 |    $0.00747 |      133.9 |   $0.09967 |
| #119 |     ▼ -7     | Command Code GOAT             | muse-spark-1.2    |     $10 |          81,250 |       1,310 |    $0.00764 |      131.0 |   $0.09398 |
| #120 |     ▲ +8     | Command Code GOAT             | grok-4.5          |     $10 |          34,250 |       1,060 |    $0.00944 |      106.0 |   $0.27548 |
| #121 |     ▼ -2     | Ollama Max                    | kimi-k3           |    $100 |          75,383 |       9,718 |    $0.01029 |       97.2 |   $0.13650 |
| #122 |     ▼ -2     | Ollama Pro                    | kimi-k3           |     $20 |          75,383 |       1,943 |    $0.01029 |       97.2 |   $0.13652 |
| #123 |     ▼ -2     | Command Code GOAT             | glm-5.3           |     $10 |          74,953 |         893 |    $0.01120 |       89.3 |   $0.14948 |
| #124 |     ▲ +5     | Command Code GOAT             | grok-4.6          |     $10 |          48,586 |         747 |    $0.01338 |       74.7 |   $0.27548 |
| #125 |     ▼ -3     | Command Code GOAT             | qwen3.8-max       |     $10 |          89,729 |         724 |    $0.01380 |       72.4 |   $0.15385 |
| #126 |     ▼ -2     | OpenCode Go                   | glm-5.3           |     $10 |          74,953 |         670 |    $0.01493 |       67.0 |   $0.19920 |
| #127 |     ▼ -2     | Command Code GOAT             | kimi-k3           |     $10 |          75,383 |         647 |    $0.01545 |       64.7 |   $0.20492 |
| #128 |     ▲ +2     | OpenCode Go                   | grok-4.6          |     $10 |          48,586 |         560 |    $0.01786 |       56.0 |   $0.36765 |
| #129 |     ▼ -3     | OpenCode Go                   | qwen3.8-max       |     $10 |          89,729 |         543 |    $0.01843 |       54.3 |   $0.20534 |
| #130 |     ▼ -3     | OpenCode Go                   | kimi-k3           |     $10 |          75,383 |         486 |    $0.02060 |       48.6 |   $0.27322 |

> [!NOTE]
> **Looking for all reasoning effort configurations?** We evaluate and rank all **260 plan × effort combinations** across Low, Medium, High, Extra High, and Max tiers. See the complete export in [`derived/task-ranking-all-efforts.csv`](derived/task-ranking-all-efforts.csv) and [`derived/task-ranking-all-efforts.json`](derived/task-ranking-all-efforts.json), and explore all 260 combinations directly in the interactive web interface (`web/index.html`), which ranks all efforts by default.

---

## 4. Annual Pricing & Discount Comparison

When paid annually, subscriptions with discounts become significantly more cost-effective per completed task. Below are the plans offering explicit annual discounts, showing how their effective monthly fee, $/task, and rankings improve:

| Plan Name                     | Served Model      | Monthly Fee | Annual Total | Eff. Monthly | Discount | Monthly Rank | Annual Rank | Shift | Monthly $/Task | Annual $/Task |
| ----------------------------- | ----------------- | ----------: | -----------: | -----------: | :------: | :----------: | :---------: | :---: | -------------: | ------------: |
| GLM Coding Pro (老客 ¥149) 闲时   | glm-5.3-flash     |      $21.98 |      $211.01 |       $17.58 |  -20.0%  |      #9      |      #7     |  ▲ +2 |       $0.00019 |      $0.00015 |
| GLM Coding Pro (老客 ¥149) 中间值  | glm-5.3-flash     |      $21.98 |      $211.01 |       $17.58 |  -20.0%  |     #11      |     #10     |  ▲ +1 |       $0.00026 |      $0.00021 |
| GLM Coding Max (老客 ¥469) 闲时   | glm-5.3-flash     |      $69.19 |      $664.22 |       $55.35 |  -20.0%  |     #14      |     #11     |  ▲ +3 |       $0.00026 |      $0.00021 |
| Claude Pro                    | claude-sonnet-5   |      $20.00 |      $200.00 |       $16.67 |  -16.7%  |     #10      |     #12     |  ▼ -2 |       $0.00025 |      $0.00021 |
| GLM Coding Max (老客 ¥469) 中间值  | glm-5.3-flash     |      $69.19 |      $664.22 |       $55.35 |  -20.0%  |     #16      |     #15     |  ▲ +1 |       $0.00035 |      $0.00028 |
| GLM Coding Lite (老客 ¥49) 闲时   | glm-5.3-flash     |       $7.23 |       $69.41 |        $5.78 |  -20.0%  |     #17      |     #17     |   —   |       $0.00038 |      $0.00030 |
| GLM Coding Pro (老客 ¥149) 忙时   | glm-5.3-flash     |      $21.98 |      $211.01 |       $17.58 |  -20.0%  |     #18      |     #18     |   —   |       $0.00038 |      $0.00031 |
| Claude Pro                    | claude-opus-4.8   |      $20.00 |      $200.00 |       $16.67 |  -16.7%  |     #22      |     #19     |  ▲ +3 |       $0.00046 |      $0.00038 |
| Ollama Pro                    | deepseek-v4-flash |      $20.00 |      $200.00 |       $16.67 |  -16.7%  |     #24      |     #21     |  ▲ +3 |       $0.00048 |      $0.00040 |
| GLM Coding Lite (老客 ¥49) 中间值  | glm-5.3-flash     |       $7.23 |       $69.41 |        $5.78 |  -20.0%  |     #26      |     #22     |  ▲ +4 |       $0.00051 |      $0.00041 |
| GLM Coding Max (老客 ¥469) 忙时   | glm-5.3-flash     |      $69.19 |      $664.22 |       $55.35 |  -20.0%  |     #27      |     #23     |  ▲ +4 |       $0.00052 |      $0.00042 |
| GLM Coding Max ($168) 闲时      | glm-5.3-flash     |     $168.00 |     $1411.20 |      $117.60 |  -30.0%  |     #32      |     #26     |  ▲ +6 |       $0.00063 |      $0.00044 |
| GLM Coding Max (新客 ¥1078) 闲时  | glm-5.3-flash     |     $159.03 |     $1526.69 |      $127.22 |  -20.0%  |     #31      |     #28     |  ▲ +3 |       $0.00060 |      $0.00048 |
| GLM Coding Pro ($80) 闲时       | glm-5.3-flash     |      $80.00 |      $672.00 |       $56.00 |  -30.0%  |     #35      |     #30     |  ▲ +5 |       $0.00070 |      $0.00049 |
| GLM Coding Pro (老客 ¥149) 闲时   | glm-5.3           |      $21.98 |      $211.01 |       $17.58 |  -20.0%  |     #33      |     #31     |  ▲ +2 |       $0.00065 |      $0.00052 |
| GLM Coding Pro (新客 ¥538) 闲时   | glm-5.3-flash     |      $79.37 |      $761.95 |       $63.50 |  -20.0%  |     #34      |     #32     |  ▲ +2 |       $0.00070 |      $0.00056 |
| GLM Coding Max ($168) 中间值     | glm-5.3-flash     |     $168.00 |     $1411.20 |      $117.60 |  -30.0%  |     #42      |     #36     |  ▲ +6 |       $0.00084 |      $0.00059 |
| GLM Coding Lite (老客 ¥49) 忙时   | glm-5.3-flash     |       $7.23 |       $69.41 |        $5.78 |  -20.0%  |     #36      |     #37     |  ▼ -1 |       $0.00076 |      $0.00061 |
| GLM Coding Max (新客 ¥1078) 中间值 | glm-5.3-flash     |     $159.03 |     $1526.69 |      $127.22 |  -20.0%  |     #41      |     #38     |  ▲ +3 |       $0.00080 |      $0.00064 |
| Ollama Pro                    | glm-5.3-flash     |      $20.00 |      $200.00 |       $16.67 |  -16.7%  |     #37      |     #39     |  ▼ -2 |       $0.00077 |      $0.00064 |
| GLM Coding Pro ($80) 中间值      | glm-5.3-flash     |      $80.00 |      $672.00 |       $56.00 |  -30.0%  |     #48      |     #40     |  ▲ +8 |       $0.00093 |      $0.00065 |
| GLM Coding Lite ($18) 闲时      | glm-5.3-flash     |      $18.00 |      $151.20 |       $12.60 |  -30.0%  |     #49      |     #41     |  ▲ +8 |       $0.00095 |      $0.00066 |
| GLM Coding Pro (老客 ¥149) 中间值  | glm-5.3           |      $21.98 |      $211.01 |       $17.58 |  -20.0%  |     #43      |     #42     |  ▲ +1 |       $0.00086 |      $0.00069 |
| GLM Coding Max (老客 ¥469) 闲时   | glm-5.3           |      $69.19 |      $664.22 |       $55.35 |  -20.0%  |     #44      |     #43     |  ▲ +1 |       $0.00088 |      $0.00070 |
| Cursor Ultra                  | grok-4.5          |     $200.00 |     $1920.00 |      $160.00 |  -20.0%  |     #45      |     #44     |  ▲ +1 |       $0.00089 |      $0.00071 |
| GLM Coding Lite (新客 ¥118) 闲时  | glm-5.3-flash     |      $17.41 |      $167.14 |       $13.93 |  -20.0%  |     #46      |     #45     |  ▲ +1 |       $0.00092 |      $0.00073 |
| GLM Coding Pro (新客 ¥538) 中间值  | glm-5.3-flash     |      $79.37 |      $761.95 |       $63.50 |  -20.0%  |     #47      |     #46     |  ▲ +1 |       $0.00093 |      $0.00074 |
| Kimi 会员 199                   | kimi-k2.7-code    |      $29.36 |      $281.86 |       $23.49 |  -20.0%  |     #50      |     #50     |   —   |       $0.00101 |      $0.00081 |
| GLM Coding Max ($168) 忙时      | glm-5.3-flash     |     $168.00 |     $1411.20 |      $117.60 |  -30.0%  |     #56      |     #51     |  ▲ +5 |       $0.00126 |      $0.00088 |
| GLM Coding Lite ($18) 中间值     | glm-5.3-flash     |      $18.00 |      $151.20 |       $12.60 |  -30.0%  |     #57      |     #52     |  ▲ +5 |       $0.00126 |      $0.00088 |
| GLM Coding Max (老客 ¥469) 中间值  | glm-5.3           |      $69.19 |      $664.22 |       $55.35 |  -20.0%  |     #51      |     #53     |  ▼ -2 |       $0.00117 |      $0.00093 |
| Kimi 会员 699                   | kimi-k2.7-code    |     $103.12 |      $989.95 |       $82.50 |  -20.0%  |     #52      |     #54     |  ▼ -2 |       $0.00119 |      $0.00095 |
| GLM Coding Max (新客 ¥1078) 忙时  | glm-5.3-flash     |     $159.03 |     $1526.69 |      $127.22 |  -20.0%  |     #53      |     #55     |  ▼ -2 |       $0.00120 |      $0.00096 |
| GLM Coding Lite (新客 ¥118) 中间值 | glm-5.3-flash     |      $17.41 |      $167.14 |       $13.93 |  -20.0%  |     #54      |     #56     |  ▼ -2 |       $0.00122 |      $0.00098 |
| GLM Coding Pro ($80) 忙时       | glm-5.3-flash     |      $80.00 |      $672.00 |       $56.00 |  -30.0%  |     #61      |     #57     |  ▲ +4 |       $0.00140 |      $0.00098 |
| Cursor Ultra                  | grok-4.6          |     $200.00 |     $1920.00 |      $160.00 |  -20.0%  |     #55      |     #58     |  ▼ -3 |       $0.00126 |      $0.00101 |
| GLM Coding Lite (老客 ¥49) 闲时   | glm-5.3           |       $7.23 |       $69.41 |        $5.78 |  -20.0%  |     #58      |     #59     |  ▼ -1 |       $0.00128 |      $0.00103 |
| GLM Coding Pro (老客 ¥149) 忙时   | glm-5.3           |      $21.98 |      $211.01 |       $17.58 |  -20.0%  |     #59      |     #60     |  ▼ -1 |       $0.00130 |      $0.00104 |
| GLM Coding Pro (新客 ¥538) 忙时   | glm-5.3-flash     |      $79.37 |      $761.95 |       $63.50 |  -20.0%  |     #60      |     #61     |  ▼ -1 |       $0.00139 |      $0.00111 |
| Cursor Pro+                   | grok-4.6          |      $60.00 |      $576.00 |       $48.00 |  -20.0%  |     #62      |     #62     |   —   |       $0.00141 |      $0.00113 |
| Ollama Pro                    | deepseek-v4-pro   |      $20.00 |      $200.00 |       $16.67 |  -16.7%  |     #63      |     #63     |   —   |       $0.00144 |      $0.00120 |
| Kimi 会员 199                   | kimi-k3           |      $29.36 |      $281.86 |       $23.49 |  -20.0%  |     #65      |     #64     |  ▲ +1 |       $0.00153 |      $0.00122 |
| GLM Coding Lite ($18) 忙时      | glm-5.3-flash     |      $18.00 |      $151.20 |       $12.60 |  -30.0%  |     #72      |     #65     |  ▲ +7 |       $0.00189 |      $0.00133 |
| GLM Coding Lite (老客 ¥49) 中间值  | glm-5.3           |       $7.23 |       $69.41 |        $5.78 |  -20.0%  |     #67      |     #66     |  ▲ +1 |       $0.00171 |      $0.00137 |
| GLM Coding Max (老客 ¥469) 忙时   | glm-5.3           |      $69.19 |      $664.22 |       $55.35 |  -20.0%  |     #68      |     #67     |  ▲ +1 |       $0.00175 |      $0.00140 |
| Kimi 会员 699                   | kimi-k3           |     $103.12 |      $989.95 |       $82.50 |  -20.0%  |     #70      |     #68     |  ▲ +2 |       $0.00179 |      $0.00143 |
| GLM Coding Lite (新客 ¥118) 忙时  | glm-5.3-flash     |      $17.41 |      $167.14 |       $13.93 |  -20.0%  |     #71      |     #70     |  ▲ +1 |       $0.00183 |      $0.00146 |
| GLM Coding Max ($168) 闲时      | glm-5.3           |     $168.00 |     $1411.20 |      $117.60 |  -30.0%  |     #80      |     #71     |  ▲ +9 |       $0.00213 |      $0.00149 |
| GLM Coding Max (新客 ¥1078) 闲时  | glm-5.3           |     $159.03 |     $1526.69 |      $127.22 |  -20.0%  |     #75      |     #73     |  ▲ +2 |       $0.00201 |      $0.00161 |
| GLM Coding Pro ($80) 闲时       | glm-5.3           |      $80.00 |      $672.00 |       $56.00 |  -30.0%  |     #83      |     #74     |  ▲ +9 |       $0.00236 |      $0.00165 |
| Cursor Pro                    | grok-4.6          |      $20.00 |      $192.00 |       $16.00 |  -20.0%  |     #78      |     #75     |  ▲ +3 |       $0.00207 |      $0.00165 |
| SuperGrok Heavy               | grok-4.5          |     $300.00 |     $3000.00 |      $250.00 |  -16.7%  |     #76      |     #76     |   —   |       $0.00202 |      $0.00168 |
| SuperGrok                     | grok-4.5          |      $30.00 |      $300.00 |       $25.00 |  -16.7%  |     #77      |     #77     |   —   |       $0.00202 |      $0.00168 |
| GLM Coding Pro (新客 ¥538) 闲时   | glm-5.3           |      $79.37 |      $761.95 |       $63.50 |  -20.0%  |     #82      |     #79     |  ▲ +3 |       $0.00234 |      $0.00187 |
| GLM Coding Max ($168) 中间值     | glm-5.3           |     $168.00 |     $1411.20 |      $117.60 |  -30.0%  |     #89      |     #82     |  ▲ +7 |       $0.00283 |      $0.00198 |
| Kimi 会员 99                    | kimi-k2.7-code    |      $14.60 |      $140.16 |       $11.68 |  -20.0%  |     #86      |     #83     |  ▲ +3 |       $0.00251 |      $0.00201 |
| GLM Coding Lite (老客 ¥49) 忙时   | glm-5.3           |       $7.23 |       $69.41 |        $5.78 |  -20.0%  |     #87      |     #84     |  ▲ +3 |       $0.00256 |      $0.00204 |
| GLM Coding Max (新客 ¥1078) 中间值 | glm-5.3           |     $159.03 |     $1526.69 |      $127.22 |  -20.0%  |     #88      |     #86     |  ▲ +2 |       $0.00268 |      $0.00215 |
| GLM Coding Pro ($80) 中间值      | glm-5.3           |      $80.00 |      $672.00 |       $56.00 |  -30.0%  |     #95      |     #88     |  ▲ +7 |       $0.00315 |      $0.00220 |
| GLM Coding Lite ($18) 闲时      | glm-5.3           |      $18.00 |      $151.20 |       $12.60 |  -30.0%  |     #97      |     #89     |  ▲ +8 |       $0.00319 |      $0.00223 |
| SuperGrok                     | grok-4.6          |      $30.00 |      $300.00 |       $25.00 |  -16.7%  |     #90      |     #91     |  ▼ -1 |       $0.00286 |      $0.00239 |
| SuperGrok Heavy               | grok-4.6          |     $300.00 |     $3000.00 |      $250.00 |  -16.7%  |     #91      |     #92     |  ▼ -1 |       $0.00286 |      $0.00239 |
| GLM Coding Lite (新客 ¥118) 闲时  | glm-5.3           |      $17.41 |      $167.14 |       $13.93 |  -20.0%  |     #93      |     #94     |  ▼ -1 |       $0.00309 |      $0.00247 |
| GLM Coding Pro (新客 ¥538) 中间值  | glm-5.3           |      $79.37 |      $761.95 |       $63.50 |  -20.0%  |     #94      |     #95     |  ▼ -1 |       $0.00312 |      $0.00250 |
| Cursor Ultra (Fast)           | grok-4.6          |     $200.00 |     $1920.00 |      $160.00 |  -20.0%  |     #96      |     #96     |   —   |       $0.00316 |      $0.00253 |
| GLM Coding Max ($168) 忙时      | glm-5.3           |     $168.00 |     $1411.20 |      $117.60 |  -30.0%  |     #105     |     #98     |  ▲ +7 |       $0.00425 |      $0.00298 |
| GLM Coding Lite ($18) 中间值     | glm-5.3           |      $18.00 |      $151.20 |       $12.60 |  -30.0%  |     #106     |     #99     |  ▲ +7 |       $0.00426 |      $0.00298 |
| Kimi 会员 99                    | kimi-k3           |      $14.60 |      $140.16 |       $11.68 |  -20.0%  |     #99      |     #100    |  ▼ -1 |       $0.00380 |      $0.00304 |
| GLM Coding Max (新客 ¥1078) 忙时  | glm-5.3           |     $159.03 |     $1526.69 |      $127.22 |  -20.0%  |     #103     |     #101    |  ▲ +2 |       $0.00402 |      $0.00322 |
| GLM Coding Lite (新客 ¥118) 中间值 | glm-5.3           |      $17.41 |      $167.14 |       $13.93 |  -20.0%  |     #104     |     #103    |  ▲ +1 |       $0.00412 |      $0.00329 |
| Ollama Pro                    | kimi-k2.7-code    |      $20.00 |      $200.00 |       $16.67 |  -16.7%  |     #102     |     #104    |  ▼ -2 |       $0.00396 |      $0.00330 |
| GLM Coding Pro ($80) 忙时       | glm-5.3           |      $80.00 |      $672.00 |       $56.00 |  -30.0%  |     #109     |     #105    |  ▲ +4 |       $0.00472 |      $0.00331 |
| GLM Coding Pro (新客 ¥538) 忙时   | glm-5.3           |      $79.37 |      $761.95 |       $63.50 |  -20.0%  |     #108     |     #106    |  ▲ +2 |       $0.00468 |      $0.00375 |
| Kimi 会员 49                    | kimi-k2.7-code    |       $7.23 |       $69.41 |        $5.78 |  -20.0%  |     #112     |     #109    |  ▲ +3 |       $0.00501 |      $0.00401 |
| Ollama Pro                    | glm-5.2           |      $20.00 |      $200.00 |       $16.67 |  -16.7%  |     #110     |     #110    |   —   |       $0.00488 |      $0.00407 |
| GLM Coding Lite ($18) 忙时      | glm-5.3           |      $18.00 |      $151.20 |       $12.60 |  -30.0%  |     #116     |     #111    |  ▲ +5 |       $0.00636 |      $0.00445 |
| GLM Coding Lite (新客 ¥118) 忙时  | glm-5.3           |      $17.41 |      $167.14 |       $13.93 |  -20.0%  |     #114     |     #114    |   —   |       $0.00615 |      $0.00492 |
| Ollama Pro                    | glm-5.3           |      $20.00 |      $200.00 |       $16.67 |  -16.7%  |     #117     |     #117    |   —   |       $0.00747 |      $0.00622 |
| Ollama Pro                    | kimi-k3           |      $20.00 |      $200.00 |       $16.67 |  -16.7%  |     #122     |     #120    |  ▲ +2 |       $0.01029 |      $0.00858 |

> [!TIP]
> Plans without published annual discounts (e.g. ChatGPT Plus / Pro, Command Code GOAT, OpenCode) maintain the same effective monthly fee ($12 \times$ monthly with 0% discount). Consequently, discounted subscriptions like **Claude Pro** and **GLM Coding Plans** climb several spots under annual billing.

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

| Tier Rank | Plan Name                     | Served Model      | Fee/mo | Output Tok/Task | Tasks/Month | Cost / Task | Tasks / $1 |
| :-------: | ----------------------------- | ----------------- | -----: | --------------: | ----------: | ----------: | ---------: |
|     #1    | ChatGPT Plus                  | gpt-5.6-luna      |    $20 |           7,918 |     948,598 |    $0.00002 |   47,429.9 |
|     #2    | Command Code GOAT             | gpt-5.6-luna      |    $10 |           7,918 |      90,212 |    $0.00011 |    9,021.2 |
|     #3    | OpenCode Go                   | gpt-5.6-luna      |    $10 |           7,918 |      67,656 |    $0.00015 |    6,765.6 |
|     #4    | ChatGPT Plus                  | gpt-5.6-terra     |    $20 |          11,453 |     104,881 |    $0.00019 |    5,244.0 |
|     #5    | GLM Coding Pro (老客 ¥149) 闲时   | glm-5.3-flash     | $21.98 |          67,491 |     114,074 |    $0.00019 |    5,189.9 |
|     #6    | Claude Pro                    | claude-sonnet-5   |    $20 |          50,414 |      78,748 |    $0.00025 |    3,937.4 |
|     #7    | GLM Coding Pro (老客 ¥149) 中间值  | glm-5.3-flash     | $21.98 |          67,491 |      85,552 |    $0.00026 |    3,892.3 |
|     #8    | GLM Coding Lite (老客 ¥49) 闲时   | glm-5.3-flash     |  $7.23 |          67,491 |      19,010 |    $0.00038 |    2,629.3 |
|     #9    | GLM Coding Pro (老客 ¥149) 忙时   | glm-5.3-flash     | $21.98 |          67,491 |      57,045 |    $0.00038 |    2,595.3 |
|    #10    | Claude Pro                    | claude-opus-4.8   |    $20 |          36,648 |      43,331 |    $0.00046 |    2,166.6 |
|    #11    | Ollama Pro                    | deepseek-v4-flash |    $20 |         104,492 |      41,414 |    $0.00048 |    2,070.7 |
|    #12    | GLM Coding Lite (老客 ¥49) 中间值  | glm-5.3-flash     |  $7.23 |          67,491 |      14,254 |    $0.00051 |    1,971.5 |
|    #13    | ChatGPT Plus                  | gpt-5.6-sol       |    $20 |          17,645 |      34,911 |    $0.00057 |    1,745.5 |
|    #14    | Command Code GOAT             | glm-5.3-flash     |    $10 |          67,491 |      17,316 |    $0.00058 |    1,731.6 |
|    #15    | GLM Coding Pro (老客 ¥149) 闲时   | glm-5.3           | $21.98 |          74,953 |      33,888 |    $0.00065 |    1,541.8 |
|    #16    | GLM Coding Lite (老客 ¥49) 忙时   | glm-5.3-flash     |  $7.23 |          67,491 |       9,512 |    $0.00076 |    1,315.7 |
|    #17    | Ollama Pro                    | glm-5.3-flash     |    $20 |          67,491 |      25,975 |    $0.00077 |    1,298.8 |
|    #18    | ChatGPT Plus                  | gpt-5.5           |    $20 |          18,737 |      25,644 |    $0.00078 |    1,282.2 |
|    #19    | GLM Coding Pro (老客 ¥149) 中间值  | glm-5.3           | $21.98 |          74,953 |      25,416 |    $0.00086 |    1,156.3 |
|    #20    | GLM Coding Lite (新客 ¥118) 闲时  | glm-5.3-flash     | $17.41 |          67,491 |      19,010 |    $0.00092 |    1,091.9 |
|    #21    | GLM Coding Lite ($18) 闲时      | glm-5.3-flash     |    $18 |          67,491 |      19,010 |    $0.00095 |    1,056.1 |
|    #22    | Kimi 会员 199                   | kimi-k2.7-code    | $29.36 |          54,054 |      29,008 |    $0.00101 |      988.0 |
|    #23    | GLM Coding Lite (新客 ¥118) 中间值 | glm-5.3-flash     | $17.41 |          67,491 |      14,254 |    $0.00122 |      818.7 |
|    #24    | GLM Coding Lite ($18) 中间值     | glm-5.3-flash     |    $18 |          67,491 |      14,254 |    $0.00126 |      791.9 |
|    #25    | GLM Coding Lite (老客 ¥49) 闲时   | glm-5.3           |  $7.23 |          74,953 |       5,644 |    $0.00128 |      780.6 |
|    #26    | GLM Coding Pro (老客 ¥149) 忙时   | glm-5.3           | $21.98 |          74,953 |      16,944 |    $0.00130 |      770.9 |
|    #27    | Ollama Pro                    | deepseek-v4-pro   |    $20 |         101,214 |      13,925 |    $0.00144 |      696.2 |
|    #28    | Kimi 会员 199                   | kimi-k3           | $29.36 |          75,383 |      19,248 |    $0.00153 |      655.6 |
|    #29    | OpenCode Go                   | glm-5.3-flash     |    $10 |          67,491 |       6,494 |    $0.00154 |      649.4 |
|    #30    | GLM Coding Lite (老客 ¥49) 中间值  | glm-5.3           |  $7.23 |          74,953 |       4,229 |    $0.00171 |      585.0 |
|    #31    | Command Code GOAT             | gpt-5.6-sol       |    $10 |          17,645 |       5,667 |    $0.00177 |      566.7 |
|    #32    | GLM Coding Lite (新客 ¥118) 忙时  | glm-5.3-flash     | $17.41 |          67,491 |       9,512 |    $0.00183 |      546.4 |
|    #33    | GLM Coding Lite ($18) 忙时      | glm-5.3-flash     |    $18 |          67,491 |       9,512 |    $0.00189 |      528.5 |
|    #34    | OpenCode Go                   | kimi-k2.7-code    |    $10 |          54,054 |       5,052 |    $0.00198 |      505.2 |
|    #35    | Command Code GOAT             | kimi-k2.7-code    |    $10 |          54,054 |       5,052 |    $0.00198 |      505.2 |
|    #36    | SuperGrok                     | grok-4.5          |    $30 |          34,250 |      14,861 |    $0.00202 |      495.4 |
|    #37    | Cursor Pro                    | grok-4.6          |    $20 |          48,586 |       9,674 |    $0.00207 |      483.7 |
|    #38    | Command Code GOAT             | glm-5.2           |    $10 |          48,956 |       4,782 |    $0.00209 |      478.2 |
|    #39    | Command Code GOAT             | deepseek-v4-pro   |    $10 |         101,214 |       4,642 |    $0.00215 |      464.2 |
|    #40    | OpenCode Go                   | glm-5.2           |    $10 |          48,956 |       4,100 |    $0.00244 |      410.0 |
|    #41    | Kimi 会员 99                    | kimi-k2.7-code    | $14.60 |          54,054 |       5,809 |    $0.00251 |      397.9 |
|    #42    | GLM Coding Lite (老客 ¥49) 忙时   | glm-5.3           |  $7.23 |          74,953 |       2,828 |    $0.00256 |      391.2 |
|    #43    | SuperGrok                     | grok-4.6          |    $30 |          48,586 |      10,476 |    $0.00286 |      349.2 |
|    #44    | OpenCode Go                   | deepseek-v4-pro   |    $10 |         101,214 |       3,482 |    $0.00287 |      348.2 |
|    #45    | GLM Coding Lite (新客 ¥118) 闲时  | glm-5.3           | $17.41 |          74,953 |       5,644 |    $0.00309 |      324.2 |
|    #46    | GLM Coding Lite ($18) 闲时      | glm-5.3           |    $18 |          74,953 |       5,644 |    $0.00319 |      313.5 |
|    #47    | SuperGrok Lite                | grok-4.6          |    $10 |          48,586 |       3,087 |    $0.00324 |      308.7 |
|    #48    | Kimi 会员 99                    | kimi-k3           | $14.60 |          75,383 |       3,847 |    $0.00380 |      263.5 |
|    #49    | Ollama Pro                    | kimi-k2.7-code    |    $20 |          54,054 |       5,052 |    $0.00396 |      252.6 |
|    #50    | GLM Coding Lite (新客 ¥118) 中间值 | glm-5.3           | $17.41 |          74,953 |       4,229 |    $0.00412 |      242.9 |
|    #51    | GLM Coding Lite ($18) 中间值     | glm-5.3           |    $18 |          74,953 |       4,229 |    $0.00426 |      235.0 |
|    #52    | Command Code GOAT             | gemini-3.7-flash  |    $10 |          87,640 |       2,230 |    $0.00449 |      223.0 |
|    #53    | Ollama Pro                    | glm-5.2           |    $20 |          48,956 |       4,100 |    $0.00488 |      205.0 |
|    #54    | Kimi 会员 49                    | kimi-k2.7-code    |  $7.23 |          54,054 |       1,443 |    $0.00501 |      199.6 |
|    #55    | GLM Coding Lite (新客 ¥118) 忙时  | glm-5.3           | $17.41 |          74,953 |       2,828 |    $0.00615 |      162.5 |
|    #56    | Command Code GOAT             | gemini-3.8-flash  |    $10 |         120,488 |       1,622 |    $0.00617 |      162.2 |
|    #57    | GLM Coding Lite ($18) 忙时      | glm-5.3           |    $18 |          74,953 |       2,828 |    $0.00636 |      157.1 |
|    #58    | Ollama Pro                    | glm-5.3           |    $20 |          74,953 |       2,678 |    $0.00747 |      133.9 |
|    #59    | Command Code GOAT             | muse-spark-1.2    |    $10 |          81,250 |       1,310 |    $0.00764 |      131.0 |
|    #60    | Command Code GOAT             | grok-4.5          |    $10 |          34,250 |       1,060 |    $0.00944 |      106.0 |
|    #61    | Ollama Pro                    | kimi-k3           |    $20 |          75,383 |       1,943 |    $0.01029 |       97.2 |
|    #62    | Command Code GOAT             | glm-5.3           |    $10 |          74,953 |         893 |    $0.01120 |       89.3 |
|    #63    | Command Code GOAT             | grok-4.6          |    $10 |          48,586 |         747 |    $0.01338 |       74.7 |
|    #64    | Command Code GOAT             | qwen3.8-max       |    $10 |          89,729 |         724 |    $0.01380 |       72.4 |
|    #65    | OpenCode Go                   | glm-5.3           |    $10 |          74,953 |         670 |    $0.01493 |       67.0 |
|    #66    | Command Code GOAT             | kimi-k3           |    $10 |          75,383 |         647 |    $0.01545 |       64.7 |
|    #67    | OpenCode Go                   | grok-4.6          |    $10 |          48,586 |         560 |    $0.01786 |       56.0 |
|    #68    | OpenCode Go                   | qwen3.8-max       |    $10 |          89,729 |         543 |    $0.01843 |       54.3 |
|    #69    | OpenCode Go                   | kimi-k3           |    $10 |          75,383 |         486 |    $0.02060 |       48.6 |

### Pro Band: >$30 and ≤$100 / month
For professional software engineers and daily power users:

| Tier Rank | Plan Name                    | Served Model      | Fee/mo | Output Tok/Task | Tasks/Month | Cost / Task | Tasks / $1 |
| :-------: | ---------------------------- | ----------------- | -----: | --------------: | ----------: | ----------: | ---------: |
|     #1    | ChatGPT Pro 5x               | gpt-5.6-luna      |   $100 |           7,918 |   4,743,117 |    $0.00002 |   47,431.2 |
|     #2    | ChatGPT Pro 5x               | gpt-5.6-terra     |   $100 |          11,453 |     524,404 |    $0.00019 |    5,244.0 |
|     #3    | Claude Max 5x (9/14+)        | claude-sonnet-5   |   $100 |          50,414 |     389,277 |    $0.00026 |    3,892.8 |
|     #4    | GLM Coding Max (老客 ¥469) 闲时  | glm-5.3-flash     | $69.19 |          67,491 |     266,184 |    $0.00026 |    3,847.1 |
|     #5    | GLM Coding Max (老客 ¥469) 中间值 | glm-5.3-flash     | $69.19 |          67,491 |     199,627 |    $0.00035 |    2,885.2 |
|     #6    | Claude Max 5x (9/14+)        | claude-opus-5     |   $100 |          33,436 |     234,777 |    $0.00043 |    2,347.8 |
|     #7    | Ollama Max                   | deepseek-v4-flash |   $100 |         104,492 |     207,070 |    $0.00048 |    2,070.7 |
|     #8    | GLM Coding Max (老客 ¥469) 忙时  | glm-5.3-flash     | $69.19 |          67,491 |     133,084 |    $0.00052 |    1,923.5 |
|     #9    | ChatGPT Pro 5x               | gpt-5.6-sol       |   $100 |          17,645 |     174,554 |    $0.00057 |    1,745.5 |
|    #10    | GLM Coding Pro (新客 ¥538) 闲时  | glm-5.3-flash     | $79.37 |          67,491 |     114,074 |    $0.00070 |    1,437.2 |
|    #11    | GLM Coding Pro ($80) 闲时      | glm-5.3-flash     |    $80 |          67,491 |     114,074 |    $0.00070 |    1,425.9 |
|    #12    | Ollama Max                   | glm-5.3-flash     |   $100 |          67,491 |     129,877 |    $0.00077 |    1,298.8 |
|    #13    | ChatGPT Pro 5x               | gpt-5.5           |   $100 |          18,737 |     128,217 |    $0.00078 |    1,282.2 |
|    #14    | GLM Coding Max (老客 ¥469) 闲时  | glm-5.3           | $69.19 |          74,953 |      79,063 |    $0.00088 |    1,142.7 |
|    #15    | GLM Coding Pro (新客 ¥538) 中间值 | glm-5.3-flash     | $79.37 |          67,491 |      85,552 |    $0.00093 |    1,077.9 |
|    #16    | GLM Coding Pro ($80) 中间值     | glm-5.3-flash     |    $80 |          67,491 |      85,552 |    $0.00093 |    1,069.4 |
|    #17    | GLM Coding Max (老客 ¥469) 中间值 | glm-5.3           | $69.19 |          74,953 |      59,304 |    $0.00117 |      857.1 |
|    #18    | GLM Coding Pro (新客 ¥538) 忙时  | glm-5.3-flash     | $79.37 |          67,491 |      57,045 |    $0.00139 |      718.7 |
|    #19    | GLM Coding Pro ($80) 忙时      | glm-5.3-flash     |    $80 |          67,491 |      57,045 |    $0.00140 |      713.1 |
|    #20    | Cursor Pro+                  | grok-4.6          |    $60 |          48,586 |      42,465 |    $0.00141 |      707.7 |
|    #21    | Ollama Max                   | deepseek-v4-pro   |   $100 |         101,214 |      69,627 |    $0.00144 |      696.3 |
|    #22    | GLM Coding Max (老客 ¥469) 忙时  | glm-5.3           | $69.19 |          74,953 |      39,531 |    $0.00175 |      571.3 |
|    #23    | GLM Coding Pro (新客 ¥538) 闲时  | glm-5.3           | $79.37 |          74,953 |      33,888 |    $0.00234 |      427.0 |
|    #24    | GLM Coding Pro ($80) 闲时      | glm-5.3           |    $80 |          74,953 |      33,888 |    $0.00236 |      423.6 |
|    #25    | SuperGrok Plus               | grok-4.6          |   $100 |          48,586 |      41,987 |    $0.00238 |      419.9 |
|    #26    | GLM Coding Pro (新客 ¥538) 中间值 | glm-5.3           | $79.37 |          74,953 |      25,416 |    $0.00312 |      320.2 |
|    #27    | GLM Coding Pro ($80) 中间值     | glm-5.3           |    $80 |          74,953 |      25,416 |    $0.00315 |      317.7 |
|    #28    | Claude Max 5x (9/14+)        | claude-fable-5    |   $100 |          35,970 |      25,674 |    $0.00390 |      256.7 |
|    #29    | Ollama Max                   | kimi-k2.7-code    |   $100 |          54,054 |      25,266 |    $0.00396 |      252.7 |
|    #30    | GLM Coding Pro (新客 ¥538) 忙时  | glm-5.3           | $79.37 |          74,953 |      16,944 |    $0.00468 |      213.5 |
|    #31    | GLM Coding Pro ($80) 忙时      | glm-5.3           |    $80 |          74,953 |      16,944 |    $0.00472 |      211.8 |
|    #32    | Ollama Max                   | glm-5.2           |   $100 |          48,956 |      20,494 |    $0.00488 |      204.9 |
|    #33    | Ollama Max                   | glm-5.3           |   $100 |          74,953 |      13,386 |    $0.00747 |      133.9 |
|    #34    | Ollama Max                   | kimi-k3           |   $100 |          75,383 |       9,718 |    $0.01029 |       97.2 |

### Power & Enterprise Band: >$100 and ≤$300 / month
For heavy agentic automation and team subscriptions:

| Tier Rank | Plan Name                     | Served Model    | Fee/mo  | Output Tok/Task | Tasks/Month | Cost / Task | Tasks / $1 |
| :-------: | ----------------------------- | --------------- | ------: | --------------: | ----------: | ----------: | ---------: |
|     #1    | ChatGPT Pro 20x               | gpt-5.6-luna    |    $200 |           7,918 |  18,972,215 |    $0.00001 |   94,861.1 |
|     #2    | ChatGPT Pro 20x               | gpt-5.6-terra   |    $200 |          11,453 |   2,097,616 |    $0.00010 |   10,488.1 |
|     #3    | Claude Max 20x (9/14+)        | claude-sonnet-5 |    $200 |          50,414 |     778,554 |    $0.00026 |    3,892.8 |
|     #4    | ChatGPT Pro 20x               | gpt-5.6-sol     |    $200 |          17,645 |     698,215 |    $0.00029 |    3,491.1 |
|     #5    | ChatGPT Pro 20x               | gpt-5.5         |    $200 |          18,737 |     512,868 |    $0.00039 |    2,564.3 |
|     #6    | Claude Max 20x (9/14+)        | claude-opus-5   |    $200 |          33,436 |     469,554 |    $0.00043 |    2,347.8 |
|     #7    | Claude Max 20x (9/14+)        | claude-opus-4.8 |    $200 |          36,648 |     428,400 |    $0.00047 |    2,142.0 |
|     #8    | GLM Coding Max (新客 ¥1078) 闲时  | glm-5.3-flash   | $159.03 |          67,491 |     266,184 |    $0.00060 |    1,673.8 |
|     #9    | GLM Coding Max ($168) 闲时      | glm-5.3-flash   |    $168 |          67,491 |     266,184 |    $0.00063 |    1,584.4 |
|    #10    | GLM Coding Max (新客 ¥1078) 中间值 | glm-5.3-flash   | $159.03 |          67,491 |     199,627 |    $0.00080 |    1,255.3 |
|    #11    | GLM Coding Max ($168) 中间值     | glm-5.3-flash   |    $168 |          67,491 |     199,627 |    $0.00084 |    1,188.3 |
|    #12    | Cursor Ultra                  | grok-4.5        |    $200 |          34,250 |     225,898 |    $0.00089 |    1,129.5 |
|    #13    | Kimi 会员 699                   | kimi-k2.7-code  | $103.12 |          54,054 |      87,024 |    $0.00119 |      843.9 |
|    #14    | GLM Coding Max (新客 ¥1078) 忙时  | glm-5.3-flash   | $159.03 |          67,491 |     133,084 |    $0.00120 |      836.9 |
|    #15    | Cursor Ultra                  | grok-4.6        |    $200 |          48,586 |     159,243 |    $0.00126 |      796.2 |
|    #16    | GLM Coding Max ($168) 忙时      | glm-5.3-flash   |    $168 |          67,491 |     133,084 |    $0.00126 |      792.2 |
|    #17    | Kimi 会员 699                   | kimi-k3         | $103.12 |          75,383 |      57,745 |    $0.00179 |      560.0 |
|    #18    | GLM Coding Max (新客 ¥1078) 闲时  | glm-5.3         | $159.03 |          74,953 |      79,063 |    $0.00201 |      497.2 |
|    #19    | SuperGrok Heavy               | grok-4.5        |    $300 |          34,250 |     148,613 |    $0.00202 |      495.4 |
|    #20    | GLM Coding Max ($168) 闲时      | glm-5.3         |    $168 |          74,953 |      79,063 |    $0.00213 |      470.6 |
|    #21    | GLM Coding Max (新客 ¥1078) 中间值 | glm-5.3         | $159.03 |          74,953 |      59,304 |    $0.00268 |      372.9 |
|    #22    | GLM Coding Max ($168) 中间值     | glm-5.3         |    $168 |          74,953 |      59,304 |    $0.00283 |      353.0 |
|    #23    | SuperGrok Heavy               | grok-4.6        |    $300 |          48,586 |     104,763 |    $0.00286 |      349.2 |
|    #24    | Cursor Ultra (Fast)           | grok-4.6        |    $200 |          48,586 |      63,269 |    $0.00316 |      316.3 |
|    #25    | GLM Coding Max (新客 ¥1078) 忙时  | glm-5.3         | $159.03 |          74,953 |      39,531 |    $0.00402 |      248.6 |
|    #26    | GLM Coding Max ($168) 忙时      | glm-5.3         |    $168 |          74,953 |      39,531 |    $0.00425 |      235.3 |
|    #27    | Claude Max 20x (9/14+)        | claude-fable-5  |    $200 |          35,970 |      33,575 |    $0.00596 |      167.9 |

---

## 6. Unbenchmarked Models (Marked for Future Evaluation)

The following models from the `real-api-pricing` dataset have **no DeepSWE v1.1 evaluation** at all — meaning their output token consumption per task is unknown. Their ranking values are left empty (`null`) and flagged as **`[Pending DeepSWE]`**:

> **Note**: API-only rows (e.g. "Claude Opus 5 API") for models that **are** in DeepSWE are intentionally excluded from ranking because they carry no monthly token quota — not because the model itself is unevaluated.

| Served Model                 | Plans Offering This Model                                                   | DeepSWE Status       | Action Plan                                                |
| ---------------------------- | --------------------------------------------------------------------------- | :------------------: | ---------------------------------------------------------- |
| `composer-2.5`               | Cursor Pro (Composer Fast), Cursor Pro (Standard), Cursor Pro+ (Composer... | ⚠️ [Pending DeepSWE] | Awaiting evaluation in DeepSWE or community saturation run |
| `deepseek-v4-flash-fast`     | Command Code GOAT                                                           | ⚠️ [Pending DeepSWE] | Awaiting evaluation in DeepSWE or community saturation run |
| `deepseek-v4.1-flash`        | Command Code GOAT, DeepSeek V4.1 Flash API 忙时, DeepSeek V4.1 Flash API 闲... | ⚠️ [Pending DeepSWE] | Awaiting evaluation in DeepSWE or community saturation run |
| `glm-5.1`                    | Ollama Max, Ollama Pro, OpenCode Go                                         | ⚠️ [Pending DeepSWE] | Awaiting evaluation in DeepSWE or community saturation run |
| `glm-5.2-fast`               | Command Code GOAT                                                           | ⚠️ [Pending DeepSWE] | Awaiting evaluation in DeepSWE or community saturation run |
| `hy3`                        | Command Code GOAT, OpenCode Go                                              | ⚠️ [Pending DeepSWE] | Awaiting evaluation in DeepSWE or community saturation run |
| `hy4-preview`                | Command Code GOAT, OpenCode Go                                              | ⚠️ [Pending DeepSWE] | Awaiting evaluation in DeepSWE or community saturation run |
| `inkling`                    | Command Code GOAT                                                           | ⚠️ [Pending DeepSWE] | Awaiting evaluation in DeepSWE or community saturation run |
| `inkling-small`              | Command Code GOAT                                                           | ⚠️ [Pending DeepSWE] | Awaiting evaluation in DeepSWE or community saturation run |
| `kimi-k2.6`                  | OpenCode Go                                                                 | ⚠️ [Pending DeepSWE] | Awaiting evaluation in DeepSWE or community saturation run |
| `kimi-k2.7-code-highspeed`   | Command Code GOAT                                                           | ⚠️ [Pending DeepSWE] | Awaiting evaluation in DeepSWE or community saturation run |
| `longcat-2.0`                | OpenCode Go                                                                 | ⚠️ [Pending DeepSWE] | Awaiting evaluation in DeepSWE or community saturation run |
| `mimo-v2.5`                  | Command Code GOAT, OpenCode Go                                              | ⚠️ [Pending DeepSWE] | Awaiting evaluation in DeepSWE or community saturation run |
| `mimo-v2.5-pro`              | Command Code GOAT, OpenCode Go                                              | ⚠️ [Pending DeepSWE] | Awaiting evaluation in DeepSWE or community saturation run |
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
