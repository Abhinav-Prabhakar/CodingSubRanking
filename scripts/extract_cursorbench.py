#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Extract CursorBench 4.0 data (output token consumption per task, score, cost, steps)."""

import json
import re
import csv
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DATA_DIR = ROOT / "data"

# Source path where raw HTML is cached
HTML_SOURCE = Path("/Users/abhinav/.gemini/antigravity/brain/b73cc716-1b8a-4e17-aecb-2ff10ff23ab7/.system_generated/steps/10/content.md")


def extract_cursorbench():
    with open(HTML_SOURCE, "r", encoding="utf-8") as f:
        html = f.read()

    tbody_match = re.search(r'<tbody>(.*?)</tbody>', html, re.DOTALL)
    if not tbody_match:
        raise ValueError("Could not find tbody in CursorBench HTML")

    rows = re.findall(r'<tr.*?>(.*?)</tr>', tbody_match.group(1), re.DOTALL)
    results = []

    # Map model entry name to base model and reasoning effort
    for row in rows:
        cols = re.findall(r'<td.*?>(.*?)</td>', row, re.DOTALL)
        clean_cols = [re.sub(r'<.*?>', '', c).strip() for c in cols]
        if len(clean_cols) < 6:
            continue

        rank = int(clean_cols[0])
        full_name = clean_cols[1]
        score_pct = float(clean_cols[2].replace("%", "").strip())
        cost_usd = float(clean_cols[3].replace("$", "").replace(",", "").strip())
        tokens_per_task = int(clean_cols[4].replace(",", "").strip())
        steps_per_task = int(clean_cols[5].replace(",", "").strip())

        # Determine base model and reasoning tier
        effort = "Standard"
        base_name = full_name
        for tier in ["Extra High", "Max", "High", "Medium", "Low", "Minimal"]:
            if full_name.endswith(tier):
                effort = tier
                base_name = full_name[:-len(tier)].strip()
                break

        # Canonical model ID mapping matching adopted.csv
        canonical_id = None
        if "Fable 5.1" in base_name:
            canonical_id = "claude-fable-5"
        elif "Opus 5" in base_name:
            canonical_id = "claude-opus-5"
        elif "Sonnet 5" in base_name:
            canonical_id = "claude-sonnet-5"
        elif "GPT-5.6 Sol" in base_name:
            canonical_id = "gpt-5.6-sol"
        elif "GPT-5.6 Terra" in base_name:
            canonical_id = "gpt-5.6-terra"
        elif "GPT-5.6 Luna" in base_name:
            canonical_id = "gpt-5.6-luna"
        elif "Grok 4.6" in base_name:
            canonical_id = "grok-4.6"
        elif "Gemini 3.8 Flash" in base_name:
            canonical_id = "gemini-3.8-flash"
        elif "Muse Spark 1.3" in base_name:
            canonical_id = "muse-spark-1.3"
        elif "Composer 2.5" in base_name:
            canonical_id = "composer-2.5"

        results.append({
            "rank": rank,
            "display_name": full_name,
            "base_model": base_name,
            "canonical_model_id": canonical_id,
            "reasoning_effort": effort,
            "score_pct": score_pct,
            "cost_usd_per_task": cost_usd,
            "output_tokens_per_task": tokens_per_task,
            "steps_per_task": steps_per_task,
            "source_url": "https://cursor.com/cursorbench"
        })

    # Save to json
    json_path = DATA_DIR / "cursorbench.json"
    with open(json_path, "w", encoding="utf-8") as f:
        json.dump(results, f, indent=2, ensure_ascii=False)
    print(f"Saved {len(results)} CursorBench records to {json_path}")

    # Save to csv
    csv_path = DATA_DIR / "cursorbench.csv"
    with open(csv_path, "w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=[
            "rank", "display_name", "base_model", "canonical_model_id",
            "reasoning_effort", "score_pct", "cost_usd_per_task",
            "output_tokens_per_task", "steps_per_task", "source_url"
        ])
        writer.writeheader()
        writer.writerows(results)
    print(f"Saved {len(results)} CursorBench records to {csv_path}")

    return results


if __name__ == "__main__":
    extract_cursorbench()
