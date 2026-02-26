def color_by_adherence(v):
    if v < 0.3:
        return "red"        # Strong funnel bypass
    elif v > 1:
        return "orange"     # Anomalous / definition mismatch
    else:
        return "steelblue"  # Normal
