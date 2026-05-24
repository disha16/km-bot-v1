#!/usr/bin/env python3
"""Generate a public-source-only research action plan from a problem statement.

Examples:
  python scripts/create_research_plan.py "Research the autonomous drone market in India" --mock
  python scripts/create_research_plan.py "Research the autonomous drone market in India" --format markdown --output outputs/drone_market_india.md
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
SRC_ROOT = REPO_ROOT / "src"
if str(SRC_ROOT) not in sys.path:
    sys.path.insert(0, str(SRC_ROOT))

from research_planner.planner import (  # noqa: E402
    DEFAULT_MODEL,
    generate_mock_plan,
    generate_research_plan,
    plan_to_markdown,
)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Create a public-source-only MBB-style secondary research action plan."
    )
    parser.add_argument(
        "problem_statement",
        help="The problem statement to break down, e.g. 'Research the autonomous drone market in India'.",
    )
    parser.add_argument(
        "--context",
        default=None,
        help="Optional extra context such as decision objective, geography, time horizon, or audience.",
    )
    parser.add_argument(
        "--model",
        default=DEFAULT_MODEL,
        help=f"AI model to use. Default: {DEFAULT_MODEL}",
    )
    parser.add_argument(
        "--format",
        choices=["markdown", "json"],
        default="markdown",
        help="Output format. Default: markdown.",
    )
    parser.add_argument(
        "--output",
        default=None,
        help="Optional output file path. If omitted, prints to stdout.",
    )
    parser.add_argument(
        "--mock",
        action="store_true",
        help="Use deterministic mock output for local smoke tests without an AI call.",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()

    if args.mock:
        plan = generate_mock_plan(args.problem_statement)
    else:
        plan = generate_research_plan(
            problem_statement=args.problem_statement,
            user_context=args.context,
            model=args.model,
        )

    if args.format == "json":
        rendered = json.dumps(plan, indent=2, ensure_ascii=False)
    else:
        rendered = plan_to_markdown(plan)

    if args.output:
        output_path = Path(args.output)
        output_path.parent.mkdir(parents=True, exist_ok=True)
        output_path.write_text(rendered + "\n", encoding="utf-8")
        print(f"Wrote research plan to {output_path}")
    else:
        print(rendered)

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
