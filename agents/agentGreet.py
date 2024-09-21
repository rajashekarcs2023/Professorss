from uagents import Agent, Context

# Create the agent
agentGreet = Agent(name="agentGreet", seed="greeting_recovery_phrase")

@agentGreet.on_message("greet")
async def handle_greeting(ctx: Context, message):
    # Extract the name from the message
    name = message.get('name', 'User')
    
    # Create a personalized greeting
    greeting = f"Hello, {name}! Nice to meet you."
    
    # Log the greeting
    ctx.logger.info(f"Greeting sent: {greeting}")
    
    # You can send the greeting to another agent if needed, similar to the rubric_agent
    # await ctx.send(agent="some_other_agent", performative="inform", content={"greeting": greeting})

if __name__ == "__main__":
    agentGreet.run()