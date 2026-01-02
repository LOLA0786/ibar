from app.core.rules import evaluate_rules
from app.ml.predict import predict_risk

RISK_THRESHOLD = 0.65

def shadow_evaluate(user_id, venue_id, country, state, pour_ml):
    allowed, rule_reason = evaluate_rules(
        country,
        state,
        {"pour_ml": pour_ml}
    )

    if not allowed:
        return {"block": True, "reason": rule_reason}

    risk = predict_risk({
        "country": country,
        "state": state,
        "venue_id": venue_id,
        "pour_ml": pour_ml
    })

    if risk > RISK_THRESHOLD:
        return {
            "block": True,
            "reason": f"ML_RISK_{int(risk*100)}%"
        }

    return {"block": False, "reason": "ALLOW"}
