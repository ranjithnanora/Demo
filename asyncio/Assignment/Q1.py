"""
1.
Write an asynchronous Python program that fetches data from two
different URLs concurrently using the aiohttp library.
Print the length of the data fetched from each URL.
"""
import asyncio
import aiohttp

#print(dir(aiohttp))
async def fetch_url_and_display_length(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            data = await response.text()

    print(f"Length of content in URL {url} is {len(data)}")

async def main():
    task1 = asyncio.create_task(fetch_url_and_display_length("https://www.geeksforgeeks.org/python/python-taskgroups-with-asyncio/"))
    task2=asyncio.create_task(fetch_url_and_display_length("https://www.python.org/"))

    await asyncio.gather(task1, task2)

asyncio.run(main())