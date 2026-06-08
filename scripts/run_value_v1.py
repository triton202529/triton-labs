import pandas as pd
from pathlib import Path

from triton_labs.models.equities.value.value_v1 import (
    ValueInput,
    calculate_value_score,
)

SAMPLE_DATA = [
    {
        "ticker": "BRK.B",
        "pe": 18,
        "forward_pe": 17,
        "pb": 1.6,
        "ps": 2.5,
        "ev_ebitda": 10,
        "debt_to_equity": 0.25,
        "free_cash_flow_yield": 0.08,
    },
    {
        "ticker": "AAPL",
        "pe": 32,
        "forward_pe": 29,
        "pb": 45,
        "ps": 8,
        "ev_ebitda": 22,
        "debt_to_equity": 1.5,
        "free_cash_flow_yield": 0.03,
    },
    {
        "ticker": "CHEAP",
        "pe": 7,
        "forward_pe": 6,
        "pb": 0.8,
        "ps": 0.7,
        "ev_ebitda": 4,
        "debt_to_equity": 0.1,
        "free_cash_flow_yield": 0.14,
    }
]


def main():
    results = []

    for row in SAMPLE_DATA:
        item = ValueInput(**row)
        results.append(calculate_value_score(item))

    df = pd.DataFrame(results)

    output_path = Path("data/intelligence/value_scores.csv")
    output_path.parent.mkdir(parents=True, exist_ok=True)

    df.to_csv(output_path, index=False)

    print(df)
    print()
    print(f"Saved: {output_path}")


if __name__ == "__main__":
    main()