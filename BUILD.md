# Building and Reproducing the Rankings

This repository contains the complete reproducible pipeline to compute task-adjusted coding subscription rankings from raw quota data and DeepSWE benchmarks.

## Prerequisites

- Python 3.10+
- Standard library modules (`csv`, `json`, `pathlib`, `urllib`)
- Network access on first run (the DeepSWE leaderboard artifact is fetched once and cached as `data/deepswe.json`; delete the cache to refresh)

## Pipeline Execution Order

Run the following commands from the repository root:

```bash
# 1. Fetch + normalize DeepSWE v1.1 leaderboard records
python3 scripts/extract_deepswe.py

# 2. Build model-to-token-consumption mapping
python3 scripts/build_model_consumption_map.py

# 3. Compute task-adjusted rankings and export derived files
python3 scripts/compute_task_ranking.py

# 4. Generate markdown tables and report (README.md)
python3 scripts/build_readme.py
```

## Generated Assets

- `data/deepswe.json`: Verbatim DeepSWE v1.1 leaderboard artifact (70 configurations, 28 models).
- `data/deepswe-configs.json`: Normalized per-config records — median output tokens/task, Pass@1, mean cost, mean steps — with repo-convention model ids and effort labels.
- `data/model-token-consumption.json`: Canonical model mapping with reasoning tiers and unbenchmarked placeholders (baseline = Medium tier, or nearest available).
- `derived/task-ranking.json` & `derived/task-ranking.csv`: Full task-adjusted rankings and metrics (112 plan × model points).
- `derived/unbenchmarked-models.json` & `derived/unbenchmarked-models.csv`: Catalog of models awaiting DeepSWE evaluation.

## Deploying the web page

`web/index.html` is a self-contained static page (data embedded at build time). It is deployed to GitHub Pages automatically by `.github/workflows/deploy-pages.yml` on every push to `main`. After regenerating `derived/task-ranking.json`, re-embed the fresh numbers into `web/index.html` before pushing.
