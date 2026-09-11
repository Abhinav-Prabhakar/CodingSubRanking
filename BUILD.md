# Building and Reproducing the Rankings

This repository contains the complete reproducible pipeline to compute task-adjusted coding subscription rankings from raw quota data and CursorBench benchmarks.

## Prerequisites

- Python 3.10+
- Standard library modules (`csv`, `json`, `pathlib`, `re`, `urllib`)

## Pipeline Execution Order

Run the following commands from the repository root:

```bash
# 1. Extract CursorBench 4.0 benchmark records
python3 scripts/extract_cursorbench.py

# 2. Build model-to-token-consumption mapping
python3 scripts/build_model_consumption_map.py

# 3. Compute task-adjusted rankings and export derived files
python3 scripts/compute_task_ranking.py

# 4. Generate markdown tables and report
python3 scripts/generate_markdown_report.py
```

## Generated Assets

- `data/cursorbench.json` & `data/cursorbench.csv`: Clean extracted benchmark data from `cursor.com/cursorbench`.
- `data/model-token-consumption.json`: Canonical model mapping with reasoning tiers and unbenchmarked placeholders.
- `derived/task-ranking.json` & `derived/task-ranking.csv`: Full task-adjusted rankings and metrics.
- `derived/unbenchmarked-models.json` & `derived/unbenchmarked-models.csv`: Catalog of models awaiting CursorBench evaluation.
