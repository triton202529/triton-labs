from triton_labs.models.equities.quality.quality_v1 import (
    QualityInput,
    calculate_quality_score,
)

from triton_labs.models.equities.value.value_v1 import (
    ValueInput,
    calculate_value_score,
)

from triton_labs.models.equities.growth.growth_v1 import (
    GrowthInput,
    calculate_growth_score,
)

from triton_labs.models.equities.risk.risk_v1 import (
    RiskInput,
    calculate_risk_score,
)

from triton_labs.models.equities.fusion.fusion_v1 import (
    FusionInput,
    calculate_fusion_score,
)


def run_equity_intelligence(ticker: str):

    quality = calculate_quality_score(
        QualityInput(
            ticker=ticker,
            roe=0.35,
            roic=0.24,
            roa=0.18,
            gross_margin=0.68,
            operating_margin=0.42,
            net_margin=0.36,
            debt_to_equity=0.40,
            interest_coverage=18,
            operating_cash_flow=118_000_000_000,
            free_cash_flow=74_000_000_000,
            free_cash_flow_margin=0.31,
        )
    )

    value = calculate_value_score(
        ValueInput(
            ticker=ticker,
            pe=18,
            forward_pe=17,
            pb=1.6,
            ps=2.5,
            ev_ebitda=10,
            debt_to_equity=0.25,
            free_cash_flow_yield=0.08,
        )
    )

    growth = calculate_growth_score(
        GrowthInput(
            ticker=ticker,
            revenue_growth=0.15,
            eps_growth=0.18,
            free_cash_flow_growth=0.14,
            gross_margin_growth=0.02,
            operating_margin_growth=0.03,
        )
    )

    risk = calculate_risk_score(
        RiskInput(
            ticker=ticker,
            volatility=0.18,
            beta=0.85,
            max_drawdown=0.25,
            debt_to_equity=0.25,
        )
    )

    fusion = calculate_fusion_score(
        FusionInput(
            ticker=ticker,
            quality_score=quality["quality_score"],
            value_score=value["value_score"],
            growth_score=growth["growth_score"],
            risk_score=risk["risk_score"],
        )
    )

    return {
        "ticker": ticker,
        "quality": quality,
        "value": value,
        "growth": growth,
        "risk": risk,
        "fusion": fusion,
    }