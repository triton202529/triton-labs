from dataclasses import dataclass
from triton_labs.utils.scoring import score_higher_is_better, score_lower_is_better, clamp_score


@dataclass
class ValueInput:
    ticker: str
    pe: float = None
    forward_pe: float = None
    pb: float = None
    ps: float = None
    ev_ebitda: float = None
    debt_to_equity: float = None
    free_cash_flow_yield: float = None


def classify_value(score: float) -> str:
    score = clamp_score(score)

    if score >= 90:
        return "Deep Value"
    if score >= 80:
        return "Strong Value"
    if score >= 70:
        return "Good Value"
    if score >= 60:
        return "Fair Value"

    return "Expensive"


def calculate_value_score(data: ValueInput) -> dict:

    valuation_score = (
        score_lower_is_better(data.pe, excellent=8, poor=40) * 0.25 +
        score_lower_is_better(data.forward_pe, excellent=8, poor=35) * 0.20 +
        score_lower_is_better(data.pb, excellent=1.0, poor=8.0) * 0.15 +
        score_lower_is_better(data.ps, excellent=1.0, poor=15.0) * 0.10 +
        score_lower_is_better(data.ev_ebitda, excellent=5, poor=25) * 0.20 +
        score_higher_is_better(data.free_cash_flow_yield, excellent=0.10, poor=0.00) * 0.10
    )

    debt_penalty = (
        score_lower_is_better(data.debt_to_equity, excellent=0.30, poor=3.00)
    )

    final_score = (
        valuation_score * 0.85 +
        debt_penalty * 0.15
    )

    final_score = round(clamp_score(final_score), 2)

    return {
        "ticker": data.ticker,
        "value_score": final_score,
        "value_class": classify_value(final_score),
        "valuation_score": round(clamp_score(valuation_score), 2),
        "debt_score": round(clamp_score(debt_penalty), 2),
        "model": "VALUE_V1",
        "lifecycle_state": "Research",
        "execution_authority": False
    }
