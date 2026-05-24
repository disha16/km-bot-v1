"""AI-backed research action plan generator.

This module turns a business problem statement into a consultant-style secondary
research plan. It is intentionally backend-only and public-source-only for v1.
"""

from __future__ import annotations

import json
import os
from typing import Any, Dict, List, Optional


DEFAULT_MODEL = os.getenv("KM_BOT_MODEL", "gpt-4.1-mini")

PUBLIC_SOURCE_POLICY = (
    "Use only public information sources. Do not recommend confidential client "
    "data, paid expert calls, private databases, leaked materials, or non-public "
    "company documents. If a useful source would normally be private or paid, "
    "replace it with a public proxy such as regulator filings, government data, "
    "public company reports, trade body publications, procurement portals, news, "
    "public datasets, app stores, patent databases, job postings, public pricing "
    "pages, academic papers, or credible interviews already published online."
)

SYSTEM_PROMPT = f"""
You are a senior strategy consultant helping build a secondary market research plan.
Think like a top-tier consulting team, but do not use jargon for its own sake.

Your job is to take a user problem statement and break it into a practical research
action plan. The output must be a simple, useful table that a junior researcher can
execute.

Operating principles:
1. Start from the decision the user likely needs to make, not from generic facts.
2. Break the problem into mutually exclusive, collectively exhaustive workstreams where possible.
3. Convert each workstream into answerable research questions.
4. Prefer public source triangulation over single-source claims.
5. Identify what each source type is good for and how it should be used.
6. Separate facts to collect from hypotheses to test.
7. Surface gaps, judgment calls, and user inputs needed to sharpen the work.
8. Keep recommendations execution-oriented and specific.

Source policy:
{PUBLIC_SOURCE_POLICY}

Do not perform the research. Create the action plan only.
Return valid JSON matching the provided schema.
""".strip()

RESEARCH_PLAN_SCHEMA: Dict[str, Any] = {
    "name": "research_action_plan",
    "schema": {
        "type": "object",
        "additionalProperties": False,
        "properties": {
            "problem_statement": {"type": "string"},
            "interpreted_decision_context": {"type": "string"},
            "research_objective": {"type": "string"},
            "scope_boundaries": {
                "type": "object",
                "additionalProperties": False,
                "properties": {
                    "in_scope": {"type": "array", "items": {"type": "string"}},
                    "out_of_scope": {"type": "array", "items": {"type": "string"}},
                },
                "required": ["in_scope", "out_of_scope"],
            },
            "initial_hypotheses": {"type": "array", "items": {"type": "string"}},
            "research_plan": {
                "type": "array",
                "items": {
                    "type": "object",
                    "additionalProperties": False,
                    "properties": {
                        "workstream": {"type": "string"},
                        "things_to_be_answered": {"type": "string"},
                        "public_sources_to_use": {"type": "string"},
                        "how_to_use_sources": {"type": "string"},
                        "expected_output": {"type": "string"},
                        "user_comments_or_inputs_needed": {"type": "string"},
                        "priority": {"type": "string", "enum": ["High", "Medium", "Low"]},
                    },
                    "required": [
                        "workstream",
                        "things_to_be_answered",
                        "public_sources_to_use",
                        "how_to_use_sources",
                        "expected_output",
                        "user_comments_or_inputs_needed",
                        "priority",
                    ],
                },
            },
            "cross_checks": {"type": "array", "items": {"type": "string"}},
            "likely_gaps": {"type": "array", "items": {"type": "string"}},
            "suggested_user_inputs": {"type": "array", "items": {"type": "string"}},
            "source_policy": {"type": "string"},
        },
        "required": [
            "problem_statement",
            "interpreted_decision_context",
            "research_objective",
            "scope_boundaries",
            "initial_hypotheses",
            "research_plan",
            "cross_checks",
            "likely_gaps",
            "suggested_user_inputs",
            "source_policy",
        ],
    },
}


def build_user_prompt(problem_statement: str, user_context: Optional[str] = None) -> str:
    """Create the user prompt passed to the model."""

    context_block = f"\nAdditional user context:\n{user_context.strip()}\n" if user_context else ""
    return f"""
Problem statement:
{problem_statement.strip()}
{context_block}
Create a secondary market research action plan. Keep it public-source-only.
The table must be practical enough for a researcher to execute immediately.
""".strip()


def generate_research_plan(
    problem_statement: str,
    user_context: Optional[str] = None,
    model: str = DEFAULT_MODEL,
) -> Dict[str, Any]:
    """Generate a public-source-only research action plan using an AI model."""

    if not problem_statement or not problem_statement.strip():
        raise ValueError("problem_statement is required")

    try:
        from openai import OpenAI
    except ImportError as exc:
        raise RuntimeError(
            "The openai package is required. Install it with: pip install openai"
        ) from exc

    client = OpenAI()
    response = client.chat.completions.create(
        model=model,
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": build_user_prompt(problem_statement, user_context)},
        ],
        response_format={
            "type": "json_schema",
            "json_schema": {
                "name": RESEARCH_PLAN_SCHEMA["name"],
                "schema": RESEARCH_PLAN_SCHEMA["schema"],
                "strict": True,
            },
        },
        temperature=0.2,
    )

    content = response.choices[0].message.content
    if not content:
        raise RuntimeError("Model returned an empty response")

    plan = json.loads(content)
    plan["source_policy"] = PUBLIC_SOURCE_POLICY
    return plan


def generate_mock_plan(problem_statement: str) -> Dict[str, Any]:
    """Deterministic fallback for local smoke tests without calling an AI model."""

    clean_problem = problem_statement.strip()
    return {
        "problem_statement": clean_problem,
        "interpreted_decision_context": (
            "Understand whether the market is attractive, where growth is concentrated, "
            "which segments matter, and what evidence is needed to support an entry or investment view."
        ),
        "research_objective": (
            "Build a public-source-backed view of market size, growth, segments, competitive landscape, "
            "regulation, customer demand, and open questions."
        ),
        "scope_boundaries": {
            "in_scope": [
                "Publicly available market, regulatory, company, customer, and technology signals",
                "Evidence that can be collected through desk research",
            ],
            "out_of_scope": [
                "Private client data",
                "Paid expert calls",
                "Non-public company documents",
            ],
        },
        "initial_hypotheses": [
            "The market may have multiple segments with different growth drivers and regulatory constraints.",
            "Public data will likely require triangulation because no single source will be complete.",
        ],
        "research_plan": [
            {
                "workstream": "Market definition and segmentation",
                "things_to_be_answered": "What exactly is included in the market, and which segments should be analyzed separately?",
                "public_sources_to_use": "Government policy documents, regulator websites, industry association publications, public company descriptions, credible news explainers.",
                "how_to_use_sources": "Create a market map, define segment boundaries, and list inclusion/exclusion rules before sizing.",
                "expected_output": "Market definition, segment taxonomy, and scope note.",
                "user_comments_or_inputs_needed": "Confirm geography, time horizon, and whether the plan is for entry, investment, partnership, or strategy refresh.",
                "priority": "High",
            },
            {
                "workstream": "Market size and growth",
                "things_to_be_answered": "How large is the market today, how fast is it growing, and what are the credible ranges?",
                "public_sources_to_use": "Government datasets, public tenders, listed company filings, trade body reports, credible media, academic papers.",
                "how_to_use_sources": "Triangulate top-down and bottom-up estimates; document assumptions and confidence levels.",
                "expected_output": "Sizing range, growth drivers, and confidence assessment.",
                "user_comments_or_inputs_needed": "Provide any preferred sizing definition, currency, and forecast horizon.",
                "priority": "High",
            },
            {
                "workstream": "Competitive and ecosystem landscape",
                "things_to_be_answered": "Who are the relevant players, where do they compete, and what capabilities differentiate them?",
                "public_sources_to_use": "Company websites, public case studies, app stores, job postings, patents, press releases, procurement portals, investor materials.",
                "how_to_use_sources": "Build a competitor long list, tag by segment, and infer capabilities from public evidence.",
                "expected_output": "Competitor map and capability matrix.",
                "user_comments_or_inputs_needed": "Confirm if specific competitor types should be emphasized or excluded.",
                "priority": "Medium",
            },
        ],
        "cross_checks": [
            "Check every market-size estimate against at least two independent public sources.",
            "Separate observed facts from inferred conclusions.",
        ],
        "likely_gaps": [
            "Segment-level revenue may be unavailable in public sources.",
            "Demand-side data may require proxies such as procurement volume, hiring, or adoption case studies.",
        ],
        "suggested_user_inputs": [
            "Decision objective",
            "Target geography and time horizon",
            "Known hypotheses to test",
        ],
        "source_policy": PUBLIC_SOURCE_POLICY,
    }


def plan_to_markdown(plan: Dict[str, Any]) -> str:
    """Render a generated plan as a concise Markdown document with the core table."""

    lines: List[str] = []
    lines.append(f"# Research Action Plan: {plan.get('problem_statement', '').strip()}")
    lines.append("")
    lines.append(f"**Decision context:** {plan.get('interpreted_decision_context', '').strip()}")
    lines.append("")
    lines.append(f"**Research objective:** {plan.get('research_objective', '').strip()}")
    lines.append("")

    hypotheses = plan.get("initial_hypotheses") or []
    if hypotheses:
        lines.append("## Initial Hypotheses")
        lines.append("")
        for item in hypotheses:
            lines.append(f"- {item}")
        lines.append("")

    lines.append("## Research Plan")
    lines.append("")
    lines.append(
        "| Workstream | Things To Be Answered | Public Sources To Use | How To Use Sources | Expected Output | User Comments / Inputs Needed | Priority |"
    )
    lines.append("| --- | --- | --- | --- | --- | --- | --- |")
    for row in plan.get("research_plan", []):
        lines.append(
            "| {workstream} | {things} | {sources} | {how} | {output} | {inputs} | {priority} |".format(
                workstream=_escape_md(row.get("workstream", "")),
                things=_escape_md(row.get("things_to_be_answered", "")),
                sources=_escape_md(row.get("public_sources_to_use", "")),
                how=_escape_md(row.get("how_to_use_sources", "")),
                output=_escape_md(row.get("expected_output", "")),
                inputs=_escape_md(row.get("user_comments_or_inputs_needed", "")),
                priority=_escape_md(row.get("priority", "")),
            )
        )
    lines.append("")

    _append_list_section(lines, "Cross-Checks", plan.get("cross_checks") or [])
    _append_list_section(lines, "Likely Gaps", plan.get("likely_gaps") or [])
    _append_list_section(lines, "Suggested User Inputs", plan.get("suggested_user_inputs") or [])

    lines.append("## Source Policy")
    lines.append("")
    lines.append(plan.get("source_policy", PUBLIC_SOURCE_POLICY))
    lines.append("")
    return "\n".join(lines)


def _append_list_section(lines: List[str], title: str, items: List[str]) -> None:
    if not items:
        return
    lines.append(f"## {title}")
    lines.append("")
    for item in items:
        lines.append(f"- {item}")
    lines.append("")


def _escape_md(value: str) -> str:
    return str(value).replace("|", "\\|").replace("\n", " ").strip()
