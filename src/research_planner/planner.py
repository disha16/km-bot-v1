"""AI-backed research action plan generator.

This module turns a business problem statement into a consultant-style secondary
research plan. It is intentionally backend-only and public-source-only for v1.
"""

from __future__ import annotations

import json
import os
from typing import Any, Dict, List, Optional


DEFAULT_MODEL = os.getenv("KM_BOT_MODEL", "gpt-4.1-mini")

BANNED_SOURCES = ["Grand View Research", "IMARC", "Future Market Insights"]

PREFERRED_SOURCE_HIERARCHY = [
    "Regulatory filings, government datasets, official statistics, procurement portals, and court/regulator records",
    "Company investor relations, annual reports, SEC filings, earnings transcripts, pricing pages, product docs, and official announcements",
    "Industry associations, standards bodies, trade bodies, public conference materials, and academic or patent databases",
    "Reputable business press, specialist trade press, public interviews, podcasts, and case studies",
    "Public digital exhaust such as job postings, app stores, review sites, web traffic proxies, developer communities, and public customer forums",
]

PUBLIC_SOURCE_POLICY = (
    "Use only public information sources. Do not recommend confidential client data, "
    "paid expert calls, private databases, leaked materials, or non-public company documents. "
    "Do not use or cite banned low-confidence aggregator sources: "
    f"{', '.join(BANNED_SOURCES)}. If a useful source would normally be private or paid, "
    "replace it with a public proxy such as regulator filings, government data, public company reports, "
    "trade body publications, procurement portals, public pricing pages, product documentation, "
    "news, academic papers, patent databases, app stores, job postings, public customer reviews, "
    "credible interviews already published online, or other verifiable public sources."
)

PREFERRED_SOURCE_HIERARCHY_TEXT = "\n- ".join(PREFERRED_SOURCE_HIERARCHY)
BANNED_SOURCES_TEXT = "\n- ".join(BANNED_SOURCES)

SYSTEM_PROMPT = f"""
You are a senior MBB-style strategy consultant and VC research lead helping build a
secondary market research action plan. Think like a partner giving an analyst an
execution-ready workplan: hypothesis-led, source-specific, and designed to expose
both opportunities and evidence gaps.

Your job is to take a user problem statement and break it into a practical research
action plan. The output must be a simple, useful table that a junior researcher can
execute. Do not perform the research or invent facts. Plan the research.

Operating principles:
1. Start from the decision the user likely needs to make, not from generic facts.
2. Select the likely research template: sector study, market-entry screen, investment thesis,
   company diligence, competitive landscape, pricing/economics study, or quick screen.
3. Break the problem into MECE-ish workstreams, but prioritize usefulness over rigid labels.
4. Convert each workstream into answerable research questions and explicit output artifacts.
5. Prefer public source triangulation over single-source claims.
6. Separate disclosed data, estimated data, proxy data, and unavailable data.
7. Surface gaps, judgment calls, and user inputs needed to sharpen the work.
8. Keep recommendations execution-oriented and specific.
9. Identify both direct competitors and indirect substitutes when competition is relevant.
10. For market sizing, require bottom-up validation and at least two triangulation paths.
11. For financial analysis, require public comparables and relevant metrics where available.
12. For moats, require evidence of the mechanism, not generic claims like "brand" or "technology".

Public-source policy:
{PUBLIC_SOURCE_POLICY}

Preferred public-source hierarchy:
- {PREFERRED_SOURCE_HIERARCHY_TEXT}

Banned sources:
- {BANNED_SOURCES_TEXT}

Quality bar:
- Every plan row should be specific enough that a researcher knows exactly what to search for.
- Include public-source examples, not just generic phrases like "industry reports".
- Make the user-input column meaningful; use it to identify decision context, scope, definitions,
  time horizon, threshold economics, target buyer, or hypotheses that need clarification.
- Use 6-10 workstreams unless the problem is very narrow.
- Do not include private interviews, expert calls, paid databases, or non-public documents.

Return valid JSON matching the provided schema.
""".strip()

RESEARCH_PLAN_SCHEMA: Dict[str, Any] = {
    "name": "research_action_plan",
    "schema": {
        "type": "object",
        "additionalProperties": False,
        "properties": {
            "problem_statement": {"type": "string"},
            "template_selected": {"type": "string"},
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
            "quality_checks": {"type": "array", "items": {"type": "string"}},
            "source_policy": {"type": "string"},
        },
        "required": [
            "problem_statement",
            "template_selected",
            "interpreted_decision_context",
            "research_objective",
            "scope_boundaries",
            "initial_hypotheses",
            "research_plan",
            "cross_checks",
            "likely_gaps",
            "suggested_user_inputs",
            "quality_checks",
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
Use the VC/MBB-style quality bar: template selection, hypothesis-led workstreams,
source hierarchy, banned-source compliance, TAM triangulation, public comparables
where relevant, explicit gaps, and meaningful user inputs.
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
        "template_selected": "Sector study / market-entry screen",
        "interpreted_decision_context": (
            "Understand whether the market is attractive, where growth is concentrated, "
            "which segments matter, and what evidence is needed to support an entry or investment view."
        ),
        "research_objective": (
            "Build a public-source-backed view of market size, growth, segments, competitive landscape, "
            "regulation, customer demand, economics, risks, and open questions."
        ),
        "scope_boundaries": {
            "in_scope": [
                "Publicly available market, regulatory, company, customer, financial, and technology signals",
                "Evidence that can be collected through desk research",
                "Public proxies where direct segment-level data is unavailable",
            ],
            "out_of_scope": [
                "Private client data",
                "Paid expert calls",
                "Non-public company documents",
                "Banned low-confidence aggregator sources",
            ],
        },
        "initial_hypotheses": [
            "The market likely contains multiple segments with different buyer needs, growth rates, and regulatory constraints.",
            "Public data will likely require triangulation because no single source will be complete.",
            "The best initial opportunity may sit in a narrower use case rather than the broad market label.",
        ],
        "research_plan": [
            {
                "workstream": "Market definition and segmentation",
                "things_to_be_answered": "What exactly is included in the market, and which buyer/use-case segments should be analyzed separately?",
                "public_sources_to_use": "Government policy documents, regulator websites, industry association publications, public company descriptions, product pages, credible news explainers.",
                "how_to_use_sources": "Create a market map, define segment boundaries, state inclusion/exclusion rules, and distinguish hardware, software, services, and data layers where relevant.",
                "expected_output": "Market definition, segment taxonomy, and scope note.",
                "user_comments_or_inputs_needed": "Confirm geography, time horizon, and whether the plan is for entry, investment, partnership, or strategy refresh.",
                "priority": "High",
            },
            {
                "workstream": "Market size, growth, and TAM triangulation",
                "things_to_be_answered": "How large is the market today, how fast is it growing, and what credible sizing range can be defended?",
                "public_sources_to_use": "Government datasets, public tenders, listed company filings, trade body reports, credible media, academic papers, public pricing pages.",
                "how_to_use_sources": "Triangulate at least two top-down public estimates with a bottom-up build from buyer counts, adoption rates, pricing, and usage intensity; document assumptions and confidence levels.",
                "expected_output": "Sizing range, segment-level growth view, assumptions table, and confidence assessment.",
                "user_comments_or_inputs_needed": "Provide preferred market definition, currency, forecast horizon, and minimum market-size threshold.",
                "priority": "High",
            },
            {
                "workstream": "Demand, buyer needs, and use-case prioritization",
                "things_to_be_answered": "Which buyers have urgent problems, budget, and adoption readiness? Which use cases are pull-driven versus technology-push?",
                "public_sources_to_use": "Procurement portals, RFPs, case studies, public customer logos, review sites, app stores, public interviews, trade press, job postings.",
                "how_to_use_sources": "Map buyer types to pain points, budget signals, procurement language, adoption proof points, and substitute solutions.",
                "expected_output": "Buyer/use-case prioritization matrix with demand signals and evidence quality.",
                "user_comments_or_inputs_needed": "Confirm target customer types, willingness to sell to government buyers, and any excluded verticals.",
                "priority": "High",
            },
            {
                "workstream": "Competitive and ecosystem landscape",
                "things_to_be_answered": "Who are the direct competitors, indirect substitutes, channels, and ecosystem partners, and where do they compete?",
                "public_sources_to_use": "Company websites, public case studies, app stores, job postings, patents, press releases, procurement wins, investor materials, reputable press.",
                "how_to_use_sources": "Build a competitor long list, tag by segment, compare capabilities, capture recent moves, and separate disclosed facts from inferred capabilities.",
                "expected_output": "Competitor map, direct/indirect substitute table, and capability matrix.",
                "user_comments_or_inputs_needed": "Confirm whether specific competitor archetypes, business models, or price points should be emphasized or excluded.",
                "priority": "High",
            },
            {
                "workstream": "Business model, unit economics, and public comparables",
                "things_to_be_answered": "What business models exist, what economic drivers matter, and which public comps can be used as proxies?",
                "public_sources_to_use": "Public company filings, earnings transcripts, investor presentations, pricing pages, customer contracts where public, analyst-day materials, IPO filings.",
                "how_to_use_sources": "Identify 3-4 public comps or proxy comps; collect growth, margin, revenue mix, pricing model, retention, and valuation metrics where available.",
                "expected_output": "Business-model map and public-comps metrics table.",
                "user_comments_or_inputs_needed": "Clarify whether the output is for venture investment, acquisition, market entry, or operating strategy.",
                "priority": "Medium",
            },
            {
                "workstream": "Regulation, adoption barriers, and risks",
                "things_to_be_answered": "Which regulations, certifications, procurement constraints, data/privacy rules, or operational barriers could accelerate or block adoption?",
                "public_sources_to_use": "Regulator websites, official policy documents, standards bodies, court/regulator actions, procurement rules, trade associations, credible legal explainers.",
                "how_to_use_sources": "Separate binding rules from draft policy, identify near-term regulatory changes, and map each barrier to affected segments.",
                "expected_output": "Regulatory and risk register with segment impact and mitigation notes.",
                "user_comments_or_inputs_needed": "Confirm risk tolerance and whether regulated or government-heavy segments are in scope.",
                "priority": "Medium",
            },
        ],
        "cross_checks": [
            "Check every market-size estimate against at least two independent public sources and one bottom-up proxy.",
            "Separate observed facts, estimated figures, proxy signals, and unavailable data.",
            "Verify that no banned source is used or cited.",
            "Make sure direct competitors, indirect substitutes, and recent competitive moves are covered.",
        ],
        "likely_gaps": [
            "Segment-level revenue may be unavailable in public sources.",
            "Private-company metrics such as retention, margins, CAC, or contract value may require public proxies.",
            "Demand-side data may require proxies such as procurement volume, hiring, customer case studies, or public adoption signals.",
        ],
        "suggested_user_inputs": [
            "Decision objective",
            "Target geography and time horizon",
            "Known hypotheses to test",
            "Target buyer or segment preferences",
            "Minimum attractiveness thresholds",
        ],
        "quality_checks": [
            "Specificity: every row has concrete questions, source categories, and output artifacts.",
            "Source quality: primary public sources are prioritized over secondary summaries.",
            "Bottom-up rigor: market sizing includes triangulation and public proxies.",
            "Comparables coverage: financial work includes public comps where relevant.",
            "Banned-source compliance: no Grand View Research, IMARC, or Future Market Insights.",
        ],
        "source_policy": PUBLIC_SOURCE_POLICY,
    }


def plan_to_markdown(plan: Dict[str, Any]) -> str:
    """Render a generated plan as a concise Markdown document with the core table."""

    lines: List[str] = []
    lines.append(f"# Research Action Plan: {plan.get('problem_statement', '').strip()}")
    lines.append("")

    template = plan.get("template_selected")
    if template:
        lines.append(f"**Template selected:** {template.strip()}")
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
    _append_list_section(lines, "Quality Checks", plan.get("quality_checks") or [])

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
