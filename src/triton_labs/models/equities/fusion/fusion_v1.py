from dataclasses import dataclass
from triton_labs.utils.scoring import clamp_score


@dataclass
class FusionInput:
    ticker: str
    quality_score: float
    value_score: float
    growth_score: float
    risk_score: float


def classify_fusion(score: float) -> str:

    if score >= 90:
        return "Exceptional Opportunity"

    if score >= 80:
        return "High Conviction"

    if score >= 70:
        return "Attractive"

    if score >= 60:
        return "Watchlist"

    return "Avoid"


def determine_action(score: float) -> str:

    if score >= 85:
        return "STRONG_BUY"

    if score >= 75:
        return "BUY"

    if score >= 65:
        return "WATCH"

    return "AVOID"


def calculate_fusion_score(data: FusionInput):

    score = (
        data.quality_score * 0.35 +
        data.value_score * 0.25 +
        data.growth_score * 0.20 +
        data.risk_score * 0.20
    )

    score = round(clamp_score(score), 2)

    return {
        "ticker": data.ticker,
        "fusion_score": score,
        "fusion_class": classify_fusion(score),
        "action": determine_action(score),
        "model": "FUSION_V1",
        "lifecycle_state": "Research",
        "execution_authority": False
    }