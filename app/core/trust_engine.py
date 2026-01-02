def compute_trust(
    account_days: int,
    pours: int,
    reports: int,
    blocks: int
) -> int:
    score = 50
    score += min(account_days // 7, 15)
    score += min(pours, 20)
    score -= reports * 15
    score -= blocks * 25
    return max(0, min(100, score))
