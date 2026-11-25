# Casebook

## Case 1 — The payer paid $8,400. Are we owed $800?

[Try the interactive investigation](investigate-the-800.html) before reading the worked answers. Download the HTML file and open it in a browser.

Start with the synthetic claim and remittance. The pricing worklist predicts $9,200 and the payer paid $8,400. Before contacting the payer, retrieve the effective contract terms, accepted claim facts, remittance adjustments, and payment history. Reconcile the payer-paid amount to the same revision and account for reversals or later transactions.

| Variant | Evidence found | Calculation | Next action |
| --- | --- | --- | --- |
| Genuine shortfall | Rate $9,200, no other applicable adjustments, paid $8,400 | $9,200 − $8,400 = $800 | Verify the evidence packet and filing window, then route to contract recovery. |
| Stale rate | Effective amendment sets rate at $8,400 | $8,400 − $8,400 = $0 | Correct the date-effective contract model and reprice affected accounts. |
| Patient share | Rate $9,200, documented patient responsibility $800 | $9,200 − $800 − $8,400 = $0 | Reconcile the allocation. Verify applicable billing rules before contacting the patient. |
| Contract exception | Documented exception reduces payer liability by $800 | $9,200 − $800 − $8,400 = $0 | Confirm that the model applies the exception to this kind of encounter. |
| Missing amendment | Rate cannot be verified | Expected amount unknown | Obtain the controlling version before treating it as recoverable. |
| Conflicting remittance | Two incompatible payment observations | Actual amount unresolved | Reconcile transaction sequence, reversals and posting before any recovery action. |

The [lab fixtures](../data/cases.json) model each variant in integer cents. The calculation is specific to the synthetic contract, which defines the expected payer amount as the allowed rate minus documented patient responsibility and a contract exception. Real contract pricing can include multiple lines, ordering rules, coordination of benefits, outliers or stop-loss provisions.

**Operational handoff.** Attach the controlling clause, version, calculation, remittance reference, and unresolved questions. Send only verified differences to recovery. **Prevention.** Version rates by effective date and add a regression case for each exception.

## Case 2 — A clearinghouse receipt is missing

Keep the original delivery ID and exact bytes. Check the partner’s receipt lookup and forwarding history. If the partner has the file, reconcile the existing delivery. If the evidence is ambiguous, track the filing deadline and open a work item. Walk through this scenario in the [animated claims workflow](https://github.com/sakti1977/claims-platform/blob/main/docs/claims-workflow.html).

## Case 3 — Remittance arrived, but cash is missing

A synthetic 835 reports $10,000 in payments and a $300 provider-level offset, implying an expected net deposit of $9,700. The posting batch shows $10,000 at the claim level. Reconcile the expected transfer to the bank and post the $300 offset using approved accounting handling. If the bank has no matching deposit, keep cash status unresolved. See the [data lineage guide](data-lineage.md).

