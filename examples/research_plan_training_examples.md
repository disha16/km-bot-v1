# Research Planner Training Examples

Use this file to capture gold-standard examples that teach the planner how to think like the lead consultant.

## How To Use This File

For each real problem statement, save three things: the original problem, the first generated output, and the corrected version. The corrected version is the training asset because it captures the consultant's judgment, decomposition style, source discipline, and preferred level of specificity.

| Field | What To Capture |
| --- | --- |
| Problem statement | The exact user prompt. |
| Context | Audience, decision objective, geography, time horizon, and known hypotheses. |
| Model output | The unedited output. |
| Consultant correction | The rewritten version in the preferred style. |
| Feedback tags | Examples: too generic, missing buyer segmentation, weak public sources, unclear output artifact, not MECE, wrong scope. |
| Rubric scores | Specificity, source quality, bottom-up rigor, comparables coverage, recency, gap identification, banned-source compliance. |

## Standing Style Rules From The VC Research Training Document

These rules should be reflected in every corrected example.

| Rule | What It Means In A Corrected Example |
| --- | --- |
| Public-source-only | Use public filings, regulator data, government datasets, procurement portals, company pages, public pricing, investor materials, reputable press, academic papers, patents, job postings, reviews, and public digital exhaust. |
| Banned-source compliance | Do not use Grand View Research, IMARC, or Future Market Insights. |
| Template selection | State whether the work is a sector study, market-entry screen, investment thesis, company diligence, competitive landscape, pricing/economics study, or quick screen. |
| TAM triangulation | Require at least two triangulation paths and one bottom-up method. |
| Competitor rigor | Separate direct competitors, indirect substitutes, channels, partners, and recent moves. |
| Financial discipline | When relevant, identify 3-4 public comps or proxy comps and the metrics to collect. |
| Moat discipline | Ask what mechanism creates durability and what evidence proves it. |
| Gap discipline | Identify what public data will not answer and propose proxies. |

## Gold-Standard Example Template

### Problem Statement

`[Paste exact user problem statement]`

### Context

`[Audience, geography, decision objective, time horizon, known hypotheses, excluded segments, and output expectation.]`

### Expected Planner Behavior

The plan should first identify the decision context and select a template. It should then break the problem into workstreams that are specific to the market and decision, not generic business-school categories. It should require public-source triangulation, name public-source categories, identify likely evidence gaps, and ask for user inputs that would sharpen the scope.

### Consultant Correction

| Workstream | Things To Be Answered | Public Sources To Use | How To Use Sources | Expected Output | User Comments / Inputs Needed | Priority |
| --- | --- | --- | --- | --- | --- | --- |
| `[Workstream]` | `[Specific questions]` | `[Concrete public source categories and examples]` | `[Triangulation, proxy, or analysis method]` | `[Artifact]` | `[Scope or decision input needed]` | High/Medium/Low |

### Feedback Tags

`[too generic / missing segmentation / weak source hierarchy / no bottom-up sizing / missing public comps / weak gaps / banned-source risk / unclear decision context]`

## Example 1: Autonomous Drone Market In India

### Problem Statement

Research the autonomous drone market in India.

### Context

Audience is a founder evaluating whether to build a B2B autonomous drone solution for Indian enterprise and government customers over the next 24 months. Public information only.

### Expected Planner Behavior

The plan should break the problem into market definition, demand/use cases, regulation, market size, competition, buyer economics, adoption barriers, and white-space hypotheses. It should avoid private databases and expert calls. It should suggest public proxies such as DGCA sources, Ministry publications, procurement portals, company websites, public tenders, job postings, patents, academic papers, news, startup funding announcements, and public case studies.

### Consultant Review Notes

- Strong output should make clear whether the market includes hardware, software, services, data analytics, autonomy stack, or drone-enabled services.
- Strong output should separate defense, agriculture, inspection, logistics, mapping, and surveillance use cases.
- Strong output should not treat the drone market as one homogeneous market.
- Strong output should say where public data will be weak and what proxies can fill the gap.
- Strong output should ask whether the user wants a venture-backable software opportunity, a services business, or a broader sector map.

## Ten US Industry Prompts For Training Examples

Use these prompts to generate first-pass outputs, then rewrite them into gold-standard examples using the rubric above.

| # | Industry | Example Problem Statement | What The Corrected Example Should Stress |
| --- | --- | --- | --- |
| 1 | US home healthcare | Research the US home healthcare market and identify attractive segments for a new tech-enabled services platform. | Separate skilled home health, personal care, hospice, remote monitoring, payer dynamics, labor constraints, and reimbursement. |
| 2 | US construction software | Research the US construction software market and identify where a vertical SaaS entrant could win. | Segment by trade, workflow, customer size, buyer, integration needs, and substitution from spreadsheets or ERPs. |
| 3 | US specialty pet care | Research the US specialty pet care market, including diagnostics, insurance, wellness, and premium services. | Separate vet clinics, diagnostics, insurance, specialty services, consumer willingness-to-pay, and channel conflict. |
| 4 | US cold chain logistics | Research the US cold chain logistics market and identify growth areas across food, pharma, and e-commerce. | Segment by temperature band, end market, asset type, regulation, customer concentration, and utilization economics. |
| 5 | US industrial automation | Research the US industrial automation market and identify high-growth use cases for AI-enabled workflow automation. | Separate hardware automation, software, integrators, plant workflows, ROI triggers, and adoption barriers. |
| 6 | US outpatient mental health | Research the US outpatient mental health market and identify where digital-first or hybrid models are gaining traction. | Separate payer, provider type, acuity, modality, reimbursement, clinician supply, and regulatory considerations. |
| 7 | US EV charging infrastructure | Research the US EV charging infrastructure market and assess opportunities in fleet, workplace, multifamily, and highway charging. | Segment site types, utilization, incentives, interconnection, hardware/software/services, and ownership models. |
| 8 | US cybersecurity for SMBs | Research the US SMB cybersecurity market and identify unmet needs, buyer segments, and go-to-market opportunities. | Separate buyer maturity, channel, managed service providers, compliance triggers, product bundles, and willingness-to-pay. |
| 9 | US foodservice equipment | Research the US foodservice equipment market and identify growth opportunities driven by automation, labor shortages, and energy efficiency. | Segment by venue, equipment category, replacement cycle, energy regulation, labor ROI, and distributor/OEM channel. |
| 10 | US senior living technology | Research the US senior living technology market and identify opportunities across care coordination, staffing, safety, and family engagement. | Separate facility types, buyer roles, reimbursement/payment source, staffing pain points, integration constraints, and adoption proof. |
