# core/stimuli.py

import random

# Define primitive stimuli space
STIMULI_TYPES = ["warmth", "cold", "light", "dark", "pressure", "release"]

def generate_random_stimulus():
    """Simulate a random environmental stimulus."""
    stimulus = random.choice(STIMULI_TYPES)
    intensity = random.uniform(0.0, 1.0)
    return {
        "type": stimulus,
        "intensity": round(intensity, 2)
    }
