#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Re-embed the data blobs in web/index.html from the derived ranking outputs.

Regenerates ROWS (default-tier benchmarked ranking), BENCH (DeepSWE configs),
PENDING (models without DeepSWE evaluation) and TIERS (per-model per-tier
median output tokens & Pass@1), plus the hardcoded count strings that reference
them, so the static page stays byte-faithful to derived/*.json.

Run after compute_task_ranking.py.
"""

import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DERIVED = ROOT / "derived"
DATA = ROOT / "data"
HTML = ROOT / "web" / "index.html"


def main():
    rankings = json.loads((DERIVED / "task-ranking.json").read_text(encoding="utf-8"))["rankings"]
    unbenchmarked = json.loads((DERIVED / "unbenchmarked-models.json").read_text(encoding="utf-8"))
    all_efforts = json.loads((DERIVED / "task-ranking-all-efforts.json").read_text(encoding="utf-8"))
    dswe = json.loads((DATA / "deepswe-configs.json").read_text(encoding="utf-8"))
    model_map = json.loads((DATA / "model-token-consumption.json").read_text(encoding="utf-8"))

    n_all_efforts = all_efforts["metadata"]["total_configurations"]

    # ROWS: benchmarked plans at default tier (client expands across TIERS for all efforts)
    rows = [{
        "p": r["plan_name"], "m": r["served_model"],
        "fee": r["price_usd"], "feeAnn": r["effective_monthly_fee_usd"], "annDisc": r["annual_discount_pct"],
        "tok": r["output_tokens_per_task"], "mtok": r["monthly_tokens"], "tasks": r["monthly_tasks"],
        "cpt": r["cost_per_task_usd"], "tpd": r["tasks_per_dollar"],
        "cptAnn": r["cost_per_task_annual_usd"], "tpdAnn": r["tasks_per_dollar_annual"],
        "raw": r["raw_usd_per_mtok"], "craw": r["cohort_raw_rank"],
        "mRank": r["task_rank"], "aRank": r["annual_task_rank"], "aShift": r["annual_rank_shift"],
    } for r in rankings]

    # BENCH: DeepSWE configurations ordered by leaderboard rank
    bench = [{
        "r": e["rank"], "n": f"{e['display_name']} {e['reasoning_effort']}",
        "s": e["score_pct"], "c": e["cost_usd_per_task"],
        "t": e["output_tokens_per_task"], "st": e["steps_per_task"],
    } for e in dswe]

    # PENDING: served models with no DeepSWE evaluation
    pending = sorted(k for k, v in model_map.items() if v.get("deepswe_status") != "available")

    # TIERS: per-model per-tier {median output tokens, Pass@1}
    tiers = {}
    for model_id, info in model_map.items():
        if info.get("deepswe_status") != "available":
            continue
        tiers[model_id] = {
            tier: {"t": tok, "s": info.get("all_scores", {}).get(tier)}
            for tier, tok in info.get("all_tiers", {}).items()
        }

    html = HTML.read_text(encoding="utf-8")

    def splice(name, payload, pretty=False):
        nonlocal html
        text = json.dumps(payload, ensure_ascii=False, indent=2 if pretty else None)
        html = re.sub(rf"const {name} = .*?;", f"const {name} = {text};", html, count=1, flags=re.S)

    splice("ROWS", rows)
    splice("BENCH", bench)
    splice("PENDING", pending)
    splice("TIERS", tiers, pretty=True)

    # Hardcoded count strings that mirror the blobs
    n_pending_models = len(pending)
    n_pending_plans = sum(1 for e in unbenchmarked if e.get("billing") == "subscription" and e.get("benchmark_status") == "pending")
    n_families = sum(1 for v in model_map.values() if v.get("deepswe_status") == "available")
    terra_shift = max((r["rank_delta"] for r in rankings if r["served_model"] == "gpt-5.6-terra"), default=0)

    html = re.sub(r"\d+ plan × effort configurations", f"{n_all_efforts} plan × effort configurations", html)
    html = re.sub(r"all evaluated effort tiers \(\d+ configurations", f"all evaluated effort tiers ({n_all_efforts} configurations", html)
    html = re.sub(r"\+\d+ spots", f"+{terra_shift} spots", html)
    html = re.sub(r">\d+ model families with plans<", f">{n_families} model families with plans<", html)
    html = re.sub(r">\d+ models</span>", f">{n_pending_models} models</span>", html)
    html = re.sub(r">\d+ plans pending</span>", f">{n_pending_plans} plans pending</span>", html)

    HTML.write_text(html, encoding="utf-8")
    print(f"web/index.html updated: {len(rows)} ROWS, {len(bench)} BENCH, {len(pending)} PENDING, "
          f"{len(tiers)} TIERS models | all-efforts={n_all_efforts}, pending plans={n_pending_plans}, terra +{terra_shift}")


if __name__ == "__main__":
    main()
