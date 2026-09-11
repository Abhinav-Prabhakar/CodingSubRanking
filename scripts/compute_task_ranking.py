#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Compute task-adjusted coding subscription rankings using DeepSWE output token consumption."""

import csv
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DATA_DIR = ROOT / "data"
DERIVED_DIR = ROOT / "derived"
DERIVED_DIR.mkdir(exist_ok=True)


ANNUAL_DISCOUNT_RULES = {
    "claude_pro": {"annual_usd": 200.0, "effective_monthly_usd": 200.0 / 12.0, "discount_pct": round((1.0 - (200.0 / 12.0) / 20.0) * 100, 1)},
    "supergrok": {"annual_usd": 300.0, "effective_monthly_usd": 300.0 / 12.0, "discount_pct": round((1.0 - (300.0 / 12.0) / 30.0) * 100, 1)},
    "ollama_pro": {"annual_usd": 200.0, "effective_monthly_usd": 200.0 / 12.0, "discount_pct": round((1.0 - (200.0 / 12.0) / 20.0) * 100, 1)},
}


def get_annual_pricing(plan_id: str, price_usd: float):
    """Return (annual_fee_usd, effective_monthly_fee_usd, discount_pct)."""
    if plan_id in ANNUAL_DISCOUNT_RULES:
        rule = ANNUAL_DISCOUNT_RULES[plan_id]
        return rule["annual_usd"], rule["effective_monthly_usd"], rule["discount_pct"]
    # GLM Coding Plans: 20% discount on continuous monthly / annual commitment for new-customer tiers
    if plan_id.startswith("glm_coding_") and "_new_" in plan_id:
        eff_m = price_usd * 0.8
        ann_usd = eff_m * 12.0
        return ann_usd, eff_m, 20.0
    # Default: 12x monthly, 0% discount
    return price_usd * 12.0, price_usd, 0.0


def compute_task_rankings():
    # Load model token consumption mapping
    with open(DATA_DIR / "model-token-consumption.json", "r", encoding="utf-8") as f:
        model_map = json.load(f)

    # Load adopted subscription data
    with open(DATA_DIR / "adopted.csv", "r", encoding="utf-8-sig") as f:
        rows = list(csv.DictReader(f))

    # Raw ranking by $/MTok for delta comparison
    # Only consider subscriptions with price_usd > 0 and monthly_tokens > 0
    valid_subs = [r for r in rows if float(r.get("monthly_tokens") or 0) > 0 and float(r.get("price_usd") or 0) > 0]
    valid_subs.sort(key=lambda x: float(x["real_usd_per_mtok"]))
    raw_rank_map = {f"{r['plan_id']}__{r['served_model']}": idx + 1 for idx, r in enumerate(valid_subs)}

    benchmarked_points = []
    unbenchmarked_points = []

    for r in rows:
        model = r["served_model"]
        plan_id = r["plan_id"]
        key = f"{plan_id}__{model}"
        m_tokens = float(r.get("monthly_tokens") or 0)
        p_usd = float(r.get("price_usd") or 0)
        raw_price_mtok = float(r.get("real_usd_per_mtok") or 0)
        raw_rank = raw_rank_map.get(key)

        m_info = model_map.get(model, {})
        status = m_info.get("deepswe_status", "pending")

        if status == "available" and m_tokens > 0 and p_usd > 0:
            default_tier = m_info.get("default_tier", "Medium")
            out_tokens = m_info.get("default_output_tokens_per_task")
            score_pct = m_info.get("default_score_pct")

            monthly_tasks = m_tokens / out_tokens
            cost_per_task = p_usd / monthly_tasks
            tasks_per_dollar = monthly_tasks / p_usd

            # Annual pricing
            ann_fee_usd, eff_monthly_usd, ann_disc_pct = get_annual_pricing(plan_id, p_usd)
            cost_per_task_ann = eff_monthly_usd / monthly_tasks
            tasks_per_dollar_ann = monthly_tasks / eff_monthly_usd

            # Also compute for all tiers
            tier_computations = {}
            for t_name, t_tokens in m_info.get("all_tiers", {}).items():
                t_tasks = m_tokens / t_tokens
                t_cost = p_usd / t_tasks
                t_tasks_per_usd = t_tasks / p_usd
                t_cost_ann = eff_monthly_usd / t_tasks
                t_tasks_per_usd_ann = t_tasks / eff_monthly_usd
                t_score = m_info.get("all_scores", {}).get(t_name)
                tier_computations[t_name] = {
                    "output_tokens_per_task": t_tokens,
                    "score_pct": t_score,
                    "monthly_tasks": round(t_tasks, 1),
                    "cost_per_task_usd": round(t_cost, 6),
                    "tasks_per_dollar": round(t_tasks_per_usd, 1),
                    "cost_per_task_annual_usd": round(t_cost_ann, 6),
                    "tasks_per_dollar_annual": round(t_tasks_per_usd_ann, 1),
                }

            entry = {
                "plan_id": plan_id,
                "plan_name": r["plan_name"],
                "billing": r["billing"],
                "price": float(r["price"]),
                "currency": r["currency"],
                "price_usd": p_usd,
                "annual_fee_usd": round(ann_fee_usd, 2),
                "effective_monthly_fee_usd": round(eff_monthly_usd, 2),
                "annual_discount_pct": ann_disc_pct,
                "served_model": model,
                "benchmarked_model_name": m_info.get("benchmarked_name"),
                "benchmark_status": "available",
                "default_tier": default_tier,
                "benchmark_score_pct": score_pct,
                "output_tokens_per_task": out_tokens,
                "monthly_tokens": int(m_tokens),
                "monthly_tasks": round(monthly_tasks, 1),
                "cost_per_task_usd": round(cost_per_task, 6),
                "tasks_per_dollar": round(tasks_per_dollar, 1),
                "cost_per_task_annual_usd": round(cost_per_task_ann, 6),
                "tasks_per_dollar_annual": round(tasks_per_dollar_ann, 1),
                "raw_usd_per_mtok": raw_price_mtok,
                "raw_token_rank": raw_rank,
                "confidence": r.get("confidence", "medium"),
                "chart_tier": r.get("chart_tier", "main"),
                "source": r.get("source", ""),
                "tier_computations": tier_computations
            }
            benchmarked_points.append(entry)
        else:
            ann_fee_usd, eff_monthly_usd, ann_disc_pct = get_annual_pricing(plan_id, p_usd) if p_usd > 0 else (0, 0, 0)
            entry = {
                "plan_id": plan_id,
                "plan_name": r["plan_name"],
                "billing": r["billing"],
                "price": float(r["price"]) if r.get("price") else 0,
                "currency": r["currency"],
                "price_usd": p_usd,
                "annual_fee_usd": round(ann_fee_usd, 2) if p_usd > 0 else None,
                "effective_monthly_fee_usd": round(eff_monthly_usd, 2) if p_usd > 0 else None,
                "annual_discount_pct": ann_disc_pct if p_usd > 0 else None,
                "served_model": model,
                "benchmark_status": "pending",
                "benchmark_note": "[Pending DeepSWE]",
                "output_tokens_per_task": None,
                "monthly_tokens": int(m_tokens) if m_tokens else None,
                "monthly_tasks": None,
                "cost_per_task_usd": None,
                "tasks_per_dollar": None,
                "cost_per_task_annual_usd": None,
                "tasks_per_dollar_annual": None,
                "raw_usd_per_mtok": raw_price_mtok if raw_price_mtok else None,
                "raw_token_rank": raw_rank,
                "confidence": r.get("confidence", "medium"),
                "chart_tier": r.get("chart_tier", "main"),
                "source": r.get("source", "")
            }
            unbenchmarked_points.append(entry)

    # Sort benchmarked points by cost_per_task_usd ascending (cheapest task first)
    benchmarked_points.sort(key=lambda x: x["cost_per_task_usd"])
    for rank, p in enumerate(benchmarked_points, 1):
        p["task_rank"] = rank

    # Recompute relative rank among benchmarked cohort
    benchmarked_by_raw = sorted(benchmarked_points, key=lambda x: x["raw_usd_per_mtok"])
    benchmarked_raw_order = {p["plan_id"] + "__" + p["served_model"]: idx + 1 for idx, p in enumerate(benchmarked_by_raw)}
    for p in benchmarked_points:
        cohort_raw_rank = benchmarked_raw_order[p["plan_id"] + "__" + p["served_model"]]
        p["cohort_raw_rank"] = cohort_raw_rank
        # rank delta = cohort_raw_rank - task_rank (positive = climbed in rank due to low verbosity)
        p["rank_delta"] = cohort_raw_rank - p["task_rank"]

    # Compute annual ranking and annual shift
    benchmarked_by_ann = sorted(benchmarked_points, key=lambda x: x["cost_per_task_annual_usd"])
    for rank, p in enumerate(benchmarked_by_ann, 1):
        p["annual_task_rank"] = rank
        # Shift vs monthly task rank (positive = climbed higher under annual pricing due to discount)
        p["annual_rank_shift"] = p["task_rank"] - rank

    # Save benchmarked ranking
    out_json = DERIVED_DIR / "task-ranking.json"
    with open(out_json, "w", encoding="utf-8") as f:
        json.dump({
            "metadata": {
                "benchmark": "DeepSWE v1.1 (deepswe.datacurve.ai)",
                "metric": "Output token consumption (median output tokens / task)",
                "default_reasoning_tier": "Medium / nearest available",
                "reference_data": "FeiZhuLulu/real-api-pricing",
                "annual_pricing_rules": "12x monthly default; Claude Pro ($200/yr), SuperGrok ($300/yr), Ollama Pro ($200/yr), GLM new plans (20% off)",
                "total_benchmarked_plans": len(benchmarked_points),
                "total_unbenchmarked_plans": len(unbenchmarked_points)
            },
            "rankings": benchmarked_points
        }, f, indent=2, ensure_ascii=False)
    print(f"Saved {len(benchmarked_points)} task-ranked points to {out_json}")

    # Save benchmarked CSV
    csv_fields = [
        "task_rank", "cohort_raw_rank", "rank_delta", "annual_task_rank", "annual_rank_shift",
        "plan_name", "price_usd", "effective_monthly_fee_usd", "annual_fee_usd", "annual_discount_pct",
        "served_model", "output_tokens_per_task", "benchmark_score_pct",
        "monthly_tokens", "monthly_tasks", "cost_per_task_usd", "tasks_per_dollar",
        "cost_per_task_annual_usd", "tasks_per_dollar_annual",
        "raw_usd_per_mtok", "confidence", "plan_id"
    ]
    out_csv = DERIVED_DIR / "task-ranking.csv"
    with open(out_csv, "w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=csv_fields, extrasaction="ignore")
        writer.writeheader()
        writer.writerows(benchmarked_points)
    print(f"Saved {len(benchmarked_points)} task-ranked points to {out_csv}")

    # Save unbenchmarked models
    unbench_json = DERIVED_DIR / "unbenchmarked-models.json"
    with open(unbench_json, "w", encoding="utf-8") as f:
        json.dump(unbenchmarked_points, f, indent=2, ensure_ascii=False)

    unbench_csv = DERIVED_DIR / "unbenchmarked-models.csv"
    with open(unbench_csv, "w", encoding="utf-8", newline="") as f:
        unbench_fields = ["plan_name", "price_usd", "effective_monthly_fee_usd", "annual_fee_usd", "annual_discount_pct", "served_model", "monthly_tokens", "raw_usd_per_mtok", "benchmark_note", "confidence", "plan_id"]
        writer = csv.DictWriter(f, fieldnames=unbench_fields, extrasaction="ignore")
        writer.writeheader()
        writer.writerows(unbenchmarked_points)
    print(f"Saved {len(unbenchmarked_points)} unbenchmarked points to {unbench_csv}")

    return benchmarked_points, unbenchmarked_points


if __name__ == "__main__":
    compute_task_rankings()
