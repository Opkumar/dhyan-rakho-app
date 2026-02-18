def calculate_risk(predicted_cases: int) -> str:
    if predicted_cases >= 18:
        return "High"
    elif predicted_cases >= 10:
        return "Medium"
    return "Low"
def calculate_water_risk(water: dict) -> int:
    """
    Converts water quality parameters into a numeric risk score (0–5)
    """
    if not water:
        return 0

    risk = 0

    if water.get("ph", 7) < 6.5 or water.get("ph", 7) > 8.5:
        risk += 1

    if water.get("turbidity", 0) > 5:
        risk += 1

    if water.get("chlorine", 0.2) < 0.2:
        risk += 1

    if water.get("bacteria_level", "").lower() == "high":
        risk += 2

    return risk


def calculate_risk(predicted_cases: int) -> str:
    """
    Converts predicted cases into outbreak risk level
    """
    if predicted_cases >= 18:
        return "High"
    elif predicted_cases >= 10:
        return "Medium"
    return "Low"
