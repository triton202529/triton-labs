def clamp_score(value, minimum=0, maximum=100):
    if value is None:
        return 0
    try:
        return max(minimum, min(maximum, float(value)))
    except Exception:
        return 0


def score_higher_is_better(value, excellent, poor):
    if value is None:
        return 0
    try:
        value = float(value)
        if value >= excellent:
            return 100
        if value <= poor:
            return 0
        return ((value - poor) / (excellent - poor)) * 100
    except Exception:
        return 0


def score_lower_is_better(value, excellent, poor):
    if value is None:
        return 0
    try:
        value = float(value)
        if value <= excellent:
            return 100
        if value >= poor:
            return 0
        return ((poor - value) / (poor - excellent)) * 100
    except Exception:
        return 0
