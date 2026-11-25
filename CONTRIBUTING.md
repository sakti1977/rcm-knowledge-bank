# Editorial and source control

Use a pull request for policy and metric changes. A reviewer should be able to reproduce every example and locate every consequential claim in its source.

## Page template

1. Reader question and scope. Name the country, scheme, payer and setting as appropriate.
2. Definition and workflow. Identify inputs, decision owner, outputs and common failures.
3. Evidence. Identify issuing body, title, section, URL, effective period and verification date. Label it formal guidance, audit observation, reported response or practice to test.
4. Synthetic example. Include assumptions, working, expected result, failure mode and patient impact.
5. Review status. Use Draft, Source-verified or Practitioner-reviewed with reviewer scope and date. Keep historical audit findings and policy editions identified by period.

## Source register and review triggers

| Authority | Scope and evidence type | Review trigger |
| --- | --- | --- |
| [CMS NCCI](https://www.cms.gov/medicare/coding-billing/national-correct-coding-initiative-ncci-edits/medicare-ncci-faq-library) | U.S. Medicare coding rules and explanatory guidance | New edit-file release, correction or annual manual |
| [CAG](https://cag.gov.in/en/audit-report) and [NHA](https://nha.gov.in/) | Indian audit observations and AB PM-JAY program guidance | New audit, state circular or scheme/package revision |
| [NHS England Payment Scheme](https://www.england.nhs.uk/long-read/2026-27-nhs-payment-scheme/) | English NHS 2026/27 formal payment scheme | Revised scheme, annex or clarification |
| [IHACPA](https://www.ihacpa.gov.au/health-care/pricing/national-efficient-price-determination) | Australian public hospital determination | Annual price, cost or classification release |
| [NIST AI RMF GenAI profile](https://www.nist.gov/publications/artificial-intelligence-risk-management-framework-generative-artificial-intelligence) | Voluntary AI risk and evaluation guidance | New edition or evaluation policy change |

Initial source research was reviewed on 2026-11-25. Independent practitioner review is pending. Use original synthetic records in this repository. Link to licensed standards and code sets instead of redistributing restricted material.

## Change note example

**Synthetic rate amendment.** At the start of the new effective period the eligible case rate drops from $9,200 to $8,400. Keep prior-period pricing reproducible. Regression checks cover the day before the boundary, the day of the boundary, and review when the controlling version is missing. Change notes should state the original rule, updated rule, effective date, impacted settings and who verified the change.

