#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Extract DeepSWE v1.1 benchmark data (output token consumption per task, score, cost, steps).

Source: https://deepswe.datacurve.ai/ — Datacurve's long-horizon software engineering
benchmark (113 tasks, 91 repos, 5 languages). The leaderboard artifact at
https://deepswe.datacurve.ai/artifacts/v1.1/leaderboard-live.json contains one row per
configuration (harness + model + reasoning effort) with exact mean/median output tokens.

Methodology note: we use `median_output_tokens` per configuration, consistent with the
previous CursorBench "median completion tokens per task" convention.
"""

import json
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DATA_DIR = ROOT / "data"

ARTIFACT_URL = "https://deepswe.datacurve.ai/artifacts/v1.1/leaderboard-live.json"
SOURCE_URL = "https://deepswe.datacurve.ai/"

# DeepSWE model ids use dashes for version dots (gpt-5-6-luna); normalize to the
# dotted ids used by adopted.csv (gpt-5.6-luna).
MODEL_ID_MAP = {
    "claude-fable-5": "claude-fable-5",
    "claude-opus-4-8": "claude-opus-4.8",
    "claude-opus-5": "claude-opus-5",
    "claude-sonnet-4-6": "claude-sonnet-4.6",
    "claude-sonnet-5": "claude-sonnet-5",
    "deepseek-v4-flash": "deepseek-v4-flash",
    "deepseek-v4-pro": "deepseek-v4-pro",
    "gemini-3-1-pro-preview": "gemini-3.1-pro-preview",
    "gemini-3-5-flash": "gemini-3.5-flash",
    "gemini-3-6-flash": "gemini-3.6-flash",
    "gemini-3-7-flash": "gemini-3.7-flash",
    "gemini-3-8-flash": "gemini-3.8-flash",
    "glm-5-2": "glm-5.2",
    "glm-5-3": "glm-5.3",
    "glm-5-3-flash": "glm-5.3-flash",
    "gpt-5-4": "gpt-5.4",
    "gpt-5-5": "gpt-5.5",
    "gpt-5-6-luna": "gpt-5.6-luna",
    "gpt-5-6-sol": "gpt-5.6-sol",
    "gpt-5-6-terra": "gpt-5.6-terra",
    "gpt-6-astra": "gpt-6-astra",
    "grok-4-5": "grok-4.5",
    "grok-4-6": "grok-4.6",
    "kimi-k2-7-code": "kimi-k2.7-code",
    "kimi-k3": "kimi-k3",
    "muse-spark-1-1": "muse-spark-1.1",
    "muse-spark-1-2": "muse-spark-1.2",
    "qwen3-8-max": "qwen3.8-max",
}

DISPLAY_NAMES = {
    "claude-fable-5": "Claude Fable 5",
    "claude-opus-4.8": "Claude Opus 4.8",
    "claude-opus-5": "Claude Opus 5",
    "claude-sonnet-4.6": "Claude Sonnet 4.6",
    "claude-sonnet-5": "Claude Sonnet 5",
    "deepseek-v4-flash": "DeepSeek V4 Flash",
    "deepseek-v4-pro": "DeepSeek V4 Pro",
    "gemini-3.1-pro-preview": "Gemini 3.1 Pro Preview",
    "gemini-3.5-flash": "Gemini 3.5 Flash",
    "gemini-3.6-flash": "Gemini 3.6 Flash",
    "gemini-3.7-flash": "Gemini 3.7 Flash",
    "gemini-3.8-flash": "Gemini 3.8 Flash",
    "glm-5.2": "GLM-5.2",
    "glm-5.3": "GLM-5.3",
    "glm-5.3-flash": "GLM-5.3 Flash",
    "gpt-5.4": "GPT-5.4",
    "gpt-5.5": "GPT-5.5",
    "gpt-5.6-luna": "GPT-5.6 Luna",
    "gpt-5.6-sol": "GPT-5.6 Sol",
    "gpt-5.6-terra": "GPT-5.6 Terra",
    "gpt-6-astra": "GPT-6 Astra",
    "grok-4.5": "Grok 4.5",
    "grok-4.6": "Grok 4.6",
    "kimi-k2.7-code": "Kimi K2.7 Code",
    "kimi-k3": "Kimi K3",
    "muse-spark-1.1": "Muse Spark 1.1",
    "muse-spark-1.2": "Muse Spark 1.2",
    "qwen3.8-max": "Qwen3.8 Max",
}

# DeepSWE effort labels -> repo convention
EFFORT_MAP = {
    "low": "Low",
    "medium": "Medium",
    "high": "High",
    "xhigh": "Extra High",
    "max": "Max",
    None: "Standard",
}


def fetch_artifact():
    cache = DATA_DIR / "deepswe.json"
    if cache.exists():
        with open(cache, "r", encoding="utf-8") as f:
            return json.load(f)
    req = urllib.request.Request(ARTIFACT_URL, headers={"User-Agent": "CodingSubRanking/1.0"})
    with urllib.request.urlopen(req, timeout=60) as resp:
        data = json.load(resp)
    with open(cache, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
    return data


def extract_deepswe():
    artifact = fetch_artifact()
    rows = artifact["rows"]

    configs = []
    for r in rows:
        source_model = r["model"]
        model_id = MODEL_ID_MAP.get(source_model)
        if model_id is None:
            raise ValueError(f"Unknown DeepSWE model id: {source_model!r} — extend MODEL_ID_MAP")
        effort = EFFORT_MAP.get(r.get("reasoning_effort"), r.get("reasoning_effort"))
        median_tokens = r.get("median_output_tokens")
        if median_tokens is None:
            continue  # skip configurations without usable consumption data
        configs.append({
            "model_id": model_id,
            "source_model": source_model,
            "display_name": DISPLAY_NAMES[model_id],
            "reasoning_effort": effort,
            "score_pct": round(r["pass_at_1"] * 100, 1),
            "cost_usd_per_task": round(r["mean_cost_usd"], 2),
            "output_tokens_per_task": int(round(median_tokens)),
            "mean_output_tokens": round(r["mean_output_tokens"], 1),
            "steps_per_task": int(round(r["mean_agent_steps"])),
            "n_attempted": r["n_attempted"],
            "harness": r.get("harness"),
            "source_url": SOURCE_URL,
        })

    # Leaderboard order: score desc, then cost asc
    configs.sort(key=lambda c: (-c["score_pct"], c["cost_usd_per_task"]))
    for rank, c in enumerate(configs, 1):
        c["rank"] = rank

    out = DATA_DIR / "deepswe-configs.json"
    with open(out, "w", encoding="utf-8") as f:
        json.dump(configs, f, indent=2, ensure_ascii=False)

    models = sorted({c["model_id"] for c in configs})
    print(f"Saved {len(configs)} DeepSWE configurations across {len(models)} models -> {out}")
    print(f"Artifact generated_at: {artifact.get('generated_at')}")


if __name__ == "__main__":
    extract_deepswe()
