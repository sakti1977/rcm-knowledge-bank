import argparse
import json
from pathlib import Path


def pricing_decision(case):
    if case["rate"] is None:
        return {"verdict": "review", "evidence": ["missing_rate"]}
    if len(set(case["payments"])) != 1:
        return {"verdict": "review", "evidence": ["conflicting_payment"]}
    expected = case["rate"] - case["patient_share"] - case["exception"]
    paid = case["payments"][0]
    verdict = "shortfall" if paid < expected else "matched" if paid == expected else "review"
    evidence = ["rate", "paid"]
    evidence.extend(field for field in ("patient_share", "exception") if case[field])
    return {"verdict": verdict, "evidence": evidence, "expected_cents": expected}


def load_cases():
    return json.loads((Path(__file__).parent / "data" / "cases.json").read_text(encoding="utf-8"))


def score(cases, predictions):
    totals = {"cases": len(cases), "correct": 0, "supported_correct": 0, "missed_review": 0}
    for case in cases:
        predicted = predictions.get(case["id"], {})
        gold = case["gold"]
        correct = predicted.get("verdict") == gold["verdict"]
        cited = set(predicted.get("evidence", []))
        totals["correct"] += correct
        totals["supported_correct"] += (
            correct and set(gold["evidence"]) <= cited <= set(case["available_evidence"])
        )
        totals["missed_review"] += gold["verdict"] == "review" and not correct
    return totals


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--score", type=Path)
    args = parser.parse_args()
    cases = load_cases()
    if args.score:
        predictions = json.loads(args.score.read_text(encoding="utf-8"))
        print(json.dumps(score(cases, predictions), indent=2))
        return
    threshold = {case["id"]: {
        "verdict": "shortfall" if case["payments"][0] < case["worklist_rate"] else "matched"
    } for case in cases}
    deterministic = {case["id"]: pricing_decision(case) for case in cases}
    print("Threshold-only baseline:", score(cases, threshold))
    print("Deterministic baseline:", score(cases, deterministic))
    print(f"First-pass payer acceptance: {88 / 90:.1%}")
    print(f"Straight-through acceptance: {88 / 100:.1%}")


if __name__ == "__main__":
    main()

