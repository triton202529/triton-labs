from dataclasses import dataclass
from triton_labs.utils.scoring import score_lower_is_better, clamp_score


@dataclass
class RiskInput:
    ticker: str
    volatility: float = None
    beta: float = None
    max_drawdown: float = None
    debt_to_equity: float = None


def classify_risk(score: float) -> str:
    score = clamp_score(score)

    if score >= 90:
        return "Very Low Risk"
    if score >= 80:
        return "Low Risk"
    if score >= 70:
        return "Moderate Risk"
    if score >= 60:
        return "Elevated Risk"

    return "High Risk"


def calculate_risk_score(data: RiskInput) -> dict:

    score = (
        score_lower_is_better(data.volatility, 0.10, 0.60) * 0.30 +
        score_lower_is_better(data.beta, 0.50, 2.50) * 0.20 +
        score_lower_is_better(data.max_drawdown, 0.10, 0.80) * 0.35 +
        score_lower_is_better(data.debt_to_equity, 0.30, 3.00) * 0.15
    )

    score = round(clamp_score(score), 2)

    return {
        "ticker": data.ticker,
        "risk_score": score,
        "risk_class": classify_risk(score),
        "model": "RISK_V1",
        "lifecycle_state": "Research",
        "execution_authority": False
    }