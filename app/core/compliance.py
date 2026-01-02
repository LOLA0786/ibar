from app.models.regulatory import RegulatoryTrace

def shadow_evaluate(user_id, venue_id, country, state, pour_ml):
    # Shadow mode — never blocks unless obvious
    block = False
    reason = "ALLOW"

    if country == "IN" and state == "GJ":
        block = True
        reason = "STATE_PROHIBITION"

    return {
        "block": block,
        "reason": reason
    }
