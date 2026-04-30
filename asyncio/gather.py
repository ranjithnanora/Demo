import asyncio

async def task(n):
    await asyncio.sleep(1)
    print("executed!")
    return n

async def main():
    results =  await asyncio.gather(
        task(1),
        task(2),
        task(3)
    )
    print(results)



asyncio.run(main())