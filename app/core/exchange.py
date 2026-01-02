def compute_exchange_ratio(from_country, to_country, brand):
    """
    This is NOT currency FX.
    This is regulatory equivalence.
    """

    # Example heuristics (replace with learned model later)
    if from_country == "AE" and to_country == "IN":
        return 0.8   # duty-free → excise adjusted

    if from_country == "US" and to_country == "SG":
        return 0.9

    return 1.0
