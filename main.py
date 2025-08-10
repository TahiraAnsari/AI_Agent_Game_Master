import os
from dotenv import load_dotenv
<<<<<<< HEAD
from agents import Runner, AsyncOpenAI, OpenAIChatCompletionsModel
from agents.run import RunConfig

# Import agents
from my_agent.item_agent import item_agent
from my_agent.monster_agent import monster_agent
from my_agent.narrator_agent import narrator_agent
from my_agent.triage_agent import triage_agent
load_dotenv()

# Configure model
client = AsyncOpenAI(
    api_key=os.getenv("GEMINI_API_KEY"),
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)
model = OpenAIChatCompletionsModel(
    model="gemini-2.0-flash",
    openai_client=client
)
config = RunConfig(model=model, tracing_disabled=True)

# Inject model into agents
narrator_agent.model = model
monster_agent.model = model
item_agent.model = model
triage_agent.model = model

def main():
    print("\U0001F3AE Welcome to Fantasy Game!")
    
    while True:
        choice = input("\nWhat do you do? (type 'quit' to exit): ").strip()
        if choice.lower() == "quit":
            print("Thanks for playing! Goodbye.")
            break
        
        result = Runner.run_sync(triage_agent, choice, run_config=config)
        print("\n" + result.final_output)

if __name__ == "__main__":
    main()
=======
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
>>>>>>> 968674fc0f7896be8e22f338207bfc4c8960604d
