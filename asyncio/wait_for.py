import asyncio

async def slow():
    await asyncio.sleep(5)

async def main():
    try:
        await asyncio.wait_for(slow(), timeout=2)
    except asyncio.TimeoutError:
        print("Too slow!")

asyncio.run(main())