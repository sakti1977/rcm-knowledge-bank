# AI benchmark for underpayment triage

Decide whether the case is a shortfall, matched payment, or requires review. A deterministic pricing component calculates expected payment from approved contract terms. An AI assistant can explain the decision and cite immutable evidence IDs. A reviewer controls recovery, coding, contract activation and patient billing.

## Run a comparable evaluation

1. Run `python lab.py` to record the threshold-only and deterministic baselines.
2. Give an assistant the input fields and the evidence IDs one case at a time. Remove `gold` from the input. Ask it for a verdict, evidence IDs, and a brief rationale. Do not give it the answers, tools that mutate claims, or access to real records.
3. Save a JSON object keyed by fixture ID. Each value has `verdict` and an `evidence` array, such as `{"u01":{"verdict":"shortfall","evidence":["rate","paid"]}}`.
4. Run `python lab.py --score predictions.json`. Report verdict accuracy, supported correct decisions, and missed review cases. The scorer requires the complete expected evidence set and rejects unknown evidence IDs for a supported result. Missing predictions count as incorrect.
5. Manually review the reasoning for invented facts and misleading explanations. Report review time and false recovery referrals alongside the automated score. A small synthetic dataset is suitable for learning, with broader blinded data needed before operational conclusions.

The first challenge set covers a genuine shortfall, a stale rate, patient share, a contract exception, missing terms and conflicting remittance. Additional use cases can compare document extraction, grounded appeal drafting and worklist prioritization against simpler baselines. Keep confidence and escalation decisions visible.

Reference for evaluation governance: [NIST Generative AI Risk Management Profile](https://www.nist.gov/publications/artificial-intelligence-risk-management-framework-generative-artificial-intelligence).

