import os
from dotenv import load_dotenv
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
