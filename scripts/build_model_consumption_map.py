#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Generate canonical model token consumption mapping from DeepSWE data and adopted.csv."""

import csv
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DATA_DIR = ROOT / "data"

TIER_ORDER = ["Low", "Medium", "High", "Extra High", "Max", "Standard"]
MEDIUM_INDEX = TIER_ORDER.index("Medium")


def pick_default_tier(tiers):
    """Medium if available, else the tier nearest to Medium in effort ordering."""
    if "Medium" in tiers:
        return "Medium"
    if "Standard" in tiers:
        return "Standard"
    return min(tiers, key=lambda t: abs(TIER_ORDER.index(t) - MEDIUM_INDEX))


def build_model_token_map():
    # Load DeepSWE configuration data
    with open(DATA_DIR / "deepswe-configs.json", "r", encoding="utf-8") as f:
        configs = json.load(f)

    # Group DeepSWE data by canonical model_id
    dswe_by_model = {}
    for entry in configs:
        mid = entry["model_id"]
        info = dswe_by_model.setdefault(mid, {
            "display_name": entry["display_name"],
            "tiers": {},
            "scores": {},
        })
        effort = entry["reasoning_effort"]
        info["tiers"][effort] = entry["output_tokens_per_task"]
        info["scores"][effort] = entry["score_pct"]

    # Load unique served models from adopted.csv
    adopted_path = DATA_DIR / "adopted.csv"
    unique_models = set()
    with open(adopted_path, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for r in reader:
            unique_models.add(r["served_model"])

    mapping = {}
    for m in sorted(unique_models):
        if m in dswe_by_model:
            info = dswe_by_model[m]
            default_tier = pick_default_tier(info["tiers"])
            mapping[m] = {
                "model_id": m,
                "deepswe_status": "available",
                "benchmarked_name": info["display_name"],
                "default_tier": default_tier,
                "default_output_tokens_per_task": info["tiers"][default_tier],
                "default_score_pct": info["scores"][default_tier],
                "all_tiers": {t: info["tiers"][t] for t in sorted(info["tiers"], key=TIER_ORDER.index)},
                "all_scores": {t: info["scores"][t] for t in sorted(info["tiers"], key=TIER_ORDER.index)},
                "note": f"DeepSWE v1.1 data available across {len(info['tiers'])} tier(s); baseline = {default_tier}"
                        + ("" if default_tier == "Medium" else " (nearest to Medium)")
            }
        else:
            mapping[m] = {
                "model_id": m,
                "deepswe_status": "pending",
                "benchmarked_name": None,
                "default_tier": None,
                "default_output_tokens_per_task": None,
                "default_score_pct": None,
                "all_tiers": {},
                "all_scores": {},
                "note": "Not evaluated on DeepSWE v1.1; marked pending"
            }

    out_file = DATA_DIR / "model-token-consumption.json"
    with open(out_file, "w", encoding="utf-8") as f:
        json.dump(mapping, f, indent=2, ensure_ascii=False)
    n_available = sum(1 for v in mapping.values() if v["deepswe_status"] == "available")
    print(f"Generated model token consumption mapping: {n_available} available / {len(mapping)} models -> {out_file}")


if __name__ == "__main__":
    build_model_token_map()
