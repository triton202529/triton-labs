import pandas as pd
from pathlib import Path

from triton_labs.models.equities.risk.risk_v1 import (
    RiskInput,
    calculate_risk_score,
)

SAMPLE_DATA = [
    {
        "ticker": "BRK.B",
        "volatility": 0.18,
        "beta": 0.85,
        "max_drawdown": 0.25,
        "debt_to_equity": 0.25,
    },
    {
        "ticker": "SPY",
        "volatility": 0.20,
        "beta": 1.00,
        "max_drawdown": 0.35,
        "debt_to_equity": 0.50,
    },
    {
        "ticker": "MEME",
        "volatility": 0.70,
        "beta": 3.20,
        "max_drawdown": 0.90,
        "debt_to_equity": 4.00,
    }
]


def main():
    results = []

    for row in SAMPLE_DATA:
        item = RiskInput(**row)
        results.append(calculate_risk_score(item))

    df = pd.DataFrame(results)

    output_path = Path("data/intelligence/risk_scores.csv")
    output_path.parent.mkdir(parents=True, exist_ok=True)

    df.to_csv(output_path, index=False)

    print(df)
    print()
    print(f"Saved: {output_path}")


if __name__ == "__main__":
    main()