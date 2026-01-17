def score_signals(signals):
    score = 0
    reasons = []

    overlap = signals["overlap_ratio"]
    caption_empty = signals["caption_empty"]
    negation = signals["negation_flag"]

    # Overlap contribution (softened)
    if overlap >= 0.10:
        score += 2
        reasons.append("Meaningful semantic overlap detected")
    elif overlap >= 0.03:
        score += 1
        reasons.append("Partial semantic overlap detected")
    else:
        score -= 1
        reasons.append("Very low semantic overlap")

    # Caption contribution (stronger positive)
    if caption_empty == 0:
        score += 2
        reasons.append("Caption provides supporting context")
    else:
        score -= 1
        reasons.append("Caption is missing")

    # Negation penalty (soft)
    if negation == 1:
        score -= 1
        reasons.append("Negation weakens consistency")

    # Final decision
    if score >= 1:
        return "CONSISTENT", " | ".join(reasons)
    else:
        return "CONTRADICTORY", " | ".join(reasons)
