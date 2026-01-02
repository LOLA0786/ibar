from app.models.regulatory import RegulatoryTrace
from app.core.rules import evaluate_rules
from app.core.inference import infer_block_probability

def shadow_evaluate(user_id, venue_id, country, state, pour_ml):
    allowed, rule_reason = evaluate_rules(
        country,
        state,
        {"pour_ml": pour_ml}
    )

    if not allowed:
        return {"block": True, "reason": rule_reason}

    traces = RegulatoryTrace.__table__.select().execute().fetchall()

    prob = infer_block_probability(
        traces,
        {
            "country": country,
            "state": state,
            "pour_ml": pour_ml
        }
    )

    if prob > 0.7:
        return {"block": True, "reason": "INFERRED_RISK"}

    return {"block": False, "reason": "ALLOW"}
