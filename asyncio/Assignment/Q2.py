"""
2.
Implement an asynchronous Python program that reads from a file and
prints its content line by line using the aiofiles library.
"""

import aiofiles
import asyncio

async def read_file_and_print(path):
    async with aiofiles.open(path) as f:
        async for line in f:
            print(line, end="")


asyncio.run(read_file_and_print("demo"))