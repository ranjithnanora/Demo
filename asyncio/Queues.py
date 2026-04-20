import asyncio

async def producer(q):
    await q.put("data")

async def consumer(q):
    item = await q.get()
    print(item)

async def main():
    q = asyncio.Queue()
    await asyncio.gather(producer(q), consumer(q))

asyncio.run(main())