def calculate_risk(predicted_cases: int) -> str:
    if predicted_cases >= 18:
        return "High"
    elif predicted_cases >= 10:
        return "Medium"
    return "Low"
