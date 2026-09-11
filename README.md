# Task-Adjusted AI Coding Subscription Rankings

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
$$\text{Real Unit Price} = \frac{\text{Monthly Fee}}{\text{Monthly Usable Tokens}}$$

While this was a major leap forward over comparing sticker prices, it made an implicit assumption: **that all LLMs consume an equal number of tokens to accomplish the same job.**

In real-world agentic software development, this assumption fails drastically:
- Some models are highly concise, requiring only **7,000 – 10,000 output tokens** to inspect, edit, test, and complete a complex task.
- Other models are heavily verbose or require expansive reasoning steps, consuming **120,000 – 160,000 output tokens** for the same workload — a **15× to 20× difference in token consumption**.

### The Task-Adjusted Formulation

To find the true purchasing power of an AI coding subscription, we adjust for output token consumption per task ($C_{\text{task}}$):

1. **Monthly Task Capacity ($N_{\text{tasks}}$)**:
   $$N_{\text{tasks}} = \frac{T_{\text{monthly}}}{C_{\text{task}}}$$
   *(How many real tasks your monthly token pool can actually solve)*

2. **Effective Cost per Task ($Cost_{\text{task}}$)**:
   $$Cost_{\text{task}} = \frac{P_{\text{monthly}}}{N_{\text{tasks}}} = \frac{P_{\text{monthly}} \times C_{\text{task}}}{T_{\text{monthly}}}$$
   *(What you actually pay per completed task)*

3. **Tasks per Dollar Spent ($Tasks_{\$}$)**:
   $$Tasks_{\$\$} = \frac{N_{\text{tasks}}}{P_{\text{monthly}}} = \frac{1}{Cost_{\text{task}}}$$
   *(The true efficiency metric: completed tasks delivered per dollar)*

---

## 2. CursorBench 4.0 Token Consumption Data

Below is the complete dataset extracted directly from [CursorBench 4.0](https://cursor.com/cursorbench). For each model configuration, it records the benchmark score, average cost, steps, and specifically the **Output Tokens / Task** (median completion tokens):

| Rank | Model & Effort Tier       | CursorBench Score | Cost / Task | Output Tokens / Task | Steps / Task |
| :--: | ------------------------- | ----------------: | ----------: | -------------------: | -----------: |
|  #1  | Fable 5.1 Max             |             51.8% |      $17.28 |              117,236 |          128 |
|  #2  | Fable 5.1 Extra High      |             51.6% |      $13.01 |               87,294 |          101 |
|  #3  | Fable 5.1 High            |             49.2% |       $9.08 |               58,438 |           77 |
|  #4  | Fable 5.1 Medium          |             46.8% |       $7.05 |               45,411 |           63 |
|  #5  | Opus 5 Max                |             46.6% |      $11.95 |               85,384 |          106 |
|  #6  | Opus 5 Extra High         |             46.1% |      $11.43 |               80,094 |          103 |
|  #7  | Fable 5.1 Low             |             45.1% |       $5.44 |               34,795 |           51 |
|  #8  | Opus 5 High               |             44.7% |       $9.00 |               61,405 |           86 |
|  #9  | Opus 5 Medium             |             43.3% |       $6.94 |               45,272 |           72 |
| #10  | GPT-5.6 Sol Max           |             41.7% |       $8.23 |               42,944 |           99 |
| #11  | Muse Spark 1.3 Max        |             41.6% |       $2.64 |               52,005 |           98 |
| #12  | Grok 4.6 Extra High       |             41.4% |       $6.10 |               49,814 |           56 |
| #13  | GPT-5.6 Terra Max         |             41.3% |       $5.14 |               60,814 |          107 |
| #14  | Opus 5 Low                |             40.7% |       $4.87 |               31,995 |           57 |
| #15  | Grok 4.6 High             |             40.4% |       $5.20 |               41,387 |           48 |
| #16  | Gemini 3.8 Flash High     |             39.6% |       $4.70 |              162,565 |          324 |
| #17  | GPT-5.6 Sol Extra High    |             37.7% |       $4.40 |               24,729 |           55 |
| #18  | Muse Spark 1.3 Extra High |             37.5% |       $2.10 |               40,891 |           83 |
| #19  | Gemini 3.8 Flash Medium   |             37.3% |       $4.06 |              128,364 |          290 |
| #20  | Grok 4.6 Medium           |             36.1% |       $3.48 |               24,893 |           40 |
| #21  | GPT-5.6 Luna Max          |             35.9% |       $1.03 |               87,284 |          208 |
| #22  | GPT-5.6 Sol High          |             35.7% |       $2.85 |               16,174 |           41 |
| #23  | Sonnet 5 Max              |             34.1% |       $7.17 |              149,257 |          140 |
| #24  | GPT-5.6 Terra Extra High  |             33.6% |       $1.81 |               23,436 |           43 |
| #25  | Grok 4.6 Low              |             33.4% |       $2.25 |               16,307 |           32 |
| #26  | Muse Spark 1.3 High       |             33.4% |       $1.66 |               30,654 |           69 |
| #27  | GPT-5.6 Luna Extra High   |             33.0% |       $0.44 |               40,598 |           98 |
| #28  | Muse Spark 1.3 Medium     |             32.6% |       $1.49 |               27,255 |           64 |
| #29  | Sonnet 5 Extra High       |             32.0% |       $4.55 |               83,373 |          102 |
| #30  | GPT-5.6 Sol Medium        |             31.1% |       $1.77 |               10,111 |           32 |
| #31  | Sonnet 5 High             |             30.8% |       $3.48 |               61,146 |           85 |
| #32  | GPT-5.6 Terra High        |             30.7% |       $1.11 |               13,162 |           33 |
| #33  | GPT-5.6 Luna High         |             29.4% |       $0.25 |               23,368 |           64 |
| #34  | Muse Spark 1.3 Low        |             29.3% |       $0.93 |               17,483 |           47 |
| #35  | Sonnet 5 Medium           |             28.0% |       $2.31 |               39,114 |           65 |
| #36  | Composer 2.5              |             27.7% |       $0.68 |               17,347 |           41 |
| #37  | GPT-5.6 Terra Medium      |             27.6% |       $0.64 |                7,307 |           25 |
| #38  | GPT-5.6 Terra Low         |             25.2% |       $0.52 |                5,914 |           23 |
| #39  | GPT-5.6 Sol Low           |             24.6% |       $0.87 |                4,885 |           21 |
| #40  | Muse Spark 1.3 Minimal    |             24.3% |       $0.56 |               10,620 |           34 |
| #41  | Sonnet 5 Low              |             24.1% |       $1.39 |               23,772 |           46 |
| #42  | GPT-5.6 Luna Medium       |             22.2% |       $0.08 |                7,642 |           32 |
| #43  | GPT-5.6 Luna Low          |             16.0% |       $0.03 |                3,288 |           18 |

> [!NOTE]
> For models evaluated across multiple reasoning effort tiers (Low, Medium, High, Extra High, Max), our standard baseline ranking adopts the **Medium** tier (or **Standard** tier for Composer 2.5) to ensure consistent, balanced comparisons across all subscriptions. Full breakdowns across all tiers are exported in `derived/task-ranking.json`.

---

## 3. Primary Task-Adjusted Ranking (All Benchmarked Plans)

Ranked primarily by **Effective Cost per Task ($/Task)** (cheapest task first), alongside **Tasks per Dollar** and **Monthly Task Capacity**.

The column **Shift vs Raw** indicates the ranking change compared to the traditional raw token price ($/MTok) ranking:
- **▲ +X**: Model is concise and jumped **up** X spots in cost-effectiveness.
- **▼ -X**: Model is verbose and dropped **down** X spots in cost-effectiveness.

| Rank | Shift vs Raw | Plan Name                    | Served Model               | Fee/mo | Output Tok/Task | Tasks/Month | Cost / Task | Tasks / $1 | Raw $/MTok |
| :--: | :----------: | ---------------------------- | -------------------------- | -----: | --------------: | ----------: | ----------: | ---------: | ---------: |
|  #1  |     ▲ +1     | ChatGPT Pro 20x              | gpt-5.6-luna               |   $200 |           7,642 |  19,657,420 |    $0.00001 |   98,287.1 |   $0.00133 |
|  #2  |     ▲ +2     | ChatGPT Plus                 | gpt-5.6-luna               |    $20 |           7,642 |     982,858 |    $0.00002 |   49,142.9 |   $0.00266 |
|  #3  |     ▲ +2     | ChatGPT Pro 5x               | gpt-5.6-luna               |   $100 |           7,642 |   4,914,420 |    $0.00002 |   49,144.2 |   $0.00266 |
|  #4  |     ▼ -3     | OpenCode Go                  | muse-spark-1.3-contributor |    $10 |          27,255 |     458,631 |    $0.00002 |   45,863.1 |   $0.00080 |
|  #5  |     ▲ +4     | ChatGPT Pro 20x              | gpt-5.6-terra              |   $200 |           7,307 |   3,287,806 |    $0.00006 |   16,439.0 |   $0.00833 |
|  #6  |     ▼ -3     | Command Code GOAT            | muse-spark-1.3-contributor |    $10 |          27,255 |     152,878 |    $0.00006 |   15,287.8 |   $0.00240 |
|  #7  |     ▲ +7     | Command Code GOAT            | gpt-5.6-luna               |    $10 |           7,642 |      93,470 |    $0.00011 |    9,347.0 |   $0.01400 |
|  #8  |     ▲ +9     | ChatGPT Plus                 | gpt-5.6-terra              |    $20 |           7,307 |     164,390 |    $0.00012 |    8,219.5 |   $0.01665 |
|  #9  |     ▲ +9     | ChatGPT Pro 5x               | gpt-5.6-terra              |   $100 |           7,307 |     821,952 |    $0.00012 |    8,219.5 |   $0.01665 |
| #10  |     ▲ +9     | OpenCode Go                  | gpt-5.6-luna               |    $10 |           7,642 |      70,100 |    $0.00014 |    7,009.9 |   $0.01867 |
| #11  |     ▲ +4     | ChatGPT Pro 20x              | gpt-5.6-sol                |   $200 |          10,111 |   1,218,475 |    $0.00016 |    6,092.4 |   $0.01623 |
| #12  |     ▼ -2     | Cursor Ultra (Standard)      | composer-2.5               |   $200 |          17,347 |   1,146,746 |    $0.00017 |    5,733.7 |   $0.01005 |
| #13  |     ▼ -2     | Cursor Pro+ (Standard)       | composer-2.5               |    $60 |          17,347 |     305,799 |    $0.00020 |    5,096.7 |   $0.01131 |
| #14  |     ▼ -8     | Claude Pro                   | claude-sonnet-5            |    $20 |          39,114 |     101,498 |    $0.00020 |    5,074.9 |   $0.00504 |
| #15  |     ▼ -8     | Claude Max 20x (9/14+)       | claude-sonnet-5            |   $200 |          39,114 |   1,003,477 |    $0.00020 |    5,017.4 |   $0.00510 |
| #16  |     ▼ -8     | Claude Max 5x (9/14+)        | claude-sonnet-5            |   $100 |          39,114 |     501,738 |    $0.00020 |    5,017.4 |   $0.00510 |
| #17  |     ▼ -1     | Cursor Pro (Standard)        | composer-2.5               |    $20 |          17,347 |      69,660 |    $0.00029 |    3,483.0 |   $0.01655 |
| #18  |     ▲ +6     | ChatGPT Plus                 | gpt-5.6-sol                |    $20 |          10,111 |      60,924 |    $0.00033 |    3,046.2 |   $0.03247 |
| #19  |     ▲ +6     | ChatGPT Pro 5x               | gpt-5.6-sol                |   $100 |          10,111 |     304,619 |    $0.00033 |    3,046.2 |   $0.03247 |
| #20  |     ▲ +1     | Cursor Ultra (Composer Fast) | composer-2.5               |   $200 |          17,347 |     406,912 |    $0.00049 |    2,034.6 |   $0.02833 |
| #21  |     ▲ +2     | Cursor Pro+ (Composer Fast)  | composer-2.5               |    $60 |          17,347 |     108,509 |    $0.00055 |    1,808.5 |   $0.03188 |
| #22  |    ▼ -10     | Claude Max 20x (9/14+)       | claude-opus-5              |   $200 |          45,272 |     346,793 |    $0.00058 |    1,734.0 |   $0.01274 |
| #23  |    ▼ -10     | Claude Max 5x (9/14+)        | claude-opus-5              |   $100 |          45,272 |     173,396 |    $0.00058 |    1,734.0 |   $0.01274 |
| #24  |     ▼ -4     | Cursor Ultra                 | grok-4.6                   |   $200 |          24,893 |     310,810 |    $0.00064 |    1,554.1 |   $0.02585 |
| #25  |     ▼ -3     | Cursor Pro+                  | grok-4.6                   |    $60 |          24,893 |      82,883 |    $0.00072 |    1,381.4 |   $0.02908 |
| #26  |     ▲ +1     | Cursor Pro (Composer Fast)   | composer-2.5               |    $20 |          17,347 |      24,719 |    $0.00081 |    1,235.9 |   $0.04664 |
| #27  |     ▲ +8     | Command Code GOAT            | gpt-5.6-sol                |    $10 |          10,111 |       9,890 |    $0.00101 |      989.0 |   $0.10000 |
| #28  |     ▼ -2     | Cursor Pro                   | grok-4.6                   |    $20 |          24,893 |      18,881 |    $0.00106 |      944.0 |   $0.04255 |
| #29  |     ▼ -1     | SuperGrok Plus               | grok-4.6                   |   $100 |          24,893 |      81,951 |    $0.00122 |      819.5 |   $0.04902 |
| #30  |      —       | SuperGrok                    | grok-4.6                   |    $30 |          24,893 |      20,448 |    $0.00147 |      681.6 |   $0.05894 |
| #31  |      —       | SuperGrok Heavy              | grok-4.6                   |   $300 |          24,893 |     204,475 |    $0.00147 |      681.6 |   $0.05894 |
| #32  |      —       | Cursor Ultra (Fast)          | grok-4.6                   |   $200 |          24,893 |     123,488 |    $0.00162 |      617.4 |   $0.06506 |
| #33  |      —       | SuperGrok Lite               | grok-4.6                   |    $10 |          24,893 |       6,026 |    $0.00166 |      602.6 |   $0.06667 |
| #34  |      —       | Command Code GOAT            | muse-spark-1.3             |    $10 |          27,255 |       3,904 |    $0.00256 |      390.4 |   $0.09398 |
| #35  |     ▲ +1     | Claude Max 5x (9/14+)        | claude-fable-5             |   $100 |          45,411 |      20,336 |    $0.00492 |      203.4 |   $0.10828 |
| #36  |     ▼ -7     | Command Code GOAT            | gemini-3.8-flash           |    $10 |         128,364 |       1,522 |    $0.00657 |      152.2 |   $0.05118 |
| #37  |     ▲ +1     | Command Code GOAT            | grok-4.6                   |    $10 |          24,893 |       1,458 |    $0.00686 |      145.8 |   $0.27548 |
| #38  |     ▼ -1     | Claude Max 20x (9/14+)       | claude-fable-5             |   $200 |          45,411 |      26,595 |    $0.00752 |      133.0 |   $0.16560 |
| #39  |      —       | OpenCode Go                  | grok-4.6                   |    $10 |          24,893 |       1,093 |    $0.00915 |      109.3 |   $0.36765 |

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

| Tier Rank | Plan Name                  | Served Model               | Fee/mo | Output Tok/Task | Tasks/Month | Cost / Task | Tasks / $1 |
| :-------: | -------------------------- | -------------------------- | -----: | --------------: | ----------: | ----------: | ---------: |
|     #1    | ChatGPT Plus               | gpt-5.6-luna               |    $20 |           7,642 |     982,858 |    $0.00002 |   49,142.9 |
|     #2    | OpenCode Go                | muse-spark-1.3-contributor |    $10 |          27,255 |     458,631 |    $0.00002 |   45,863.1 |
|     #3    | Command Code GOAT          | muse-spark-1.3-contributor |    $10 |          27,255 |     152,878 |    $0.00006 |   15,287.8 |
|     #4    | Command Code GOAT          | gpt-5.6-luna               |    $10 |           7,642 |      93,470 |    $0.00011 |    9,347.0 |
|     #5    | ChatGPT Plus               | gpt-5.6-terra              |    $20 |           7,307 |     164,390 |    $0.00012 |    8,219.5 |
|     #6    | OpenCode Go                | gpt-5.6-luna               |    $10 |           7,642 |      70,100 |    $0.00014 |    7,009.9 |
|     #7    | Claude Pro                 | claude-sonnet-5            |    $20 |          39,114 |     101,498 |    $0.00020 |    5,074.9 |
|     #8    | Cursor Pro (Standard)      | composer-2.5               |    $20 |          17,347 |      69,660 |    $0.00029 |    3,483.0 |
|     #9    | ChatGPT Plus               | gpt-5.6-sol                |    $20 |          10,111 |      60,924 |    $0.00033 |    3,046.2 |
|    #10    | Cursor Pro (Composer Fast) | composer-2.5               |    $20 |          17,347 |      24,719 |    $0.00081 |    1,235.9 |
|    #11    | Command Code GOAT          | gpt-5.6-sol                |    $10 |          10,111 |       9,890 |    $0.00101 |      989.0 |
|    #12    | Cursor Pro                 | grok-4.6                   |    $20 |          24,893 |      18,881 |    $0.00106 |      944.0 |
|    #13    | SuperGrok                  | grok-4.6                   |    $30 |          24,893 |      20,448 |    $0.00147 |      681.6 |
|    #14    | SuperGrok Lite             | grok-4.6                   |    $10 |          24,893 |       6,026 |    $0.00166 |      602.6 |
|    #15    | Command Code GOAT          | muse-spark-1.3             |    $10 |          27,255 |       3,904 |    $0.00256 |      390.4 |
|    #16    | Command Code GOAT          | gemini-3.8-flash           |    $10 |         128,364 |       1,522 |    $0.00657 |      152.2 |
|    #17    | Command Code GOAT          | grok-4.6                   |    $10 |          24,893 |       1,458 |    $0.00686 |      145.8 |
|    #18    | OpenCode Go                | grok-4.6                   |    $10 |          24,893 |       1,093 |    $0.00915 |      109.3 |

### Pro Band: >$30 and ≤$100 / month
For professional software engineers and daily power users:

| Tier Rank | Plan Name                   | Served Model    | Fee/mo | Output Tok/Task | Tasks/Month | Cost / Task | Tasks / $1 |
| :-------: | --------------------------- | --------------- | -----: | --------------: | ----------: | ----------: | ---------: |
|     #1    | ChatGPT Pro 5x              | gpt-5.6-luna    |   $100 |           7,642 |   4,914,420 |    $0.00002 |   49,144.2 |
|     #2    | ChatGPT Pro 5x              | gpt-5.6-terra   |   $100 |           7,307 |     821,952 |    $0.00012 |    8,219.5 |
|     #3    | Cursor Pro+ (Standard)      | composer-2.5    |    $60 |          17,347 |     305,799 |    $0.00020 |    5,096.7 |
|     #4    | Claude Max 5x (9/14+)       | claude-sonnet-5 |   $100 |          39,114 |     501,738 |    $0.00020 |    5,017.4 |
|     #5    | ChatGPT Pro 5x              | gpt-5.6-sol     |   $100 |          10,111 |     304,619 |    $0.00033 |    3,046.2 |
|     #6    | Cursor Pro+ (Composer Fast) | composer-2.5    |    $60 |          17,347 |     108,509 |    $0.00055 |    1,808.5 |
|     #7    | Claude Max 5x (9/14+)       | claude-opus-5   |   $100 |          45,272 |     173,396 |    $0.00058 |    1,734.0 |
|     #8    | Cursor Pro+                 | grok-4.6        |    $60 |          24,893 |      82,883 |    $0.00072 |    1,381.4 |
|     #9    | SuperGrok Plus              | grok-4.6        |   $100 |          24,893 |      81,951 |    $0.00122 |      819.5 |
|    #10    | Claude Max 5x (9/14+)       | claude-fable-5  |   $100 |          45,411 |      20,336 |    $0.00492 |      203.4 |

### Power & Enterprise Band: >$100 and ≤$300 / month
For heavy agentic automation and team subscriptions:

| Tier Rank | Plan Name                    | Served Model    | Fee/mo | Output Tok/Task | Tasks/Month | Cost / Task | Tasks / $1 |
| :-------: | ---------------------------- | --------------- | -----: | --------------: | ----------: | ----------: | ---------: |
|     #1    | ChatGPT Pro 20x              | gpt-5.6-luna    |   $200 |           7,642 |  19,657,420 |    $0.00001 |   98,287.1 |
|     #2    | ChatGPT Pro 20x              | gpt-5.6-terra   |   $200 |           7,307 |   3,287,806 |    $0.00006 |   16,439.0 |
|     #3    | ChatGPT Pro 20x              | gpt-5.6-sol     |   $200 |          10,111 |   1,218,475 |    $0.00016 |    6,092.4 |
|     #4    | Cursor Ultra (Standard)      | composer-2.5    |   $200 |          17,347 |   1,146,746 |    $0.00017 |    5,733.7 |
|     #5    | Claude Max 20x (9/14+)       | claude-sonnet-5 |   $200 |          39,114 |   1,003,477 |    $0.00020 |    5,017.4 |
|     #6    | Cursor Ultra (Composer Fast) | composer-2.5    |   $200 |          17,347 |     406,912 |    $0.00049 |    2,034.6 |
|     #7    | Claude Max 20x (9/14+)       | claude-opus-5   |   $200 |          45,272 |     346,793 |    $0.00058 |    1,734.0 |
|     #8    | Cursor Ultra                 | grok-4.6        |   $200 |          24,893 |     310,810 |    $0.00064 |    1,554.1 |
|     #9    | SuperGrok Heavy              | grok-4.6        |   $300 |          24,893 |     204,475 |    $0.00147 |      681.6 |
|    #10    | Cursor Ultra (Fast)          | grok-4.6        |   $200 |          24,893 |     123,488 |    $0.00162 |      617.4 |
|    #11    | Claude Max 20x (9/14+)       | claude-fable-5  |   $200 |          45,411 |      26,595 |    $0.00752 |      133.0 |

---

## 6. Unbenchmarked Models (Marked for Future Evaluation)

The following models from the `real-api-pricing` dataset are **not yet evaluated in CursorBench 4.0**. Their token consumption values are left empty (`null`) and flagged as **`[Pending CursorBench]`**:

| Served Model                 | Plans Offering This Model                                                   | CursorBench Status       | Action Plan                                                    |
| ---------------------------- | --------------------------------------------------------------------------- | :----------------------: | -------------------------------------------------------------- |
| `claude-fable-5`             | Claude Fable 5 API                                                          | ⚠️ [Pending CursorBench] | Awaiting evaluation in CursorBench or community saturation run |
| `claude-opus-4.8`            | Claude Max 20x (9/14+), Claude Pro                                          | ⚠️ [Pending CursorBench] | Awaiting evaluation in CursorBench or community saturation run |
| `claude-opus-5`              | Claude Opus 5 API                                                           | ⚠️ [Pending CursorBench] | Awaiting evaluation in CursorBench or community saturation run |
| `claude-sonnet-5`            | Claude Sonnet 5 API                                                         | ⚠️ [Pending CursorBench] | Awaiting evaluation in CursorBench or community saturation run |
| `deepseek-v4-flash`          | DeepSeek V4 Flash API 忙时, DeepSeek V4 Flash API 闲时, Ollama Max, Ollama Pro  | ⚠️ [Pending CursorBench] | Awaiting evaluation in CursorBench or community saturation run |
| `deepseek-v4-flash-fast`     | Command Code GOAT                                                           | ⚠️ [Pending CursorBench] | Awaiting evaluation in CursorBench or community saturation run |
| `deepseek-v4-pro`            | Command Code GOAT, DeepSeek V4 Pro API 忙时, DeepSeek V4 Pro API 闲时, Ollam... | ⚠️ [Pending CursorBench] | Awaiting evaluation in CursorBench or community saturation run |
| `deepseek-v4.1-flash`        | Command Code GOAT, DeepSeek V4.1 Flash API 忙时, DeepSeek V4.1 Flash API 闲... | ⚠️ [Pending CursorBench] | Awaiting evaluation in CursorBench or community saturation run |
| `gemini-3.7-flash`           | Command Code GOAT                                                           | ⚠️ [Pending CursorBench] | Awaiting evaluation in CursorBench or community saturation run |
| `glm-5.1`                    | Ollama Max, Ollama Pro, OpenCode Go                                         | ⚠️ [Pending CursorBench] | Awaiting evaluation in CursorBench or community saturation run |
| `glm-5.2`                    | Command Code GOAT, Ollama Max, Ollama Pro, OpenCode Go                      | ⚠️ [Pending CursorBench] | Awaiting evaluation in CursorBench or community saturation run |
| `glm-5.2-fast`               | Command Code GOAT                                                           | ⚠️ [Pending CursorBench] | Awaiting evaluation in CursorBench or community saturation run |
| `glm-5.3`                    | Command Code GOAT, GLM Coding Lite (新客 ¥118) 中间值, GLM Coding Lite (新客 ¥1... | ⚠️ [Pending CursorBench] | Awaiting evaluation in CursorBench or community saturation run |
| `glm-5.3-flash`              | Command Code GOAT, GLM Coding Lite (新客 ¥118) 中间值, GLM Coding Lite (新客 ¥1... | ⚠️ [Pending CursorBench] | Awaiting evaluation in CursorBench or community saturation run |
| `gpt-5.5`                    | ChatGPT Plus, ChatGPT Pro 20x, ChatGPT Pro 5x                               | ⚠️ [Pending CursorBench] | Awaiting evaluation in CursorBench or community saturation run |
| `gpt-5.6-luna`               | GPT-5.6 Luna API                                                            | ⚠️ [Pending CursorBench] | Awaiting evaluation in CursorBench or community saturation run |
| `gpt-5.6-sol`                | GPT-5.6 Sol API                                                             | ⚠️ [Pending CursorBench] | Awaiting evaluation in CursorBench or community saturation run |
| `gpt-5.6-terra`              | GPT-5.6 Terra API                                                           | ⚠️ [Pending CursorBench] | Awaiting evaluation in CursorBench or community saturation run |
| `grok-4.5`                   | Command Code GOAT, Cursor Ultra, SuperGrok, SuperGrok Heavy                 | ⚠️ [Pending CursorBench] | Awaiting evaluation in CursorBench or community saturation run |
| `grok-4.6`                   | Grok 4.6 API (<200k)                                                        | ⚠️ [Pending CursorBench] | Awaiting evaluation in CursorBench or community saturation run |
| `hy3`                        | Command Code GOAT, OpenCode Go                                              | ⚠️ [Pending CursorBench] | Awaiting evaluation in CursorBench or community saturation run |
| `hy4-preview`                | Command Code GOAT, OpenCode Go                                              | ⚠️ [Pending CursorBench] | Awaiting evaluation in CursorBench or community saturation run |
| `inkling`                    | Command Code GOAT                                                           | ⚠️ [Pending CursorBench] | Awaiting evaluation in CursorBench or community saturation run |
| `inkling-small`              | Command Code GOAT                                                           | ⚠️ [Pending CursorBench] | Awaiting evaluation in CursorBench or community saturation run |
| `kimi-k2.6`                  | OpenCode Go                                                                 | ⚠️ [Pending CursorBench] | Awaiting evaluation in CursorBench or community saturation run |
| `kimi-k2.7-code`             | Command Code GOAT, Kimi 会员 199, Kimi 会员 49, Kimi 会员 699, Kimi 会员 99, Oll... | ⚠️ [Pending CursorBench] | Awaiting evaluation in CursorBench or community saturation run |
| `kimi-k2.7-code-highspeed`   | Command Code GOAT                                                           | ⚠️ [Pending CursorBench] | Awaiting evaluation in CursorBench or community saturation run |
| `kimi-k3`                    | Command Code GOAT, Kimi 会员 199, Kimi 会员 699, Kimi 会员 99, Ollama Max, Oll... | ⚠️ [Pending CursorBench] | Awaiting evaluation in CursorBench or community saturation run |
| `longcat-2.0`                | OpenCode Go                                                                 | ⚠️ [Pending CursorBench] | Awaiting evaluation in CursorBench or community saturation run |
| `mimo-v2.5`                  | Command Code GOAT, OpenCode Go                                              | ⚠️ [Pending CursorBench] | Awaiting evaluation in CursorBench or community saturation run |
| `mimo-v2.5-pro`              | Command Code GOAT, OpenCode Go                                              | ⚠️ [Pending CursorBench] | Awaiting evaluation in CursorBench or community saturation run |
| `minimax-m2.5`               | OpenCode Go                                                                 | ⚠️ [Pending CursorBench] | Awaiting evaluation in CursorBench or community saturation run |
| `minimax-m2.7`               | MiniMax Token Plan Plus, MiniMax Token Plan Plus (Global), Ollama Max, O... | ⚠️ [Pending CursorBench] | Awaiting evaluation in CursorBench or community saturation run |
| `minimax-m3`                 | Command Code GOAT, MiniMax Token Plan Max, MiniMax Token Plan Max (Globa... | ⚠️ [Pending CursorBench] | Awaiting evaluation in CursorBench or community saturation run |
| `muse-spark-1.2`             | Command Code GOAT                                                           | ⚠️ [Pending CursorBench] | Awaiting evaluation in CursorBench or community saturation run |
| `muse-spark-1.2-contributor` | Command Code GOAT, OpenCode Go                                              | ⚠️ [Pending CursorBench] | Awaiting evaluation in CursorBench or community saturation run |
| `nemotron-3-ultra`           | Command Code GOAT                                                           | ⚠️ [Pending CursorBench] | Awaiting evaluation in CursorBench or community saturation run |
| `omen-alpha`                 | OpenCode Go                                                                 | ⚠️ [Pending CursorBench] | Awaiting evaluation in CursorBench or community saturation run |
| `qwen3.6-plus`               | Command Code GOAT, OpenCode Go                                              | ⚠️ [Pending CursorBench] | Awaiting evaluation in CursorBench or community saturation run |
| `qwen3.7-max`                | Command Code GOAT, OpenCode Go                                              | ⚠️ [Pending CursorBench] | Awaiting evaluation in CursorBench or community saturation run |
| `qwen3.7-plus`               | Alibaba Cloud Coding Plan Pro, Command Code GOAT, OpenCode Go, 阿里云百炼 Cod... | ⚠️ [Pending CursorBench] | Awaiting evaluation in CursorBench or community saturation run |
| `qwen3.8-27b`                | Command Code GOAT                                                           | ⚠️ [Pending CursorBench] | Awaiting evaluation in CursorBench or community saturation run |
| `qwen3.8-flash`              | Command Code GOAT, OpenCode Go                                              | ⚠️ [Pending CursorBench] | Awaiting evaluation in CursorBench or community saturation run |
| `qwen3.8-max`                | Command Code GOAT, OpenCode Go                                              | ⚠️ [Pending CursorBench] | Awaiting evaluation in CursorBench or community saturation run |
| `qwen3.8-max-0902`           | Command Code GOAT                                                           | ⚠️ [Pending CursorBench] | Awaiting evaluation in CursorBench or community saturation run |
| `step-3.5-flash`             | Command Code GOAT, Step Plan Max (¥699), Step Plan Mini (¥49), Step Plan... | ⚠️ [Pending CursorBench] | Awaiting evaluation in CursorBench or community saturation run |
| `step-3.7-flash`             | Command Code GOAT, Step Plan Max (¥699), Step Plan Mini (¥49), Step Plan... | ⚠️ [Pending CursorBench] | Awaiting evaluation in CursorBench or community saturation run |

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
