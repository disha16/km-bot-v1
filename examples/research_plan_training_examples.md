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

## Example 1

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
