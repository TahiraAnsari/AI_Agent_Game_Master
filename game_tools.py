<<<<<<< HEAD
from agents import function_tool
import random

@function_tool
def roll_dice() -> str:
    return f"you rolled a {random.randint(1,6)}!"

@function_tool
def generate_event() -> str:
    events = [
        "You encountered a drogon!",
        "You found a treasure chest.",
        "You fell into a trap!",
        "You met a mysterious wizard"
    ]
=======
from agents import function_tool
import random

@function_tool
def roll_dice() -> str:
    return f"you rolled a {random.randint(1,6)}!"

@function_tool
def generate_event() -> str:
    events = [
        "You encountered a drogon!",
        "You found a treasure chest.",
        "You fell into a trap!",
        "You met a mysterious wizard"
    ]
>>>>>>> 968674fc0f7896be8e22f338207bfc4c8960604d
    return random.choice(events)