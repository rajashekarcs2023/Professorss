from uagents import Agent, Context
from uagents.setup import fund_agent_if_low
from pydantic import BaseModel

class Message(BaseModel):
    content: str

agent_weather = Agent(
    name="agent_weather",
    port=8001,
    endpoint=["http://127.0.0.1:8001/submit"],
)

fund_agent_if_low(agent_weather.wallet.address())

@agent_weather.on_message(model=Message)
async def handle_message(ctx: Context, sender: str, msg: Message):
    ctx.logger.info(f"Weather agent received: {msg.content}")
    # Here you would typically call a weather API
    # For this example, we'll just return a placeholder response
    response = f"The weather is sunny today! (Responding to: {msg.content})"
    return Message(content=response)

if __name__ == "__main__":
    agent_weather.run()