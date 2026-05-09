import random


def generate_ai_confidence():

    confidence = random.randint(78, 99)

    return confidence


def calculate_risk_level(
    verification_count
):

    if verification_count >= 10:

        return "HIGH"

    elif verification_count >= 5:

        return "MEDIUM"

    else:

        return "LOW"