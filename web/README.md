# Web Frontend

This directory holds the live static page (`index.html`) for the Task-Adjusted AI Coding Subscription Rankings, its data contract (`schema.json`), and deployment notes. The page embeds `derived/task-ranking.json` at build time and is deployed to GitHub Pages by `.github/workflows/deploy-pages.yml` on every push to `main`.

## Data source

Token-consumption figures come from **DeepSWE v1.1** ([deepswe.datacurve.ai](https://deepswe.datacurve.ai)) — median output tokens per task, per model and reasoning-effort tier. Regenerate with `python3 scripts/extract_deepswe.py` (see `BUILD.md`).

## Interactive features

1. **Interactive Toggle**: Switch between **Raw Token Price ($/MTok)** and **Task-Adjusted Price ($/Task)** to dynamically visualize the Pareto shift.
2. **Reasoning Effort Selector**: Pills across Low, Medium, High, Extra High, and Max effort — the ranking recomputes live from per-tier DeepSWE token data (nearest available tier when a model lacks the selected one).
3. **Price Band Tabs**: Quick filters for $0–$30 (Budget), $30–$100 (Pro), and $100–$300 (Power/Enterprise).
4. **Pending Evaluation Inspector**: Chip cloud of models awaiting DeepSWE evaluation to monitor missing coverage.
5. **Search & sort**: Filter by plan or model; sort any numeric column.
