import pandas as pd
from pathlib import Path

from triton_labs.models.equities.momentum.momentum_v1 import (
    MomentumInput,
    calculate_momentum_score,
)

SAMPLE_DATA = [
    {
        "ticker": "NVDA",
        "relative_strength": 95,
        "trend_strength": 90,
        "volume_expansion": 1.8,
        "position_vs_52w_high": 0.97,
    },
    {
        "ticker": "MSFT",
        "relative_strength": 75,
        "trend_strength": 72,
        "volume_expansion": 1.2,
        "position_vs_52w_high": 0.88,
    },
    {
        "ticker": "FALLING",
        "relative_strength": 20,
        "trend_strength": 15,
        "volume_expansion": 0.7,
        "position_vs_52w_high": 0.30,
    }
]


def main():

    results = []

    for row in SAMPLE_DATA:
        item = MomentumInput(**row)
        results.append(calculate_momentum_score(item))

    df = pd.DataFrame(results)

    output_path = Path("data/intelligence/momentum_scores.csv")
    output_path.parent.mkdir(parents=True, exist_ok=True)

    df.to_csv(output_path, index=False)

    print(df)
    print()
    print(f"Saved: {output_path}")


if __name__ == "__main__":
    main()