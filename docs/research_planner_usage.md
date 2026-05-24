# Research Planner Usage

## What This Does

The research planner converts a problem statement into a public-source-only secondary research action plan. It is backend-only for now; there is no frontend. The first use case is `secondary_market_research`.

Example problem statement:

> Research the autonomous drone market in India.

The tool returns a structured Markdown table with workstreams, questions to answer, public sources to use, how to use them, expected outputs, user comments or inputs needed, and priority.

## Run With AI

Set `OPENAI_API_KEY` in your environment, then run:

```bash
python scripts/create_research_plan.py "Research the autonomous drone market in India" --output outputs/drone_market_india.md
```

You can add user context:

```bash
python scripts/create_research_plan.py \
  "Research the autonomous drone market in India" \
  --context "Audience is a founder evaluating B2B market entry over the next 24 months." \
  --output outputs/drone_market_india.md
```

## Run A Local Smoke Test Without AI

```bash
python scripts/create_research_plan.py "Research the autonomous drone market in India" --mock
```

## Output Formats

Markdown is the default because it is easy to read and paste into a working document. JSON is available for programmatic use.

```bash
python scripts/create_research_plan.py "Research the autonomous drone market in India" --format json --output outputs/drone_market_india.json
```

## Public-Information Constraint

The planner is constrained to public information only. It should not recommend confidential client data, paid expert calls, private datasets, leaked material, or non-public company documents. If a private source would normally be useful, the planner should suggest a public proxy instead.

## How To Make It More MBB-ish

The planner should be trained through a combination of rules, examples, and rubrics. Add rules to define source discipline and decomposition structure. Add examples to teach your preferred style. Add rubrics to make your feedback reusable.

A practical training loop is:

| Step | Action |
| --- | --- |
| 1 | Generate a plan for a real problem statement. |
| 2 | Mark rows as strong, weak, missing, or too generic. |
| 3 | Rewrite the weak parts in your preferred style. |
| 4 | Save the before/after pair as a gold-standard example. |
| 5 | Update the prompt contract only when the same issue appears repeatedly. |

Start with 5-10 gold-standard examples. Do not fine-tune until you have enough reviewed examples to see stable patterns.
