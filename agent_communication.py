import asyncio
from uagents import Agent
from uagents.setup import fund_agent_if_low
from pydantic import BaseModel

class Message(BaseModel):
    content: str

class AgentCommunication:
    def __init__(self):
        self.temp_agent = None

    def initialize_agent(self):
        if self.temp_agent is None:
            self.temp_agent = Agent(name="temp_agent", port=8005)
            fund_agent_if_low(self.temp_agent.wallet.address())

    async def send_message_to_coordinator(self, message_content):
        self.initialize_agent()
        message = Message(content=message_content)
        response = await self.temp_agent.submit_message("coordinator_agent", message)
        return response.content if response else "No response received"

    def get_response(self, message_content):
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        try:
            response = loop.run_until_complete(self.send_message_to_coordinator(message_content))
        finally:
            loop.close()
        return response

def get_agent_comm():
    return AgentCommunication()