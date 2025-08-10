from agents import Agent
from .narrator_agent import narrator_agent
from .monster_agent import monster_agent
from .item_agent import item_agent

triage_agent = Agent(
    name="TriageAgent",
    instructions=(
        "You decide which agent should handle the player's request: "
        "NarratorAgent for story progression, "
        "MonsterAgent for battles, "
        "ItemAgent for rewards or loot."
    ),
    model=None,  # Will be injected from main.py
    handoffs=[narrator_agent, monster_agent, item_agent]
)
