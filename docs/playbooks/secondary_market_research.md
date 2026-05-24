# Playbook: Secondary Market Research Action Planner

## Purpose

This playbook defines how KM Bot v1 should turn a problem statement into a public-source-only research action plan. The goal is not to produce the research answer yet. The goal is to create a clear workplan that shows what must be answered, which public sources should be used, how each source should be used, and what comments or inputs are needed from the user.

## Core Flow

The planner should behave like a strong consulting manager giving a junior researcher a scoped workplan. It should begin with the business decision implied by the problem statement, break the problem into workstreams, define answerable questions, identify public sources, and call out gaps or user inputs.

| Step | What The Planner Should Do | Output |
| --- | --- | --- |
| 1. Interpret the decision | Infer why the research matters: market entry, investment, partnership, strategy, diligence, or monitoring. | Decision context |
| 2. Define scope | Set geography, market boundaries, segments, time horizon, and exclusions. | In-scope and out-of-scope notes |
| 3. Build hypotheses | Create a few plausible hypotheses to guide research without pretending they are proven. | Initial hypotheses |
| 4. Create workstreams | Break the problem into MECE-ish workstreams such as market size, growth, customer demand, regulation, competition, economics, and risks. | Research plan rows |
| 5. Map public sources | Recommend public source categories and examples. | Source plan |
| 6. Explain how to use sources | Specify whether sources should be used for sizing, triangulation, segmentation, competitor mapping, regulatory interpretation, or proxy evidence. | Methods column |
| 7. Identify gaps | Call out what public research may not answer and what user input would improve the plan. | Gaps and user inputs |

## Public Source Policy

The current version must use **public information only**. It should not recommend confidential client data, private datasets, leaked material, paid expert calls, or non-public company documents. If a useful source would normally be private or paid, the planner should propose a public proxy.

| Source Category | Good For | Example Uses |
| --- | --- | --- |
| Government and regulator sites | Policy, licensing, market rules, procurement, official statistics. | Define regulatory constraints, estimate adoption from permits or tenders. |
| Public company filings and investor materials | Revenue signals, strategy, segment exposure, capex, partnerships. | Infer market participation and economics. |
| Industry associations and trade bodies | Market definitions, participant lists, standards, adoption themes. | Build segment taxonomy and ecosystem map. |
| Procurement portals and tenders | Demand signals, buyer types, budget ranges, use cases. | Estimate public-sector demand and use-case mix. |
| Company websites and press releases | Product positioning, customer logos, partnerships, launches. | Build competitor and capability map. |
| Job postings and hiring pages | Capability buildout, geographic expansion, technology priorities. | Infer where players are investing. |
| Patent and academic databases | Technology maturity and innovation areas. | Identify technical barriers and emerging use cases. |
| News, interviews, and conference materials | Recent developments, founder claims, case examples. | Capture momentum and validate timeline. |
| App stores, marketplaces, and review sites | Customer feedback and adoption proxies where relevant. | Identify user pain points and product differentiation. |

## Output Contract

The main output should be a simple Markdown table with these columns.

| Column | Definition |
| --- | --- |
| Workstream | The part of the problem being investigated. |
| Things To Be Answered | The specific questions the researcher must answer. |
| Public Sources To Use | Public source categories or examples. |
| How To Use Sources | The research method, triangulation approach, or analysis technique. |
| Expected Output | What artifact the researcher should produce. |
| User Comments / Inputs Needed | What the user should clarify or provide. |
| Priority | High, Medium, or Low. |

## Training The Tool To Think Like You

The best path is **rules plus examples plus review rubrics**. Rules give the model consistent structure. Examples teach judgment and style. Rubrics let you correct outputs without rewriting the whole prompt every time.

| Training Lever | Why It Matters | What To Add |
| --- | --- | --- |
| Rules | Prevent generic research plans and enforce public-source-only behavior. | Source policy, MECE-ish workstreams, hypothesis-led planning, citation discipline. |
| Examples | Teach your preferred decomposition, level of detail, and tone. | 5-10 gold-standard problem statements with your ideal research plans. |
| Rubric | Makes feedback repeatable and turns your taste into a checklist. | Criteria for executive usefulness, source quality, workstream quality, gaps, and actionability. |
| Iteration notes | Captures your corrections over time. | Before/after examples showing what was weak and how you would fix it. |

Do not start with fine-tuning. Start with a strong prompt contract and a small set of high-quality examples. Once the tool has 30-50 reviewed outputs and recurring failure patterns are clear, consider retrieval over example plans or fine-tuning later.
