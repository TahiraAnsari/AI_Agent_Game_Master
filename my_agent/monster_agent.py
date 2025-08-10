from agents import Agent
from game_tools import roll_dice, generate_event

monster_agent = Agent(
    name="MonsterAgent",
    instructions=(
        "You handle dangerous monster encounters. "
        "Describe the monster vividly—its size, smell, sounds, and movements. "
        "Ask the player what they want to do: fight, run, negotiate, or use an item. "
        "If they choose to fight, use roll_dice to determine outcome. "
        "Use generate_event for unexpected twists."
    ),
    model=None,  # Will be injected from main.py
    tools=[roll_dice, generate_event]
)
