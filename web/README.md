# Web Frontend Staging

This directory holds the scaffolding, data contracts, and ready-to-mount components for the web edition of the Task-Adjusted AI Coding Subscription Rankings.

## Current Status: Staged

As instructed, the web application build is kept in a ready-to-deploy staged state, with all data contracts formalized in `schema.json` and consuming `derived/task-ranking.json`.

When prompted to build the web page, the following interactive features are already mapped out:
1. **Interactive Toggle**: Switch between **Raw Token Price ($/MTok)** and **Task-Adjusted Price ($/Task)** to dynamically visualize the Pareto shift.
2. **Reasoning Effort Selector**: Slider/toggle across Low, Medium, High, and Max reasoning effort to see how thinking tokens affect the economics.
3. **Price Band Tabs**: Quick filters for $0–$30 (Budget), $30–$100 (Pro), and $100–$300 (Power/Enterprise).
4. **Pending Evaluation Inspector**: Filter for unbenchmarked models to monitor missing coverage.
