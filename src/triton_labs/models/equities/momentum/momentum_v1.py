from dataclasses import dataclass
from triton_labs.utils.scoring import score_higher_is_better, clamp_score


@dataclass
class MomentumInput:
    ticker: str
    relative_strength: float = None
    trend_strength: float = None
    volume_expansion: float = None
    position_vs_52w_high: float = None


def classify_momentum(score: float):

    if score >= 90:
        return "Explosive Momentum"

    if score >= 80:
        return "Strong Momentum"

    if score >= 70:
        return "Positive Momentum"

    if score >= 60:
        return "Neutral Momentum"

    return "Weak Momentum"


def calculate_momentum_score(data: MomentumInput):

    score = (
        score_higher_is_better(data.relative_strength, 100, 0) * 0.35 +
        score_higher_is_better(data.trend_strength, 100, 0) * 0.30 +
        score_higher_is_better(data.volume_expansion, 2.0, 0.5) * 0.15 +
        score_higher_is_better(data.position_vs_52w_high, 1.0, 0.0) * 0.20
    )

    score = round(clamp_score(score), 2)

    return {
        "ticker": data.ticker,
        "momentum_score": score,
        "momentum_class": classify_momentum(score),
        "model": "MOMENTUM_V1",
        "lifecycle_state": "Research",
        "execution_authority": False
    }