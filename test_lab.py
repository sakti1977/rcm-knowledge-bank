import unittest

from lab import load_cases, pricing_decision, score


class LabTest(unittest.TestCase):
    def test_fixture_decisions_and_evidence(self):
        cases = load_cases()
        predictions = {case["id"]: pricing_decision(case) for case in cases}
        self.assertEqual({"cases": 6, "correct": 6, "supported_correct": 6, "missed_review": 0},
                         score(cases, predictions))

    def test_unknown_evidence_and_missing_predictions(self):
        cases = load_cases()
        verdict = {"u01": {"verdict": "shortfall", "evidence": ["rate", "paid", "invented"]}}
        self.assertEqual({"cases": 6, "correct": 1, "supported_correct": 0, "missed_review": 2},
                         score(cases, verdict))

    def test_price_and_patient_share(self):
        cases = {case["id"]: case for case in load_cases()}
        self.assertEqual(920000, pricing_decision(cases["u01"])["expected_cents"])
        self.assertEqual(840000, pricing_decision(cases["u03"])["expected_cents"])

