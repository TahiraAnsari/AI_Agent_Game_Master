from agents import Agent

item_agent = Agent(
    name="ItemAgent",
    instructions=(
        "You are the reward master. "
        "When the player succeeds in a task or defeats a monster, "
        "give them a unique fantasy item. "
        "Describe the item's appearance, magical properties, and possible uses. "
        "Ensure the reward feels special and meaningful."
    ),
    model=None  # Will be injected from main.py
)
