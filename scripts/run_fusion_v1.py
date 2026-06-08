import pandas as pd
from pathlib import Path

from triton_labs.models.equities.fusion.fusion_v1 import (
    FusionInput,
    calculate_fusion_score,
)

SAMPLE_DATA = [
    {
        "ticker": "MSFT",
        "quality_score": 99.5,
        "value_score": 55,
        "growth_score": 57,
        "risk_score": 85,
    },
    {
        "ticker": "AAPL",
        "quality_score": 94,
        "value_score": 27,
        "growth_score": 65,
        "risk_score": 70,
    },
    {
        "ticker": "SUPER",
        "quality_score": 95,
        "value_score": 90,
        "growth_score": 95,
        "risk_score": 90,
    },
    {
        "ticker": "TRASH",
        "quality_score": 20,
        "value_score": 15,
        "growth_score": 10,
        "risk_score": 5,
    }
]


def main():

    results = []

    for row in SAMPLE_DATA:
        item = FusionInput(**row)
        results.append(calculate_fusion_score(item))

    df = pd.DataFrame(results)

    output_path = Path("data/fusion/fusion_scores.csv")
    output_path.parent.mkdir(parents=True, exist_ok=True)

    df.to_csv(output_path, index=False)

    print(df)
    print()
    print(f"Saved: {output_path}")


if __name__ == "__main__":
    main()