from collections import Counter

def infer_block_probability(traces, context):
    """
    traces: list of RegulatoryTrace
    context: dict(country, state, pour_ml)
    """

    relevant = [
        t for t in traces
        if t.country == context["country"]
        and t.state == context["state"]
        and t.pour_ml >= context["pour_ml"]
    ]

    if not relevant:
        return 0.0

    decisions = Counter(t.decision for t in relevant)
    block_ratio = decisions.get("BLOCK", 0) / len(relevant)

    return block_ratio
