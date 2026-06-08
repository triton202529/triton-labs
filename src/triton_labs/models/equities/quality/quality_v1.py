from dataclasses import dataclass
from triton_labs.utils.scoring import score_higher_is_better, score_lower_is_better, clamp_score


@dataclass
class QualityInput:
    ticker: str
    roe: float = None
    roic: float = None
    roa: float = None
    gross_margin: float = None
    operating_margin: float = None
    net_margin: float = None
    debt_to_equity: float = None
    interest_coverage: float = None
    operating_cash_flow: float = None
    free_cash_flow: float = None
    free_cash_flow_margin: float = None


def classify_quality(score: float) -> str:
    score = clamp_score(score)

    if score >= 90:
        return "Elite Quality"
    if score >= 80:
        return "High Quality"
    if score >= 70:
        return "Good Quality"
    if score >= 60:
        return "Average Quality"
    return "Below Desired Quality Threshold"


def calculate_quality_score(data: QualityInput) -> dict:
    profitability_score = (
        score_higher_is_better(data.roe, excellent=0.25, poor=0.00) * 0.35 +
        score_higher_is_better(data.roic, excellent=0.20, poor=0.00) * 0.45 +
        score_higher_is_better(data.roa, excellent=0.12, poor=0.00) * 0.20
    )

    capital_efficiency_score = (
        score_higher_is_better(data.roic, excellent=0.20, poor=0.00) * 0.40 +
        score_higher_is_better(data.operating_margin, excellent=0.30, poor=0.00) * 0.35 +
        score_higher_is_better(data.net_margin, excellent=0.20, poor=0.00) * 0.25
    )

    financial_strength_score = (
        score_lower_is_better(data.debt_to_equity, excellent=0.30, poor=2.50) * 0.55 +
        score_higher_is_better(data.interest_coverage, excellent=12.0, poor=1.5) * 0.45
    )

    cash_generation_score = (
        score_higher_is_better(data.operating_cash_flow, excellent=1_000_000_000, poor=0) * 0.30 +
        score_higher_is_better(data.free_cash_flow, excellent=750_000_000, poor=0) * 0.35 +
        score_higher_is_better(data.free_cash_flow_margin, excellent=0.20, poor=0.00) * 0.35
    )

    final_score = (
        profitability_score * 0.35 +
        capital_efficiency_score * 0.25 +
        financial_strength_score * 0.20 +
        cash_generation_score * 0.20
    )

    final_score = round(clamp_score(final_score), 2)

    return {
        "ticker": data.ticker,
        "quality_score": final_score,
        "quality_class": classify_quality(final_score),
        "profitability_score": round(clamp_score(profitability_score), 2),
        "capital_efficiency_score": round(clamp_score(capital_efficiency_score), 2),
        "financial_strength_score": round(clamp_score(financial_strength_score), 2),
        "cash_generation_score": round(clamp_score(cash_generation_score), 2),
        "model": "QUALITY_V1",
        "lifecycle_state": "Research",
        "execution_authority": False
    }
