import pandas as pd
from pathlib import Path

from triton_labs.models.equities.growth.growth_v1 import (
    GrowthInput,
    calculate_growth_score,
)

SAMPLE_DATA = [
    {
        "ticker": "NVDA",
        "revenue_growth": 0.80,
        "eps_growth": 0.95,
        "free_cash_flow_growth": 0.60,
        "gross_margin_growth": 0.08,
        "operating_margin_growth": 0.07,
    },
    {
        "ticker": "MSFT",
        "revenue_growth": 0.15,
        "eps_growth": 0.18,
        "free_cash_flow_growth": 0.14,
        "gross_margin_growth": 0.02,
        "operating_margin_growth": 0.03,
    },
    {
        "ticker": "STAGNANT",
        "revenue_growth": 0.01,
        "eps_growth": -0.05,
        "free_cash_flow_growth": -0.10,
        "gross_margin_growth": -0.05,
        "operating_margin_growth": -0.08,
    }
]


def main():
    results = []

    for row in SAMPLE_DATA:
        item = GrowthInput(**row)
        results.append(calculate_growth_score(item))

    df = pd.DataFrame(results)

    output_path = Path("data/intelligence/growth_scores.csv")
    output_path.parent.mkdir(parents=True, exist_ok=True)

    df.to_csv(output_path, index=False)

    print(df)
    print()
    print(f"Saved: {output_path}")


if __name__ == "__main__":
    main()