import asyncio

from agents.agentGreet import agentGreet

async def main():
    await asyncio.gather(
        agentGreet.run(),
       
    )

if __name__ == "__main__":
    asyncio.run(main())