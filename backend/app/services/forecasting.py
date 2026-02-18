import random

def forecast_cases(location: str, disease: str):
    predicted_cases = random.randint(5, 25)
    confidence = round(random.uniform(0.7, 0.9), 2)
    return predicted_cases, confidence
