import asyncio


async def producer(word,q):
    for ch in word:
        await q.put(ch)
        await asyncio.sleep(2)
    await q.put(None)


async def consumer(q):
    while True:
        val = await  q.get()
        if val is None:
            break
        print(val)
        q.task_done()
async def main(word):
    q = asyncio.Queue()
    task=asyncio.gather(consumer(q), producer(word, q))
    await task



asyncio.run(main("Hello"))


