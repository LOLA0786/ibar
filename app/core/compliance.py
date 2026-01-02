from app.core.rules import evaluate_rules
from app.models.regulatory import RegulatoryTrace

def shadow_evaluate(user_id, venue_id, country, state, pour_ml):
    allowed, reason = evaluate_rules(
        country,
        state,
        {"pour_ml": pour_ml}
    )

    return {
        "block": not allowed,
        "reason": reason
    }
