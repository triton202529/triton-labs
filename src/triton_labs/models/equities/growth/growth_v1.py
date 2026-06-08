from dataclasses import dataclass
from triton_labs.utils.scoring import score_higher_is_better, clamp_score


@dataclass
class GrowthInput:
    ticker: str
    revenue_growth: float = None
    eps_growth: float = None
    free_cash_flow_growth: float = None
    gross_margin_growth: float = None
    operating_margin_growth: float = None


def classify_growth(score: float) -> str:
    score = clamp_score(score)

    if score >= 90:
        return "Hyper Growth"
    if score >= 80:
        return "Strong Growth"
    if score >= 70:
        return "Good Growth"
    if score >= 60:
        return "Moderate Growth"

    return "Low Growth"


def calculate_growth_score(data: GrowthInput) -> dict:

    score = (
        score_higher_is_better(data.revenue_growth, 0.30, 0.00) * 0.30 +
        score_higher_is_better(data.eps_growth, 0.30, 0.00) * 0.30 +
        score_higher_is_better(data.free_cash_flow_growth, 0.25, 0.00) * 0.20 +
        score_higher_is_better(data.gross_margin_growth, 0.10, -0.10) * 0.10 +
        score_higher_is_better(data.operating_margin_growth, 0.10, -0.10) * 0.10
    )

    score = round(clamp_score(score), 2)

    return {
        "ticker": data.ticker,
        "growth_score": score,
        "growth_class": classify_growth(score),
        "model": "GROWTH_V1",
        "lifecycle_state": "Research",
        "execution_authority": False
    }