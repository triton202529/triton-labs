import pandas as pd
from pathlib import Path

from triton_labs.models.equities.quality.quality_v1 import (
    QualityInput,
    calculate_quality_score,
)


SAMPLE_DATA = [
    {
        "ticker": "MSFT",
        "roe": 0.35,
        "roic": 0.24,
        "roa": 0.18,
        "gross_margin": 0.68,
        "operating_margin": 0.42,
        "net_margin": 0.36,
        "debt_to_equity": 0.40,
        "interest_coverage": 18.0,
        "operating_cash_flow": 118_000_000_000,
        "free_cash_flow": 74_000_000_000,
        "free_cash_flow_margin": 0.31,
    },
    {
        "ticker": "AAPL",
        "roe": 1.45,
        "roic": 0.55,
        "roa": 0.28,
        "gross_margin": 0.46,
        "operating_margin": 0.30,
        "net_margin": 0.25,
        "debt_to_equity": 1.50,
        "interest_coverage": 25.0,
        "operating_cash_flow": 110_000_000_000,
        "free_cash_flow": 95_000_000_000,
        "free_cash_flow_margin": 0.24,
    },
    {
        "ticker": "WEAK",
        "roe": 0.04,
        "roic": 0.02,
        "roa": 0.01,
        "gross_margin": 0.18,
        "operating_margin": 0.02,
        "net_margin": 0.01,
        "debt_to_equity": 3.50,
        "interest_coverage": 1.0,
        "operating_cash_flow": 50_000_000,
        "free_cash_flow": -20_000_000,
        "free_cash_flow_margin": -0.03,
    },
]


def main():
    results = []

    for row in SAMPLE_DATA:
        item = QualityInput(**row)
        results.append(calculate_quality_score(item))

    df = pd.DataFrame(results)

    output_path = Path("data/intelligence/quality_scores.csv")
    output_path.parent.mkdir(parents=True, exist_ok=True)

    df.to_csv(output_path, index=False)

    print(df)
    print()
    print(f"Saved: {output_path}")


if __name__ == "__main__":
    main()