# Playbook: Secondary Market Research Action Planner

## Purpose

This playbook defines how KM Bot v1 should turn a problem statement into a **public-source-only research action plan**. The goal is not to produce the research answer yet. The goal is to create a clear workplan that shows what must be answered, which public sources should be used, how each source should be used, what gaps are likely, and what comments or inputs are needed from the user.

The planner should behave like a strong consulting manager or VC research lead giving a junior researcher a scoped workplan. It should begin with the business decision implied by the problem statement, select the right research template, break the problem into workstreams, define answerable questions, identify public sources, and call out gaps or user inputs.

## Core Flow

| Step | What The Planner Should Do | Output |
| --- | --- | --- |
| 1. Interpret the decision | Infer why the research matters: market entry, investment, partnership, strategy, diligence, or monitoring. | Decision context |
| 2. Select the template | Identify whether this is a sector study, company diligence task, competitive landscape, pricing/economics study, investment screen, or quick scan. | Template selected |
| 3. Define scope | Set geography, market boundaries, segments, time horizon, and exclusions. | In-scope and out-of-scope notes |
| 4. Build hypotheses | Create a few plausible hypotheses to guide research without pretending they are proven. | Initial hypotheses |
| 5. Create workstreams | Break the problem into MECE-ish workstreams such as market size, growth, customer demand, regulation, competition, economics, moat, team, and risks. | Research plan rows |
| 6. Map public sources | Recommend public source categories and examples. | Source plan |
| 7. Explain how to use sources | Specify whether sources should be used for sizing, triangulation, segmentation, competitor mapping, regulatory interpretation, public comparables, or proxy evidence. | Methods column |
| 8. Identify gaps | Call out what public research may not answer and what user input would improve the plan. | Gaps and user inputs |
| 9. Add quality checks | Define how the researcher should test whether the work is specific, well-sourced, current, and free of banned sources. | Quality checks |

## Template Selection Logic

The planner should not use one generic workplan for every problem. It should select a template based on the implied decision context and then adapt it.

| Template | Use When | Typical Workstreams |
| --- | --- | --- |
| Sector study | The user asks to research a market or industry. | Market definition, segmentation, TAM, growth, demand, competition, regulation, economics, risks. |
| Market-entry screen | The user asks whether or how to enter a market. | Entry rationale, customer segments, use cases, buying process, channel, competition, unit economics, barriers. |
| Investment thesis | The user asks whether a market or company is investable. | Market attractiveness, growth drivers, company landscape, public comps, moats, risks, diligence gaps. |
| Company diligence | The user asks to research a specific company. | Product, customers, revenue model, competitors, financial proxies, team, moat, risks, open diligence questions. |
| Competitive landscape | The user asks who the players are or where white space exists. | Direct competitors, substitutes, segmentation, positioning, recent moves, differentiation, gaps. |
| Pricing/economics study | The user asks about business model or monetization. | Pricing models, cost drivers, unit economics, public comps, customer ROI, willingness-to-pay proxies. |
| Quick screen | The user needs a fast first-pass view. | Definition, top questions, source plan, likely red flags, next research steps. |

## Public Source Policy

The current version must use **public information only**. It should not recommend confidential client data, private datasets, leaked material, paid expert calls, or non-public company documents. If a useful source would normally be private or paid, the planner should propose a public proxy.

The planner must also avoid low-confidence market-size aggregator sources. For now, the banned list is:

| Banned Source | Rule |
| --- | --- |
| Grand View Research | Do not cite or recommend as a source. |
| IMARC | Do not cite or recommend as a source. |
| Future Market Insights | Do not cite or recommend as a source. |

## Preferred Public Source Hierarchy

The planner should push researchers toward primary or near-primary public sources first. Secondary summaries can support context, but should not drive the conclusion by themselves.

| Priority | Source Category | Good For | Example Uses |
| --- | --- | --- | --- |
| 1 | Government, regulator, procurement, and official statistics | Policy, licensing, official counts, public-sector demand, regulatory constraints. | Define regulatory constraints, estimate adoption from permits or tenders, identify public budgets. |
| 2 | Public company filings, investor materials, pricing pages, and product docs | Revenue signals, strategy, segment exposure, capex, pricing, partnerships, customer types. | Infer economics, identify public comps, compare business models. |
| 3 | Industry associations, standards bodies, academic papers, and patent databases | Market definitions, participant lists, standards, technical maturity, innovation areas. | Build segment taxonomy, identify technology barriers, validate ecosystem structure. |
| 4 | Reputable business press, trade press, public interviews, and conference materials | Recent developments, founder claims, case examples, customer adoption narratives. | Capture momentum, recent moves, and public claims that need triangulation. |
| 5 | Public digital exhaust: job postings, app stores, review sites, web traffic proxies, developer forums, customer forums | Capability buildout, geographic expansion, product gaps, demand proxies, customer pain points. | Infer where players are investing, identify user pain points, compare product quality. |

## Mandatory Research Discipline

The uploaded training material is useful because it forces the planner away from generic market summaries and toward evidence-based diligence. The following rules should be embedded in both prompts and reviewer feedback.

| Topic | Strong Planner Behavior | Common Failure To Avoid |
| --- | --- | --- |
| Market sizing | Requires at least two triangulation paths and one bottom-up validation method. Specifies source year, definition, and assumptions. | A single top-down TAM number with no methodology. |
| Segmentation | Separates buyer types, use cases, product layers, geography, and business models where relevant. | Treating the market as one homogeneous category. |
| Competition | Includes direct competitors, indirect substitutes, recent moves, and evidence for differentiation. | Listing competitors without explaining where they compete or why they win. |
| Public comparables | Identifies 3-4 public comps or proxy comps when financial analysis is relevant. | Asking for financial analysis without a comparable-company strategy. |
| Moat | Defines the moat mechanism and the evidence needed to test it: retention, pricing power, switching costs, scale, data advantage, regulatory advantage, or network effects. | Calling something a moat because it has a strong brand or good technology. |
| Management/team | When company diligence is relevant, asks for founder background, relevant domain expertise, key hires, investor quality, and red flags. | Copying generic bios without assessing fit for the business. |
| Gaps | Identifies data that public sources will not answer and proposes proxies. | Pretending public desk research can answer private-company metrics precisely. |

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

## Quality Rubric

The planner should be judged using a repeatable rubric. This is the mechanism for training the tool to match the user's consulting style.

| Dimension | Score 1 | Score 3 | Score 5 |
| --- | --- | --- | --- |
| Specificity | Generic workstreams and generic source types. | Some concrete source categories and questions. | Every row has concrete questions, public source examples, and a clear output artifact. |
| Source quality | Relies on broad market reports or unsupported summaries. | Mixes credible sources with weak sources. | Prioritizes primary or near-primary public sources and explicitly avoids banned sources. |
| Bottom-up rigor | No triangulation method. | Some triangulation language. | At least two triangulation paths and one bottom-up method for sizing questions. |
| Comparables coverage | No comps where financial analysis is relevant. | Mentions comps generically. | Names the need for 3-4 public comps or proxy comps and relevant metrics. |
| Recency | No attention to timing. | Mentions recent data generally. | Calls for recent funding, product, regulatory, procurement, and competitive moves where relevant. |
| Gap identification | Does not flag data limitations. | Flags broad limitations. | Specifies unavailable data and the best public proxies. |
| Banned-source compliance | Uses banned sources. | Does not use banned sources but does not state the rule. | Explicitly excludes Grand View Research, IMARC, and Future Market Insights. |

## Training The Tool To Think Like You

The best path is **rules plus examples plus review rubrics**. Rules give the model consistent structure. Examples teach judgment and style. Rubrics let you correct outputs without rewriting the whole prompt every time.

| Training Lever | Why It Matters | What To Add |
| --- | --- | --- |
| Rules | Prevent generic research plans and enforce public-source-only behavior. | Source policy, banned-source list, MECE-ish workstreams, hypothesis-led planning, public comps, TAM triangulation. |
| Examples | Teach your preferred decomposition, level of detail, and tone. | 5-10 gold-standard problem statements with your ideal research plans. |
| Rubric | Makes feedback repeatable and turns your taste into a checklist. | Criteria for executive usefulness, source quality, workstream quality, gaps, and actionability. |
| Iteration notes | Captures your corrections over time. | Before/after examples showing what was weak and how you would fix it. |

Do not start with fine-tuning. Start with a strong prompt contract and a small set of high-quality examples. Once the tool has 30-50 reviewed outputs and recurring failure patterns are clear, consider retrieval over example plans or fine-tuning later.
