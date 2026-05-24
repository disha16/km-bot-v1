# Research Planner Usage

The research planner creates a **public-source-only secondary market research action plan** from a problem statement. It does not conduct the research. It creates the workplan a researcher should execute.

## Quickstart

Run the AI-backed planner:

```bash
python scripts/create_research_plan.py "Research the autonomous drone market in India" --output outputs/drone_market_india.md
```

Run deterministic mock mode for local smoke tests:

```bash
python scripts/create_research_plan.py "Research the autonomous drone market in India" --mock --output outputs/drone_market_india_mock.md
```

Add optional context:

```bash
python scripts/create_research_plan.py \
  "Research the US home healthcare market" \
  --context "Audience is a seed-stage founder evaluating a tech-enabled services platform. Focus on public information only." \
  --output outputs/us_home_healthcare.md
```

JSON output is also available:

```bash
python scripts/create_research_plan.py "Research the US home healthcare market" --format json --output outputs/us_home_healthcare.json
```

## What The Planner Produces

The output is a Markdown file with a simple table.

| Column | Meaning |
| --- | --- |
| Workstream | The major research module. |
| Things To Be Answered | The specific questions the researcher must answer. |
| Public Sources To Use | Public source categories or examples to use. |
| How To Use Sources | The research method, triangulation method, or analysis approach. |
| Expected Output | The artifact the researcher should create. |
| User Comments / Inputs Needed | Scope, decision context, thresholds, or hypotheses the user should clarify. |
| Priority | High, Medium, or Low. |

## Current Guardrails

The planner is intentionally constrained for v1.

| Guardrail | Rule |
| --- | --- |
| Public information only | The planner must not recommend private datasets, paid expert calls, leaked information, confidential client data, or non-public company documents. |
| Banned low-confidence aggregators | The planner must not use or recommend Grand View Research, IMARC, or Future Market Insights. |
| Research planning only | The planner should not invent facts or perform final analysis. It should design the workplan. |
| MBB/VC-style quality bar | The planner should be hypothesis-led, MECE-ish, source-specific, and explicit about gaps. |

## Style Rules Added From Training Material

The planner has been updated to reflect the uploaded VC research-agent training document. The most important behaviors are:

| Rule | Expected Behavior |
| --- | --- |
| Template selection | Identify whether the problem is a sector study, market-entry screen, investment thesis, company diligence, competitive landscape, pricing/economics study, or quick screen. |
| TAM triangulation | For market sizing, require at least two triangulation paths and one bottom-up public proxy. |
| Public comparables | When financial analysis matters, identify the need for 3-4 public comps or proxy comps and the relevant metrics. |
| Moat discipline | Do not accept generic moat claims. Require evidence for switching costs, network effects, scale, data advantage, regulatory advantage, retention, or pricing power. |
| Gap discipline | Identify what public desk research cannot answer and propose proxy signals. |

## How To Train The Tool Further

Use **rules + examples + review rubrics**.

1. Generate first-pass plans for 10-20 realistic problem statements.
2. Rewrite the weak rows the way you would as an ex-MBB reviewer.
3. Save each corrected example in `examples/research_plan_training_examples.md`.
4. Tag the failure mode, such as `too generic`, `weak public sources`, `missing buyer segmentation`, `no bottom-up sizing`, or `unclear user input`.
5. Promote repeated corrections into explicit rules in `docs/playbooks/secondary_market_research.md` and the planner prompt.

Fine-tuning is not the first step. Start with rules, retrieved examples, and a rubric. Consider fine-tuning only after collecting many reviewed examples and seeing stable failure patterns.
