import os
from dotenv import load_dotenv
from agents import Agent, Runner, AsyncOpenAI, OpenAIChatCompletionsModel
from agents.run import RunConfig
from game_tools import roll_dice, generate_event

gemini_key = ""

load_dotenv()
client = AsyncOpenAI(
    api_key=gemini_key, 
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

model = OpenAIChatCompletionsModel(
    model = "gemini-2.0-flash",
    openai_client= client
    )
config = RunConfig(
        model=model,
        tracing_disabled=True   
)

narrator_agent = Agent(
    name="NarratorAgent",
    instructions="You narrate the adventure. Ask the player for choices.",
    model=model
)

monster_agent = Agent(
    name="MonsterAgent",
    instructions="You handle moster encounters using roll_dice and generate_event.",
    model=model,
    tools=[roll_dice, generate_event]
)

item_agnet = Agent(
    name="ItemAgent",
    instructions="You provide rewards or item to player.",
    model=model
)

def main():
    print("\U0001F3AE Welcome to Fantasy Game!")
    choice = input("Do you enter the forest or turn back?")

    result1 = Runner.run_sync(narrator_agent, choice,run_config=config)
    print("\nStory:", result1.final_output)

    result2 = Runner.run_sync(monster_agent, "Start encounter",run_config=config)
    print("\nEncounter:", result2.final_output)

    result3 = Runner.run_sync(item_agnet, "Give rewars",run_config=config)
    print("\nReward:", result3.final_output)


if __name__ == "__main__":
    main()