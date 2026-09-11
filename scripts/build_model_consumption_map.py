#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Generate canonical model token consumption mapping from CursorBench data and adopted.csv."""

import csv
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DATA_DIR = ROOT / "data"


def build_model_token_map():
    # Load CursorBench data
    cb_path = DATA_DIR / "cursorbench.json"
    with open(cb_path, "r", encoding="utf-8") as f:
        cb_data = json.load(f)

    # Group CursorBench data by canonical_model_id
    cb_by_model = {}
    for entry in cb_data:
        mid = entry["canonical_model_id"]
        if not mid:
            continue
        if mid not in cb_by_model:
            cb_by_model[mid] = {
                "base_model": entry["base_model"],
                "tiers": {},
                "scores": {}
            }
        effort = entry["reasoning_effort"]
        cb_by_model[mid]["tiers"][effort] = entry["output_tokens_per_task"]
        cb_by_model[mid]["scores"][effort] = entry["score_pct"]

    # Load unique served models from adopted.csv
    adopted_path = DATA_DIR / "adopted.csv"
    unique_models = set()
    with open(adopted_path, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for r in reader:
            unique_models.add(r["served_model"])

    # Muse contributor variant shares same consumption as muse-spark-1.3
    if "muse-spark-1.3" in cb_by_model:
        cb_by_model["muse-spark-1.3-contributor"] = dict(cb_by_model["muse-spark-1.3"])

    mapping = {}
    for m in sorted(unique_models):
        if m in cb_by_model:
            info = cb_by_model[m]
            # Standard baseline tier: Medium if available, else first available
            default_tier = "Medium" if "Medium" in info["tiers"] else ("Standard" if "Standard" in info["tiers"] else list(info["tiers"].keys())[0])
            mapping[m] = {
                "model_id": m,
                "cursorbench_status": "available",
                "benchmarked_name": info["base_model"],
                "default_tier": default_tier,
                "default_output_tokens_per_task": info["tiers"][default_tier],
                "default_score_pct": info["scores"][default_tier],
                "all_tiers": info["tiers"],
                "all_scores": info["scores"],
                "note": f"CursorBench 4.0 data available across {len(info['tiers'])} tier(s)"
            }
        else:
            mapping[m] = {
                "model_id": m,
                "cursorbench_status": "pending",
                "benchmarked_name": None,
                "default_tier": None,
                "default_output_tokens_per_task": None,
                "default_score_pct": None,
                "all_tiers": {},
                "all_scores": {},
                "note": "Not evaluated on CursorBench 4.0; marked pending"
            }

    out_file = DATA_DIR / "model-token-consumption.json"
    with open(out_file, "w", encoding="utf-8") as f:
        json.dump(mapping, f, indent=2, ensure_ascii=False)
    print(f"Generated model token consumption mapping with {len(mapping)} models -> {out_file}")


if __name__ == "__main__":
    build_model_token_map()
