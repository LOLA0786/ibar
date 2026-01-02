import hashlib
import time

def uaal_shadow_evaluate(context: dict):
    """
    Shadow-mode evaluation only.
    Does NOT block execution.
    """

    risk_flags = []

    if context["pour_ml"] > 120:
        risk_flags.append("LARGE_POUR")

    if context["hour"] < 11 or context["hour"] > 23:
        risk_flags.append("OUT_OF_HOURS")

    score = min(1.0, 0.2 * len(risk_flags))

    evidence = hashlib.sha256(
        f"{context}{time.time()}".encode()
    ).hexdigest()

    return {
        "shadow_score": score,
        "flags": risk_flags,
        "shadow_evidence": evidence
    }
