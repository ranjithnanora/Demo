"""
3.
Create an asynchronous Python program that simulates a simple
producer-consumer scenario using asyncio.Queue.
The producer should generate numbers from 1 to 5 and put them in the queue,
while the consumer should retrieve and print them.
"""
import asyncio


async def producer(q):
    for i in range(1,6):
        await q.put(i)
        await asyncio.sleep(1)
    await q.put("END")

async def consumer(q):
    while True:
        val=await q.get()
        if val=="END":
            break
        print(val)
        q.task_done()

async def main():
    q=asyncio.Queue()
    task=asyncio.gather(consumer(q), producer(q))
    await task

asyncio.run(main())
