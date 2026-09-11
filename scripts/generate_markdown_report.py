#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Generate comprehensive Markdown tables and rankings for README.md."""

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DERIVED_DIR = ROOT / "derived"
DATA_DIR = ROOT / "data"


def format_table(rows, headers, alignments):
    col_widths = [len(h) for h in headers]
    for row in rows:
        for i, val in enumerate(row):
            col_widths[i] = max(col_widths[i], len(str(val)))

    lines = []
    # Header
    header_line = "| " + " | ".join(h.ljust(col_widths[i]) for i, h in enumerate(headers)) + " |"
    lines.append(header_line)

    # Separator
    sep_cells = []
    for i, align in enumerate(alignments):
        w = col_widths[i]
        if align == "right":
            sep_cells.append("-" * (w - 1) + ":")
        elif align == "center":
            sep_cells.append(":" + "-" * (w - 2) + ":")
        else:
            sep_cells.append("-" * w)
    lines.append("| " + " | ".join(sep_cells) + " |")

    # Rows
    for row in rows:
        row_cells = []
        for i, val in enumerate(row):
            s = str(val)
            align = alignments[i]
            if align == "right":
                row_cells.append(s.rjust(col_widths[i]))
            elif align == "center":
                row_cells.append(s.center(col_widths[i]))
            else:
                row_cells.append(s.ljust(col_widths[i]))
        lines.append("| " + " | ".join(row_cells) + " |")

    return "\n".join(lines)


def build_markdown_tables():
    with open(DERIVED_DIR / "task-ranking.json", "r", encoding="utf-8") as f:
        rank_data = json.load(f)
    rankings = rank_data["rankings"]

    with open(DERIVED_DIR / "unbenchmarked-models.json", "r", encoding="utf-8") as f:
        unbenchmarked = json.load(f)

    with open(DATA_DIR / "deepswe-configs.json", "r", encoding="utf-8") as f:
        dswe_list = json.load(f)

    # 1. DeepSWE Summary Table
    cb_headers = ["Rank", "Model & Effort Tier", "DeepSWE Score (Pass@1)", "Cost / Task", "Output Tokens / Task (median)", "Steps / Task"]
    cb_align = ["center", "left", "right", "right", "right", "right"]
    cb_rows = []
    for entry in dswe_list:
        cb_rows.append([
            f"#{entry['rank']}",
            f"{entry['display_name']} {entry['reasoning_effort']}",
            f"{entry['score_pct']:.1f}%",
            f"${entry['cost_usd_per_task']:.2f}",
            f"{entry['output_tokens_per_task']:,}",
            f"{entry['steps_per_task']:,}"
        ])
    cb_md = format_table(cb_rows, cb_headers, cb_align)

    # 2. Main Task-Adjusted Ranking Table
    main_headers = ["Rank", "Shift vs Raw", "Plan Name", "Served Model", "Fee/mo", "Output Tok/Task", "Tasks/Month", "Cost / Task", "Tasks / $1", "Raw $/MTok"]
    main_align = ["center", "center", "left", "left", "right", "right", "right", "right", "right", "right"]
    main_rows = []
    for r in rankings:
        delta = r["rank_delta"]
        if delta > 0:
            shift_str = f"▲ +{delta}"
        elif delta < 0:
            shift_str = f"▼ {delta}"
        else:
            shift_str = "—"

        main_rows.append([
            f"#{r['task_rank']}",
            shift_str,
            r["plan_name"],
            r["served_model"],
            f"${r['price_usd']:.0f}" if r['price_usd'].is_integer() else f"${r['price_usd']:.2f}",
            f"{r['output_tokens_per_task']:,}",
            f"{r['monthly_tasks']:,.0f}",
            f"${r['cost_per_task_usd']:.5f}",
            f"{r['tasks_per_dollar']:,.1f}",
            f"${r['raw_usd_per_mtok']:.5f}"
        ])
    main_md = format_table(main_rows, main_headers, main_align)

    # 3. Price Bands
    bands = [
        ("Budget ($0 – $30/mo)", [r for r in rankings if r["price_usd"] <= 30]),
        ("Pro ($30 – $100/mo)", [r for r in rankings if 30 < r["price_usd"] <= 100]),
        ("Power / Enterprise ($100 – $300/mo)", [r for r in rankings if 100 < r["price_usd"] <= 300]),
    ]
    band_tables = {}
    for band_name, band_plans in bands:
        b_rows = []
        band_sorted = sorted(band_plans, key=lambda x: x["cost_per_task_usd"])
        for b_rank, r in enumerate(band_sorted, 1):
            delta = r["rank_delta"]
            shift_str = f"▲ +{delta}" if delta > 0 else (f"▼ {delta}" if delta < 0 else "—")
            b_rows.append([
                f"#{b_rank}",
                r["plan_name"],
                r["served_model"],
                f"${r['price_usd']:.0f}" if r['price_usd'].is_integer() else f"${r['price_usd']:.2f}",
                f"{r['output_tokens_per_task']:,}",
                f"{r['monthly_tasks']:,.0f}",
                f"${r['cost_per_task_usd']:.5f}",
                f"{r['tasks_per_dollar']:,.1f}"
            ])
        b_headers = ["Tier Rank", "Plan Name", "Served Model", "Fee/mo", "Output Tok/Task", "Tasks/Month", "Cost / Task", "Tasks / $1"]
        b_align = ["center", "left", "left", "right", "right", "right", "right", "right"]
        band_tables[band_name] = format_table(b_rows, b_headers, b_align)

    # 4. Unbenchmarked Models Summary Table
    # Load model-token-consumption map to distinguish truly-pending models from
    # API-only rows for benchmarked models (which have monthly_tokens=0 but the
    # model IS in DeepSWE — those should NOT appear in this table).
    with open(DATA_DIR / "model-token-consumption.json", "r", encoding="utf-8") as f:
        model_map = json.load(f)

    # Only include rows whose served_model is genuinely pending (not benchmarked)
    unbench_by_model = {}
    for u in unbenchmarked:
        m = u["served_model"]
        if model_map.get(m, {}).get("deepswe_status", "pending") != "pending":
            continue  # Skip API-only rows for DeepSWE-benchmarked models
        if m not in unbench_by_model:
            unbench_by_model[m] = []
        unbench_by_model[m].append(u["plan_name"])

    unbench_headers = ["Served Model", "Plans Offering This Model", "DeepSWE Status", "Action Plan"]
    unbench_align = ["left", "left", "center", "left"]
    unbench_rows = []
    for m in sorted(unbench_by_model.keys()):
        plans_str = ", ".join(sorted(set(unbench_by_model[m])))
        if len(plans_str) > 75:
            plans_str = plans_str[:72] + "..."
        unbench_rows.append([
            f"`{m}`",
            plans_str,
            "⚠️ [Pending DeepSWE]",
            "Awaiting evaluation in DeepSWE or community saturation run"
        ])
    unbench_md = format_table(unbench_rows, unbench_headers, unbench_align)

    return {
        "deepswe_table": cb_md,
        "main_ranking_table": main_md,
        "band_tables": band_tables,
        "unbenchmarked_table": unbench_md
    }


if __name__ == "__main__":
    tables = build_markdown_tables()
    print("Tables built successfully.")
    print("Sample of Main Table (first 500 chars):")
    print(tables["main_ranking_table"][:500])
