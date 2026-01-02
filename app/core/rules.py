RULES = {
    "IN": {
        "MH": {
            "max_ml_per_pour": 90,
            "dry_days": [],
            "allow_hotels_only": False
        },
        "GJ": {
            "prohibited": True
        }
    },
    "AE": {
        "DXB": {
            "hotel_only": True,
            "tourist_allowed": True
        }
    },
    "US": {
        "TX": {
            "last_pour_hour": 2
        }
    }
}

def evaluate_rules(country, state, context):
    rules = RULES.get(country, {}).get(state, {})

    if rules.get("prohibited"):
        return False, "STATE_PROHIBITION"

    if rules.get("max_ml_per_pour") and context["pour_ml"] > rules["max_ml_per_pour"]:
        return False, "POUR_LIMIT_EXCEEDED"

    return True, "ALLOW"
