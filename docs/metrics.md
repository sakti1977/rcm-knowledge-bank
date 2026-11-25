# Metrics dictionary

Definitions below are proposed operational measures for the lab. Document differences before comparing organizations or programs.

| KPI | Numerator / denominator or clock | Exclusions and interpretation |
| --- | --- | --- |
| First-pass payer acceptance | Original claims accepted by payer on first transmission within the window / original claims transmitted on routes supplying payer acknowledgments | Use a mature sent cohort. Missing and rejected acknowledgments count as failures after the cutoff. Report route coverage. |
| Straight-through payer acceptance | Complete received claims accepted without manual rework within the window / all complete received claims in scope | The lab uses acknowledgment-covered routes and counts held claims in the denominator. Report incomplete intake separately. |
| Scrub hold rate | First scrub decisions placing claims on hold / all first scrub decisions | Keep one initial result per original claim and measure hold age alongside the rate. |
| Initial denial rate | Initially denied claims / first adjudicated claims in a mature cohort | Specify claim versus line and define partial denials separately. |
| Confirmed underpayment rate | Claims with a verified payer shortfall / claims reconciled against an applicable contract | Publish contract coverage and keep unresolved evidence out of the verified numerator. |
| Net days in A/R | Net patient receivables / average daily net patient service revenue over a declared period | Disclose the accounting conventions, period and exclusions. |
| Settlement turnaround | Elapsed time from a named starting event to disbursement | Segment by scheme and show pending cases separately to expose unresolved aging. |

## Reproducible example

Of 100 complete claims on covered routes, 10 have been held. Of the 90 transmitted, 88 were accepted on the first pass and two failed that measure. First-pass acceptance is **88/90 = 97.8%**. Straight-through acceptance is **88/100 = 88.0%**. Report both with the number of holds and the observation window.

Run `python lab.py` to reproduce the calculations.

