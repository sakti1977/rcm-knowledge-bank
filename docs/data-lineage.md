# Data lineage from encounter to cash

Keep event time, receipt time, processing time, source version, and audit history. Preserve links to the original objects so an investigator can reconstruct each decision.

| Handoff | Authoritative evidence to retain | Matching strategy | Exception |
| --- | --- | --- | --- |
| EHR → billing | Encounter and charge events, source revisions | Hospital and encounter ID, charge and service-line IDs | Quarantine conflicting versions and reconcile corrections. |
| Billing → clearinghouse | Approved claim revision, exact transmission and manifest | Submission intent, delivery ID, interchange/group/transaction identifiers | Check partner status when delivery is unknown. |
| Clearinghouse or payer → billing | Original acknowledgment and sender | Transaction controls for 999 and partner-specific claim references for 277CA | Keep conflicting or ambiguous replies in a review queue. |
| Payer → payment posting | Remittance, claim references, adjustments and reversals | Payer/provider scope, patient control and payer claim IDs, service-line references where available | Multiple remittances or conflicting identifiers need reconciliation. |
| Payer → bank | Deposit and trace information | Trace, payer and account scope, amount and settlement window | Investigate combined or missing deposits and trace mismatches. |
| Posting → finance | Posting batch and general ledger entries | Posting ID, account, amount and adjustment trail | Balance the batch and account for unapplied cash and offsets. |

Keep transport, adjudication, cash settlement, and posting as separate events. For an 835 and deposit, reconcile the whole payment and explain any provider-level adjustments before assuming a mismatch.

**Design exercise.** An 835 arrives before the 277CA. Store the remittance and match it using available claim references. Retain the missing acknowledgment as an independent exception. Never create fabricated receipt or acknowledgment events to complete a timeline.

Reference: [CMS Claims Processing Manual, Chapter 24](https://www.cms.gov/regulations-and-guidance/guidance/manuals/downloads/clm104c24.pdf). Use the applicable companion guide for exact mappings.

