import random

def validate_disaster_image(disaster_type):

    confidence_score = random.randint(80, 99)

    validation_result = {
        "disaster_type": disaster_type,
        "confidence": confidence_score,
        "status": "VALID"
    }

    return validation_result