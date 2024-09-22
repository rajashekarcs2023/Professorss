from uagents import Agent, Context
from uagents.setup import fund_agent_if_low
from pydantic import BaseModel

class Message(BaseModel):
    content: str

coordinator_agent = Agent(
    name="coordinator_agent",
    port=8000,
    endpoint=["http://127.0.0.1:8000/submit"],
)

fund_agent_if_low(coordinator_agent.wallet.address())

@coordinator_agent.on_message(model=Message)
async def message_handler(ctx: Context, sender: str, msg: Message):
    ctx.logger.info(f"Received message from {sender}: {msg.content}")
    
    if "weather" in msg.content.lower():
        response = await ctx.send("agent_weather", Message(content=msg.content))
    elif "greet" in msg.content.lower() or "hello" in msg.content.lower():
        response = await ctx.send("agent_greet", Message(content=msg.content))
    else:
        response = Message(content="I'm not sure how to process that request. Try asking about weather or greetings.")
    
    return response

if __name__ == "__main__":
    coordinator_agent.run()