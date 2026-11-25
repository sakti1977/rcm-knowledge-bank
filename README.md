# Healthcare Revenue Cycle Knowledge Bank

A practical learning resource for hospital billing, finance, product, and engineering teams. Start with an encounter and follow the evidence through payment. All case records and contract terms are synthetic.

| If you want to… | Start here |
| --- | --- |
| Learn the lifecycle and terminology | [Revenue cycle and glossary](docs/foundations.md) |
| Investigate a payment difference | [Casebook](docs/casebook.md) |
| Locate the evidence across systems | [Data lineage](docs/data-lineage.md) |
| Reproduce a KPI calculation | [Metrics dictionary](docs/metrics.md) |
| Compare funding models and local challenges | [Regional profiles](docs/regions.md) |
| Evaluate AI for exception triage | [AI benchmark](docs/ai-benchmark.md) |
| Verify, correct, or update an entry | [Editorial guide and source register](CONTRIBUTING.md) |

The companion [claims platform](https://github.com/sakti1977/claims-platform) demonstrates submission, acknowledgment, rule rollback, and lost-receipt recovery with synthetic claims.

## Run the examples

From the repository root with Python 3.10+:

```sh
python -m unittest -v
python lab.py
python lab.py --score path/to/predictions.json
```

The first lab calculates expected payer payment, compares it with the synthetic remittance, and scores deterministic and threshold-only baselines. The optional scoring command accepts AI predictions in the documented format. The first edition draws on official sources for regional profiles. Independent practitioner review is pending.

